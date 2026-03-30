numbers = []
for number in range(1,21) :
    numbers.append(number)
    print(number)

print(numbers)

toMillion = [num for num in range (1,1000000)]
print(min(toMillion))
print(max(toMillion))
print(sum(toMillion))

oddnum = [odd for odd in range(1,21,2)]
print(oddnum)

threemult = []
for a in range(1,11) :
    threemult.append(a*3)

print(threemult)

threemult = []
threemult = [a*3 for a in range(1,11)]
for num in threemult :
    print(num)

cubes = [c**3 for c in range(1,11)] 
for num in cubes :
    print(num)