#learning try, except and else

while True :
    try :
        print("Please enter two numbers to addition, or type q to leave ")
        x = input()

        if x.lower() == "q" :
            exit()

        y = input()
        if y.lower() == "q" :
            exit()

        z = int(x) + int(y)
    except ValueError :
        print("Please enter a number")
    else :
        print(x,"+",y,"=",z)





