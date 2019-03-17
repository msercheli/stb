# -*- coding: utf-8 -*-

name = 'stb'

version = '2.34'

description = \
    """
    Single-file-header-only C/C++ libraries
    """
authors = ['Sean T. Barrett']

def commands():
    #env.PYTHONPATH.append("{root}/python")
    #env.PATH.append("{root}/bin/{system.platform}")
    env.REZ_STB_INCLUDE_PATH = "{root}/include"

uuid = 'repository.stb'

