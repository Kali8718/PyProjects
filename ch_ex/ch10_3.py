#program to prompt guests for their name and store it in a text file 

filename = "guests.txt"
guests = []

while True :
    guest = input(("What is your name ? type N when done : "))
    if guest == "N" or guest == "n" :
        break
    guests.append(guest)

with open(filename, 'w') as file_object : 
    for guest in guests :
        file_object.write(guest)
        file_object.write("\n")

