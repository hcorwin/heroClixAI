#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from Heros import *

window = Tk()
window.title("HeroClixAI")

myCapHero = CaptainAmerica()
myIronManHero = IronMan()
myThorHero = Thor()
enemyCapHero = CaptainAmerica()
enemyIronManHero = IronMan()
enemyThorHero = Thor()
heroArray = [myCapHero, myIronManHero, myThorHero,
             enemyCapHero, enemyIronManHero, enemyThorHero]

ourCapToEnemyCapDistance = 0
ourCapToEnemyIronmanDistance = 0
ourCapToEnemyThorDistance = 0

ourIronmanToEnemyCapDistance = 0
ourIronmanToEnemyIronmanDistance = 0
ourIronmanToEnemyThorDistance = 0

ourThorToEnemyCapDistance = 0
ourThorToEnemyIronmanDistance = 0
ourThorToEnemyThorDistance = 0

ourCapToOurIronmanDistance = 0
ourCapToOurThorDistance = 0
ourIronmanToOurThorDistance = 0

enemyCapToEnemyIronmanDistance = 0
enemyCapToEnemyThorDistance = 0
enemyIronmanToEnemyThorDistance = 0

capsClosestEnemyDistance = 0
ironmansClosestEnemyDistance = 0
thorsClosestEnemyDistance = 0
            

# Used to determine what moves we should make this turn
def getMove():
    
    # we want caps distance to be smallest, if it isn't, we are moving cap to the closest enemy, unless attacks are
    # happening
    allSmallest = min(capsClosestEnemyDistance, ironmansClosestEnemyDistance, thorsClosestEnemyDistance)
    characterPlaces = [myCapHero.location, myThorHero.location, myIronManHero.location, enemyCapHero.location,
                       enemyIronManHero.location, enemyThorHero.location]

    # attack with Thor first, hes a big boy

    # Check if Thor has Sidestep
    if 6 <= myThorHero.placeInDial <= 8:

        # If Thor has 2 action tokens, move with Sidestep into Enemy Thor's range
        if myThorHero.actionToken == 2:
            return 0

        # if thorSmallest <= myThorHero.range and myThorHero.inPlay and myThorHero.actionToken == 0:
        #     # if thor can attack, attack whoever is close. Get name of closest target
        #     if thorSmallest == thorToCapDistance:
        #         print("Thor attack Cap")
        #     if thorSmallest == thorToIronDistance:
        #         print("Thor attack Iron man")
        #     if thorSmallest == thorToThorDistance:
        #         print("Thor attack Thor")

    # if were here that means thor cannot attack, check if Iron Man can attack

    # Check if Ironman has Sidestep
    if 3 <= myIronManHero.placeInDial <= 6:

        # If Iron man has 2 action tokens, move with Sidestep into a safe attacking range of Thor or Cap
        if myIronManHero.actionToken == 2:
            return 0

        # if ironManSmallest <= myIronManHero.range and myIronManHero.inPlay and myThorHero.actionToken == 0:
        #     # if iron man can attack, attack whoever is close. Get the name of closest target
        #     if ironManSmallest == ironToCapDistance:
        #         print("Iron Man attack Cap")
        #     if ironManSmallest == ironToIronDistance:
        #         print("Iron Man attack Iron Man")
        #     if ironManSmallest == ironToThorDistance:
        #         print("Iron Man attack Thor")

    # if we are here, that means thor nor iron man can attack, if cap is all that is left, he needs to attack

    # Check if Captain America has Sidestep
    if 4 <= myCapHero.placeInDial <= 6:

        # If Iron man has 2 action tokens then he can only move with Sidestep, Move closer to enemy
        if myCapHero.actionToken == 2:
            return 0

        # if capSmallest <= myCapHero.range and myCapHero.inPlay and myCapHero.actionToken == 0:
        #     if capSmallest == capToCapDistance:
        #         print("Cap attack Cap")
        #     if capSmallest == capToIronDistance:
        #         print("Cap attack Iron Man")
        #     if capSmallest == capToThorDistance:
        #         print("Cap attack Thor")
    # if we didn't attack, then we need to move, lets move towards thor so we can kill that guy, then iron man, then cap
    # decide who are going after in the order Thor > Iron Man > Cap
    goToLocation = ""
    if not enemyThorHero.inPlay:
        if not enemyIronManHero.inPlay:
            goToLocation = enemyCapHero.location
        goToLocation = enemyIronManHero.location
    else:
        goToLocation = enemyThorHero.location
    if myThorHero.inPlay and myThorHero.actionToken == 0:
        tempMap = whatTheFuckThisThingIsHuge
        # remove all instances of the characters location from the map
        for q, v in tempMap.items():
            for i in characterPlaces:
                if v == i:
                    v.remove(i)
        if thorToThorDistance > myThorHero.movement[myThorHero.placeInDial][0]:
            newSpot = bfs(tempMap, myThorHero.location, goToLocation)[myThorHero.movement[myThorHero.placeInDial][0]]
        else:
            newSpot = bfs(tempMap, myThorHero.location, goToLocation)[
                myThorHero.movement[myThorHero.placeInDial][0] - 5]
        myThorHero.location = newSpot
        print("Move Thor to ", newSpot)
    if myIronManHero.inPlay and myThorHero.actionToken == 0:
        tempMap = whatTheFuckThisThingIsHuge
        characterPlaces = [myCapHero.location, myThorHero.location, myIronManHero.location, enemyCapHero.location,
                           enemyIronManHero.location, enemyThorHero.location]
        # remove all instances of the characters location from the map
        for q, v in tempMap.items():
            for i in characterPlaces:
                if v == i:
                    v.remove(i)
        if ironToThorDistance > myIronManHero.movement[myIronManHero.placeInDial][0]:
            newSpot2 = bfs(tempMap, myIronManHero.location, goToLocation)[
                myIronManHero.movement[myIronManHero.placeInDial][0]]
        else:
            newSpot2 = bfs(tempMap, myIronManHero.location, goToLocation)[
                myIronManHero.movement[myIronManHero.placeInDial][0] - 5]
        myIronManHero.location = newSpot2
        print("Move Iron Man to ", newSpot2)
    if myCapHero.inPlay and myCapHero.actionToken == 0:
        tempMap = whatTheFuckThisThingIsHuge
        characterPlaces = [myCapHero.location, myThorHero.location, myIronManHero.location, enemyCapHero.location,
                           enemyIronManHero.location, enemyThorHero.location]
        # remove all instances of the characters location from the map
        for q, v in tempMap.items():
            for i in characterPlaces:
                if v == i:
                    v.remove(i)
        if capToThorDistance > myCapHero.movement[myCapHero.placeInDial][0]:
            newSpot3 = bfs(tempMap, myCapHero.location, goToLocation)[
                myCapHero.movement[myCapHero.placeInDial][0]]
        else:
            newSpot3 = bfs(tempMap, myCapHero.location, goToLocation)[
                myCapHero.movement[myCapHero.placeInDial][0] - 5]
        myCapHero.location = newSpot3
        print("Move Cap to ", newSpot3)

