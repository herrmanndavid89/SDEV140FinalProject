# Step 1: Create the inventory dictionary
inventory = {}
from breezypythongui import EasyFrame

class videoGame():
    def __init__(self, title, quantity):
        self.title = title
        self.quantity = quantity

    def __str__(self):
        return f"{self.title}: {self.quantity}"

class VideoGameStore(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Video Game Store Inventory", width=300, height=200)

        # Create the inventory dictionary
        self.inventory = {}

        # Create the input fields and buttons
        self.lblTitle = self.addLabel(text="Title:", row=0, column=0)
        self.txtTitle = self.addTextField(text="", row=0, column=1, columnspan=2)

        self.lblQuantity = self.addLabel(text="Quantity:", row=1, column=0)
        self.txtQuantity = self.addIntegerField(value=1, row=1, column=1, columnspan=2)

        self.btnAdd = self.addButton(text="Add Game", row=2, column=0, command=self.addGame)
        self.btnDisplay = self.addButton(text="Display Inventory", row=2, column=1, command=self.displayInventory)
        self.btnRemove = self.addButton(text="Remove Game", row=2, column=2, command=self.removeGame)

    def addGame(self):
        # Get the input values
        title = self.txtTitle.getText()
        quantity = self.txtQuantity.getNumber()
        if title == "" or quantity < 0:
            self.messageBox(title="Error", message="Please enter a valid title or quantity greater than 0.")
            return
        else:
            if title in self.inventory:
                self.inventory[title].quantity += quantity
                self.messageBox(title="Game Added", message=f"{quantity} {title} added to inventory.")
                self.txtTitle.setText("")
                return
            else:
                # Create a new videoGame object
                newGame = videoGame(title, quantity)

                # Add the game to the inventory
                self.inventory[title] = newGame
                self.messageBox(title="Game Added", message=f"{title} added to inventory.")

                # Clear the input fields
                self.txtTitle.setText("")
                self.txtQuantity.setNumber(1)

    def removeGame(self):
        # Get the input values
        title = self.txtTitle.getText()
        num = self.txtQuantity.getNumber()
        if title == "" or num < 0:
            self.messageBox(title="Error", message="Please enter a title and quantity.")
            return
        else:
            if title in self.inventory:
                if self.inventory[title].quantity > num:
                    self.inventory[title].quantity -= num
                    self.messageBox(title="Game Removed", message=f"{num} {title} removed from inventory.")
                elif self.inventory[title].quantity == num:
                    del self.inventory[title]
                    self.messageBox(title="Game Removed", message=f"{title} removed from inventory.")
                else:
                    self.messageBox(title="Error", message="Not enough games in inventory.")
                self.txtTitle.setText("")
            else:
                self.messageBox(title="Error", message="Game not found in inventory.")

    def displayInventory(self):
        # Create the inventory string
        inventory_str = "Current inventory:\n"
        if(len(self.inventory) == 0):
            inventory_str += "No games in inventory."
        else:
            for game in self.inventory.values():
                inventory_str += f"{game}\n"
        # Display the inventory
        self.messageBox(title="Inventory", message=inventory_str)

app = VideoGameStore()
app.mainloop()