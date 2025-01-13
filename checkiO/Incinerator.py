# 1
# class Warrior:
#     health = 50
#     attack = 5
#     is_alive = True
#
# class Knight(Warrior):
#     attack = Warrior.attack+2
#
# def fight(unit_1, unit_2):
#     attacker = unit_1
#     defender = unit_2
#     while unit_1.is_alive and unit_2.is_alive:
#         defender.health -= attacker.attack
#         defender.is_alive = defender.health > 0
#         attacker, defender = defender, attacker
#     return unit_1.is_alive
#
# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# dave = Warrior()
# mark = Warrior()
#
# print(fight(chuck, bruce))
# print(fight(dave, carl))
# print(chuck.is_alive)
# print(bruce.is_alive)
# print(carl.is_alive)
# print(dave.is_alive)
# print(fight(carl, mark))
# print(carl.is_alive)

# 2
# class Warrior:
#     health = 50
#     attack = 5
#     is_alive = True

# class Knight(Warrior):
#     attack = Warrior.attack+2
#
# class Army():
#     warriors = []
#     def __init__(self):
#         self.warriors = []
#     def add_units(self, unit, number):
#         for i in range(number):
#             self.warriors.append(unit())
#
# class Battle():
#     def fight(self, army_1, army_2):
#         first_unit = army_1.warriors.pop(0)
#         second_unit = army_2.warriors.pop(0)
#         while True:
#             first_win = fight(first_unit, second_unit)
#             if(army_1.warriors == [] and not first_win) or (army_2.warriors == [] and first_win):
#                 break
#             if first_win:
#                 second_unit = army_2.warriors.pop(0)
#             else:
#                 first_unit = army_1.warriors.pop(0)
#         return first_win
#
#
# def fight(unit_1, unit_2):
#     attacker = unit_1
#     defender = unit_2
#     while unit_1.is_alive and unit_2.is_alive:
#         defender.health -= attacker.attack
#         defender.is_alive = defender.health > 0
#         attacker, defender = defender, attacker
#     return unit_1.is_alive
# #
# # my_army = Army()
# # my_army.add_units(Knight, 3)
# #
# # enemy_army = Army()
# # enemy_army.add_units(Warrior, 3)
# #
# # army_3 = Army()
# # army_3.add_units(Warrior, 20)
# # army_3.add_units(Knight, 5)
# #
# # army_4 = Army()
# # army_4.add_units(Warrior, 30)
# #
# # battle = Battle()
# # print(battle.fight(my_army, enemy_army))
# # print(battle.fight(army_3, army_4))
#
# army_1 = Army()
# army_2 = Army()
# army_1.add_units(Warrior, 10)
# army_2.add_units(Warrior, 11)
# battle = Battle()
# print(battle.fight(army_1, army_2))

# class Warrior:
#     health = 50
#     attack = 5
#     defense = 0
#     vampirism = 0
#     is_alive = True
#
# class Knight(Warrior):
#     attack = 7
#
# class Defender(Warrior):        #3
#     health = 60
#     attack = 3
#     defense = 2
#
# class Vampire(Warrior):         #4
#     health = 40
#     attack = 4
#     vampirism = 50
#
# class Lancer(Warrior):          #5
#     attack = 6
#
# class Healer(Warrior):          #6
#     attack = 0
#     health = 60
#     def heal(self, warrior):
#         warrior.health += 2
#         if warrior.health>type(warrior).health:
#             warrior.health = type(warrior).health
#
# class Army():
#     warriors = []
#     def __init__(self):
#         self.warriors = []
#     def add_units(self, unit, number):
#         for i in range(number):
#             self.warriors.append(unit())
#
# class Battle():
#     def fight(self, army_1, army_2):
#         first_unit = army_1.warriors.pop(0)
#         second_unit = army_2.warriors.pop(0)
#         while True:
#             first_win = fight(first_unit, second_unit,allie_army=army_1.warriors, enemies_army=army_2.warriors)
#             if(army_1.warriors == [] and not first_win) or (army_2.warriors == [] and first_win):
#                 break
#             if first_win:
#                 second_unit = army_2.warriors.pop(0)
#             else:
#                 first_unit = army_1.warriors.pop(0)
#         return first_win
#
#
# def fight(unit_1, unit_2, enemies_army=[], allie_army = []):
#     attacker = unit_1
#     defender = unit_2
#     while unit_1.is_alive and unit_2.is_alive:
#         if enemies_army != [] and type(attacker) == Lancer:
#             if int(attacker.attack*0.5) > enemies_army[0].defense:
#                 enemies_army[0].health -= (int(attacker.attack*0.5) - defender.defense)
#             # army2[0] -= 0
#         if allie_army != [] and type(allie_army[0]) == Healer:
#             allie_army[0].heal(attacker)
#         if attacker.attack > defender.defense:
#             defender.health -= (attacker.attack - defender.defense)
#             attacker.health += round((attacker.attack - defender.defense)*attacker.vampirism/100)
#         defender.is_alive = defender.health > 0
#         attacker, defender = defender, attacker
#         enemies_army,allie_army = allie_army, enemies_army
#     return unit_1.is_alive

# unit_1 = Defender()
# unit_2 = Warrior()
# print(type(unit_1) == Defender)
# fight(unit_1, unit_2)
# print(unit_1.health)

# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# dave = Warrior()
# mark = Warrior()
# bob = Defender()
# mike = Knight()
# rog = Warrior()
# lancelot = Defender()
# eric = Vampire()
# adam = Vampire()
# richard = Defender()
# ogre = Warrior()
# freelancer = Lancer()
# vampire = Vampire()
#
# print(fight(chuck, bruce) == True,
# fight(dave, carl) == False,
# chuck.is_alive == True,
# bruce.is_alive == False,
# carl.is_alive == True,
# dave.is_alive == False,
# fight(carl, mark) == False,
# carl.is_alive == False,
# fight(bob, mike) == False,
# fight(lancelot, rog) == True,
# fight(eric, richard) == False,
# fight(ogre, adam) == True,
# fight(freelancer, vampire) == True,
# freelancer.is_alive == True)
#
# my_army = Army()
# my_army.add_units(Defender, 2)
# my_army.add_units(Vampire, 2)
# my_army.add_units(Lancer, 4)
# my_army.add_units(Warrior, 1)
#
# enemy_army = Army()
# enemy_army.add_units(Warrior, 2)
# enemy_army.add_units(Lancer, 2)
# enemy_army.add_units(Defender, 2)
# enemy_army.add_units(Vampire, 3)
#
# army_3 = Army()
# army_3.add_units(Warrior, 1)
# army_3.add_units(Lancer, 1)
# army_3.add_units(Defender, 2)
#
# army_4 = Army()
# army_4.add_units(Vampire, 3)
# army_4.add_units(Warrior, 1)
# army_4.add_units(Lancer, 2)
#
# battle = Battle()
#
# print(battle.fight(my_army, enemy_army) == True)
# print(battle.fight(army_3, army_4) == False)

# army_warrior = Army()
# army_lancer = Army()
# army_warrior.add_units(Warrior,2)
# army_lancer.add_units(Lancer,1)
# army_lancer.add_units(Warrior, 1)
# battle = Battle()
# print(battle.fight(army_warrior, army_lancer))

#
# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# dave = Warrior()
# mark = Warrior()
# bob = Defender()
# mike = Knight()
# rog = Warrior()
# lancelot = Defender()
# eric = Vampire()
# adam = Vampire()
# richard = Defender()
# ogre = Warrior()
# freelancer = Lancer()
# vampire = Vampire()
# priest = Healer()
#
# print(fight(chuck, bruce) == True,
# fight(dave, carl) == False,
# chuck.is_alive == True,
# bruce.is_alive == False,
# carl.is_alive == True,
# dave.is_alive == False,
# fight(carl, mark) == False,
# carl.is_alive == False,
# fight(bob, mike) == False,
# fight(lancelot, rog) == True,
# fight(eric, richard) == False,
# fight(ogre, adam) == True,
# fight(freelancer, vampire) == True,
# freelancer.is_alive == True,
# freelancer.health == 14,
# priest.heal(freelancer),
# freelancer.health == 16)
#
# my_army = Army()
# my_army.add_units(Defender, 2)
# my_army.add_units(Healer, 1)
# my_army.add_units(Vampire, 2)
# my_army.add_units(Lancer, 2)
# my_army.add_units(Healer, 1)
# my_army.add_units(Warrior, 1)
#
# enemy_army = Army()
# enemy_army.add_units(Warrior, 2)
# enemy_army.add_units(Lancer, 4)
# enemy_army.add_units(Healer, 1)
# enemy_army.add_units(Defender, 2)
# enemy_army.add_units(Vampire, 3)
# enemy_army.add_units(Healer, 1)
#
# army_3 = Army()
# army_3.add_units(Warrior, 1)
# army_3.add_units(Lancer, 1)
# army_3.add_units(Healer, 1)
# army_3.add_units(Defender, 2)
#
# army_4 = Army()
# army_4.add_units(Vampire, 3)
# army_4.add_units(Warrior, 1)
# army_4.add_units(Healer, 1)
# army_4.add_units(Lancer, 2)
#
# battle = Battle()
#
# print(battle.fight(my_army, enemy_army) == False)
# print(battle.fight(army_3, army_4) == True)


