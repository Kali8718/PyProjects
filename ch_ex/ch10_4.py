#recording visits in a log txt file
from datetime import datetime


filename = "guest_log.txt"

while True :
    guest = input("Before you enter, please write your name (enter q to quit) : ")
    if guest == 'q' or guest == 'quit' :
        break
    time = datetime.now()
    time = str(time)
    phrase = "guest " + guest + " has joined the server at " + time
    with open(filename, 'a') as file_object :
        file_object.write(phrase)
        file_object.write("\n")
        file_object.close()  #used to open txt file even when while loop is still running
        
    
