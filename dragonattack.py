#introduces the program and controls

print("")
print("******* Welcome to Dragon Attack! *******")
print("Your objective is to kill the dragon racing towards you.")
print("You have 5 turns to fire a cannonball at it, and save yourself.")
print("You have access to a series of actions that need to be done in a certain order to successfully shoot the cannonball")
print("Type \"take torch\" to take a torch, this will go out after 1 use and you have access to 3")
print("Type \"take cannonball\" to take a cannonball")
print("Type \"light fuse\" to light the fuse, lighting the fuse uses up a torch")
print("Type \"load cannonball\" to load a cannonball")
print("Think logically about how a cannonball should be fired, and victory is assured. Good Luck!")
print("")

########
# Code #
########

gameRound = 1
cannonballTaken = False
cannonballLoaded = False
torchTaken = False
fuseLit = False
torchAmt = 3

while True:
    #show states (for testing only, delete when game works)
    print("Round Number = " + str(gameRound))
    print("Cannonball taken = " + str(cannonballTaken))
    print("Cannball loaded = " + str(cannonballLoaded))
    print("Torch taken = " + str(torchTaken))
    print("Torch amt = " + str(torchAmt))
    print("Fuse lit = " + str(fuseLit))
    
    if gameRound == 100:
        print("You lost")
        break
    
    print("-----------------------------------------------")
    
    #ask user for their action
    action = input("What will you do?").lower()
    
    #action gets processed
    if action == "quit":
        break
    elif action == "take torch":
        if torchTaken:
            print("You already have a torch in your hand")
        elif torchAmt == 0:
            print("You ran out of torches")
            print("You lost")
            break
        else:
            torchTaken = True
    elif action == "take cannonball":
        if cannonballTaken:
            print("You already have a cannonball")
        else:
            cannonballTaken = True  
    elif action == "light fuse":
        if fuseLit:
            print("Fuse is already lit")
        elif not torchTaken:
            print("You have nothing to light the fuse with")
        elif not cannonballLoaded: 
            torchAmt -= 1
            torchTaken = False
            print("No cannonball to fire")
            if torchAmt == 0:
                print("You lost")
                break
        elif torchTaken and torchAmt > 0:#fuse can only be lit once a torch is taken and fuse is not already lit
            fuseLit = True
            print("The dragon is dead, you won!")
            break           
    elif action == "load cannonball":
        if cannonballLoaded:
            print("Cannonball is already loaded")
        elif not cannonballTaken:
            print("You don't have a cannonball to load")
        elif cannonballTaken:#cannonball can only be loaded once a cannonball is taken and there isn't already a cannonball loaded
            cannonballLoaded = True
    else:
        print("That is not an action")
  
    
    
    #updates round number
    gameRound += 1    
        
       
