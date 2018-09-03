# -*- coding: utf-8 -*-
'''
Create and organize directory for DnD_Engine. 
'''
import sys
import os
import shutil
import openpyxl

ROOT_PATH = os.getcwd()
DOCS_PATH = os.path.join(ROOT_PATH,'docs')
BIN_PATH = os.path.join(ROOT_PATH,'bin')
RESOURCES_PATH = os.path.join(ROOT_PATH,'.resources')
GAMES_PATH = os.path.join(ROOT_PATH,'Games')

while True:
    
    try:
        os.mkdir(RESOURCES_PATH)
    except FileExistsError:
        
        print('Warning! Previous installation detected. Proceed with caution.')
        ask = input("Do you want to continue? [Y/n]: ")
        if ask.upper() == 'N':
            print('Aborting installation.')
            break
        else:
            pass
    
    core_monster_manual = os.path.join(DOCS_PATH,'5E Monster Spreadsheet.xlsx')
    reduced_core_monster_manual = os.path.join(RESOURCES_PATH,'5E_mM_.xlsx')
    
    base_mm = openpyxl.load_workbook(core_monster_manual)
    base_mm.save(reduced_core_monster_manual)
    red_mm = openpyxl.load_workbook(reduced_core_monster_manual)
    deleteSheets = ['News & Updates', 'References', 'PC Races']
    
    for sheet in red_mm:
        if sheet.title in deleteSheets:
            red_mm.remove(sheet)
            
    red_mm.save(reduced_core_monster_manual)
    
    break