import json
from difflib import get_close_matches

data=json.load(open("data.json"))
def translate(word):
    word=word.lower()
    
    if word in data:
        return data[word]
    
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
        yn=input("Did you mean %s instead?\n Enter Y if yes,or N if no." %get_close_matches(word,data.keys())[0])

        if yn=="Y":
              return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return("The word Doesn't exist!\n Please double cheak it.")
        else:
            return("We didn't understand your entry")
            
                        
    else:
        return("The word Doesn't exist!\n Please double cheak it.")
       
word=input("Enter word: ")

output=translate(word)
if type(output)==list:
    for item in output:
        print("*--> "+item)           
else:
    print(output)
