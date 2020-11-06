import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre"
]

characters = [
    "alvin et les Chipmunks",
    "babar",
    "Betty Boop",
    "Calimero",
    "casper",
    "Le chat Potté",
    "kirikou"
]

def show_random_quote(my_list):
    rand_numb = random.randint(0, len(my_list) -1) # random number
    item = my_list[rand_numb] # quote from the list
    return item

def capitalize(words):
    for item in words:
        item.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit : {}".format(character, quote)

user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme.")

while user_answer != "B":
    print(message(show_random_quote(characters), show_random_quote(quotes)))
    user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme.")