# Find the distances between all units on the board
def getDistances():
    ourCapToEnemyCapDistance = len(bfs(whatTheFuckThisThingIsHuge, myCapHero.location, enemyCapHero.location))
    ourCapToEnemyIronmanDistance = len(bfs(whatTheFuckThisThingIsHuge, myCapHero.location, enemyIronManHero.location))
    ourCapToEnemyThorDistance = len(bfs(whatTheFuckThisThingIsHuge, myCapHero.location, enemyThorHero.location))
    capsClosestEnemyDistance = min(ourCapToEnemyCapDistance, ourCapToEnemyIronmanDistance, ourCapToEnemyThorDistance)

    ourIronmanToEnemyCapDistance = len(bfs(whatTheFuckThisThingIsHuge, myIronManHero.location, enemyCapHero.location))
    ourIronmanToEnemyIronmanDistance = len(bfs(whatTheFuckThisThingIsHuge, myIronManHero.location, enemyIronManHero.location))
    ourIronmanToEnemyThorDistance = len(bfs(whatTheFuckThisThingIsHuge, myIronManHero.location, enemyThorHero.location))
    ironmansClosestEnemyDistance = min(ourIronmanToEnemyCapDistance, ourIronmanToEnemyIronmanDistance, ourIronmanToEnemyThorDistance)

    ourThorToEnemyCapDistance = len(bfs(whatTheFuckThisThingIsHuge, myThorHero.location, enemyCapHero.location))
    ourThorToEnemyIronmanDistance = len(bfs(whatTheFuckThisThingIsHuge, myThorHero.location, enemyIronManHero.location))
    ourThorToEnemyThorDistance = len(bfs(whatTheFuckThisThingIsHuge, myThorHero.location, enemyThorHero.location))
    thorsClosestEnemyDistance = min(ourThorToEnemyCapDistance, ourThorToEnemyIronmanDistance, ourThorToEnemyThorDistance)

    ourCapToOurIronmanDistance = len(bfs(whatTheFuckThisThingIsHuge, myCapHero.location, myIronManHero.location))
    ourCapToOurThorDistance = len(bfs(whatTheFuckThisThingIsHuge, myCapHero.location, myThorHero.location))
    ourIronmanToOurThorDistance = len(bfs(whatTheFuckThisThingIsHuge, myIronManHero.location, myThorHero.location))

    enemyCapToEnemyIronmanDistance = len(bfs(whatTheFuckThisThingIsHuge, enemyCapHero.location, enemyIronManHero.location))
    enemyCapToEnemyThorDistance = len(bfs(whatTheFuckThisThingIsHuge, enemyCapHero.location, enemyThorHero.location))
    enemyIronmanToEnemyThorDistance = len(bfs(whatTheFuckThisThingIsHuge, enemyIronManHero.location, enemyThorHero.location))

# Check if we can attack an enemy
def canAttack(unit):
    # Check to see if any enemy is in LOS
    thor = lineOfSight(unit.location, unit.range)[0]
    tony = lineOfSight(unit.location, unit.range)[1]
    cap = lineOfSight(unit.location, unit.range)[2]

    # We want to prioritize thor, then Iron Man, then Cap
    if(thor):
        print(unit.__str__+ " Attacks Thor")
    elif(tony):
        print(unit.__str__+ " Attacks Iron Man")
    elif(cap):
        print(unit.__str__+ " Attacks Captain America")
    else:
        return False
# Check if the charge ability is useful
def canCharge(unit):
    

# Check if the sidestep ability is useful
def canSidestep(unit):


# Check if the running shot ability is useful
def canRunningShot(unit):

# Check if we can have Cap closeCombat
def canCloseCombat():
    # Check if 
    if()
# Check if Tony RangedCombat
def canRangedCombat():
    

# Check if thor can LS
def canLightningSmash():
    count = 0
    if(getDistances.)
    if(count>=2):
        return True
    else:
        return False


