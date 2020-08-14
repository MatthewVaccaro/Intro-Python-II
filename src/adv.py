from room import Room
from player import Player
from item import Item
import sys
# Declare all the rooms

items = {
    'torch': Item("Torch", "It's bright and can burn yourself...perhaps others as well"),
    'apple': Item("Apple", "You can't call anyone with this, but it's yummy"),
    'rope': Item("Rope", "30 Ft, but you can make it longer with a simple class call"),
    'map': Item("Map", "Did they make this in the dark or something?"),
    'chest': Item("Chest", "I don't think we should open this, we saw what happened in Indian Jones to that Nazi guy"),
}


room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", [items['apple'], items['torch'], ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [items['rope']]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", [items['torch']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", [items['chest']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

chapterCount = 0
cardinalDirs = ("n", "e", "s", "w")
player = Player("Terminal Lad", room['outside'])


def chooseDirection():
    direction = input('choose dirrection [N]orth, [E]ast, [S]outh, [W]est --> ')
    return direction


while True:

    print(
        f"\n---------------------------------- ⚔️ {player.name} Chapter: {chapterCount} ⚔️ ----------------------------------")
    chapterCount += 1
    print(f"\n 🧙‍♂{player.currentRoom}\n")
    print(f"🎒{player.showInventory()}\n")
    print(f" 🏰 In the Room there is:\n{player.currentRoom.showItems()}\n")
    command = chooseDirection().lower()
    # Quit Command
    if command == 'q':
        sys.exit("😝 Thanks for playing")
    #Grab Command
    elif "grab" in command:
        pickUp = command.split(' ')
        if pickUp[1] in items:
            player.grab(items[pickUp[1]])
        else:
            print("🤬 Nope, Can't do that")
    # Drop Command
    elif "drop" in command: 
        pickUp = command.split(' ')
        if pickUp[1] in items:
            player.drop(items[pickUp[1]])
        else:
            print("🤬 Nope, Can't do that")
    #Show Inventory
    # elif "i" in command:
    #     print(f"🎒{player.showInventory()}\n")
    # Wrong Input Action
    elif command not in cardinalDirs:
        print("🤬 Nope, Can't do that")
    #Move Action
    else:
        player.move(f'{command}_to')