# 7&8
# class Weapon:
#     health = 0
#     attack = 0
#     attack = 0
#     defense = 0
#     vampirism = 0
#     heal_power = 0
#     def __init__(self, health=None, attack=None, defense=None, vampirism=None, heal_power=None):
#         if health is not None:
#             self.health = health
#         if attack is not None:
#             self.attack = attack
#         if defense is not None:
#             self.defense = defense
#         if vampirism is not None:
#             self.vampirism = vampirism
#         if heal_power is not None:
#             self.heal_power = heal_power
#
# class Sword(Weapon):
#     health = 5
#     attack = 2
#
# class Shield(Weapon):
#     health = 20
#     attack = -1
#     defense = 2
# class GreatAxe(Weapon):
#     health = -15
#     attack = 5
#     defense = -2
#     vampirism = 10
# class Katana(Weapon):
#     health = -20
#     attack = 6
#     defense = -5
#     vampirism = 50
# class MagicWand(Weapon):
#     health = 30
#     attack = 3
#     heal_power = 3
#
# class Warrior:
#     health = 50
#     attack = 5
#     defense = False
#     vampirism = False
#     heal_power = False
#     is_alive = True
#     weapon = Weapon()
#     def equip_weapon(self, weapon_name):
#         self.weapon = weapon_name
#         self.health+=weapon_name.health
#         self.attack+=weapon_name.attack
#         if type(self.defense) != bool:
#             self.defense+=weapon_name.defense
#             if self.defense<0:
#                 self.defense=0
#         if type(self.vampirism) != bool:
#             self.vampirism+= weapon_name.vampirism
#             if self.vampirism<0:
#                 self.vampirism=0
#         if type(self.heal_power) != bool:
#             self.heal_power+= weapon_name.heal_power
#             if self.heal_power<0:
#                 self.heal_power=0
#
#
# class Knight(Warrior):
#     attack = 7
#
# class Defender(Warrior):        #3
#     health = 60
#     attack = 3
#     defense = 2
#
# class Vampire(Warrior):         #4
#     health = 40
#     attack = 4
#     vampirism = 50
#
# class Lancer(Warrior):          #5
#     attack = 6
#
# class Healer(Warrior):          #6
#     attack = 0
#     health = 60
#     heal_power = 2
#     def heal(self, warrior):
#         warrior.health += self.heal_power
#         if warrior.health > (type(warrior).health+int(warrior.weapon.health)):
#             warrior.health = type(warrior).health+int(warrior.weapon.health)
#
# class Army():
#     units = []
#     def __init__(self):
#         self.units = []
#     def add_units(self, unit, number):
#         for i in range(number):
#             self.units.append(unit())
#
# class Battle():
#     def fight(self, army_1, army_2):
#         first_unit = army_1.units.pop(0)
#         second_unit = army_2.units.pop(0)
#         while True:
#             first_win = fight(first_unit, second_unit, allie_army=army_1.units, enemies_army=army_2.units)
#             if(army_1.units == [] and not first_win) or (army_2.units == [] and first_win):
#                 break
#             if first_win:
#                 second_unit = army_2.units.pop(0)
#             else:
#                 first_unit = army_1.units.pop(0)
#         return first_win
#     def straight_fight(self, army_1, army_2):
#         allie_army = army_1.units
#         enemies_army = army_2.units
#         while allie_army!=[] and enemies_army!=[]:
#             for i in range(min(len(allie_army), len(enemies_army))):
#                 fight(allie_army[i],enemies_army[i])
#             allie_army = [unit for unit in allie_army if unit.is_alive]
#             enemies_army = [unit for unit in enemies_army if unit.is_alive]
#         return allie_army!=[]
#
#
# def fight(unit_1, unit_2, enemies_army=[], allie_army = []):
#     attacker = unit_1
#     defender = unit_2
#     while unit_1.is_alive and unit_2.is_alive:
#         if enemies_army != [] and type(attacker) == Lancer:
#             if int(attacker.attack*0.5) > int(enemies_army[0].defense):
#                 enemies_army[0].health -= (int(attacker.attack*0.5) - int(defender.defense))
#             # army2[0] -= 0
#         if allie_army != [] and type(allie_army[0]) == Healer:
#             allie_army[0].heal(attacker)
#         if attacker.attack > int(defender.defense):
#             defender.health -= (attacker.attack - int(defender.defense))
#             attacker.health += int((attacker.attack - int(defender.defense))*int(attacker.vampirism)/100)
#             if attacker.health > (type(attacker).health+int(attacker.weapon.health)):
#                 attacker.health = type(attacker).health + int(attacker.weapon.health)
#         defender.is_alive = defender.health > 0
#         attacker, defender = defender, attacker
#         enemies_army,allie_army = allie_army, enemies_army
#     return unit_1.is_alive


# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# dave = Warrior()
# mark = Warrior()
# bob = Defender()
# mike = Knight()
# rog = Warrior()
# lancelot = Defender()
# eric = Vampire()
# adam = Vampire()
# richard = Defender()
# ogre = Warrior()
# freelancer = Lancer()
# vampire = Vampire()
# priest = Healer()
#
# print(fight(chuck, bruce) == True,
# fight(dave, carl) == False,
# chuck.is_alive == True,
# bruce.is_alive == False,
# carl.is_alive == True,
# dave.is_alive == False,
# fight(carl, mark) == False,
# carl.is_alive == False,
# fight(bob, mike) == False,
# fight(lancelot, rog) == True,
# fight(eric, richard) == False,
# fight(ogre, adam) == True,
# fight(freelancer, vampire) == True,
# freelancer.is_alive == True,
# freelancer.health == 14,
# priest.heal(freelancer),
# freelancer.health == 16)
#
# my_army = Army()
# my_army.add_units(Defender, 2)
# my_army.add_units(Healer, 1)
# my_army.add_units(Vampire, 2)
# my_army.add_units(Lancer, 2)
# my_army.add_units(Healer, 1)
# my_army.add_units(Warrior, 1)
#
# enemy_army = Army()
# enemy_army.add_units(Warrior, 2)
# enemy_army.add_units(Lancer, 4)
# enemy_army.add_units(Healer, 1)
# enemy_army.add_units(Defender, 2)
# enemy_army.add_units(Vampire, 3)
# enemy_army.add_units(Healer, 1)
#
# army_3 = Army()
# army_3.add_units(Warrior, 1)
# army_3.add_units(Lancer, 1)
# army_3.add_units(Healer, 1)
# army_3.add_units(Defender, 2)
#
# army_4 = Army()
# army_4.add_units(Vampire, 3)
# army_4.add_units(Warrior, 1)
# army_4.add_units(Healer, 1)
# army_4.add_units(Lancer, 2)
#
# army_5 = Army()
# army_5.add_units(Warrior, 10)
#
# army_6 = Army()
# army_6.add_units(Warrior, 6)
# army_6.add_units(Lancer, 5)
#
# battle = Battle()
#
# print(battle.fight(my_army, enemy_army) == False)
# print(battle.fight(army_3, army_4) == True)
# print(battle.straight_fight(army_5, army_6) == False)

