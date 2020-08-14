# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def showItems(self):
        if len(self.items) == 0:
            return f"Ehh...Theres no items here"
        else:
            return [item.__str__() for item in self.items]
                

    def __str__(self):
        return f"You just entered the {self.name} and it's {self.description}"
