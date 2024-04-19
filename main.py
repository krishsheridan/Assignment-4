import json
import os

# Function to load game names from a JSON file
def loadgamenames(filename):
    # Check if the file exists
    if os.path.exists(filename):
        # If the file exists, load game names from it
        with open(filename, 'r') as file:
            try:
                game_names = json.load(file)
            except json.JSONDecodeError:
                # If there's a decoding error, set game_names to an empty list
                game_names = []
    else:
        # If the file doesn't exist, set game_names to an empty list
        game_names = []
    return game_names

# Function to save game names to a JSON file
def savegamenames(game_names, filename):
    # Save game names to the specified file
    with open(filename, 'w') as file:
        json.dump(game_names, file, indent=4)

# Function to add a game to the list of game names
def addgame(game_names, game):
    if game not in game_names:
        # If the game is not already in the list, add it
        game_names.append(game)
        return True
    else:
        # If the game is already in the list, inform the user
        print("Game already exists")
        return False

# Function to remove a game from the list of game names
def removegame(game_names, game):
    if game in game_names:
        # If the game is in the list, remove it
        game_names.remove(game)
        return True
    else:
        # If the game is not in the list, inform the user
        print("Game not found")
        return False

# Function to list all game names
def listgamenames(game_names):
    if game_names:
        # If there are game names in the list, print them
        print("List of Game Names:")
        for idx, game in enumerate(game_names, start=1):
            print(f"{idx}. {game}")
    else:
        # If there are no game names in the list, inform the user
        print("No games found")

# Main function
def main():
    filename = "game_names.json"
    # Load game names from the JSON file
    game_names = loadgamenames(filename)

    while True:
        print("\nOptions:")
        print("1. Add a game")
        print("2. Remove a game")
        print("3. List all game names")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt user to enter the name of the game to add
            game = input("Enter the name of the game to add: ")
            # If the game is successfully added, save the updated list to the file
            if addgame(game_names, game):
                savegamenames(game_names, filename)
        elif choice == '2':
            # Prompt user to enter the name of the game to remove
            game = input("Enter the name of the game to remove: ")
            # If the game is successfully removed, save the updated list to the file
            if removegame(game_names, game):
                savegamenames(game_names, filename)
        elif choice == '3':
            # List all game names
            listgamenames(game_names)
        elif choice == '4':
            # Exit the program
            print("Exiting program")
            break
        else:
            # Inform the user of an invalid choice
            print("Invalid choice. Please enter a number from 1 to 4")

if __name__ == "__main__":
    main()
