"""
ex5.py - More Variables and Printing

Copy of ex4.py, I believe what was done in ex4 covers ex5 as well.

msimo - 2/19/15

Learn Python the hard way!
<learnpythonthehardway.org>

Tested only with Python 3.3.6
"""

import random

#Defining player health
player_max_health = 10
player_current_health = player_max_health

#Defining player weapon
player_weapon = "Dagger"
weapon_attack = 2

#Defining player skills
player_skill = "Quick Strike"

#Defining all enemy attributes
enemy_name = "Typhoid Rat"
enemy_max_health = 20
enemy_current_health = enemy_max_health
enemy_attack = 1

while (enemy_current_health > 0):
	#Print player and enemy stats.
	print("\nPlayer HP: {0}/{1} // {2}'s' HP: {3}/{4}".format(player_current_health, player_max_health, enemy_name, enemy_current_health, enemy_max_health))
	#If 0 is chosen, player performs a basic attack.
	if(random.randint(0, 1) == 0):
		print("Player attacks {0} for {1} damage!".format(enemy_name, weapon_attack))
		enemy_current_health -= weapon_attack

	#Else the chosen player performs a Quick Strike.
	else:
		player_damage = random.randrange(weapon_attack, (weapon_attack+3))
		print("Player perfoms {0} on {1} for {2} damage!".format(player_skill, enemy_name, player_damage))
		enemy_current_health -= player_damage

	#Enemy attacks second, let's make it easier for our hero to win this encounter.
	print("{0} attacks the hero for {1} damage!".format(enemy_name, enemy_attack))
	player_current_health -= enemy_attack

	if(player_current_health <= 0):
		print("\nOur hero has died to {0}! Rest in peace...".format(enemy_name))
		break
	if(enemy_current_health <= 0):
		print("\nYou have won the encounter against {0}!".format(enemy_name))
		break