# ogre = Warrior()
# lancelot = Knight()
# richard = Defender()
# eric = Vampire()
# freelancer = Lancer()
# priest = Healer()
#
# sword = Sword()
# shield = Shield()
# axe = GreatAxe()
# katana = Katana()
# wand = MagicWand()
# super_weapon = Weapon(50, 10, 5, 150, 8)
#
# ogre.equip_weapon(sword)
# ogre.equip_weapon(shield)
# ogre.equip_weapon(super_weapon)
# lancelot.equip_weapon(super_weapon)
# richard.equip_weapon(shield)
# eric.equip_weapon(super_weapon)
# freelancer.equip_weapon(axe)
# freelancer.equip_weapon(katana)
# priest.equip_weapon(wand)
# priest.equip_weapon(shield)
#
# print(ogre.health == 125,
# lancelot.attack == 17,
# richard.defense == 4,
# eric.vampirism == 200,
# freelancer.health == 15,
# priest.heal_power == 5,
#
# fight(ogre, eric) == False,
# fight(priest, richard) == False,
# fight(lancelot, freelancer) == True)
#
# my_army = Army()
# my_army.add_units(Knight, 1)
# my_army.add_units(Lancer, 1)
#
# enemy_army = Army()
# enemy_army.add_units(Vampire, 1)
# enemy_army.add_units(Healer, 1)
#
# my_army.units[0].equip_weapon(axe)
# my_army.units[1].equip_weapon(super_weapon)
#
# enemy_army.units[0].equip_weapon(katana)
# enemy_army.units[1].equip_weapon(wand)
#
# battle = Battle()
#
# print(battle.fight(my_army, enemy_army) == True)

# 9

# class Weapon:
#     health = 0
#     attack = 0
#     attack = 0
#     defense = 0
#     vampirism = 0
#     heal_power = 0
#     def __init__(self, health=None, attack=None, defense=None, vampirism=None, heal_power=None):
#         if health is not None:
#             self.health = health
#         if attack is not None:
#             self.attack = attack
#         if defense is not None:
#             self.defense = defense
#         if vampirism is not None:
#             self.vampirism = vampirism
#         if heal_power is not None:
#             self.heal_power = heal_power
#
# class Sword(Weapon):
#     health = 5
#     attack = 2
#
# class Shield(Weapon):
#     health = 20
#     attack = -1
#     defense = 2
# class GreatAxe(Weapon):
#     health = -15
#     attack = 5
#     defense = -2
#     vampirism = 10
# class Katana(Weapon):
#     health = -20
#     attack = 6
#     defense = -5
#     vampirism = 50
# class MagicWand(Weapon):
#     health = 30
#     attack = 3
#     heal_power = 3
#
# class Warrior:
#     health = 50
#     attack = 5
#     defense = False
#     vampirism = False
#     heal_power = False
#     is_alive = True
#     weapon = Weapon()
#     def equip_weapon(self, weapon_name):
#         self.weapon = weapon_name
#         self.health+=weapon_name.health
#         self.attack+=weapon_name.attack
#         if type(self.defense) != bool:
#             self.defense+=weapon_name.defense
#             if self.defense<0:
#                 self.defense=0
#         if type(self.vampirism) != bool:
#             self.vampirism+= weapon_name.vampirism
#             if self.vampirism<0:
#                 self.vampirism=0
#         if type(self.heal_power) != bool:
#             self.heal_power+= weapon_name.heal_power
#             if self.heal_power<0:
#                 self.heal_power=0
#
#
# class Knight(Warrior):
#     attack = 7
#
# class Defender(Warrior):        #3
#     health = 60
#     attack = 3
#     defense = 2
#
# class Vampire(Warrior):         #4
#     health = 40
#     attack = 4
#     vampirism = 50
#
# class Lancer(Warrior):          #5
#     attack = 6
#
# class Healer(Warrior):          #6
#     attack = 0
#     health = 60
#     heal_power = 2
#     def heal(self, warrior):
#         warrior.health += self.heal_power
#         if warrior.health > (type(warrior).health+int(warrior.weapon.health)):
#             warrior.health = type(warrior).health+int(warrior.weapon.health)
#
# class Warlord(Warrior):
#     attack = 4
#     health = 100
#     defense = 2
#
# class Army():
#     units = []
#     def __init__(self):
#         self.units = []
#     def add_units(self, unit, number):
#         for i in range(number):
#             if type(unit())== Warlord and Warlord in [type(i) for i in self.units]:
#                 break
#             self.units.append(unit())
#
#     def move_units(self):
#         type_army = [type(i) for i in self.units]
#         if Warlord not in type_army:
#             return
#         new_army = []
#         if Lancer in type_army:
#             new_army.append(self.units.pop(type_army.index(Lancer)))
#             type_army.pop(type_army.index(Lancer))
#         else:
#             warriors = [i for i in type_army if i != Healer and i != Warlord]
#             if warriors != []:
#                 # x = type_army.index(Warlord)
#                 x = type_army.index(warriors[0])
#                 new_army.append(self.units.pop(x))
#                 type_army.pop(x)
#         while Healer in type_army:
#             new_army.append(self.units.pop(type_army.index(Healer)))
#             type_army.pop(type_army.index(Healer))
#         new_army.extend([i for i in self.units if type(i) != Warlord])
#         new_army.extend([i for i in self.units if type(i) == Warlord])
#         self.units=new_army
#
# class Battle():
#     def fight(self, army_1, army_2):
#         army_1.move_units()
#         army_2.move_units()
#         first_unit = army_1.units.pop(0)
#         second_unit = army_2.units.pop(0)
#         while True:
#             first_win = fight(first_unit, second_unit, allie_army=army_1.units, enemies_army=army_2.units)
#             if(army_1.units == [] and not first_win) or (army_2.units == [] and first_win):
#                 break
#             if first_win:
#                 army_2.move_units()
#                 second_unit = army_2.units.pop(0)
#             else:
#                 army_1.move_units()
#                 first_unit = army_1.units.pop(0)
#         return first_win
#     def straight_fight(self, army_1, army_2):
#         allie_army = army_1.units
#         enemies_army = army_2.units
#         while allie_army!=[] and enemies_army!=[]:
#             army_1.move_units()
#             army_2.move_units()
#             for i in range(min(len(allie_army), len(enemies_army))):
#                 fight(allie_army[i],enemies_army[i])
#             allie_army = [unit for unit in allie_army if unit.is_alive]
#             enemies_army = [unit for unit in enemies_army if unit.is_alive]
#         return allie_army!=[]
#
#
# def fight(unit_1, unit_2, enemies_army=[], allie_army = []):
#     attacker = unit_1
#     defender = unit_2
#     while unit_1.is_alive and unit_2.is_alive:
#         if enemies_army != [] and type(attacker) == Lancer:
#             if int(attacker.attack*0.5) > int(enemies_army[0].defense):
#                 enemies_army[0].health -= (int(attacker.attack*0.5) - int(defender.defense))
#             # army2[0] -= 0
#         if allie_army != [] and type(allie_army[0]) == Healer:
#             allie_army[0].heal(attacker)
#         if attacker.attack > int(defender.defense):
#             defender.health -= (attacker.attack - int(defender.defense))
#             attacker.health += int((attacker.attack - int(defender.defense))*int(attacker.vampirism)/100)
#             if attacker.health > (type(attacker).health+int(attacker.weapon.health)):
#                 attacker.health = type(attacker).health + int(attacker.weapon.health)
#         defender.is_alive = defender.health > 0
#         attacker, defender = defender, attacker
#         enemies_army,allie_army = allie_army, enemies_army
#     return unit_1.is_alive
#
# ronald = Warlord()
# heimdall = Knight()
#
# print(+fight(heimdall, ronald) == False)
# my_army = Army()
# my_army.add_units(Warlord, 1)
# my_army.add_units(Warrior, 2)
# my_army.add_units(Lancer, 2)
# my_army.add_units(Healer, 2)
#
# enemy_army = Army()
# enemy_army.add_units(Warlord, 3)
# enemy_army.add_units(Vampire, 1)
# enemy_army.add_units(Healer, 2)
# enemy_army.add_units(Knight, 2)
#
# my_army.move_units()
# enemy_army.move_units()
#
# print(type(my_army.units[0]) == Lancer,
# type(my_army.units[1]) == Healer,
# type(my_army.units[-1]) == Warlord,
#
# type(enemy_army.units[0]) == Vampire,
# type(enemy_army.units[-1]) == Warlord,
# type(enemy_army.units[-2]) == Knight)
#
# #6, not 8, because only 1 Warlord per army could be
# print(len(enemy_army.units) == 6)
#
# battle = Battle()
#
# print(battle.fight(my_army, enemy_army) == True)