# Check is we have a line of sight on the enemy based on our location and range
def lineOfSight(startingLocation, range):

    # Array that we will return in the end
    attackEnemyArray = [False, False, False] 
    # Will keep track of how much of the provided range we actually use
    rangeUsed = 1

    # The Letter associated with our starting location
    startingLetter = startingLocation[0]

    # The Number associated with out starting location
    startingNumber = startingLocation[1:]

    # Find the index of the Starting Letter so we can iterate through the alphabet
    for index in alphabet:
        if startingLetter == index:
            startingLetter = alphabet.index(index)

    # The Letter associated with the next location
    nextLetter = str(startingLetter)

    # The Number associated with the next location
    nextNumber = startingLocation[1:]

    # The next location we will be checking for an enemy at
    nextLocation = startingLocation

    # Used to hold the key's value that we are looking at
    tempKey = 0

    # Iterate through the dictionary and find our starting location
    for key in whatTheFuckThisThingIsHuge:
        
        if key == startingLocation:

            # Copy key's value into tempKey so key is not modified
            tempKey = key

            # Check directly above our starting location for an enemy by decrementing the number
            while rangeUsed <= range:

                # Decrement the next checked location's number to create it and then search for enemies
                nextNumber = int(nextNumber)
                nextNumber -= 1
                nextNumber = str(nextNumber)
                nextLocation = alphabet[int(nextLetter)] + nextNumber

                # We have created the next location so now check all items associated with the key to see if it exists
                for item in whatTheFuckThisThingIsHuge[tempKey]:
                    if (item == nextLocation):
                        tempKey = nextLocation
                        if (enemyThorHero.location == nextLocation):
                            attackEnemyArray[0] = [True, nextLocation]
                            rangeUsed = range
                            break
                            
                        if (enemyIronMan.location == nextLocation):
                            attackEnemyArray[1] = [True, nextLocation]
                            rangeUsed = range
                            break    

                        if (enemyCapHero.location == nextLocation):
                            attackEnemyArray[2] = [True, nextLocation]
                            rangeUsed = range
                            break

                rangeUsed += 1

            # Reset the variables before checking next sight line
            nextLetter = str(startingLetter)
            nextNumber = startingLocation[1:]
            nextLocation = startingLocation
            tempKey = key               
            rangeUsed = 1

            # Check directly below our starting location for an enemy by incrementing the number
            while rangeUsed <= range:

                # Increment the next checked location's number to create it and then search for enemies
                nextNumber = int(nextNumber)
                nextNumber += 1
                nextNumber = str(nextNumber)
                nextLocation = alphabet[int(nextLetter)] + nextNumber

                # We have created the next location so now check all items associated with the key to see if it exists
                for item in whatTheFuckThisThingIsHuge[tempKey]:
                    if (item == nextLocation):
                        tempKey = nextLocation
                        if (enemyThorHero.location == nextLocation):
                            attackEnemyArray[0] = [True, nextLocation]
                            rangeUsed = range
                            break
                            
                        if (enemyIronMan.location == nextLocation):
                            attackEnemyArray[1] = [True, nextLocation]
                            rangeUsed = range
                            break    

                        if (enemyCapHero.location == nextLocation):
                            attackEnemyArray[2] = [True, nextLocation]
                            rangeUsed = range
                            break

                rangeUsed += 1

            # Reset the variables before checking next sight line
            nextLetter = str(startingLetter)
            nextNumber = startingLocation[1:]
            nextLocation = startingLocation
            tempKey = key               
            rangeUsed = 1

            # Check directly to the left our starting location for an enemy by decrementing the letter
            while rangeUsed <= range:
                
                 # Decrement the next checked location's letter to create it and then search for enemies
                nextLetter = int(nextLetter)
                nextLetter -= 1
                nextLetter = str(nextLetter)
                nextNumber = str(nextNumber)
                nextLocation = alphabet[int(nextLetter)] + nextNumber

                # We have created the next location so now check all items associated with the key to see if it exists
                for item in whatTheFuckThisThingIsHuge[tempKey]:
                    if (item == nextLocation):
                        tempKey = nextLocation
                        if (enemyThorHero.location == nextLocation):
                            attackEnemyArray[0] = [True, nextLocation]
                            rangeUsed = range
                            break
                            
                        if (enemyIronMan.location == nextLocation):
                            attackEnemyArray[1] = [True, nextLocation]
                            rangeUsed = range
                            break    

                        if (enemyCapHero.location == nextLocation):
                            attackEnemyArray[2] = [True, nextLocation]
                            rangeUsed = range
                            break
                rangeUsed += 1
            # Reset the variables before checking next sight line
            nextLetter = str(startingLetter)
            nextNumber = startingLocation[1:]
            nextLocation = startingLocation
            tempKey = key               
            rangeUsed = 1

            # Check directly to the right our starting location for an enemy by incrementing the letter
            while rangeUsed <= range:

                 # Increment the next checked location's letter to create it and then search for enemies
                nextLetter = int(nextLetter)
                nextLetter += 1
                nextLetter = str(nextLetter)
                nextNumber = str(nextNumber)
                nextLocation = alphabet[int(nextLetter)] + nextNumber

                # We have created the next location so now check all items associated with the key to see if it exists
                for item in whatTheFuckThisThingIsHuge[tempKey]:
                    if (item == nextLocation):
                        tempKey = nextLocation
                        if (enemyThorHero.location == nextLocation):
                            attackEnemyArray[0] = [True, nextLocation]
                            rangeUsed = range
                            break
                            
                        if (enemyIronMan.location == nextLocation):
                            attackEnemyArray[1] = [True, nextLocation]
                            rangeUsed = range
                            break    

                        if (enemyCapHero.location == nextLocation):
                            attackEnemyArray[2] = [True, nextLocation]
                            rangeUsed = range
                            break
                rangeUsed += 1

            # Reset the variables before checking next sight line
            nextLetter = str(startingLetter)
            nextNumber = startingLocation[1:]
            nextLocation = startingLocation
            tempKey = key               
            rangeUsed = 1

            # Check directly to the top left diagonal of our starting location for an enemy
            while rangeUsed <= range:

                 # Decrement the next checked location's number and letter to create it and then search for enemies
                nextLetter = int(nextLetter)
                nextNumber = int(nextNumber)
                nextLetter -= 1
                nextNumber -= 1
                nextLetter = str(nextLetter)
                nextNumber = str(nextNumber)
                nextLocation = alphabet[int(nextLetter)] + nextNumber

                # We have created the next location so now check all items associated with the key to see if it exists
                for item in whatTheFuckThisThingIsHuge[tempKey]:
                    if (item == nextLocation):
                        tempKey = nextLocation
                        if (enemyThorHero.location == nextLocation):
                            attackEnemyArray[0] = [True, nextLocation]
                            rangeUsed = range
                            break
                            
                        if (enemyIronMan.location == nextLocation):
                            attackEnemyArray[1] = [True, nextLocation]
                            rangeUsed = range
                            break    

                        if (enemyCapHero.location == nextLocation):
                            attackEnemyArray[2] = [True, nextLocation]
                            rangeUsed = range
                            break
                rangeUsed += 1

            # Reset the variables before checking next sight line
            nextLetter = str(startingLetter)
            nextNumber = startingLocation[1:]
            nextLocation = startingLocation
            tempKey = key               
            rangeUsed = 1

            # Check directly to the top right diagonal of our starting location for an enemy
            while rangeUsed <= range:

                 # Increment the next checked location's letter and decrement the number to create it and then search for enemies
                nextLetter = int(nextLetter)
                nextNumber = int(nextNumber)
                nextLetter += 1
                nextNumber -= 1
                nextLetter = str(nextLetter)
                nextNumber = str(nextNumber)
                nextLocation = alphabet[int(nextLetter)] + nextNumber

                # We have created the next location so now check all items associated with the key to see if it exists
                for item in whatTheFuckThisThingIsHuge[tempKey]:
                    if (item == nextLocation):
                        tempKey = nextLocation
                        if (enemyThorHero.location == nextLocation):
                            attackEnemyArray[0] = [True, nextLocation]
                            rangeUsed = range
                            break
                            
                        if (enemyIronMan.location == nextLocation):
                            attackEnemyArray[1] = [True, nextLocation]
                            rangeUsed = range
                            break    

                        if (enemyCapHero.location == nextLocation):
                            attackEnemyArray[2] = [True, nextLocation]
                            rangeUsed = range
                            break
                rangeUsed += 1

            # Reset the variables before checking next sight line
            nextLetter = str(startingLetter)
            nextNumber = startingLocation[1:]
            nextLocation = startingLocation
            tempKey = key               
            rangeUsed = 1

            # Check directly to the bottom left diagonal of our starting location for an enemy
            while rangeUsed <= range:

                 # Increment the next checked location's number and decrement the letter to create it and then search for enemies
                nextLetter = int(nextLetter)
                nextNumber = int(nextNumber)
                nextLetter -= 1
                nextNumber += 1
                nextLetter = str(nextLetter)
                nextNumber = str(nextNumber)
                nextLocation = alphabet[int(nextLetter)] + nextNumber

                # We have created the next location so now check all items associated with the key to see if it exists
                for item in whatTheFuckThisThingIsHuge[tempKey]:
                    if (item == nextLocation):
                        tempKey = nextLocation
                        if (enemyThorHero.location == nextLocation):
                            attackEnemyArray[0] = [True, nextLocation]
                            rangeUsed = range
                            break
                            
                        if (enemyIronMan.location == nextLocation):
                            attackEnemyArray[1] = [True, nextLocation]
                            rangeUsed = range
                            break    

                        if (enemyCapHero.location == nextLocation):
                            attackEnemyArray[2] = [True, nextLocation]
                            rangeUsed = range
                            break
                rangeUsed += 1

            # Reset the variables before checking next sight line
            nextLetter = str(startingLetter)
            nextNumber = startingLocation[1:]
            nextLocation = startingLocation
            tempKey = key               
            rangeUsed = 1

            # Check directly to the bottom right diagonal of our starting location for an enemy
            while rangeUsed <= range:

                 # Increment the next checked location's number and letter to create it and then search for enemies
                nextLetter = int(nextLetter)
                nextNumber = int(nextNumber)
                nextLetter += 1
                nextNumber += 1
                nextLetter = str(nextLetter)
                nextNumber = str(nextNumber)
                nextLocation = alphabet[int(nextLetter)] + nextNumber

                # We have created the next location so now check all items associated with the key to see if it exists
                for item in whatTheFuckThisThingIsHuge[tempKey]:
                    if (item == nextLocation):
                        tempKey = nextLocation
                        if (enemyThorHero.location == nextLocation):
                            attackEnemyArray[0] = [True, nextLocation]
                            rangeUsed = range
                            break
                            
                        if (enemyIronMan.location == nextLocation):
                            attackEnemyArray[1] = [True, nextLocation]
                            rangeUsed = range
                            break    

                        if (enemyCapHero.location == nextLocation):
                            attackEnemyArray[2] = [True, nextLocation]
                            rangeUsed = range
                            break
                rangeUsed += 1

    return(attackEnemyArray)
    print(attackEnemyArray)                

                

