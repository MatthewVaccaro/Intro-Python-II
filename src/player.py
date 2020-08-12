# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def move(self, direction):
        if hasattr(self.currentRoom, f"{direction}"):
            self.currentRoom = getattr(self.currentRoom, f'{direction}')
        else:
            print("\n\nYou cannot walk that way.\n\n")

    def __str__(self):
        f"Ayy, {self.name} you're in {self.currentRoom}"

