users = []
if users :
    for user in users :
        if user == 'admin' :
            print(f'hello {user}, would you like a status report ?')
        else :
            print(f"hello {user}, welcome :)")
else :
    print('we need to add more users')