import random
import json

# quotes = [
#     "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
#     "On doit pouvoir choisir entre s'écouter parler et se faire entendre"
# ]

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
def read_values_from_json():
    values = [] # create a new empty list
    with open('characters.json') as f:
        data = json.load(f) # load the data from that file. data = entries
        for entry in data :
            values.append(entry['characters']) # add each element in my list
        return values # return my complete list

def message(character, quote):
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    return "{} a dit : {}".format(n_character, n_quote)

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb] # get a quote from a list
    return item # return the item

def get_random_quote():
    all_values = read_values_from_json('quotes.json', 'quote')
    return get_random_item_in(all_values)

def get_random_character():
    all_values = read_values_from_json('characters.json', 'character')
    return get_random_item_in(all_values)

# Programm
user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

while user_answer != "B":
    print(message(get_random_character(), get_random_quote()))
    user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')