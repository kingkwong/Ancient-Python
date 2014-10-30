class BaseCharacter (object):
    def __init__(self,name):
        self.name = name
    def printName(self): 
        print ('Your name is ' + self.name )
       
class NPC (BaseCharacter):
    pass

class Friendly (NPC):
    pass

class Enemy (NPC):
    def __init__(self):
        self.attackDamage = 5
    def printDamage(self):
        print ('The enemy does ' + str(self.attackDamage) + ' damage')

class Weapons (BaseCharacter):
    def __init__(self, weapons):
        self.weaponsList = weapons
    def printWeapons(self):
        print ('Your weapon is a ' + self.weaponsList)

class PC (Weapons):
    pass

class Archer (PC):
    pass

class Butcher (PC):
    pass

class Green_Lantern (PC):
    pass

bc = BaseCharacter(input('Name? '))
bc.printName()
em = Enemy()
em.printDamage()
wp = Weapons(input('Weapon: '))
wp.printWeapons()


