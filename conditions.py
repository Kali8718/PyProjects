age = 50
print(age < 19)
#operators that can be used != <= >= == < > 
#to check multiple conditions : and/or are used 
x = 1
y = 0

if x == 1 or y == 1 :
    print('you pass the or test :)')
else :
    print('you dont pass the or test :(')

if x == 1 and y == 1 :
    print('you pass the and test :)')
else :
    print('you dont pass the and test :(')

#to check if an item exists in a list "in" is used :
letters = ['a','b','c','d'] 
if "b" in letters :
    print('letters does exist :)')
else :
    print('letter doesnt exist')

#on the other hand "not in" is used to check if an item is not in a list 
if "b" not in letters :
    print('letters doesnt exist :)')
else :
    print('letter does exist')

#checking if a list is empty : python will return true when evaluating a list that's not empty
aList = []
if aList :
    print('this list is not empty')
else :
    print('this list is empty')


