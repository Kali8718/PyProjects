digits = [a for a in range(1,11)]
print(digits)

print(f"the first three numbers in this list are {digits[:3]}")
print(f"items in the middle of this list are {digits[3:7]}")
print(f"last three items in this list are {digits[7:10]}")

my_pizzas = ['margherita','pepperoni','hawaiian']
friends_pizzas = my_pizzas[:]
friends_pizzas.extend(['mincedmeat','quatro formago'])

print("my favorite pizzas are :")
for item in my_pizzas :
    print(item)

print("\nmy friend's favorite pizzas are :")
for item in friends_pizzas :
    print(item)

