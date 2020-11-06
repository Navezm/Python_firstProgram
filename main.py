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
    # TO DO get a random number
    item = my_list[1] # quote from the list
    print(item)
    return "Everything went well!"

# user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme.")

# while user_answer != "B":
#     print(show_random_quote(quotes))
#     user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter le programme.")

# for item in characters:
#     up_item = item.capitalize()
#     print(up_item)

def create_message(character, quote):
    print("{} a dit : {}".format(character, quote))

create_message(characters[0], quotes[1])