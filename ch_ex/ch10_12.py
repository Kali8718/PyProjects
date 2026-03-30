#ask for user favorite number and store it 
import json

filename = "ch10_11.json"

def ask_fav_num() :
    num = input("What is your favorite number ? : ")
    with open(filename,'w') as file_object :
        json.dump(num, file_object)

def display_num() :
    with open(filename) as f :
        num = json.load(f)
        output = "your favorite number is " + num
        return output


try :
    print(display_num())

except FileNotFoundError :
    ask_fav_num()





