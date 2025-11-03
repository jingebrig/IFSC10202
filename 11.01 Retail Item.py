#Create a Class called RetailItem that holds data about an Item in a retail store.
#The RetailItem class should have the following attributes:
    #Description - Description of the item (default "")
    #UnitsOnHand - the number of units in inventory (default 0)
    #Price - the item's retail price (default 0)
#Create a constructor for the RetialItem class that accepts the Description, UnitOnHand, and Price, then sets them 
#to attributes in the RetailItem Class. If one of the it ems is not present, then set the attribute to the default value.
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

class RetailItem ():
    def __init__(self, description="", unitsonhand="", price="",):
        self.FirstName = description
        self.LastName = unitsonhand
        self.TNumber = price