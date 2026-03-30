current_users = ['ali','exiledguamila','nighthawk','letroll','sussy']
new_users = ['baka','NightHawk','yoku','Ali','letroll']

#in the first for we pick a value from current_users, then 2nd for run through all values in new_users
#we then pick another value in current users and run though all values in new users comparing...
for name in new_users :
    x=0
    for old_name in current_users :
        if name.lower() == old_name.lower() :
            print(f'name already used : {name}')
            x=1
    if x == 0 :
        print(f'welcome to our forum {name}')


    