# army_1 = Army()
# army_2 = Army()
# army_1.add_units(Warrior, 2)
# army_1.add_units(Lancer, 3)
# army_1.add_units(Defender, 1)
# army_1.add_units(Warlord, 1)
# army_2.add_units(Warlord, 5)
# army_2.add_units(Vampire, 1)
# army_2.add_units(Warrior, 1)
# army_2.add_units(Knight, 1)
# army_1.units[0].equip_weapon(Sword())
# army_2.units[0].equip_weapon(Shield())
# army_1.move_units()
# army_2.move_units()
# battle = Battle()
# print(battle.straight_fight(army_1, army_2))

# 10
# class Army:
#     units = []
#     army = None
#     named_units = {}
#     def train_swordsman(self,name):
#         unit = Swordsman(name, self.army, self.named_units.get('swordsman'))
#         self.units.append(unit)
#         return unit
#     def train_lancer(self,name):
#         unit = Lancer(name, self.army, self.named_units.get('lancer'))
#         self.units.append(unit)
#         return unit
#     def train_archer(self,name):
#         unit = Archer(name, self.army, self.named_units.get('archer'))
#         self.units.append(unit)
#         return unit
# class Warrior:
#     type_unit = None
#     name = None
#     army = None
#     unit = None
#     def __init__(self,name, army, type_unit):
#         self.type_unit = type_unit
#         self.army = army
#         self.name =name
#     def introduce(self):
#         return f'{self.type_unit} {self.name}, {self.army} {self.unit}'
# class Swordsman(Warrior):
#     unit = 'swordsman'
# class Lancer(Warrior):
#     unit = 'lancer'
# class Archer(Warrior):
#     unit = 'archer'
#
# class AsianArmy(Army):
#     army = "Asian"
#     named_units = {'swordsman': 'Samurai',
#                    'lancer': 'Ronin',
#                    'archer': 'Shinobi'}
# class EuropeanArmy(Army):
#     army = "European"
#     named_units = {'swordsman': 'Knight',
#                    'lancer': 'Raubritter',
#                    'archer': 'Ranger'}
# my_army = EuropeanArmy()
# enemy_army = AsianArmy()
#
# soldier_1 = my_army.train_swordsman("Jaks")
# soldier_2 = my_army.train_lancer("Harold")
# soldier_3 = my_army.train_archer("Robin")
#
# soldier_4 = enemy_army.train_swordsman("Kishimoto")
# soldier_5 = enemy_army.train_lancer("Ayabusa")
# soldier_6 = enemy_army.train_archer("Kirigae")
# print(soldier_1.introduce())
# print(soldier_6.introduce())