def updateState():
    myCapHero.location = capEntry.get()

    myIronManHero.location = ironManEntry.get()

    myThorHero.location = thorEntry.get()

    enemyCapHero.location = enemyCapEntry.get()

    enemyIronManHero.location = enemyIronManEntry.get()

    enemyThorHero.location = enemyThorEntry.get()

    if whosAttackingEntry.get():
        whosAttackingText = whosAttackingEntry.get()
    if whosDefendingEntry.get():
        whosBeingAttackedText = whosDefendingEntry.get()
    if whatWasRolledEntry.get():
        whatWasRolled = int(whatWasRolledEntry.get())


def bfs(graph, start, destination):
    beenTo = []
    queue = [[start]]

    if start == destination:
        return
    while queue:
        p = queue.pop(0)
        n = p[-1]

        if n not in beenTo:
            close = graph[n]
            for closest in close:
                np = list(p)
                np.append(closest)
                queue.append(np)

                if closest == destination:
                    return np
            beenTo.append(n)


def forceValueToHero():
    whosValueToChange = valueToEntry.get()
    whatTheValueIs = int(valueEntry.get())


def getStatsOnHero():
    whosStats = int(statsEntry.get())
    messagebox.showinfo(heroArray[whosStats], str(heroArray[whosStats].placeInDial))


