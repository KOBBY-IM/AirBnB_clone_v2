#!/usr/bin/python3
"""Defines a fabric file to be executed locally"""
from datetime import dattime
from fabric.api import *


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    local("sudo mkdir -p versions")
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filepath = "./versions/web_static_{}.tgz".format(now)
    result = local("sudo tar -cvzf {} web_static".format(filepath))
    if result.succeeded:
        return filepath
    else:
        return None
