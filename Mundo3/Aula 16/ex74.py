from random import randint 
import emoji
import json


with open('us.json', 'r') as states:
     states = json.load(states)


#Re using the variable states
emojis = emoji.emojize(':cookie:',  use_aliases=True)

print(f"You born in: {states[randint(0, len(states))]['name']} {emojis}")