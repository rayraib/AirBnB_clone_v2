#!/usr/bin/python3
'''
    script that creates and distributes an archive to your web servers,
    using the function deploy
'''
from fabric.api import run, env, put, hosts
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


@hosts('52.23.184.231', '54.173.122.229')
def deploy():
    '''
        deploy new server
    '''
    env.user = "ubuntu"

    file_path = do_pack()
    if file_path is None:
        return False
    x = do_deploy(file_path)
    return(x)
