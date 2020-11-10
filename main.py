import random
import json

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre"
]

# characters = [
#     "alvin et les Chipmunks",
#     "babar",
#     "Betty Boop",
#     "Calimero",
#     "casper",
#     "Le chat Potté",
#     "kirikou"
# ]

# Read value from json file
def read_value_from_json():
    values = [] # create a new empty list
    with open('characters.json') as f:
        data = json.load(f) # load the data from that file. data = entries
        for entry in data :
            values.append(entry['characters']) # add each element in my list
        return values # return my complete list
        
def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit : {}".format(character, quote)

def random_character():
    all_values = read_value_from_json()
    return show_random_quote(all_values)

def show_random_quote(my_list):
    rand_numb = random.randint(0, len(my_list) -1) # random number
    item = my_list[rand_numb] # quote from the list
    return item

def capitalize(words):
    for item in words:
        item.capitalize()


user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme.")

while user_answer != "B":
    print(message(random_character(), show_random_quote(quotes))
    user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme.")