# Beginning 
player = {  
    "x" : 2,
    "y" : 3
}
player1 = {
    "x" : 3,
    "y" : 3
}
Key = {  
    "x" : 1,
    "y" : 2
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
            elif ('x' in Key) and ('y' in Key) and (x == Key['x']) and (y == Key['y']):
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
    
        if "x" not in Key and "y" not in Key:
            print("", end = "")
        else:
            print("You have collect the key!")
            Key.pop('x')
            Key.pop('y')
    
    #Exit
    if player['x'] == Exit['x'] and player ['y'] == Exit['y']:
        if 'x' in Key and 'y' in Key:
            print("You don't have the key :(")
           
        else:
            print("You have win this game")
            break



    