# labels
ourCap = Label(window, text="My Cap")
ourCap.grid(row=0, column=0)

ourIronMan = Label(window, text="My Iron Man")
ourIronMan.grid(row=1, column=0)

ourThor = Label(window, text="My Thor")
ourThor.grid(row=2, column=0)

enemyCap = Label(window, text="Enemy Cap")
enemyCap.grid(row=0, column=2)

enemyIronMan = Label(window, text="Enemy Iron Man")
enemyIronMan.grid(row=1, column=2)

enemyThor = Label(window, text="Enemy Thor")
enemyThor.grid(row=2, column=2)

whosAttacking = Label(window, text="Whos Attacking")
whosAttacking.grid(row=4, column=0)

whosDefending = Label(window, text="Whos Defending")
whosDefending.grid(row=4, column=2)

emptySpace = Label(window, text="")
emptySpace.grid(row=3, column=0)

emptySpace2 = Label(window, text="")
emptySpace2.grid(row=6, column=0)

whatsRolled = Label(window, text="Number Rolled")
whatsRolled.grid(row=5, column=0)

forceValue = Label(window, text="Force Value to")
forceValue.grid(row=7, column=0)

valueToForce = Label(window, text="Value: ")
valueToForce.grid(row=7, column=2)

getStatsOn = Label(window, text="Get Stats On")
getStatsOn.grid(row=9, column=0)

# Entries
capEntry = Entry(window)
capEntry.grid(row=0, column=1)

ironManEntry = Entry(window)
ironManEntry.grid(row=1, column=1)

thorEntry = Entry(window)
thorEntry.grid(row=2, column=1)

enemyCapEntry = Entry(window)
enemyCapEntry.grid(row=0, column=3)

enemyIronManEntry = Entry(window)
enemyIronManEntry.grid(row=1, column=3)

enemyThorEntry = Entry(window)
enemyThorEntry.grid(row=2, column=3)

whosDefendingEntry = Entry(window)
whosDefendingEntry.grid(row=4, column=1)

whosAttackingEntry = Entry(window)
whosAttackingEntry.grid(row=4, column=3)

whatWasRolledEntry = Entry(window)
whatWasRolledEntry.grid(row=5, column=1)

valueToEntry = Entry(window)
valueToEntry.grid(row=7, column=1)

valueEntry = Entry(window, )
valueEntry.grid(row=7, column=3)

statsEntry = Entry(window)
statsEntry.grid(row=9, column=1)

# Buttons
attackButton = Button(window, text="Update State", bg="gray", command=updateState)
attackButton.grid(row=5, column=2)

forceButton = Button(window, text="Force Value", bg="gray", command=forceValueToHero)
forceButton.grid(row=8, column=2)

getStatsButton = Button(window, text="Get Stats", bg="gray", command=getStatsOnHero)
getStatsButton.grid(row=9, column=2)

getMoveButton = Button(window, text="Get Move", bg="gray", command=getMove)
getMoveButton.grid(row=10, column=2)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

