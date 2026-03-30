#  adding, deleting, and storing deleted items
x = ['letroll','sussy','plussy']
print(x)
print(x[0])
x[0] = 'okayge'
print(x[0])
x.append('gachiHyper')
print(x)
del x[2]
print(x)
popped_x = x.pop()
print(popped_x)
x.remove('okayge')
print(x)
x.append('sadge')
x.append('KKona')
x.append('monkaW')
x.insert(0,'baka')
print(x)
#append works on a single value, extend() can add multiple values to a list
print('this is extend fct')
noms = [1,2,3,4]
noms.extend([5,6,7])
print(noms)


#sorting a list permanently 
print("pre-sorted and post-sorted list")
x.sort()
print(x)

#reverse sorting a list permanently
print('reverse sorted list')
x.sort(reverse=True)
print(x)

#sorting a list temporarily and reverse sorting
print('temporarily sorted list can be used with sorted function')
print(sorted(x))
print(x)
print('reverse can also be used to reverse order of all items on the list, it doesnt sort in reserve alphabetic order')
x.reverse()
print(x)

#length of a list
print('length of a list can be obtained with len function')
print(len(x))

#looping through lists
print('looping through list')
for emote in x :
    print(emote)

#creating a list with a loop
print("list with numbers from 1 to 10 ")
numbers = list(range(1,11))
print(numbers)

print("list with square numbers")
squares = []
for number in range(1,101) :
    square = number **2
    squares.append(square)

print(squares)

#statistics on a list
digits = [1,2,3,4,5,6,7,8,9,0]

min(digits)
max(digits)
sum(digits)

#list comprehensions : The above loop where we made a square number list can be summarized in one line
print("The above loop where we made a square number list can be summarized in one line : 1-11 squares")
squares = [value ** 2 for value in range(1,11)]
print(squares)

#slicing through a list
print(digits[0:3])

#omiting first or last index, python begins at the first or continues to the last item
print(digits[:4])

#cloning for copying a list
clone_digits = digits[:]
print(clone_digits)


#associating a list to another, thus both variables point to the same list
clone_digits = digits

#tuples : lists that can't be modified, defined with parantheses instead of brackets
aTuple = (200,50)
print('this is a tuple')
print(aTuple)
#altough a tuples values cant be modified, the whole tuple can be re-written
aTuple = (100,200)
print(aTuple)