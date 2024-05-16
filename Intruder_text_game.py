rooms = {
    'Start Room': {
        'exits': {'east': 'Living Room'}
    },
    'Living Room': {
        'exits': {'south': 'Office', 'north': 'Meditation Room', 'east': 'Storage Room'}
    },
    'Meditation Room': {
        'exits': {'east': 'Guest Room', 'south': 'Living Room'}
    },
    'Office': {
        'exits': {'north': 'Living Room', 'east': 'Basement'}
    },
    'Guest Room': {
        'exits': {'west': 'Meditation Room', 'south': 'Kitchen'}
    },
    'Kitchen': {
        'exits': {'north': 'Guest Room', 'south': 'Storage Room'}
    },
    'Storage Room': {
        'exits': {'north': 'Kitchen', 'west': 'Living Room', 'south': 'Basement'}
    },
    'Basement': {
        'intruder': True
    }
}


def move_between_rooms(current_room, player_input, rooms):
    if player_input == 'exit':
        return 'exit'

    direction = player_input.split()[1].lower()
    if direction in rooms[current_room].get('exits', {}):
        next_room = rooms[current_room]['exits'][direction]
        return next_room
    elif 'intruder' in rooms[current_room] and rooms[current_room]['intruder']:
        print("Intruder is present! You must have at least 5 items to defeat them.")
        return current_room
    else:
        print('Invalid direction or no exit in this direction. Enter a valid direction or type "exit" to quit.')
        return current_room

def game_loop(starting_room, rooms):

    current_room = starting_room
    while current_room != 'Basement':  # Check if player is not in the "exit" room
        print(f'You are in the {current_room}.')
        exits = rooms[current_room].get('exits')
        if exits:
            available_directions = list(exits.keys())
            print(f"Available directions: {'/'.join(available_directions)}")
        else:
            print("There are no available exits from this room.")
        player_input = input("Enter a command ('go <direction>' or 'exit'): ").lower()
        if player_input.startswith('go '):
            current_room = move_between_rooms(current_room, player_input, rooms)
            if current_room == 'exit':
                print('Exiting Game')
                break
        elif player_input == 'exit':
            print('Exiting Game')
            break
        else:
            print("Invalid command: Please enter: 'go <direction>' to move between rooms or 'exit' to quit game.")

    if current_room == 'Basement':  # Check if player is in the "exit" room
        print("You have reached the 'exit' room. Exiting game.")

# Introduction message
print("Welcome to Midnight Guardian: The Intruder.")
print("It's 4 am and you've been awakened by strange noises in your home. An intruder has broken in, and you must confront them to stop them from causing harm.")
print("Navigate through your home, gather items, and outsmart the intruder before it's too late.\n")

# Start the game loop
game_loop('Start Room', rooms)
