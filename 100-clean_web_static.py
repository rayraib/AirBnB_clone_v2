#!/usr/bin/python3
'''
    script that deletes out-of-date archives, using the function do_clean:
'''
from fabric.api import run, env, hosts


env.hosts = ['52.23.184.231', '54.173.122.229']
env.user = 'ubuntu'

def do_clean(number=0):
    '''
        delete old archive files
    '''
    if number == 0:
        number = number + 2
    number = number + 1
    run(ls -t /versions | tail -n +number| xargs rm)
    run(ls -t /data/web_static/releases | tail -n +number| xargs rm)
