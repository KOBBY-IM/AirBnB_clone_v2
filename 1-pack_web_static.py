#!/usr/bin/python3
"""Defines a fabric file to be executed locally"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    local("sudo mkdir -p versions")
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "./versions/web_static_{}.tgz".format(now)
    result = local("sudo tar -cvzf {} web_static".format(file_name))
    if result.succeeded:
        return file_name
    else:
        return None
