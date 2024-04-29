"""
Simple console program to demonstrate
inventory management system
"""

filename = 'items.txt'

def print_spaces():
    spaces = "=" * 25
    print(f"\t{spaces}")
    
def menu():
    """Displays the options"""
    
    print("\n\tInventory Management Menu ")
    print_spaces()
    
    print("""
        A: Add New Item to Inventory
        L: List all the items
        R: Remove Item from Inventory
        S: Search Item in Inventory
        Q: Quit
        """)

def add_item():
    """Add an item to the inventory"""

    print("\n\tAdding an item")
    print_spaces()
    
    name = input("\tEnter a item name: ")
    qty = input("\tEnter the item quantity: ")
  
    f = open(filename, 'a')
    f.write(f"\n{name}")
    f.write(f"\n{qty}")
    f.close()

    print(f"\n\tSuccessfully added {name} to the inventory")
 
def list_item():
    """Displays all the items in the inventory"""

    print("\tItems\tQuantity")
    print_spaces()
    f = open(filename, 'r')

    while True:
        name = f.readline().rstrip()
        quantity = f.readline().rstrip()
        if not quantity:
            break

        print(f"\t{name}\t{quantity}")       

    
    f.close()

def search_item(name):
    """Searches the items in the inventory"""

    print("\n\tSearching..")
    print_spaces()

    f = open(filename, 'r')
    
    for item in f:
        if name == item.strip():
            print("\tItem: ", name)
            print("\tQty: ", next(f))
            f.close()
            return
    
    f.close()            
    print(f"\tSorry {name} is not in the inventory")
    

def remove_item():
    """Removes an item from the inventory"""

    print("\n\tRemoving..")
    print_spaces()
    
    item = input("\tEnter the item name to remove from inventory: ")

    data = []
    item_found = False
    
    with open(filename, 'r') as f:
        for line in f:
            if line.rstrip() != item:
                data.append(line)
            else:
                print(f"\tRemoved {item} from inventory")
                item_found = True
                next(f, None) # Ignore another line too
                continue 
    
    with open(filename, 'w') as f:
        for line in data:
           f.write(line)
                               
    if not item_found:
        print(f"\n\tSorry {item} is not in the inventory")

    

def look_more():
    choice = input("\n\tDo you like to continue: yes/no ")
    return choice.startswith('y')

def main():
    while True:
        menu()
        choice = input("\n\tEnter your choice: ").lower()
        print()
    
        
        if choice == 'a':
            add_item()
        elif choice == 'l':
            list_item()
        elif choice == 's':
            name = input("What do you want to search? ")
            search_item(name)
        elif choice == 'r':
            remove_item()
        elif choice == 'q':
            print("\tExiting..")
            break
        else:
            print("\n\tPlease enter an appropriate choice")
            continue

        if not look_more():
            break

        
if __name__ == '__main__':
    main()