# 11
# class AbstractCook:
#     drink = None
#     food = None
#     drink_price = 0
#     food_price = 0
#     def add_drink(self, amount, price):
#         self.drink_price += amount*price
#     def add_food(self, amount, price):
#         self.food_price+= amount*price
#     def total(self):
#         return f"{self.food}: {self.food_price}, {self.drink}: {self.drink_price}, Total: {self.food_price+self.drink_price}"
# class JapaneseCook(AbstractCook):
#     drink = "Tea"
#     food = "Sushi"
#
# class RussianCook(AbstractCook):
#     drink = "Compote"
#     food = "Dumplings"
# class ItalianCook(AbstractCook):
#     drink = "Juice"
#     food = "Pizza"
#
# client_1 = JapaneseCook()
# client_1.add_food(2, 20)
# client_1.add_drink(5, 4)
# print(client_1.total())
#
# client_2 = RussianCook()
# client_2.add_food(1, 40)
# client_2.add_drink(5, 20)
# print(client_2.total() == "Dumplings: 40, Compote: 100, Total: 140")
#
# client_3 = ItalianCook()
# client_3.add_food(2, 20)
# client_3.add_drink(2, 10)
# print(client_3.total() == "Pizza: 40, Juice: 20, Total: 60")

# 12
# class Building:
#     coords = {}
#     height = None
#     width = None
#     length = None
#     def __init__(self, south, west, width_WE, width_NS, height=10):
#         self.coords = {"south-west": (south, west),
#                        "south-east": (south, west+width_WE),
#                        "north-west": (south+width_NS, west),
#                        "north-east": (south+width_NS, west+width_WE)}
#         self.width = width_WE
#         self.length = width_NS
#         self.height = height
#
#     def corners(self):
#         return self.coords
#
#     def area(self):
#         return self.length*self.width
#
#     def volume(self):
#         return self.length*self.width*self.height
#
#     def __repr__(self):
#         return f"Building({self.coords['south-west'][0]}, {self.coords['south-west'][1]}, {self.width}, {self.length}, {self.height})"
#
# b = Building(1, 2, 2, 3)
# b2 = Building(1, 2, 2, 3, 5)
# print(b.corners())
# print(b.area() == 6)
# print(b.volume()==60)
# print(b2.volume()==30)
# print(str(b))

# 13
# class VoiceCommand:
#     channels = []
#     current = None
#     def __init__(self, channels):
#         self.channels = [i for i in channels]
#         self.current = 0
#     def first_channel(self):
#         self.current = 0
#         return self.channels[self.current]
#     def last_channel(self):
#         self.current = len(self.channels)-1
#         return self.channels[self.current]
#     def turn_channel(self, n):
#         self.current = n-1
#         return self.channels[self.current]
#     def next_channel(self):
#         self.current+=1
#         if self.current >= len(self.channels):
#             self.current = 0
#         return self.channels[self.current]
#     def previous_channel(self):
#         self.current-=1
#         if self.current <0:
#             self.current = len(self.channels)-1
#         return self.channels[self.current]
#     def current_channel(self):
#         return self.channels[self.current]
#     def is_exist(self,channel):
#         if type(channel) == int:
#             if 0 < channel <= len(self.channels):
#                 return "Yes"
#             return "No"
#         for i in self.channels:
#             if i == channel:
#                 return "Yes"
#         return "No"
# CHANNELS = ["BBC", "Discovery", "TV1000"]
#
# controller = VoiceCommand(CHANNELS)
#
# print(controller.first_channel() == "BBC",
# controller.last_channel() == "TV1000",
# controller.turn_channel(1) == "BBC",
# controller.next_channel() == "Discovery",
# controller.previous_channel() == "BBC",
# controller.current_channel() == "BBC",
# controller.is_exist(4) == "No",
# controller.is_exist("BBC") == "Yes")
# CHANNELS = ['BBC', 'Discovery', 'NickMusic', 'MTV']
# controller = VoiceCommand(CHANNELS)
# controller.next_channel()
# controller.next_channel()
# controller.next_channel()
# controller.current_channel()

# 14    !!! new standard method of the class: __new__ !!!
# class Capital:
#     capital = None
#     _instance = None
#
#     def __init__(self, city_name):
#         if self.capital == None:
#             self.capital = city_name
#
#     def __new__(cls, *args, **kwargs):   # normally responsible for creating new object of the class with different id
#         if cls._instance is None:    # if that's the first time we create an object of the class, we call super method
#             cls._instance = super(Capital, cls).__new__(cls)        # cls is basically self, but for __new__ function
#         return cls._instance            # otherwise, we just return the instance of the object, we have saved before
#
#     def name(self):
#         return self.capital


# capital_1 = Capital('Warsaw')
# capital_2 = Capital('Leinberg')
# print(id(capital_2))
# print(id(capital_1))
# print(capital_2 is capital_1)
# print(capital_1.name())
# print(capital_2.name())

