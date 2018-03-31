#!/usr/bin/python3
'''
    script that generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo, using the function do_pack
'''
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''
        generate a .tgz archive
    '''
    filename = (datetime.now().strftime('%Y%m%d%H%M%S'))
    filename = filename + ".tgz"
    local('mkdir -p versions')
    result = local('tar -cvzf web_static_{} web_static'.format(filename))
    if result.succeeded:
        local('sudo mv web_static_* versions/')
        path = os.path.abspath(filename)
        return (path)
    else:
        return None
