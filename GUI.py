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

window.mainloop()
