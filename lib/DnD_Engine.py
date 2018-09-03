import os
import sys
import openpyxl

class Game(object):
    '''
    Game class for DnD_Engine. Stores, manages, and acts as handle for items
    related to a single Campaign or Game of Dungeons and Dragons. Should not be 
    confused with Session class, which is the class handling procedures related
    to session-by-session changes or activities.
    
    Attributes:
        
        Characters: list of PlayerCharacter objects
        
        Sessions: list of Session objects
    
    Methods:
        
        PlaySession():
            
            Create and begin session. Stores session events to log following 
            session close.
            
        ConfigureGame():
            
            Modify Game settings and metadata. 
    '''
    
    def __init__(self):
        self.path = os.getcwd()
        if self._install_check_() is False:
            print('DnD_Engine not installed!')
            print('Please run setup.py in desired installation folder.')
            sys.exit()
            return
        pass
    
    def PlaySession(self):
        pass
    
    def ConfigureGame(self):
        pass
    
    def NewGame(self):
        
        #Create base monster manual
        self._write_monster_manual('default')
        
    def _write_monster_manual(self, mode = ''):
        
        manual_fname = os.path.join(self.path, 'bin', 'monsterManual.txt')
            
        if os.path.isfile(manual_fname) is not True:
            
            self._init_monster_manual(manual_fname)
            
            return
        
    def _init_monster_manual(self, fname):
        print('Initializing Monster Manual...')
        BASE_MANUAL_PATH = os.path.join(self.path, 'docs')
        BASE_MANUAL_FNAME_W_PATH = os.path.join(BASE_MANUAL_PATH, '5E Monster Spreadsheet.xlsx')
        wb = openpyxl.load_workbook(BASE_MANUAL_FNAME_W_PATH)
        monsters_sheet = wb['Monsters']
        monster_metadata = monsters_sheet['A1:N1'][0]
        monster_data = monsters_sheet['A2:N1062']
        NPCs_sheet = wb['NPCs']
        NPC_metadata = NPCs_sheet['A1:K1']
        NPC_data = NPCs_sheet['A2:K169']
        self.MonsterManual = {
                'Monsters':{},
                'NPCs':{}
                              }
        for line in monster_data:
            monsterName = line[0].value
            monsterData = {}
            for idx, row in enumerate(line[1:]):
                monsterData[monster_metadata[idx+1].value] = row.value
            self.MonsterManual['Monsters'][monsterName] = monsterData
        for line in NPC_data:
            monsterName = line[0].value
            monsterData = {}
            for idx, row in enumerate(line[1:]):
                monsterData[monster_metadata[idx+1]] = row.value
            self.MonsterManual['NPCs'][monsterName] = monsterData
        return
    
    def _install_check_(self):
        RESOURCE_DIR = os.path.join(self.path, '.resources')
        if os.path.isdir(RESOURCE_DIR) is False:
            return False
        else:
            return True
    
class Session(object):
    '''
    '''
    def __init__(self):
        pass

class Character(object):
    '''
    '''
    def __init__(self):
        pass

class PlayerCharacter(Character):
    '''
    '''
    def __init__(self):
        pass

class NPC(Character):
    '''
    '''
    def __init__(self):
        pass

class Monster(Character):
    '''
    '''
    
    def __init__(self, monster_type):
        
        self.type = monster_type.upper()
        
        try:
            
            page_data = 1
            
        except:
            
            pass
        
        return
        
class Encounter(object):
    '''
    '''
    def __init__(self):
        pass