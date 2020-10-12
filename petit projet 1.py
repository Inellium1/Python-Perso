from random import *

stock = 1000
magasin = 100


def Player1():
    Player = randint(0,4)
    return Player


def Coach1():
    Coach = randint(1,8)
    return Coach
print(Coach1())

def consommateur1():
    consommateur = random.choice([Player1(), Coach1()])
    return consommateur

liste = [Player1, Coach1]
acheteur = random.choice(liste)
print (acheteur)