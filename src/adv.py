from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Make a new player object that is currently in the 'outside' room.

vlad = Player("Vlad", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

quit = False

while not quit:
    print(f"\n{vlad.name}, \nYou're in in the {vlad.location.name}")
    print(vlad.location.description)
    print("\nWhere do you want to go?")
    command = input("\n(N)orth\n(S)outh\n(E)ast\n(W)est\n\nCommand: ")
     # _.strip() removes leading/trailing spaces
    command = command.lower().strip()
    
    # `continue` returns execution of code back to start of loop
    if command == '':
        continue

    if command == 'n':
        try:
            vlad.location = vlad.location.n_to
        except:
            print("\n\nLet's not go there...")
        
    if command == 's':
        try:
            vlad.location = vlad.location.s_to
        except:
            print("\n\nLet's not go there...")
        
    if command == 'e':
        try:
            vlad.location = vlad.location.e_to
        except:
            print("\n\nLet's not go there...")

    if command == 'w':
        try:
            vlad.location = vlad.location.w_to
        except:
            print("\n\nLet's not go there...")

    if command == 'q':
        quit = True


