9
# nombre entier, 'int'
9.11
# nombre décimal, 'float'

1 + 2 
# addition
2 - 1
# soustraction
2 * 4
# multiplication
2 ** 2 
# puissance
10 / 5
# division décimale
10 // 5
# division entière
10 % 3
# "modulo", il renvoie le reste de la divion

i = 1
i += 3
# c'est une incrémentation, ici on va ajouter 3 à 1, il est uniquement possible d'incrémenter une variable, le résulta sera donc 5

mon_age = 16
# variable
mon_age = mon_age + 2
# addition d'une variable, ici on augmente la variable de 2
mon_age_X2 = mon_age * 2
# multiplication d'une variable, ici on a multiplié le varible "mon_age" par 2
'Hello World'
# chaîne de caractère, 'str'
'''Hello World'''
# chaîne de caractère, 'str'
"Hello World"
# chaîne de caractère, 'str'
"""Hello World"""
# chaîne de caractère, 'str'
'J\'aime les fruits'
# mise en place de l'apostrophe de "J'aime", le \ avant l'apostrophe permet de la diférencier de la fermeture de la chaîne de caractère
"Je disais \" J'aime les fruits\""
# même exemple mais cette fois-ci avec des guillemets

prénom = "Cantin"
phrase = f"Je m'appelle {prénom} et j'ai {mon_age} ans."
# chaîne de caractère formaté, elle permet d'utiliser des variables dans une phrase

a = 5
b = 48
a, b = b, a
# permutation, cela permet de changer la valeur d'une variable 

x = y = 8
# permet d'attribuer une valeur à plusieurs varialbe en même temps
a = 3
type(a)
# donne le type de la variable, ici "a" est un nombre entier donc il sera affiché <class 'int'>
a = 3
print(a)
# print affiche la valeur ou le résultat de la variable ou encore le text qui est écrit. Il ne fait qu'afficher
print(f"Je m'appelle {prénom} et j'ai {mon_age} ans.")
# print peut aussi afficher une chaîne de caractère formaté

a = 5
if a > 0:
    print("a est supérieur à 0")
# if est une condition, if signifie "Si". ATTENTION ne pas oublier les : à la fin de la condition pour montrer que c'est la fin de la condition
if a > 0:
    print("a est positif")
if a < 0:
    print("a est négatif")
# Dans une condition, "if" peut être écrit autant de fois que l'on souhaite
âge = 21
if âge >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
# else est la deuxième parti d'une condition, elle permet de donner une autre possibilité à la condition
if a > 0:
    print("a est positif")
elif a < 0:
    print("a est négatif")
else:
    print("a est nul")
# elif est la contraction de "else" et "if", elif doit comporter une condition à l'inverse de else qui ne va faire que le contraire de "if" et de "elif"

a = 8
a > 0 # STRICTEMENT supérieur
a < 0 # STRICTEMENT inférieur
a >= 0 # supérieur OU égale
a <= 0 # inférieur OU égale
a == 0 # égale à
a != 0 # différent de

a = 0
a == 5
False
# a ne vaut pas 5 donc l'ordinateur nous marque False parce que ce n'est pas correct
a > -8
True
# a est effectivement supérieur à -8
a != 33.19
True
# a vaut 0 il est donc différent de 33.19

if a >= 2 and a <= 8:
    print("a est dans l'intervalle")
else:
    print("a n'est pas dans l'intervalle")
# "and" a pour fonction de réduire la longueur du programme et de faire le lien entre 2 conditions
if a < 2 or a > 8:
    print("a n'est pas dans l'intervalle")
else:
    print("a est dans l'intervalle")
# "or" fonctionne de la même façon que "and" mais avec "or" on veut savoir si a NE fait PAS parti de l'intervalle, la réflexion est plutôt négative
majeur = False
if majeur is not True:
    print("Vous n'êtes pas majeur")
# "not" a exactement la même fonction que != qui signifie "différent de", "not" nous permet de connaitre le contraire de ce que l'on marque

année = input("Saisissez une année : ")
# "input" met le programme en pause et attend que l'utilisteur entre une valeur 
type(année)
# <class 'str'>
année = int(année)
type(année)
# <class 'int'>
# "int" est la classe des nombres entier, ici on veut transformer la classe "str" de la variable "année" en "int", on veut la faire passer 
# d'une chaîne de caractère à un nombre entier

nb = 7
i = 1
while i<= 10:
    print(f"{i} * {nb} = {i * nb}")
    i += 1
# while est une boucle, elle va répéter les instructions qu'elle comporte tant que la condition est fausse (i <= 10 dans ce cas ici)

chaîne = "Bonjour les ZEROS"
for lettre in chaîne:
    print (lettre) 
# for est aussi une boucle, ici la condition est : "pour les lettre dans chaîne:" "afficher lettre" 

while 1:
    lettre = input("Taper 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break
# break sert à arrêter une boucle quelle qu"n soit la condition, ici si l'utilisateur ne saisie pas 'Q' alors le proggrame lui demandera de taper la lettre et le programme s'arrêtera que si la lettre est tapé, 
# s'il y a du code après il sera exécuté

def table_7():
    nb = 7
    i = 1
    while i <= 10:
        print(f"{i} * {nb} = {i * nb}") 
        i += 1

if __name__ == "__main__":
    table_7()
# cette dernière ligne sert à appeller la fontion et à l'exécuter dans le terminal 