# 15
# import re
# class Chat:
#     dialogue = None
#     def __init__(self):
#         self.dialogue=[]
#     def connect_human(self,human):
#         human.set_chat(self)
#     def connect_robot(self, bot):
#         bot.set_chat(self)
#     def add_text(self, name, text):
#         self.dialogue.append((name, text))
#     def show_human_dialogue(self):
#         return "\n".join([f"{i[0]} said: {i[1]}" for i in self.dialogue])
#     def show_robot_dialogue(self):
#         return "\n".join([f"{i[0]} said: {re.sub('[^0]', '1', (re.sub(r'[aeiouAEIOU]','0', i[1])))}" for i in self.dialogue])
#
# class User:
#     name = None
#     chat = None
#     def __init__(self, name):
#         self.name = name
#     def set_chat(self,chat):
#         self.chat =chat
#     def send(self,text):
#         self.chat.add_text(self.name, text)
#
# class Human(User):
#     pass
# class Robot(User):
#     pass
# chat = Chat()
# karl = Human("Karl")
# bot = Robot("R2D2")
# chat.connect_human(karl)
# chat.connect_robot(bot)
# karl.send("Hi! What's new?")
# bot.send("Hello, human. Could we speak later about it?")
# print(chat.show_human_dialogue() == """Karl said: Hi! What's new?
# R2D2 said: Hello, human. Could we speak later about it?""",
# chat.show_robot_dialogue() == """Karl said: 101111011111011
# R2D2 said: 10110111010111100111101110011101011010011011""")
# print(chat.show_robot_dialogue())
# chat1= Chat()
# print(chat1.show_robot_dialogue())

# 16
# from datetime import date
# class Person:
#     first_name= None
#     last_name=None
#     birth_date=None
#     job=None
#     working_years=None
#     salary = None
#     country = None
#     city = None
#     gender = None
#     def __init__(
#         self,
#         first_name,
#         last_name,
#         birth_date,
#         job,
#         working_years,
#         salary,
#         country,
#         city,
#         gender="unknown",
#     ):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birth_date = birth_date
#         self.job = job
#         self.working_years = working_years
#         self.salary = salary
#         self.country = country
#         self.city = city
#         self.gender = gender
#     def name(self):
#         return self.first_name + ' ' + self.last_name
#     def age(self):
#         end_date = '01.01.2018'.split('.')
#         start_date = self.birth_date.split('.')
#         end_date = date(int(end_date[2]), int(end_date[1]), int(end_date[0]))
#         start_date = date(int(start_date[2]), int(start_date[1]), int(start_date[0]))
#         years = end_date.year - start_date.year
#         if end_date.month < start_date.month or (end_date.month == start_date.month and end_date.day < start_date.day):
#             years -= 1
#         return years
#     def work(self):
#         if self.gender == 'male':
#             return f'He is a {self.job}'
#         if self.gender == 'female':
#             return f'She is a {self.job}'
#         return f'Is a {self.job}'
#     def money(self):
#         money = str(int(self.salary)* 12*int(self.working_years))
#         result = money[0:len(money)%3]
#         for i in [money[len(money)%3+3*i : len(money)%3+3*(i+1)] for i in range(0, len(money)//3)]:
#             result += ' ' + i
#         return result.strip()
#     def home(self):
#         return f'Lives in {self.city}, {self.country}'


# p1 = Person(
#         "John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male"
#     )
# p2 = Person(
#         "Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna"
#     )
# print(p1.name() == "John Smith", "Name")
# print(p1.age() == 38, "Age")
# print(p2.work() == "Is a designer", "Job")
# print(p1.money() == "648 000", "Money")
# print(p2.home() == "Lives in Vienna, Austria", "Home")

# print(Person('Adam', 'Greene', '24.12.1961', 'director', 36, 11000, 'England', 'London', 'male').age())

# 17
# from math import pi
# from math import sin
# class Parameters:
#     def __init__(self, parameter):
#         self.parameter = parameter
#
#     def choose_figure(self, figure):
#         self.figure = figure
#
#     def perimeter(self):
#         return round(self.figure.perimeter(self.parameter), 2)
#
#     def area(self):
#         return round(self.figure.area(self.parameter), 2)
#
#     def volume(self):
#         return round(self.figure.volume(self.parameter), 2) if isinstance(self.figure, Cube) else 0
#
#
# class Circle:
#     def perimeter(self, parameter):
#         return pi * 2 * parameter
#
#     def area(self, parameter):
#         return pi* parameter**2
#
#
# class Triangle:
#     def perimeter(self, parameter):
#         return 3*parameter
#
#     def area(self, parameter):
#         return 1/2 * sin(pi/3) * parameter**2
#
#
# class Square:
#     def perimeter(self, parameter):
#         return 4* parameter
#
#     def area(self, parameter):
#         return parameter**2
#
#
# class Pentagon:
#     def perimeter(self, parameter):
#         return 5*parameter
#
#     def area(self, parameter):
#         return 1/4*(5*(5+2*5**0.5))**0.5*parameter**2
#
#
# class Hexagon:
#     def perimeter(self, parameter):
#         return 6*parameter
#
#     def area(self, parameter):
#         return 1/2*3*3**0.5*parameter**2
#
#
# class Cube:
#     def perimeter(self, parameter):
#         return 12*parameter
#
#     def area(self, parameter):
#         return 6* parameter**2
#
#     def volume(self, parameter):
#         return parameter**3
#
#
# figure = Parameters(10)
#
# figure.choose_figure(Circle())
# print(figure.area())
#
# figure.choose_figure(Triangle())
# print(figure.perimeter() == 30)
#
# figure.choose_figure(Square())
# print(figure.area() == 100)
#
# figure.choose_figure(Pentagon())
# print(figure.perimeter() == 50)
#
# figure.choose_figure(Hexagon())
# print(figure.perimeter() == 60)
#
# figure.choose_figure(Cube())
# print(figure.volume() == 1000)
#
# figure = Parameters(10)
# figure.choose_figure(Pentagon())
# print(figure.area())
#
# figure = Parameters(5)
# figure.choose_figure(Triangle())
# print(figure.area())


