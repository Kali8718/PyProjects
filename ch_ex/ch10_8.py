# modified to fail siltently
filename1 = "catz.txt"
filename2 = "dogs.txt"
files = [filename1, filename2]



for file in files :
    try :
        with open(file) as file_object :
            lines = file_object.readlines()
            for line in lines :
                print(line.rstrip())
    except FileNotFoundError :
            pass



