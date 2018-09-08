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
        self.Size = 1
        self.Attributes = {
                'strength'      :       0,
                'dexterity'     :       0,
                'constitution'  :       0,
                'intelligence'  :       0,
                'wisdon'        :       0,
                'charisma'      :       0
                }
        #Bool is proficiency check, int is modifier
        self.SavingThrows = {
                'strength'      :       (False, 0),
                'dexterity'     :       (False, 0),
                'constitution'  :       (False, 0),
                'intelligence'  :       (False, 0),
                'wisdon'        :       (False, 0),
                'charisma'      :       (False, 0)
                }
        # Bool is proficiency check, int is modifier
        self.Skills = {
                'acrobatics'        :       (False, 0),
                'animal handline'   :       (False, 0),
                'arcana'            :       (False, 0),
                'athletics'         :       (False, 0),
                'deception'         :       (False, 0),
                'history'           :       (False, 0),
                'insight'           :       (False, 0),
                'intimidation'      :       (False, 0),
                'investigation'     :       (False, 0),
                'medicine'          :       (False, 0),
                'nature'            :       (False, 0),
                'perception'        :       (False, 0),
                'performance'       :       (False, 0),
                'persuasion'        :       (False, 0),
                'religion'          :       (False, 0),
                'sleight of hand'   :       (False, 0),
                'stealth'           :       (False, 0),
                'survival'          :       (False, 0)
                }
        self.ArmorClass = 0
        self.Speed = 0
        self.HitPoints = 0
        self.HitPoints_Max = 0
        self.Languages = []
        self.Darkvision = False
        self.Advantages = {
                'saving throws' :   []
                }
        self.Resistances = []
        self.Disadvantages = {}
        self.Weaknesses = {}
        self.Proficiencies = {
                'weapons'       :   [],
                'armor'         :   [],
                'tools'         :   [],
                'instruments'   :   [],
                'vehicles'      :   [],
                }
        self.Spellbook = {
                'cantrips'  :   [],
                'spells'    :   [],
                'other'     :   []
                }

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
        
        subraceDict = {
                'dwarf'     :[
                        'hill dwarf',
                        'mountain dwarf'
                        ],
                'elf'       :[
                        'high elf',
                        'wood elf',
                        'dark elf'
                        ],
                'halfling'  :[
                        'lightfoot',
                        'stout'
                        ],
                'human'     :[
                        'human'
                        ],
                'dragonborn':[
                        'black',
                        'blue',
                        'brass',
                        'bronze',
                        'copper',
                        'gold',
                        'green',
                        'red',
                        'silver',
                        'white'
                        ],
                'gnome'     :[
                        'forest gnome',
                        'rock gnome'
                        ],
                'half-elf'  :[],
                'half-orc'  :[],
                'tiefling'  :[]
                }
        
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
        
        backgroundList = [
                'acolyte',
                'charlatan',
                'criminal',
                'entertainer',
                'folk hero',
                'guild artisan',
                'hermit',
                'noble',
                'outlander',
                'sage',
                'sailor',
                'urchin'
                ]
        
        self._roll_stats_()
        
        self.Race = _rselect_from_list(raceList)
        self.__random_race_proficiency__(self.Race)
        self.Subrace = _rselect_from_list(subraceDict[self.Race])
        self.Alignment = _rselect_from_list(alignmentList)
        self.Class = _rselect_from_list(classList)
        self.Background = _rselect_from_list(backgroundList)
        
        self._apply_race_(self.Race, self.Level)
        self._apply_subrace_(self.Subrace, self.Level)
        self._apply_background_(self.Background)
        self._apply_class_(self.Class)
        self._set_proficiency_bonus_(self.Level)
        self._recalculate_modifiers_()
        
        print(self.Name)
        print(self.Race.capitalize())
        print(self.Alignment.upper())
        print(self.Class.capitalize())
        print('Attributes:')
        for (attribute, value) in self.Attributes.items():
            print('%-15s : %-3i'%(attribute.capitalize(),value))
        
    def __random_race_proficiency__(self, race):
        
        proficiencyDict = {
                'dwarf'     :   [
                        "smith's tools",
                        "brewer's tolls",
                        "mason's tools"],
                'elf'       :   [
                        ]
                }
        
        return
    
    def _apply_race_(self, race, level=1):
        
        if race == 'dwarf':
            self.Attributes['constitution'] += 2
            self.Size = 2
            self.Speed = 25
            self.Darkvision = True
            for prof in ['battleaxe', 'handaxe', 'light hammer', 'warhammer']:
                soft_append(self.Proficiencies['weapons'], prof)
            soft_append(self.Resistances, 'poison')
            soft_append(self.Advantages['saving throws'], 'poison')
            for language in ['common', 'dwarvish']:
                soft_append(self.Languages, language)

        elif race == 'elf':
            self.Attributes['dexterity'] += 2
            self.Size = 2
            self.Speed = 30
            self.Darkvision = True
            self.Skills['perception'][0] = True
            for language in ['common', 'elvish']:
                soft_append(self.Languages, language)
                
        elif race == 'halfling':
            self.Attributes['dexterity'] += 2
            self.Size = 1 #Small
            self.Speed = 25
            #!!!Lucky
            soft_append(self.Advantages['saving throws'],'fear')
            #!!!Halfling nimbleness
            for language in ['common', 'halfling']:
                soft_append(self.Languages, language)
            
        elif race == 'human':
            for attribute in self.Attributes.keys():
                self.Attributes[attribute] += 1
            self.Size = 2 #Medium
            self.Speed  = 30
            soft_append(self.Languages, 'common')
            #!!!1 additional language of choice
            
        elif race == 'dragonborn':
            self.Attributes['strength'] += 2
            self.Attributes['charisma'] += 1
            self.Size = 2
            self.Speed = 30
            soft_append(self.Spellbook['other'], 'breath weapon')
            for language in ['common', 'draconic']:
                soft_append(self.Languages, language)
                
        elif race == 'gnome':
            self.Attributes['intelligence'] += 2
            self.Size = 1
            self.Speed = 25
            self.Darkvision = True
            for ad in ['intelligence - magic', 'wisdom - magic', 'charisma - magic']:
                soft_append(self.Advantages['saving throws'], ad)
            for language in ['common', 'gnomish']:
                soft_append(self.Languages, language)
        
        elif race == 'half-elf':
            self.Attributes['charisma'] += 2
            #111 2 additional attributes of choice
            self.Size = 2
            self.Speed = 30
            self.Darkvision = True
            soft_append(self.Advantages['saving throws'], 'charm')
        
            #!!! Skill Versatility
            for language in ['common', 'elvish']:
                soft_append(self.Languages, language)
                #!!! One additional language of choice
        
        elif race == 'half-orc':
            self.Attributes['strength'] += 2
            self.Attributes['constitution'] += 1
            self.Size = 2
            self.Speed = 30
            self.Darkvision = True
            self.Skills['intimidation'][0] = True
            #!!! Relentless Endurance
            #!!! Savage Attacks
            for language in ['common', 'orc']:
                soft_append(self.Languages, language)
        
        elif race == 'tiefling':
            self.Attributes['intelligence'] += 1
            self.Attributes['charisma'] += 2
            self.Size = 2
            self.Speed = 30
            self.Darkvision = True
            soft_append(self.Resistances, 'fire')
            soft_append(self.Spellbook['cantrips'], 'thaumaturgy')
            if level >= 3:
                soft_append(self.Spellbook['spells'], 'hellish rebuke')
            if level >= 5:
                soft_append(self.Spellbook['spells'], 'darkness')
            for language in ['common', 'infernal']:
                soft_append(self.Languages, language)
            
    def _apply_subrace_(self, subrace, level):
        
        if self.Race == 'dwarf':
        
            if subrace == 'hill dwarf':
                self.Attributes['wisdom'] += 1
                self.HitPoints_Max += level
                
            elif subrace == 'mountain dwarf':
                self.Attributes['strength'] += 2
                self.Proficiencies
                
            else:
                print('Unrecognized subrace. No modifiers applied.')
                
        elif self.Race == 'elf':        
            
            if subrace == 'high elf':
                self.Attributes['intelligence'] += 1
                for prof in ['lognsword', 'shortsword', 'shortbow', 'longbow']:
                    soft_append(self.Proficiencies['weapons'], prof)
                #!!!Also add 1 cantrip of choice
                #!!!Also add 1 language of choice
                
            elif subrace == 'wood elf':
                self.Attributes['wisdon'] += 1
                for prof in ['lognsword', 'shortsword', 'shortbow', 'longbow']:
                    soft_append(self.Proficiencies['weapons'], prof)
                self.Speed = 35
                #!!!Also Mask of the Wild
                
            elif subrace == 'dark elf':
                self.Attributes['charisma'] += 1
                self.Darkvision = True      #!!!Actually should be enhanced darkvision, change later
                #!!!Sunlight Sensitivity
                soft_append(self.Spellbook['cantrips'], 'dancing lights')
                if level >= 3:
                    soft_append(self.Spellbook['spells'], 'faerie fire')
                if level >=5:
                    soft_append(self.Spellbook['spells'], 'darkness')
                for prof in ['rapier', 'shortsword', 'crossbow']:
                    soft_append(self.Proficiencies['weapons'], prof)
                    
        elif self.Race == 'halfling':
            
            if subrace == 'lightfoot':
                self.Attributes['charisma'] += 1
                #!!!Naturally stealthy
                
            elif subrace == 'stout':
                self.Attributes['constitution'] += 1
                soft_append(self.Resistances, 'poison')
                soft_append(self.Advantages['saving throws'], 'poison')
                
        elif self.Race == 'human':
            pass
        
        elif self.Race == 'dragonborn':
            
            if subrace == 'black':
                soft_append(self.Resistances, 'acid')
            elif subrace == 'blue':
                soft_append(self.Resistances, 'lightning')
            elif subrace == 'brass':
                soft_append(self.Resistances, 'fire')
            elif subrace == 'bronze':
                soft_append(self.Resistances, 'lightning')
            elif subrace == 'bronze':
                soft_append(self.Resistances, 'acid')
            elif subrace == 'gold':
                soft_append(self.Resistances, 'fire')
            elif subrace == 'green':
                soft_append(self.Resistances, 'poison')
            elif subrace == 'red':
                soft_append(self.Resistances, 'fire')
            elif subrace == 'silver':
                soft_append(self.Resistances, 'cold')
            elif subrace == 'white':
                soft_append(self.Resistances, 'cold')
                
        elif self.Race == 'gnome':
            
            if subrace == 'forest gnome':
                self.Attributes['dexterity'] += 1
                soft_append(self.Spellbook['cantrips'], 'minor illusion')
                soft_append(self.Languages, 'small beasts')
                
            elif subrace == 'rock gnome':
                self.Attributes['constitution'] += 1
                #!!! Artificier's Lore
                soft_append(self.Proficiencies['tools'], "tinker's tools")
                    #!!! Additional Tinker buffs
            
        elif self.Race == 'half-elf':
            pass
        
        elif self.Race == 'half-orc':
            pass
        
        elif self.Race == 'tiefling':
            pass
            
    def _apply_background_(self, background):
        return
    
    def _apply_class_(self, _class):
        pass
        return

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
                print('Ungrateful shit.')
        return
    
    def _set_proficiency_bonus_(self, level):
        if level == 1:
            self.ProficiencyBonus = 2
        else:
            self.ProficiencyBonus = 0
            
        return
    
    def _recalculate_modifiers_(self):
        self.Modifiers = {}
        for (key, value) in self.Attributes.items():
            self.Modifiers[key] = (value-(value%2)-10)/2

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
    
        return
    
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
    try:
        random_selector = random.randint(0,listLength)
    except ValueError:
        return None
    selection = _list[random_selector]  
    return selection

def roll(d):
    result = random.randint(1,d)
    return result

def soft_append(lst, addendum):
    if addendum not in lst:
        lst.append(addendum)
    return