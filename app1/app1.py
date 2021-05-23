import json
from difflib import get_close_matches

data = json.load(open("/home/ignareyesa/workspace/ten-apps-udemy-py/app1/data.json"))

def translate(word):
    word = word.lower()
    propose_word = get_close_matches(word, data.keys(), cutoff=0.8)
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(propose_word)>0:
        answer = input(f"Did you mean {propose_word[0]} instead? (Y/N): ")
        if answer == "Y":
            return data[propose_word[0]]
        elif answer == "N":
            return f"{word} doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return f"{word} doesn't exist. Please double check it."
    

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for i, item in enumerate(output):
        print(f"{i+1}. {item}")

else: 
    print(output)