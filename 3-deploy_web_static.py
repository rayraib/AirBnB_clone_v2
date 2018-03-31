#!/usr/bin/python3
'''
    script that creates and distributes an archive to your web servers,
    using the function deploy
'''
from fabric.api import run, env, put, hosts
from fabric.api import local
from datetime import datetime
import os

env.hosts = ['52.23.184.231', '54.173.122.229']


def do_pack():
    '''
        generate a .tgz archive
    '''
    filename = (datetime.now().strftime('%Y%m%d%H%M%S'))
    filename = "web_static_" + filename + ".tgz"
    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static/'.format(filename))
    if result.succeeded:
        path = "versions/{}".format(filename)
        return (path)
    else:
        return None


def do_deploy(archive_path):
    '''
        deploys .tgz file to servers
    '''

    # check if the archive_path is valid
    if not os.path.exists(archive_path):
        print("FAILING HERE")
        return False

    # split the path to obtain filename with and without .tgz extension
    head, tail = os.path.split(archive_path)
    full_name = tail
    full_filename = tail.split('.')
    filename = full_filename[0]

    # upload archive file to the server
    result = put(archive_path, '/tmp/{}'.format(full_name))
    if result.failed:
        return False

    # extract content from the tar file
    result = run('mkdir -p /data/web_static/releases/{}/'.format(filename))
    if result.failed:
        return False
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
        format(full_name, filename))
    if result.failed:
        return False

    # remove the tar file from server
    result = run('rm /tmp/{}'.format(full_name))
    if result.failed:
        return False
    result = run('mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/'.format(filename, filename))
    if result.failed:
        return False
    result = run('rm -rf /data/web_static/releases/{}/web_static'
                 .format(filename))
    if result.failed:
        return False
    result = run('rm /data/web_static/current')
    if result.failed:
        return False
    result = run('ln -s /data/web_static/releases/{}/ /data/web_static/current\
        '.format(filename))
    if result.failed:
        return False

    print("New version deployed!")
    return True


def deploy():
    '''
        deploy new server
    '''

    file_path = do_pack()
    print ("\n======THIS IS THE FILE PATH=======>{}\n".format(file_path))
    if file_path is None:
        return False
    result = do_deploy(file_path)
    return result 
