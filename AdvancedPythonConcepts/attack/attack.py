# import random
#
# class Enemy:  # Class Creation Basics
#     atkl = 60
#     atkh = 80
#
#     def __init__(self, atkl, atkh):
#         self.atkl = atkl
#         self.atkh = atkh
#
#     def getAtk(self):
#         print(self.atkl)
#
# enemy1 = Enemy(40, 49)
# enemy2 = Enemy(75, 90)
# enemy1.getAtk()
# enemy2.getAtk()

# playerHP = 260
# enemyatklow = 60
# enemyatkhigh = 80
#
# while playerHP > 0:
#     dmg = random.randrange(enemyatklow, enemyatkhigh)
#     playerHP = playerHP - dmg
#     if playerHP <= 30:
#         playerHP = 30
#     print('Damage given:', dmg, 'Player HP Current:', playerHP)
#
#     if playerHP > 30:
#         continue
#
#     print("You have been teleported to the nearest medical centre")
#     break

from AdvancedPythonConcepts.attack.classes.enemy import Enemy

enemy = Enemy(200, 30)
print("HP:", enemy.get_hp())

