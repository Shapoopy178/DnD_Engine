#Import dependencies
import os
import sys
import random
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
        
        name: Name of Game for file read/write and reference purposes
        
        root_path: Root working directory for DnD_Engine instance
        
        bin_path: Subdirectory for DnD_Engine containing resources and binaries
    
    Methods:
        
        PlaySession():
            
            Create and begin session. Stores session events to log following 
            session close.
            
        ConfigureGame():
            
            Modify Game settings and metadata. 
    '''
    
    def __init__(self, name):
        '''
        Inititalize Game instance. 
        
        Sets Game name and paths.
        
        Arguments:
            
            name: string
                Name of Game for file read/write and reference purposes.
                
        Assignments:
            
            name: string
                Name of Game for file read/write and reference purposes.
                
            root_path: string, absolute path
                Root working directory for DnD_Engine instance.
            
            bin_path: string, absolute path
                Subdirectory for DnD_Engine containing resources and binaries.
            
            resources_dir: string, absolute path
                Hidden subdirectory of bin_path containing cached resources and assets.
                
            game_dir: string, absolute path
                Game files directory, containing game-specific settings and files.
                root/Games/<game_dir>
        '''
        self.name = name
        self.root_path = os.getcwd()[:-4]
        self.bin_path = os.path.join(self.root_path, 'bin')
        self.resources_dir = os.path.join(self.bin_path,'.resources')
        GAMES_DIR = os.path.join(self.root_path, 'Games')
        try:
            self.game_dir = os.path.join(GAMES_DIR, name)
            os.mkdir(self.game_dir)            
        except:
            print('Could not create game directory.')
        return 
    
    def PlaySession(self):
        '''   
        '''
        pass
    
    def ConfigureGame(self):
        pass
    
    def NewGame(self):
        
        #Create base monster manual
        self._write_monster_manual()
        
    def _write_monster_manual(self):
        
        if self._install_check_():
            
            self._init_monster_manual()
            
            return
        
        else:
            
            print('Error: Monster manual could not be found.')
        
    def _init_monster_manual(self):
        print('Initializing Monster Manual...')
        BASE_MANUAL_FNAME_W_PATH = os.path.join(self.resources_dir, '5E_mM_.xlsx')
        wb = openpyxl.load_workbook(BASE_MANUAL_FNAME_W_PATH)
        self.Workbook = wb
        self._Workbook_fname = os.path.join(self.game_dir,'Monster Manual.xlsx')
        self.Workbook.save(self._Workbook_fname)
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
        if os.path.isdir(self.resources_dir) is False:
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
    def __init__(self, name):
        self.Name = name
        self.Class = ''
        self.ProficiencyBonus = 0
        self.Level = 0
        self.Race = ''
        self.Alignment = ''
        self.Attributes = {
                'Strength'      :       0,
                'Dexterity'     :       0,
                'Constitution'  :       0,
                'Intelligence'  :       0,
                'Wisdon'        :       0,
                'Charisma'      :       0
                }
        self.SavingThrows = {
                'Strength'      :       (False, 0),
                'Dexterity'     :       (False, 0),
                'Constitution'  :       (False, 0),
                'Intelligence'  :       (False, 0),
                'Wisdon'        :       (False, 0),
                'Charisma'      :       (False, 0)
                }
        self.Skills = {
                'Acrobatics'        :       (False, 0),
                'Animal Handline'   :       (False, 0),
                'Arcana'            :       (False, 0),
                'Athletics'         :       (False, 0),
                'Deception'         :       (False, 0),
                'History'           :       (False, 0),
                'Insight'           :       (False, 0),
                'Intimidation'      :       (False, 0),
                'Investigation'     :       (False, 0),
                'Medicine'          :       (False, 0),
                'Nature'            :       (False, 0),
                'Perception'        :       (False, 0),
                'Performance'       :       (False, 0),
                'Persuasion'        :       (False, 0),
                'Religion'          :       (False, 0),
                'Sleight of Hand'   :       (False, 0),
                'Stealth'           :       (False, 0),
                'Survival'          :       (False, 0)
                }
        self.ArmorClass = 0
        self.Speed = 0
        self.HitPoints = 0
        self.HitPoints_Max = 0
        self.Darkvision = False
        self.Advantages = {}
        self.Resistances = []
        self.Disadvantages = {}
        self.Weaknesses = {}
        self.Proficiencies = {}

class PlayerCharacter(Character):
    '''
    '''
    def __init__(self, name):
        Character.__init__(self, name)
        self.Inspiration = 0
        self.Initiative = 0
        self.Background = ''
        self.PlayerName = ''
        self.Experience = 0
        self.PersonalityTraits = ''
        self.Ideals = ''
        self.Bonds = ''
        self.Flaws = ''
        self.Features = ''
        self.Traits = ''
    
    def random_character(self, level=1):
        #Currently only works for base game races
        
        self.Level = level
        
        raceList = [
                'dwarf',
                'elf',
                'halfling',
                'human',
                'dragonborn',
                'gnome',
                'half-elf',
                'half-orc',
                'tiefling']
        subraceList = {
                'dwarf'     :[],
                'elf'       :[],
                'halfling'  :[],
                'human'     :[],
                'dragonborn':[],
                'gnome'     :[],
                'half-elf'  :[],
                'half-orc'  :[],
                'tiefling'  :[]}
        alignmentList = [
                'lg',
                'ln',
                'le',
                'ng',
                'tn',
                'ne',
                'cg',
                'cn',
                'ce'
                ]
        classList = [
                'barbarian',
                'bard',
                'cleric',
                'druid',
                'fighter',
                'monk',
                'paladin',
                'ranger',
                'rogue',
                'sorcerer',
                'warlock',
                'wizard'
                ]
        
        self._roll_stats_()
        
        self.Race = _rselect_from_list(raceList)
        self._apply_race_(self.Race, self.Level)
        self.Alignment = _rselect_from_list(alignmentList)
        self.Class = _rselect_from_list(classList)
        self._recalculate_modifiers_()
        
        print(self.Name)
        print(self.Race.capitalize())
        print(self.Alignment.upper())
        print(self.Class.capitalize())
        print('Attributes:')
        for (attribute, value) in self.Attributes.items():
            print('%-15s : %-3i+%3i = %i'%(attribute,value,self.Modifiers[attribute],self.Modifiers[attribute]+value))
        
    def _apply_race_(self, race, level=1):
        
        if race == 'dwarf':
            self.Attributes['Constitution'] += 2
            self.Speed = 25
            self.Darkvision = True
    def _roll_stats_(self):
        print('Autorolling stats:')
        happy_check = False
        while happy_check == False:
            for attribute, value in list(self.Attributes.items()):
                rolls = []
                for i in range(4):
                    rolls.append(roll(6))
                rolls.sort()
                self.Attributes[attribute] = sum(rolls[-3:])
                print(attribute.capitalize(), ' : ', self.Attributes[attribute])
            happy_input = input('Happy? [N/y]')
            if happy_input.upper() == 'Y':
                happy_check = True
            else:
                print('Ungrateful bastard.')
        return
    
    def _recalculate_modifiers_(self):
        self.Modifiers = {}
        for (key, value) in self.Attributes.items():
            self.Modifiers[key] = (value-(value%2)-10)/2
    
class NPC(Character):
    '''
    '''
    def __init__(self):
        pass

class Monster(Character):
    '''
    '''
    
    def __init__(self, monster_type, name = ''):
        
        self.type = monster_type.upper()
        if not name == '':
            self.Name = name
        
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

def _install_check_():
        RESOURCE_DIR = os.path.join(os.getcwd(), '.resources')
        if os.path.isdir(RESOURCE_DIR) is False:
            return False
        else:
            return True
        
def _rselect_from_list(_list):
    listLength = len(_list) - 1
    random_selector = random.randint(0,listLength)
    selection = _list[random_selector]  
    return selection

def roll(d):
    result = random.randint(1,d)
    return result