#Create a class called RetailItem that holds data about an Item in a retail store.
#The class should have the following attributes:
    #Description - description of the item (default "")
    #UnitsOnHand - the number of units in inventory (default 0)
    #Price - the item's retail price (default 0)
#Create a constructor that accepts the Description, UnitOnHand, and Price, then sets them to attributes in the RetailItem Class.
    #If one of the attributes is not present, then set the attribute to the default value.
#Create a method called InventoryValue, which returns the UnitsOnHand times Price.
#Read the 10.02 Inventory.txt file and creates three objects, one for each item.
#Display a report that displays the Description, Units On Hand, Price, and Inventory Value



class RetailItem ():
    def __init__(self, Description="", UnitsOnHand=0, Price=0):
        self.Description = Description
        self.UnitsOnHand = UnitsOnHand
        self.Price = Price

    def InventoryValue(self):
        return self.UnitsOnHand * self.Price

inventoryfile = open("10.02 Inventory.txt")
x = inventoryfile.readline()
y = x.split(",")
Item1 = RetailItem(y[0].strip(), int(y[1].strip()), float(y[2].strip()))
x = inventoryfile.readline()
y = x.split(",")

Item2 = RetailItem(y[0].strip(), int(y[1].strip()), float(y[2].strip()))
x = inventoryfile.readline()
y = x.split(",")

Item3 = RetailItem(y[0].strip(), int(y[1].strip()), float(y[2].strip()))
x = inventoryfile.readline()
y = x.split(",")

print("{:>20s}{:>20s}{:>20s}{:>20s}".format("Description", "Units on Hand", "Price", "Inventory Value"))
print("{:>20s}{:>20s}{:>20s}{:>20.2f}".format(Item1.Price))