# -*- coding: utf-8 -*-

import sys

from lib import DnD_Engine


if DnD_Engine._install_check_() is False:
    print('DnD_Engine not installed!')
    print('Please run setup.py in desired installation folder.')
    
if __name__ == '__main__':
    
    NewGame = DnD_Engine.Game('Test')
    NewGame.NewGame()