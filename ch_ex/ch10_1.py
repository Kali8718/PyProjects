#Program used to read a text file and display the content in three different methods 

filename = 'ch10_1.txt'
i = 0

i += 1 
print("This is attempt number ",i," \n")

with open(filename) as file_object :
    content = file_object.read()

print(content,"\n")

i += 1 
print("This is attempt number ",i," \n")

print
with open(filename) as file_object :
    for line in file_object :
        print(line.rstrip())
print("\n")

i += 1 
print("This is attempt number ",i," \n")

with open(filename) as file_object :
    lines = file_object.readlines()

for line in lines :
    print(line.rstrip())


