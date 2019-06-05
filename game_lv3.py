# Beginning 
import random
from random import randint
player = {  
    "x" : 6,
    "y" : 7
}
player_index = {
    "Atk" : 40,
    "Def" : 50,
    "HP" : 70,
    "Escape" : 0.45
}


player1 = {
    "x" : 7,
    "y" : 7
}
Key1 = {  
    "x" : 5,
    "y" : 6
}
Key2 = {
    "x" : 0,
    "y" : 0
}
Exit = {  
    "x" : 7,
    "y" : 0
}
Wall1 = {
    "x" : 4,
    "y" : 4

}
Wall2 = { 
    "x" : 3,
    "y" : 3
}
Wall3 = { 
    "x" : 2,
    "y" : 6
}
HP_item = {
    "x" : randint(0,7),
    "y" : randint(0,7)
}
while True:
    #Monster_location
    monster1 = {
    "x" : randint(5,7),
    "y" : randint(0,2)
}
    monster2 = {
        "x" : randint(2,4),
        "y" : randint(3,5)
    }
    monster3 = {
        "x" : randint(0,1),
        "y" : randint(6,7)

    }
    # Init map
    for x in range(8):
        for y in range(8):
            if x == Wall1["x"] and y == Wall1["y"]:
                print("W", end = " ")
            elif x == Wall2["x"] and y == Wall2["y"]:
                print("W", end = " ")
            elif x == Wall3["x"] and y == Wall3["y"]:
                print("W", end = " ")
            elif x == monster1["x"] and y == monster1["y"]:
                print("M", end = " ")
            elif x == monster2["x"] and y == monster2["y"]:
                print("M", end = " ")
            elif x == monster3["x"] and y == monster3["y"]:
                print("M", end = " ")
            
            elif x == player['x'] and y == player['y']:
                print("P", end = " ")
            elif ('x' in Key1) and ('y' in Key1) and (x == Key1['x']) and (y == Key1['y']):
                print("K", end = " ")
            elif ('x' in Key2) and ('y' in Key2) and (x == Key2['x']) and (y == Key2['y']):
                print("K", end = " ")
            elif x == Exit['x'] and y == Exit['y']:
                print("E", end = " ")
            elif x == HP_item["x"] and y == HP_item["y"]:
                print("-", end = " ") 
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
        if player['y'] == Wall1['y'] and player['x'] == Wall1["x"]:
            print("This is a wall, you must find another way!")
            player['y'] += 1
    if movement.upper() == "W":
        if player['y'] == Wall1['y'] and player['x'] == Wall1["x"]:
            print("This is a wall, you must find another way!")
            player['x'] += 1
    if movement.upper() == "S":
        if player['y'] == Wall1['y'] and player['x'] == Wall1["x"]:
            print("This is a wall, you must find another way!")
            player['x'] += - 1
    if movement.upper() == "D":
        if player['y'] == Wall1['y'] and player['x'] == Wall1["x"]:
            print("This is a wall, you must find another way!")
            player['y'] += -1
    #Wall2
    if movement.upper() == "A":
        if player['y'] == Wall2['y'] and player['x'] == Wall2["x"]:
            print("This is a wall, you must find another way!")
            player['y'] += 1
    if movement.upper() == "W":
        if player['y'] == Wall2['y'] and player['x'] == Wall2["x"]:
            print("This is a wall, you must find another way!")
            player['x'] += 1
    if movement.upper() == "S":
        if player['y'] == Wall2['y'] and player['x'] == Wall2["x"]:
            print("This is a wall, you must find another way!")
            player['x'] += - 1
    if movement.upper() == "D":
        if player['y'] == Wall2['y'] and player['x'] == Wall2["x"]:
            print("This is a wall, you must find another way!")
            player['y'] += -1
    #Wall3
    if movement.upper() == "A":
        if player['y'] == Wall3['y'] and player['x'] == Wall3["x"]:
            print("This is a wall, you must find another way!")
            player['y'] += 1
    if movement.upper() == "W":
        if player['y'] == Wall3['y'] and player['x'] == Wall3["x"]:
            print("This is a wall, you must find another way!")
            player['x'] += 1
    if movement.upper() == "S":
        if player['y'] == Wall3['y'] and player['x'] == Wall3["x"]:
            print("This is a wall, you must find another way!")
            player['x'] += - 1
    if movement.upper() == "D":
        if player['y'] == Wall3['y'] and player['x'] == Wall3["x"]:
            print("This is a wall, you must find another way!")
            player['y'] += -1
    
    #Collecting key
    if player['x'] == 5 and player['y'] == 6:
    
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

    #Monster
    monster_index1 = {
    "Atk" : 60,
    "Def" : 30,
    "HP" : 20
    }
    monster_index2 = {
    "Atk" : randint(55,70),
    "Def" : randint(20,34),
    "HP" : randint(15, 30),
    "critical" : random.uniform(0,1)
    }
    monster_index3 = {
    "Atk" : randint(55,70),
    "Def" : randint(20,34),
    "HP" : randint(15, 30),
    "critical" : random.uniform(0,1)
    }
        #Monster1
    if (monster1["x"] == player["x"] and monster1["y"] == player["y"]):
        print("You meet a monster.")
        print("Here is your index:")
        for k,v in player_index.items():
            print(f"{k}: {v}")
        print("Here is monster's index: ")
        for k,v in monster_index1.items():
            print(f"{k}: {v}")
        while True:
            action = input("What do you want to do: Attack(A) or Escape(E)?")
            if ("A" in action.upper()) or ("E" in action.upper()):
                #Attack
                if action.upper() == "A":
                    while monster_index1["HP"] >0 :
                        print("You have dealed", player_index["Atk"] - monster_index1["Def"], "damage!")
                        print("You have lose", monster_index1["Atk"] - player_index["Def"], "HP")
                        player_index["HP"] += (player_index["Def"] - monster_index1["Atk"])
                        monster_index1["HP"] += (monster_index1["Def"] - player_index["Atk"])
                        print("Your HP now is", player_index["HP"], "HP")
                    break
                #Escape
                if action. upper() == "E":
                    print("You have", player_index["Escape"] * 100, "% to escape!")
                    rate = random.uniform(0, 1)
                
                    if player_index["Escape"] < rate:
                        print("You was hitted skill from Monster")
                        print("You have lose", monster_index1["Atk"] - player_index["Def"], "HP")
                        player_index["HP"] += (player_index["Def"] - monster_index1["Atk"])
                        print("Your HP now is", player_index["HP"], "HP")
                        break
                    else:
                        print("You have escape successful! ")
                        print("Your HP now is", player_index["HP"], "HP")
                        break
        else:
            print("You pressed wrong button. Please press A or E!")
        #Monster 2 
    if (monster2["x"] == player["x"] and monster2["y"] == player["y"]):
        print("You meet a monster.")
        print("Here is your index:")
        for k,v in player_index.items():
            print(f"{k}: {v}")
        print("Here is monster's index: ")
        for k,v in monster_index2.items():
            print(f"{k}: {v}")
        
        while True:
            action = input("What do you want to do: Attack(A) or Escape(E)?")
            if ("A" in action.upper()) or ("E" in action.upper()):
            
            
                #Attack
                if action.upper() == "A":
                    while monster_index2["HP"] >0 :
                        critical2 = random.uniform(0,1)
                        if critical2 < monster_index2["critical"]:
                            print("You have dealed", player_index["Atk"] - monster_index2["Def"], "damage!")
                            print("You have lose", monster_index2["Atk"]*1.5 - player_index["Def"], "HP. (Crit damaged)")
                            player_index["HP"] += (player_index["Def"] - monster_index2["Atk"]*1.5)
                            monster_index2["HP"] += (monster_index2["Def"] - player_index["Atk"])
                            print("Your HP now is", player_index["HP"], "HP")
                        else:
                            print("You have dealed", player_index["Atk"] - monster_index2["Def"], "damage!")
                            print("You have lose", monster_index2["Atk"] - player_index["Def"], "HP.")
                            player_index["HP"] += (player_index["Def"] - monster_index2["Atk"])
                            monster_index2["HP"] += (monster_index2["Def"] - player_index["Atk"])
                    
                            print("Your HP now is", player_index["HP"], "HP")
                    break
                #Escape
                if action. upper() == "E":
                    print("You have", player_index["Escape"] * 100, "% to escape!")
                    rate = random.uniform(0, 1)
                
                    if player_index["Escape"] < rate:
                        critical_2 = random.uniform(0,1)
                        if critical_2 < monster_index2["critical"]:
                            
                            print("You have losed", monster_index2["Atk"]*1.5 - player_index["Def"], "HP. (Crit damaged)")
                            player_index["HP"] += (player_index["Def"] - monster_index2["Atk"])*1.5
                            
                            print("Your HP now is", player_index["HP"], "HP")
                            break
                        else:
                            
                            print("You have losed", monster_index2["Atk"] - player_index["Def"], "HP.")
                            player_index["HP"] += (player_index["Def"] - monster_index2["Atk"])
                            
                            print("Your HP now is", player_index["HP"], "HP")
                            break    
                    else:
                        print("You have escape successful! ")
                        print("Your HP now is", player_index["HP"], "HP")
                        break
            else:
                print("You have pressed wrong button. Please entered A/E !")      
        #Monster 3
    if (monster3["x"] == player["x"] and monster3["y"] == player["y"]):
        print("You meet a monster.")
        print("Here is your index:")
        for k,v in player_index.items():
            print(f"{k}: {v}")
        print("Here is monster's index: ")
        for k,v in monster_index3.items():
            print(f"{k}: {v}")
        while True:
            action = input("What do you want to do: Attack(A) or Escape(E)?")
            if ("A" in action.upper()) or("E" in action.upper()):
                #Attack
                if action.upper() == "A":
                    while monster_index3["HP"] >0 :
                        critical3 = random.uniform(0,1)
                        if critical3 < monster_index3["critical"]:
                            print("You have dealed", player_index["Atk"] - monster_index3["Def"], "damage!")
                            print("You have lose", monster_index3["Atk"]*1.5 - player_index["Def"], "HP. (Critical Damaged)")
                            player_index["HP"] += (player_index["Def"] - monster_index3["Atk"]*1.5)
                            monster_index3["HP"] += (monster_index3["Def"] - player_index["Atk"])
                            print("Your HP now is", player_index["HP"], "HP")
                        else:
                            print("You have dealed", player_index["Atk"] - monster_index3["Def"], "damage!")
                            print("You have lose", monster_index3["Atk"] - player_index["Def"], "HP")
                            player_index["HP"] += (player_index["Def"] - monster_index3["Atk"])
                            monster_index3["HP"] += (monster_index3["Def"] - player_index["Atk"])
                            print("Your HP now is", player_index["HP"], "HP")
                    break
                #Escape
                if action. upper() == "E":
                    print("You have", player_index["Escape"] * 100, "% to escape!")
                    rate = random.uniform(0, 1)

                
                    if player_index["Escape"] < rate:
                        print("You was hitted skill from Monster")
                        critical_3 = random.uniform(0,1)
                        if critical_3 < monster_index3["critical"]:
                            print("You have lose", monster_index3["Atk"]*1.5 - player_index["Def"], "HP. (Critical Damage)")
                            player_index["HP"] += (player_index["Def"] - monster_index3["Atk"]*1.5)
                            print("Your HP now is", player_index["HP"], "HP")
                        else:
                            print("You have lose", monster_index3["Atk"] - player_index["Def"], "HP")
                            player_index["HP"] += (player_index["Def"] - monster_index3["Atk"])
                            print("Your HP now is", player_index["HP"], "HP")
                        break
                    else:
                        print("You have escape successful! ")
                        print("Your HP now is", player_index["HP"], "HP")
                        break
            else:
                print("Yout have pressed a wrong button. Please entered A/E!")    
        #Kill the monster
    if (monster_index1["HP"] == 0) or (monster_index2["HP"] == 0) or (monster_index3["HP"] == 0) :
        print("You have killed a monster. You gain 5 HP")
        player_index["HP"] += 5
        
        #Killed by monster
    if player_index["HP"] <= 0:
        print("You was slained by a monster :( ")
        print("End game")
        break
    #HP_item
    HP_item_index = {
        "HP" : 10
    }
    if player["x"] == HP_item["x"] and player["y"] == HP_item["y"]:
        print("You get a potion. You have gained", HP_item_index["HP"], "HP")
        player_index["HP"] += HP_item_index["HP"]
        print("Your HP now is", player_index["HP"], "HP")

    
    #Exit
    if player['x'] == Exit['x'] and player ['y'] == Exit['y']:
        if ('x' in Key1 and 'y' in Key1) or ('x' in Key2 and 'y' in Key2):
            print("You don't have enough key :(")
           
        else:
            print("You have win this game")
            break



    
