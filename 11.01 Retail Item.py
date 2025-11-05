#Create a Class called RetailItem that holds data about an Item in a retail store.
#The RetailItem class should have the following attributes:
    #Description - Description of the item (default "")
    #UnitsOnHand - the number of units in inventory (default 0)
    #Price - the item's retail price (default 0)
#Create a constructor for the RetialItem class that accepts the Description, UnitOnHand, and Price, then sets them 
#to attributes in the RetailItem Class. If one of the items is not present, then set the attribute to the default value.
#Create a method called InventoryValue, which returns the UnitsOnHand times Price.
#Read 11.01 Inventory.txt and create a list of inventory items
#Print the list of inventory items with the initial inventory value using the RetailItem attributes
#Read 11.01 InventoryUpdate.txt, search for the item to update, and update the price
#Print the list of inventory items with the updated inventory value
#Create thr following functions in your main program:
    #print_inventory - which has the list at the argument. Prints the list with headings
    #find_inventory - which has the list and the name of the inventory item as the argument. This function searches the list and 
#looks for a match between the inventory item and the description. The function returns the index of the item. 
#If the item is not found a -1 is returned. See the find_ball function in 11.01 - Creating a List of Objects Using Instantiation

# RetailItem class definition
class RetailItem:
    def __init__(self, description="", units_on_hand=0, price=0):
        #"""Constructor that sets description, units on hand, and price."""
        self.description = description
        self.units_on_hand = units_on_hand
        self.price = price

    def inventory_value(self):
        #"""Return total inventory value."""
        return self.units_on_hand * self.price


# Function to print the inventory
def print_inventory(inventory_list):
    print(f"{'Description':<15} {'Units On Hand':>15} {'Price':>15} {'Inventory Value':>18}")
    index = 0
    while index < len(inventory_list):
        item = inventory_list[index]
        print(f"{item.description:<15}{item.units_on_hand:>15} {item.price:>15.2f} {item.inventory_value():>18.2f}")
        index += 1
    print()


# Function to find an inventory item by description
def find_inventory(inventory_list, name):
    index = 0
    while index < len(inventory_list):
        if inventory_list[index].description.lower() == name.lower():
            return index
        index += 1
    return -1


# ----------------------
# Read initial inventory
# ----------------------
file = open("11.01 Inventory.txt", "r")
inventory_list = []

line = file.readline()
while line != "":
    parts = line.strip().split(',')
    if len(parts) == 3:
        desc = parts[0].strip()
        units = int(parts[1].strip())
        price = float(parts[2].strip())
        item = RetailItem(desc, units, price)
        inventory_list.append(item)
    line = file.readline()
file.close()

# Print initial inventory
print_inventory(inventory_list)


# ----------------------
# Update inventory prices
# ----------------------
file = open("11.01 InventoryUpdate.txt", "r")

line = file.readline()
while line != "":
    parts = line.strip().split(',')
    if len(parts) == 2:
        desc = parts[0].strip()
        new_price = float(parts[1].strip())
        index = find_inventory(inventory_list, desc)
        if index != -1:
            inventory_list[index].price = new_price
    line = file.readline()
file.close()

# Print updated inventory
print_inventory(inventory_list)