# -*- coding: utf-8 -*-

from lib import DnD_Engine

print('Entering new character creation wizard:')
print('New player character:  [1]\nNew NPC:               [2]')
newCharacterMode = int(input(''))
charName = input('Character Name:')

if newCharacterMode == 1:
    
    newPC = DnD_Engine.PlayerCharacter(charName)
    
    randomCheck = input('Generate random character? [N/y]')
    if randomCheck.upper() == 'Y':
        newPC.random_character()
    else:
        
        automaticCheck = input('Auto-roll stats? [Y/n]')
        if automaticCheck == '' or automaticCheck.upper() == 'Y':
            newPC.semi_auto_wizard()
        else:
            newPC.manual_character()