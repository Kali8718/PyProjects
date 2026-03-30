print("a Dictionary is a collection of key-value pairs, each key is connected to a value, a key's value can be a string, number, list or even another dictionary...")

setup = {'laptop' : 'HP', 'Desktop' : 'Z230'}
print(setup)
print('to print the value of a key, type the name of the dictionary and the key in brackets')
print(setup['laptop'])
print("adding key-value pairs to a dictionnary : dict_name[key] = 'Value'")
setup['phone'] = 'huawei'
print(setup)
print("modifying values in a dictionary is the same process, removing is done with : del setup['laptop']")
del setup['laptop']
print(setup)
print('another way to type dictionaries is to open brace, indent, and type each key-value pair in a lign ending with coma')
print("one way to request a value if we're not sure the key exists is with .get(), it takes 2 arguemtns, first is the key, second is what is returned if key isnt found")

phones = {
    "Ahmed" : "A5",
    "Amine" : "S20",
    "Hamza" : "P20",
    "Anass" : "Iphone X",
}
print('New list :')
print(phones)
x = phones.get('Ahmed','item doesnt exist :(')
print(x)
x = phones.get('kek','item doesnt exist')
print(x)
print("To loop through a dictionary following expressipn is used \nfor key, value in dict.items() :")
for name, phone in phones.items() :
    print(f"{name}'s phone is an {phone}")

print("To use a dictionary's keys only : \nfor name in phones.keys() :")
#note that looping through keys is default, so ommiting .keys() still leads to same outcome

print("by default python loops through keys and values in the order they were added")
print("to loop through them sorted : \nfor name in sorted(phones.keys)) : ")
for name in sorted(phones.keys()) :
    print(name)
print("to loop through all the values in a dictionary : \nfor phone in phones.values() :")
for phone in phones.values() :
    print(phone)

print("set can be used on a dictionnary to only display unique items (discard duplicates)")
print("when words are wrapped in braces but no key-value braces it's a set")
