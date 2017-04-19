# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:51:31 2017
# Dostuff with git in Python
@author: Mike
"""

# GitPython import
import git
from git import Repo
import os

# a git dir:
#git_repo_dir = '

# Using gitorious
#http://stackoverflow.com/questions/2472552/python-way-to-clone-a-git-repository
#repo = git.Repo(')
#git.Git().clone("git://gitorious.org/git-python/mainline.git")

###############################################################################
# Using as auto cloner/downloader

''' Local config '''
# Local directory in which the many repos will be cloned to
local_dir = 'C:\\Users\\Mike\\Documents\\Github\\sayboltm\\ECE813\\shittest\\'

''' Remote config '''
# Main url of the remote to clone.. i.e. the part that is the same for all repos
#remote_main_url = 'git://github.com/bitcraze/'
remote_main_url = ''
# TODO: Why not work with git://..... ?
remote_repos = ['https://github.com/bitcraze/crazyflie2-exp-template-electronics.git',
'https://github.com/bitcraze/crazyflie2-nrf-bootloader.git',
'https://github.com/bitcraze/crazyflie2-nrf-firmware.git',
'https://github.com/bitcraze/crazyflie2-stm-bootloader.git',
'https://github.com/bitcraze/crazyflie-android-client.git',
'https://github.com/bitcraze/crazyflie-bootloader.git',
'https://github.com/bitcraze/crazyflie-clients-python.git',
'https://github.com/bitcraze/crazyflie-firmware.git',
'https://github.com/bitcraze/crazyflie-lib-python.git',
'https://github.com/bitcraze/crazyradio-firmware.git',
'https://github.com/bitcraze/lps-node-firmware.git']
# Rem
os.chdir(local_dir)

for repos in remote_repos:
    # Do command with combined remote_main_url and remote_repos
    bigstring = remote_main_url + repos
    git.Git().clone(remote_main_url + repos)
    #print(bigstring)
