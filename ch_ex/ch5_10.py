current_users = ['ali','exiledguamila','nighthawk','letroll','sussy']
new_users = ['baka','ayaya','yoku','ali','letroll']

for element in new_users :
    element = element.lower()

for name in new_users :
    if name.lower() in current_users :
        print(f'{name} is already used')
    else :
        print("Welcome ")
