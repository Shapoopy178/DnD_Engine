# -*- coding: utf-8 -*-
'''
Create and organize directory for DnD_Engine. 
'''
import sys
import os

ROOT_PATH = os.getcwd()

RESOURCES_DIR = os.path.join(ROOT_PATH,'.resources')
os.mkdir(RESOURCES_DIR)
GAMES_DIR = os.path.join(ROOT_PATH,'Games')