# 18
# class MicrowaveBase:
#     minutes = 0
#     seconds = 0
#     def set_time(self, time):
#         self.minutes = int(time.split(":")[0])
#         self.seconds = int(time.split(":")[1])
#     def add_time(self, time):
#         if time[-1] == 's':
#             self.seconds += int(time[:-1])
#             self.minutes += self.seconds // 60
#             self.seconds = self.seconds % 60
#         elif time[-1] == 'm':
#             self.minutes += int(time[:-1])
#         if self.minutes >= 90:
#             self.minutes = 90
#             self.seconds = 0
#     def del_time(self,time):
#         if time[-1] == 's':
#             self.seconds -= int(time[:-1])
#             if self.seconds<0:
#                 self.minutes-=1
#                 self.seconds+=60
#         elif time[-1] == 'm':
#             self.minutes -= int(time[:-1])
#         if self.minutes < 0:
#             self.minutes = 0
#             self.seconds = 0
#     def show_time(self):
#         return f"{self.minutes:0>2}:{self.seconds:0>2}"
#
#
#
#
# class Microwave1(MicrowaveBase):
#     def show_time(self):
#         return "_" + super(Microwave1, self).show_time()[1:]
#
#
# class Microwave2(MicrowaveBase):
#     def show_time(self):
#         return super(Microwave2, self).show_time()[:4] + "_"
#
#
# class Microwave3(MicrowaveBase):
#     pass
#
#
# class RemoteControl:
#     def __init__(self, microwave):
#         self.microwave = microwave
#     def set_time(self, time):
#         self.microwave.set_time(time)
#     def add_time(self, time):
#         self.microwave.add_time(time)
#     def del_time(self, time):
#         self.microwave.del_time(time)
#     def show_time(self):
#         return self.microwave.show_time()
#
#
# microwave_1 = Microwave1()
# microwave_2 = Microwave2()
# microwave_3 = Microwave3()
#
# remote_control_1 = RemoteControl(microwave_1)
# remote_control_1.set_time("01:00")
#
# remote_control_2 = RemoteControl(microwave_2)
# remote_control_2.add_time("90s")
#
# remote_control_3 = RemoteControl(microwave_3)
# remote_control_3.del_time("300s")
# remote_control_3.add_time("100s")
#
# print(remote_control_1.show_time() == "_1:00",
# remote_control_2.show_time() == "01:3_",
# remote_control_3.show_time() == "01:40")
#
# microwave_2 = Microwave2()
# rc_2 = RemoteControl(microwave_2)
# rc_2.set_time("89:00")
# rc_2.add_time("90s")
# rc_2.add_time("20m")
# print(rc_2.show_time())

# 19
# class Friend:
#     party = 'No party...'
#     def __init__(self,name):
#         self.name = name
#     def set_party(self, party):
#         self.party = party
#     def show_invite(self):
#         return self.party
#
#
# class Party:
#     def __init__(self,location):
#         self.location = location
#         self.friends = set()
#     def add_friend(self,friend):
#         self.friends.add(friend)
#     def del_friend(self,friend):
#         self.friends.discard(friend)
#     def send_invites(self, data_time):
#         for friend in self.friends:
#             friend.set_party(f"{self.location}: {data_time}")
# party = Party("Midnight Pub")
# nick = Friend("Nick")
# john = Friend("John")
# lucy = Friend("Lucy")
# chuck = Friend("Chuck")
#
# party.add_friend(nick)
# party.add_friend(john)
# party.add_friend(lucy)
# party.send_invites("Friday, 9:00 PM")
# party.del_friend(nick)
# party.send_invites("Saturday, 10:00 AM")
# party.add_friend(chuck)
#
# print(john.show_invite() == "Midnight Pub: Saturday, 10:00 AM",
# lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM",
# nick.show_invite() == "Midnight Pub: Friday, 9:00 PM",
# chuck.show_invite() == "No party...")


#20
# from collections import namedtuple
# class Text:
#     text = ""
#     font = None
#     def write(self, text):
#         self.text+=text
#     def set_font(self, font):
#         self.font = font
#     def show(self):
#         if self.font is None:
#             return self.text
#         return f"[{self.font}]{self.text}[{self.font}]"
#     def restore(self,version):
#         self.text = version.text
#         self.font = version.font
#
#
# class SavedText:
#     text_format = namedtuple('text_format', ['text','font'])
#     def __init__(self):
#         self.versions = []
#     def save_text(self,text):
#         self.versions.append(self.text_format(text.text, text.font))
#     def get_version(self,version):
#         return self.versions[version]
#
#
# text = Text()
# saver = SavedText()
#
# text.write("At the very beginning ")
# saver.save_text(text)
# text.set_font("Arial")
# saver.save_text(text)
# text.write("there was nothing.")
# print(text.show() == "[Arial]At the very beginning there was nothing.[Arial]")
#
# text.restore(saver.get_version(0))
# print(text.show() == "At the very beginning ")
