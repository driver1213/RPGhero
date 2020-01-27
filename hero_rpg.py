#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random

class Character:
    def __init__(self, name, power, health, crit_hit_chance, recovery_chance, damage_chance):
        self.name = name
        self.power = power
        self.health = health
        self.crit_hit_chance = crit_hit_chance
        self.recovery_chance = recovery_chance
        self.damage_chance = damage_chance

    def attack(self, enemy):
        if enemy.name != "Zombie":
            enemy.health -= self.power
        enemy.health -= self.power
        damage = random.random() < self.damage_chance
        if damage:
            self.health -= enemy.power
            print(f"{enemy.name} attacked {self.name}")

        elif self.health == enemy.power:
            print(f"{enemy.name} does no damage to {self.name}.")

        print(f"{self.name} does {self.power} damage to {enemy.name}.")
        if enemy.health <= 0:
            print(f"{enemy.name} is dead.")
        elif self.health <= 0:
            print(f"{self.name} is dead.")
        




    def alive(self):
        return self.health > 0

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")
        if self.health <=0:
            print(f"{self.name} is dead.")
        
class Hero(Character):
    def attack(self, enemy):
        crit_hit = random.random() < self.crit_hit_chance
        if crit_hit:
            enemy.health -= self.power*2
            print(f'You do {self.power*2} damage to {enemy.name}.')
            
        else:
            enemy.health -= self.power
            print(f"{self.name} does {self.power} damage to {enemy.name}.")

class Goblin(Character):
    def attack(self, enemy):
        # enemy.health -= self.power
        # print(f"{self.name} does {self.power} damage to {enemy.name}.")
        if enemy.health <= 0:
            print(f"{enemy.name} is dead.")
            
        elif self.health <= 0:
            print(f'{self.name} is dead!')


class Zombie(Character):
    def attack(self, enemy):
        # enemy.health -= self.power
        # print(f"{self.name} does {self.power} damage to {enemy.name}.")
        
        if self.health <=0 :
            enemy.health -= self.power
            print(f'{self.name} ate you! The undead can never die!')

class Medic(Character):
    def attack(self, enemy):
        # enemy.health -= self.power
        # print(f"{self.name} does {self.power} damage to {enemy.name}.")
        recovery = random.random() < self.recovery_chance
        if recovery:
            self.health += 2
            print(f'{self.name} recovered 2 points.')
        elif self.health <= 0:
            print(f'{self.name} is dead!')


class Shadow(Character):
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} does {self.power} damage to {enemy.name}.")
        
        
        # damage = random.random() < self.damage_chance
        # if damage:
        #     self.health -= enemy.power
        #     print(f"{enemy.name} attacked {self.name}")

        # else:
        #     self.health == enemy.power
        #     print(f"{enemy.name} does no damage to {self.name}.")

hero = Hero("Neo", 2, 10, 0.2, 0, 0)
goblin = Goblin("Goblin", 2, 9, 0, 0, 0)
zombie = Zombie("Zombie", 2, 8, 0, 0, 0)
medic = Medic("Medic", 2, 8, 0, 0.2, 0)
shadow = Shadow("Shadow", 2, 1, 0, 0, 0.1)





def main():
    

    while goblin.alive() and hero.alive() and zombie.alive() and shadow.alive() and medic.alive():
        hero.print_status()  #print("You have {} health and {} power.".format(hero.health, hero.power))
        # goblin.print_status()  #print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        # zombie.print_status()
        # shadow.print_status()
        # medic.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("4. fight zombie")
        print("5. fight medic")
        print("6. fight shadow")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            # Goblin attacks hero
            goblin.attack(hero)
            goblin.print_status()
        elif raw_input == "2":
            hero.health -= goblin.power
            print('You wimp!')
            if hero.health <=0:
                print('You are dead!')
        elif raw_input == "3":
            print("Goodbye.")
            break
        elif raw_input == "4":
            #Hero attacks Zombie
            hero.attack(zombie)
            print('You can\'t hurt Zombie!')
            #Zombie attacks Hero
            zombie.attack(hero)
            
        elif raw_input == "5":
            #Hero attacks Medic
            hero.attack(medic)
            #Medic attacks Hero
            medic.attack(hero)
            
        elif raw_input == "6":
            
            shadow.attack(hero)
            shadow.print_status()
            if hero.health <= 0:
                print('You are dead!')
        else:
            print("Invalid input {}".format(raw_input))

main()