whatTheFuckThisThingIsHuge = {'A1': ['B1', 'A2', 'B2'], 'B1': ['A1', 'C1', 'A2', 'B2', 'C2'],
                              'C1': ['B1', 'D1', 'B2', 'C2', 'D2'], 'D1': ['C1', 'E1', 'C2', 'D2', 'E2'],
                              'E1': ['D1', 'F1', 'D2', 'E2', 'F2'], 'F1': ['E1', 'G1', 'E2', 'F2', 'G2'],
                              'G1': ['F1', 'H1', 'F2', 'G2', 'H2'], 'H1': ['G1', 'G2', 'H2'],
                              'I1': ['J1', 'I2', 'J2'], 'J1': ['I1', 'K1', 'I2', 'J2', 'K2'],
                              'K1': ['J1', 'L1', 'J2', 'K2', 'L2'], 'L1': ['K1', 'M1', 'K2', 'L2', 'M2'],
                              'M1': ['L1', 'N1', 'L2', 'M2', 'N2'], 'N1': ['M1', 'O1', 'M2', 'N2', 'O2'],
                              'O1': ['N1', 'P1', 'N2', 'O2', 'P2'], 'P1': ['O1', 'O2', 'P2'],
                              'A2': ['A1', 'B1', 'B2', 'B3', 'A3'],
                              'B2': ['A1', 'B1', 'C1', 'C2', 'C3', 'B3', 'A3', 'A2'],
                              'C2': ['B1', 'C1', 'D1', 'D2', 'D3', 'C3', 'B3', 'B2'],
                              'D2': ['C1', 'D1', 'E1', 'E2', 'D3', 'C3', 'C2'],
                              'E2': ['D1', 'E1', 'F1', 'F2', 'D3', 'D2'], 'F2': ['E1', 'F1', 'G1', 'E2'],
                              'G2': ['F1', 'G1', 'H1', 'H2', 'H3', 'G3', 'F3'],
                              'H2': ['G1', 'H1', 'H3', 'G3', 'G2'], 'I2': ['I1', 'J1', 'J2', 'J3', 'I3'],
                              'J2': ['I1', 'J1', 'K1', 'K3', 'J3', 'I3', 'I2'],
                              'K2': ['J1', 'K1', 'L1', 'L2'], 'L2': ['K1', 'L1', 'M1', 'M2', 'M3', 'K2'],
                              'M2': ['L1', 'M1', 'N1', 'N2', 'N3', 'M3', 'L2'],
                              'N2': ['M1', 'N1', 'O1', 'O2', 'O3', 'N3', 'M3', 'M2'],
                              'O2': ['N1', 'O1', 'P1', 'P2', 'P3', 'O3', 'N3', 'N2'],
                              'P2': ['O1', 'P1', 'P3', 'O3', 'O2'],
                              'A3': ['A2', 'B2', 'B3', 'B4', 'A4'],
                              'B3': ['A2', 'B2', 'C2', 'C3', 'C4', 'B4', 'A4', 'A3'],
                              'C3': ['B2', 'C2', 'D2', 'D3', 'D4', 'C4', 'B4', 'B3'],
                              'D3': ['C2', 'D2', 'E2', 'D4', 'C4', 'C3'], 'E3': ['F3', 'F4', 'E4'],
                              'F3': ['G2', 'G3', 'G4', 'F4', 'E4', 'E3'],
                              'G3': ['G2', 'H2', 'H3', 'H4', 'G4', 'F4', 'F3'], 'H3': ['G2', 'H2', 'H4', 'G4', 'G3'],
                              'I3': ['I2', 'J2', 'J3', 'J4', 'I4', 'H4'],
                              'J3': ['I2', 'J2', 'K3', 'K4', 'J4', 'I4', 'I3'],
                              'K3': ['J2', 'L3', 'L4', 'K4', 'J4', 'J3'], 'L3': ['L4', 'K4', 'K3'],
                              'M3': ['L2', 'M2', 'N2', 'N3', 'N4', 'M4'],
                              'N3': ['M2', 'N2', 'O2', 'O3', 'O4', 'N4', 'M4', 'M3'],
                              'O3': ['N2', 'O2', 'P2', 'P3', 'P4', 'O4', 'N4', 'N3'],
                              'P3': ['O2', 'P2', 'P4', 'O4', 'O3'], 'A4': ['A3', 'B3', 'B4', 'B5', 'A5'],
                              'B4': ['A3', 'B3', 'C3', 'C4', 'B5', 'A5', 'A4'],
                              'C4': ['B3', 'C3', 'D3', 'D4', 'B5', 'B4'],
                              'D4': ['C3', 'D3', 'C4'], 'E4': ['E3', 'F3', 'F4', 'F5', 'E5'],
                              'F4': ['E3', 'F3', 'G3', 'G4', 'F5', 'E5', 'E4'],
                              'G4': ['F3', 'G3', 'H3', 'H4', 'H5', 'F5', 'F4'],
                              'H4': ['G3', 'H3', 'I3', 'I4', 'I5', 'H5', 'G5', 'G4'],
                              'I4': ['H3', 'I3', 'J3', 'J4', 'J5', 'I5', 'H5', 'H4'],
                              'J4': ['I3', 'J3', 'K3', 'K4', 'K5', 'J5', 'I5', 'I4'],
                              'K4': ['J3', 'K3', 'L3', 'L4', 'J5', 'J4'], 'L4': ['K3', 'L3', 'L4'],
                              'M4': ['M3', 'N3', 'N4'], 'N4': ['M3', 'N3', 'O3', 'O4', 'O5', 'M4'],
                              'O4': ['N3', 'O3', 'P3', 'P4', 'P5', 'O5', 'N4'],
                              'P4': ['O3', 'P3', 'P5', 'O5', 'O4'], 'A5': ['A4', 'B4', 'B5', 'B6', 'A6'],
                              'B5': ['A4', 'B4', 'C4', 'B6', 'A6', 'A5'], 'C5': ['D5', 'D6', 'C6'],
                              'D5': ['D6', 'C6', 'C5'],
                              'E5': ['E4', 'F4', 'F5', 'F6', 'E6', 'D6'], 'F5': ['E4', 'F4', 'G4', 'F6', 'E6', 'E5'],
                              'G5': ['H4', 'H5', 'H6', 'G6'], 'H5': ['G4', 'H4', 'I4', 'I5', 'I6', 'H6', 'G6', 'G5'],
                              'I5': ['H4', 'I4', 'J4', 'J5', 'J5', 'J6', 'I6', 'H6', 'H5'],
                              'J5': ['I4', 'J4', 'K4', 'K5', 'K6', 'J6', 'I6', 'I5'],
                              'K5': ['J4', 'L5', 'L6', 'K6', 'J6', 'J5'],
                              'L5': ['M5', 'M6', 'L6', 'K6', 'K5'], 'M5': ['N5', 'N6', 'M6', 'L6', 'L5'],
                              'N5': ['N6', 'M6', 'M5'],
                              'O5': ['N4', 'O4', 'P4', 'P5', 'P6', 'O6'], 'P5': ['O4', 'P4', 'P6', 'O6', 'O5'],
                              'A6': ['A5', 'B5', 'B6', 'B7', 'A7'], 'B6': ['A5', 'B5', 'B7', 'A7', 'A6'],
                              'C6': ['C5', 'D5', 'D6', 'D7', 'C7'],
                              'D6': ['C5', 'D5', 'E5', 'E6', 'E7', 'D7', 'C7', 'C6'],
                              'E6': ['D5', 'E5', 'F5', 'F6', 'F7', 'F8', 'E7', 'D7', 'D6'],
                              'F6': ['E5', 'F5', 'F7', 'E7', 'E6'],
                              'G6': ['G5', 'H5', 'H6', 'H7', 'G7'], 'H6': ['G5', 'H5', 'I5', 'I6', 'G7', 'G6'],
                              'I6': ['H5', 'I5', 'J5', 'J6', 'H6'], 'J6': ['I5', 'J5', 'K5', 'K6', 'I6'],
                              'K6': ['J5', 'K5', 'L5', 'L6', 'J6'], 'L6': ['K5', 'L5', 'M5', 'M6', 'M7', 'K6'],
                              'M6': ['L5', 'M5', 'N5', 'N6', 'N7', 'M7', 'L6'],
                              'N6': ['M5', 'N5', 'O7', 'N7', 'M7', 'M6'],
                              'O6': ['O5', 'P5', 'P6', 'P7'], 'P6': ['O5', 'P5', 'P7', 'O7', 'O6'],
                              'A7': ['A6', 'B6', 'B7', 'B8', 'A8'], 'B7': ['A6', 'B6', 'B8', 'A8', 'A7'],
                              'C7': ['C6', 'D6', 'D7'], 'D7': ['C6', 'D6', 'E6', 'E7', 'E8', 'C7'],
                              'E7': ['D6', 'E6', 'F6', 'F7', 'F8', 'E8', 'D8', 'D7'],
                              'F7': ['E6', 'F6', 'F8', 'E8', 'E7'], 'G7': ['G6', 'H6', 'H7',  'G8'],
                              'H7': ['G6', 'I7',  'G8', 'G7'], 'I7': ['J7', 'J8',  'H7'],
                              'J7': ['J8', 'I7'], 'K7': ['L7', 'L8', 'K8'],
                              'L7': ['M6', 'M7', 'M8', 'L8', 'K8', 'K7'],
                              'M7': ['L6', 'M6', 'N6', 'N7', 'N8', 'M8', 'L8', 'L7'],
                              'N7': ['M6', 'N6', 'O7', 'O8', 'N8', 'M8', 'M7'],
                              'O7': ['N6', 'P6', 'P7', 'P8', 'O8', 'N8', 'N7'], 'P7': ['O6', 'P6', 'P8', 'O8', 'O7'],
                              'A8': ['A7', 'B7', 'B8', 'B8', 'A9'], 'B8': ['A7', 'B7', 'B9', 'A9', 'A8'],
                              'C8': ['D8', 'D9', 'C9'], 'D8': ['E7', 'E8', 'E9', 'D9', 'C9', 'C8'],
                              'E8': ['D7', 'E7', 'F7', 'F8', 'F9', 'E9', 'D9', 'D8'],
                              'F8': ['E7', 'F7', 'G9', 'F9', 'E9', 'E8'],
                              'G8': ['G7', 'H7',   'G9', 'F9'],
                              'J8': ['I7', 'J7', 'J9'], 'K8': ['K7', 'L7', 'L8', 'L9', 'K9'],
                              'L8': ['K7', 'L7', 'M7', 'M8', 'M9', 'L9', 'K9', 'K8'],
                              'M8': ['L7', 'M7', 'N7', 'N8', 'L9', 'L8'],
                              'N8': ['M7', 'N7', 'O7', 'O8', 'M8'], 'O8': ['N7', 'O7', 'P7', 'P8', 'N8'],
                              'P8': ['O7', 'P7', 'O8'], 'A9': ['A8', 'B8', 'B9'], 'B9': ['A8', 'B8', 'C9', 'A9'],
                              'C9': ['B8', 'C8', 'D8', 'D9', 'B9'], 'D9': ['C8', 'D8', 'E8', 'E9', 'E10', 'C9'],
                              'E9': ['D8', 'E8', 'F8', 'F9', 'F10', 'E10', 'D10', 'D9'],
                              'F9': ['E8', 'F8', 'G8', 'G9', 'G10', 'F10', 'E10', 'E9'],
                              'G9': ['F8', 'G8',   'H10', 'G10', 'F10', 'F9'],
                              'J9': ['J8', 'K10', 'J10', 'I10'], 'K9': ['K8', 'L8', 'L9', 'L10', 'K10'],
                              'L9': ['K8', 'L8', 'M8', 'M9', 'M10', 'L10', 'K10', 'K9'],
                              'M9': ['L8', 'N9', 'N10', 'M10', 'L10', 'L9'], 'N9': ['O9', 'O10', 'N10', 'M10', 'M9'],
                              'O9': ['P9', 'P10', 'O10', 'N10', 'N9'], 'P9': ['P10', 'O10', 'O9'],
                              'A10': ['B10', 'B11', 'A11'], 'B10': ['B11', 'A11', 'A10'], 'C10': ['D10', 'D11', 'C11'],
                              'D10': ['E9', 'E10', 'E11', 'D11', 'C11', 'C10'],
                              'E10': ['D9', 'E9', 'F9', 'F10', 'F11', 'E11', 'D11', 'D10'],
                              'F10': ['E9', 'F9', 'G9', 'F11', 'E11', 'E10'],
                              'G10': ['F9', 'G9',  'H10'], 'H10': ['G9',  'I10', 'I11', 'G10'],
                              'I10': [ 'J9', 'J10', 'J11', 'I11', 'H11', 'H10'],
                              'J10': ['J9', 'K9', 'K10', 'I11', 'I10'],
                              'K10': ['J9', 'K9', 'L9', 'L10', 'J10'], 'L10': ['K9', 'L9', 'M9', 'M10', 'K10'],
                              'M10': ['L9', 'M9', 'N9', 'N10', 'N11', 'M11', 'L11', 'L10'],
                              'N10': ['M9', 'N9', 'O9', 'O10', 'N11', 'M11', 'M10'],
                              'O10': ['N9', 'O9', 'P9', 'P10', 'P11', 'N11', 'N10'],
                              'P10': ['O9', 'P9', 'P11', 'O11', 'O10'],
                              'A11': ['A10', 'A12', 'B11'], 'B11': ['A11', 'B10', 'B12'], 'C11': ['C10', 'C12', 'D11'],
                              'D11': ['C11', 'D10', 'D12', 'E11'],
                              'E11': ['D11', 'E10', 'E12', 'F11'], 'F11': ['E11', 'F10', 'F12'], 'G11': ['G12', 'H11'],
                              'H11': ['G11', 'H12', 'I11'], 'I11': ['H11', 'I10', 'I12', 'J11'],
                              'J11': ['I11', 'J12', 'K11'], 'K11': ['J11', 'K12', 'L11'],
                              'L11': ['K11', 'L12', 'M11'], 'M11': ['L11', 'M10', 'M12', 'N11'],
                              'N11': ['M11', 'N10', 'N12'],
                              'O11': ['O12', 'P11'], 'P11': ['O1', 'P10', 'P12'], 'A12': ['A11', 'A13', 'B12'],
                              'B12': ['A12', 'B11', 'B13'], 'C12': ['C11', 'D12'], 'D12': ['C12', 'D11', 'D13'],
                              'E12': ['E11', 'E13', 'F12'], 'F12': ['E12', 'F11', 'F13', 'G12'],
                              'G12': ['F12', 'G11', 'G13', 'H12'],
                              'H12': ['G12', 'H11', 'H13', 'I12'], 'I12': ['H12', 'I11', 'I13', 'J12'],
                              'J12': ['I12', 'J11', 'J13', 'K12'], 'K12': ['J12', 'K11', 'L12'],
                              'L12': ['K12', 'L11', 'M12'], 'M12': ['L12', 'M11', 'N12'], 'N12': ['M12', 'N11'],
                              'O12': ['O11', 'O13', 'P12'], 'P12': ['O12', 'P11', 'P13'], 'A13': ['A12', 'A14', 'B13'],
                              'B13': ['A13', 'B12', 'B14', 'C13'], 'C13': ['B13', 'C14', 'D13'],
                              'D13': ['C13', 'D12', 'D14'],
                              'E13': ['E12', 'E14', 'F13'], 'F13': ['E13', 'F12', 'F14'], 'G13': ['G12', 'G14', 'H13'],
                              'H13': ['G13', 'H12', 'H14'], 'I13': ['I12', 'I14', 'J13'],
                              'J13': ['I13', 'J12', 'J14', 'K13'], 'K13': ['J13', 'K14'],
                              'L13': ['L14', 'M13'], 'M13': ['L13', 'M14', 'N13'], 'N13': ['M13', 'N14', 'O13'],
                              'O13': ['N13', 'O12', 'O14', 'P13'], 'P13': ['O13', 'P12', 'P14'],
                              'A14': ['A13', 'A15', 'B14'], 'B14': ['A14', 'B13', 'B15', 'C14'],
                              'C14': ['B14', 'C13', 'C15', 'D14'], 'D14': ['C14', 'D13', 'D15'],
                              'E14': ['E13', 'F14'], 'F14': ['E14', 'F13', 'F15'], 'G14': ['G13', 'G15', 'H14'],
                              'H14': ['G14', 'H13', 'H15'], 'I14': ['I12', 'J14'], 'J14': ['I14', 'J13', 'J15', 'K14'],
                              'K14': ['J14', 'K13', 'K15', 'L14'],
                              'L14': ['K14', 'L13', 'L15', 'M14'], 'M14': ['L14', 'M13', 'M15', 'N14'],
                              'N14': ['M14', 'N13', 'N15', 'O14'],
                              'O14': ['N14', 'O13', 'O15', 'P14'], 'P14': ['O14', 'P13', 'P15'],
                              'A15': ['A14', 'A16', 'B15'], 'B15': ['A15', 'B14', 'B16', 'C15'],
                              'C15': ['B15', 'C14', 'C16', 'D15'], 'D15': ['C15', 'D14', 'D16'],
                              'E15': ['E16', 'F15'], 'F15': ['E15', 'F16', 'G15'], 'G15': ['F15', 'G14', 'G16', 'H15'],
                              'H15': ['G15', 'H14', 'H16'], 'I15': ['I16', 'J15'], 'J15': ['I15', 'J14', 'J16', 'K15'],
                              'K15': ['J15', 'K14', 'K16'],
                              'L15': ['L14', 'L16', 'M15'], 'M15': ['L15', 'M14', 'M16', 'N15'],
                              'N15': ['M15', 'N14', 'N16', 'O15'],
                              'O15': ['N15', 'O14', 'O16', 'P15'], 'P15': ['O15', 'P14', 'P16'],
                              'A16': ['A15', 'B16'], 'B16': ['A16', 'B15', 'C16'], 'C16': ['B16', 'C15', 'D16'],
                              'D16': ['C16', 'D15', 'E16'],
                              'E16': ['D16', 'E15', 'F16'], 'F16': ['E16', 'F15', 'G16'], 'G16': ['F16', 'G15', 'H16'],
                              'H16': ['G16', 'H15'], 'I16': ['I15', 'J16'], 'J16': ['I16', 'J15', 'K16'],
                              'K16': ['J16', 'K15'],
                              'L16': ['L15', 'M16'], 'M16': ['L16', 'M15', 'N16'], 'N16': ['M16', 'N15', 'O16'],
                              'O16': ['N16', 'O15', 'P16'], 'P16': ['O16', 'P15']}

waterArray = ['E1', 'F1', 'G1', 'J1', 'K1', 'L1', 'G2', 'J2', 'G3', 'H3', 'I3', 'J3', 'H4', 'I4', 'H5', 'I5', 'H6',
             'G7', 'H7', 'I7', 'E8', 'G8', 'J8', 'E9', 'F9', 'G9', 'J9', 'D10', 'E10', 'H10', 'I10', 'J10', 'D11', 'I11',
             'D12', 'J12', 'J13', 'J14', 'K14', 'L14', 'L15']
enemyThorHero.location = 'E8'
enemyIronMan.location = 'G10'
enemyCapHero.location = 'E10'
lineOfSight('F9', myIronManHero.range)
window.mainloop()
