# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom, inventory=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = inventory

    def move(self, direction):
        if hasattr(self.currentRoom, f"{direction}"):
            self.currentRoom = getattr(self.currentRoom, f'{direction}')
        else:
            print("\n\nYou cannot walk that way.\n\n")

    def grab(self, item):
        if item in self.currentRoom.items:
            self.currentRoom.items.remove(item)
            self.inventory.append(item)
            print(f"\n 🎒 {item.name} added to your inventory!")
        else:
            print(" 👀 Ahh, you can't pick that up")

    def drop(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.currentRoom.items.append(item)
            return f"\n 🎒 {item} was removed"
        else:
            return " 👀 Ahh, you can't drop that"
    
    def showInventory(self):
        if not self.inventory:
            return "Empty"
        else:
           return [f"{item.name}" for item in self.inventory]

    def __str__(self):
        f"Ayy, {self.name} you're in {self.currentRoom} with {self.inventory}"
