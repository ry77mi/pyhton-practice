from datetime import datetime
import json
from random import randint
import os

class Character:
    def __init__(self, name, race, save = 1):
        if save == 1:
            self.startingStats()
            self.lvl = 1
        else:
            self.lvl = save['lvl']
            self.str = save['str']
            self.dex = save['dex']
            self.wis = save['wis']
            self.int = save['int']
            self.con = save['con']
            self.luck = save['luck']
    
    def status(self):
        pass

    #create stats for new character
    def startingStats(self, race):
        self.str = 0
        self.dex = 0
        self.wis = 0
        self.int = 0
        self.con = 0
        self.luck = 0

        if race == 'human':
            str = (randint(1, 20) + datetime.now().microsecond) % 21
            dex = (randint(1, 20) + datetime.now().microsecond) % 21
            wis = (randint(1, 20) + datetime.now().microsecond) % 21
            int = (randint(1, 20) + datetime.now().microsecond) % 21
            con = (randint(1, 20) + datetime.now().microsecond) % 21
            luck = (randint(1, 20) + datetime.now().microsecond) % 21

    


#starting menu
def menu():
    print("\tMain Menu \nType one of the following commands-\nNew Game\nLoad Game\nHelp\nQuite")
    choice = input("enter quite or continue: ").lower()
    if choice == "quite":
        return 0
    elif choice == "new game":
        return 2
    elif choice == "load game":
        return 3
    elif choice == "help":
        return 4
    else:
        return 1


#ask the user for race of new character
def newGame():
    race = ''
    print('''Character Creation
    
    Choose your starting race:
    
    Human: The most plentiful lifeform, Humans can be found in most any corner of the universe. 
    A provific race without a bloodline, Humans are evenly balanced and have limitless 
    potental.
    
    Kobold: Descendents of dragons, these weak creatures are among the lowest in power. They 
    still have a hint of the extremely powerful dragon bloodline which can be advanced by 
    killing other draconic races. Legent tells of some kobold even advancing to dragons 
    themselves.
    
    Zombie: These newly awakened undead are the starting point for all natural undead. Through 
    rituals zombies can advance on one the path to become one of the noble undead. Possible 
    paths can result in becoming a wrath, draugher, of dread lord.
    
    Ent: These creature have a natural defense that makes then increadibly hardy warriors. 
    There natural affinity for life makes them diamentrically opposed to the undead.
    ''')
    while race != 'human' and race != 'kobold' and race != 'zombie' and race != 'ent':
        race = input('Which race will youb choose to strive for the top as? Human/Kobold/Zombie/Ent').lower()
    
    name = input('What is the name of your character?: ')
    
    player = Character(name, race)
    chapters(player)



def loadGame():
    cwd = os.getcwd()
    dir = 'saves'
    path = os.path.join(cwd, dir)

    if os.path.exists(path):
        if os.listdir(path):
            files = os.listdir(path)
            length = files.len()
            for i in range(length):
                print(i + ' ' + files[i])

            saveIndex = input('Type the number of the save you would like to load: ')
            f = open(files[saveIndex])
            data = json.load(f)
            player = Character(data.name, data.race, data)
            chapters(player, data.chapter)
    
    print('no saves found')
    return 1

def chapters(player, chapter = 1):
    if chapter == 1:
        print('Chapter 1: Current')
    else:
        print('Chapter 1: Completed') 
    if chapter == 2:
        print('Chapter 2: Current')
    elif chapter < 2:
        print('Chapter 2: Locked')
    else:
        print('Chapter 2: Completed')
    if chapter == 3:
        print('Chapter 3: Current')
    elif chapter < 3:
        print('Chapter 3: Locked')
    else:
        print('Chapter 3: Completed')
    if chapter == 4:
        print('Chapter 4: Current')
    elif chapter < 4:
        print('Chapter 4: Locked')
    else:
        print('Chapter 4: Completed')
    if chapter == 5:
        print('Chapter 5: Current')
    elif chapter < 5:
        print('Chapter 5: Locked')
    else:
        print('Chapter 5: Completed')
    
    print('Continue from chapter ' + chapter)
    input('Yes/No: ')

#help menu
def help():
    print('''\n\nThis is a choose your own adventure game. Some choices will progress the story 
while others will lead down the wrong path or may disadvantage you. The game will save 
progress upon the completion of each chapter
    
    To choose an option just type in the associated number when prompted.
            
    To quite just type \'quite\' any time.
            
    To go to the menu just type in \'menu\' at any time\n''')

    while 1:
        choice = input('Please type menu to return or quite: ').lower()

        if choice == 'menu':
            return 1
        elif choice == 'quite':
            return 0


def main():
    option = 1

    while option > 0:
        match option:
            case 1:
                option = menu()
            case 2:
                option = newGame()
            case 3:
                option = loadGame()
            case 4:
                option = help()
        

main()