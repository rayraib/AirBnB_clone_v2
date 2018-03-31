#!/usr/bin/python3
'''
    script that distributes an archive to your web servers,
    using the function do_deploy:
'''
from fabric.api import run, env, put, hosts
import os


@hosts('52.23.184.231', '54.173.122.229')
def do_deploy(archive_path):
    '''
        deploys .tgz file to servers
    '''
    env.user = 'ubuntu'

    # check if the archive_path is valid
    if not os.path.isfile(archive_path):
        return False

    # split the path to obtain filename with and without .tgz extension
    head, tail = os.path.split(archive_path)
    full_name = tail
    full_filename = tail.split('.')
    filename = full_filename[0]

    # upload archive file to the server
    put(archive_path, '/tmp/{}'.format(full_name))

    # extract content from the tar file
    run('mkdir -p /data/web_static/releases/{}/'.format(filename))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.
        format(full_name, filename))

    # remove the tar file from server
    run('rm /tmp/{}'.format(full_name))
    run('mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/'.format(filename, filename))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(filename))
    run('rm /data/web_static/current')
    run('ln -s /data/web_static/releases/{} /data/web_static/current\
        '.format(filename))

    return True
