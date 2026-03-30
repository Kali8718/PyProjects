prompt = 'enter the list of your salad components.\n'
prompt += "enter quit when you're done : \n"
salad = []

component = input(prompt)
while component.lower() != 'quit' :
    if component != quit :
        salad.append(component)
        component = input(f"{component} has been added, what else do you want :\n")

print('your order is been made, your salad will contain :') 
for item in salad :
    print(f"-{item}")