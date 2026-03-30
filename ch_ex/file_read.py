filename = 'pi.txt' 

with open(filename) as file_object :
    lines = file_object.readlines() 

pi_string = ''
for line in lines :
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

birthday = input("enter your birthday in mmddyy : ")
if birthday in pi_string :
    print("your birthday appears in first million of pi")
else :
    print("your birthday doesn't appear in the first million digits of pi")
