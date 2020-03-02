import random
from AdvancedPythonConcepts.battle.classes.magic import Spell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['Attack', 'Magic', 'Items']
        self.items = items

    def generate_Damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg): # Player or Enemy to take damage
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxHP(self):
        return self.max_hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return self.hp

    def get_mp(self):
        return self.mp

    def get_maxMP(self):
        return self.max_mp

    def reduce_mp(self, cost): # Reduce the magic points
        self.mp -= int(cost)

    def chooseAction(self):
        i = 1
        print(bcolors.BOLD, "   ", self.name, bcolors.ENDC)
        for item in self.actions:
            print("     " + str(i), ":", item)
            i = i + 1

    def chooseMagic(self):
        i = 1
        for spell in self.magic:
            print("     " + str(i), ":", spell.name, "(cost:", str(spell.cost), ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n", bcolors.OKGREEN, bcolors.BOLD, "ITEMS:", bcolors.ENDC)
        for item in self.items:
            print("     " + str(i), ".", item["item"].name, ":", item["item"].desc, " (x", item["quantity"], ")")
            i += 1

    def getStats(self):
        hp_bar = ""
        mp_bar = ""
        bar_ticks = ((self.hp/self.max_hp)*100)/4
        mp_ticks = ((self.mp / self.max_mp) * 100) / 10
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while len(mp_bar) < 10:
            hp_bar += " "

        print(bcolors.BOLD + self.name + ":      "
              + str(self.hp) + "/" + str(self.max_hp) + " |" + bcolors.OKGREEN
              + hp_bar + bcolors.ENDC + "|       "
              + bcolors.BOLD + str(self.mp) + "/" + str(self.max_mp) + bcolors.ENDC
              + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")