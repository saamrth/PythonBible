import random

health= 50

difficulty=2

potion_health= random.randint(25,50)

health = int(health + potion_health/difficulty)

print (health)


