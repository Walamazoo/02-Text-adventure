#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = "haunted.json"


# Load the contents of the files into the game and items dictionaries
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        return game
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)


def render(game,current):
    c = game[current]
    print("\nThis is the " + c["name"])
    print(c["desc"])

    if current != "END" and current != "DEAD":
        print("\nAvaliable exits: ")
        for e in c["exits"]:
            print(e["exit"].lower())
    

def get_input():
    response = input("Where will you go? ")
    response = response.upper().strip()
    return response

def update(game,current,response):
    c = game[current]
    for e in c["exits"]:
        if response == e["exit"]:
            return e["target"]

    else:
        print("That won't work. Try something else.")

    return current

# The main function for the game
def main():
    current = 'FOYER'  # The starting location
    end_game = ['END']  # Any of the end-game locations
    dead_end = ['DEAD']

    game = load_files()

    while True:
        render(game,current)

        if current in end_game:
            print("You win!")
            break

        if current in dead_end:
            print("You died!")
            break

        response = get_input()

        if response == "QUIT" or response == "Q":
            break 

        current = update(game,current,response)

    print("Thanks for playing!")

# run the main function
if __name__ == '__main__':
	main()