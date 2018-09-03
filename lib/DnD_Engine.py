import os

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
        pass
    
    def PlaySession(self):
        pass
    
    def ConfigureGame(self):
        pass
    
    def NewGame(self):
        
        #Create base monster manual
        self._write_monster_manual('default')
        
    def _write_monster_manual(mode = ''):
        
        manual_fname = os.path.join(self.path, 'bin', 'monsterManual.txt')
    
class Session(object):
    '''
    '''

class Character(object):
    '''
    '''

class PlayerCharacter(Character):
    '''
    '''

class NPC(Character):
    '''
    '''

class Monster(Character):
    '''
    '''
    
    def __init__(self, monster_type):
        
        self.type = monster_type.upper()
        
        try:
            
            page_data = 1
        
        

class Encounter(object):
    '''
    '''
    def __init__(self):
        pass