guests = ['ali','yasmine','qazam','adam','chawki']
print('it has been brought to our attention that only 2 guests can attend :(')
while len(guests) > 2 : 
    removedGuest = guests.pop()
    print(f'sorry {removedGuest} your invitation has been withdrawn')

print(guests)
print(f"i would like to inform {guests[0]} and {guests[1]} that they are still invited !")

while len(guests) != 0 :
    del guests[0]

print(guests)