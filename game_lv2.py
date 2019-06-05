# Beginning 
player = {  
    "x" : 2,
    "y" : 3
}
player1 = {
    "x" : 3,
    "y" : 3
}
Key1 = {  
    "x" : 1,
    "y" : 2
}
Key2 = {
    "x" : 0,
    "y" : 0
}
Exit = {  
    "x" : 3,
    "y" : 0
}
Wall = {
    "x" : 1,
    "y" : 1

}
while True:
    # Init map
    for x in range(4):
        for y in range(4):
            if x == Wall["x"] and y == Wall["y"]:
                print("W", end = " ")
            elif x == player['x'] and y == player['y']:
                print("P", end = " ")
            elif ('x' in Key1) and ('y' in Key1) and (x == Key1['x']) and (y == Key1['y']):
                print("K", end = " ")
            elif ('x' in Key2) and ('y' in Key2) and (x == Key2['x']) and (y == Key2['y']):
                print("K", end = " ")
            elif x == Exit['x'] and y == Exit['y']:
                print("E", end = " ")
            else:
                print("-", end = " ")
        print(" ")

    #Movement
    movement = input("W A S D ? ")
    if movement.upper() == "A":
        player['y'] += -1
    elif movement.upper() == "W":
        player['x'] += -1
    elif movement.upper() == "S":
        player['x'] += 1
    elif movement.upper() == "D":
        player['y'] += 1
    # Check if player out of map
    if player['x'] > player1['x'] or player['y'] > player1['y']:
        print("Out of range")
        break
    #Wall
    if movement.upper() == "A":
        if player['y'] == Wall ['y'] and player['x'] == Wall["x"]:
            print("This is a wall, you must find another way!")
            player['y'] += 1
    
    if movement.upper() == "W":
        if player['y'] == Wall ['y'] and player['x'] == Wall["x"]:
            print("This is a wall, you must find another way!")
            player['x'] += 1

    if movement.upper() == "S":
        if player['y'] == Wall ['y'] and player['x'] == Wall["x"]:
            print("This is a wall, you must find another way!")
            player['x'] += - 1

    if movement.upper() == "D":
        if player['y'] == Wall ['y'] and player['x'] == Wall["x"]:
            print("This is a wall, you must find another way!")
            player['y'] += -1
    #Collecting key
    if player['x'] == 1 and player['y'] == 2:
    
        if "x" not in Key1 and "y" not in Key1:
            print("", end = "")
        else:
            print("You have collect a key!")
            Key1.pop('x')
            Key1.pop('y')
    if player['x'] == 0 and player['y'] == 0:
    
        if "x" not in Key2 and "y" not in Key2:
            print("", end = "")
        else:
            print("You have collect a key!")
            Key2.pop('x')
            Key2.pop('y')
    #Exit
    if player['x'] == Exit['x'] and player ['y'] == Exit['y']:
        if ('x' in Key1 and 'y' in Key1) or ('x' in Key2 and 'y' in Key2):
            print("You don't have enough key :(")
           
        else:
            print("You have win this game")
            break



    
