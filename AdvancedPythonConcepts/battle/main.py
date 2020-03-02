from AdvancedPythonConcepts.battle.classes.game import Person,bcolors
from AdvancedPythonConcepts.battle.classes.magic import Spell
from AdvancedPythonConcepts.battle.classes.inventory import Item

# print("\n\n")
# print("NAME                                HP                                       MP")
# print("                                    _________________________                ______________")
# print(bcolors.BOLD, "Valos:       460/460 |                         |          65/65 |██████████████|")
#
# print("                      _________________________                ______________")
# print("Valos:       460/460 |                         |        65/65 |              |")
#
# print("                      _________________________                ______________")
# print("Valos:       460/460 |                         |        65/65 |              |")
#
# print("\n\n")

# Create Black Magic
fire = Spell("Fire", 10, 100, "Black Magic")
thunder = Spell("Thunder", 10, 100, "Black Magic")
blizzard = Spell("Blizzard", 10, 100, "Black Magic")
meteor = Spell("Meteor", 20, 200, "Black Magic")
quake = Spell("Quake", 14, 140, "Black Magic")

# Create White Magic
cure = Spell("Cure", 12, 120, "White Magic")
cura = Spell("Cura", 18, 200, "White Magic")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi - Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super - Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
highelixir = Item("Mega - Elixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 HP of damage", 500)

# player_magic = [{"name":"Fire", "cost": 10, "dmg": 100},
#          {"name":"Thunder", "cost": 10, "dmg": 124},
#          {"name":"Blizzard", "cost": 10, "dmg": 100}]    # THis is an array of dictionaries

player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixir, "quantity": 5},
                {"item": highelixir, "quantity": 2},
                {"item": grenade, "quantity": 5}]

player1 = Person('Valos', 3260, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura], player_items)
player2 = Person('Nick1', 4160, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura], player_items)
player3 = Person('Rober', 3089, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura], player_items)
enemy = Person('Enemy1', 1200, 65, 215, 23, [], [])

players = [player1, player2, player3]

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!!" + bcolors.ENDC)

running = True
while running:
    print(bcolors.BOLD, "NAME                              HP                            MP", bcolors.ENDC)
    for player in players:
        player.getStats()

    print('\n')

    for player in players:
        player.chooseAction()
        choice = input("Choose Action: ")

        index = int(choice) - 1
        if index == 0:
            dmg = player.generate_Damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
        elif index == 1:
            player.chooseMagic()
            magic_Choice = int(input("Select Magic to inflict damage:")) - 1

            # magic_dmg = player.generate_spell_damage(magic_Choice)
            # spell = player.get_spell_name(magic_Choice)
            # cost = player.get_spell_mp_cost(magic_Choice)
            if magic_Choice == -1:
                continue

            spell = player.magic[magic_Choice]
            magic_dmg = spell.generate_spell_damage()

            current_mp = player.get_mp()
            if spell.cost > current_mp :
                print(bcolors.FAIL + "\n Not enough MP" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)
            if spell.type == "White Magic":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE, "\n", spell.name, " heals for", str(magic_dmg), "HP.", bcolors.ENDC)
            else:
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n", spell, " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
                print("You attacked for", magic_dmg, "points of damage. Enemy HP:", enemy.get_hp())

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Select Item: ")) - 1

            if item_choice == -1:
                continue

            # item = player.items[item_choice]
            item = player.items[item_choice]['item']
            if player.items[item_choice]['quantity'] == 0:
                print(bcolors.FAIL, "\n", "None Left....", bcolors.ENDC)
                continue

            player.items[item_choice]['quantity'] = player.items[item_choice]['quantity'] - 1  #Reduce the quantity

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN, "\n", item.name, " heals for", str(item.prop), "HP", bcolors.ENDC)
            elif item.type == "elixir":
                player.hp = player.max_hp
                player.mp = player.max_mp
                print(bcolors.OKGREEN, "\n", item.name, " fully restores HP/MP", bcolors.ENDC)
            elif item.type == 'attack':
                enemy.take_damage(item.prop)
                print(bcolors.FAIL, "\n", " deals", str(item.prop), "points of damage", bcolors.ENDC)


    enemy_choice = 1
    enemy_damage = enemy.generate_Damage()
    player1.take_damage(enemy_damage)
    print("Enemy attacked for", enemy_damage, "points of damage. Player HP:", player.get_hp())

    print("======================")
    print("Enemy HP:" , bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxHP()) + bcolors.ENDC)
    # print("Your HP:", bcolors.OKGREEN, str(player.get_hp()), "/", str(player.get_maxHP()), bcolors.ENDC)
    # print("Your MP:", bcolors.OKBLUE, str(player.get_mp()), "/", str(player.get_maxMP()), bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You Lost" + bcolors.ENDC)
        running = False