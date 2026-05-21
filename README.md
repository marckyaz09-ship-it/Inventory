import json
import os

INVENTORY_FILE = "inventory.json"


def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        return json.load(open(INVENTORY_FILE))
    else:
        return {}


def save_inventory(inventory):
    json.dump(inventory, open(INVENTORY_FILE, "w"), indent=4)


def add_item(inventory):
    item_name = input("Enter item name: ").lower()
    
    if item_name in inventory:
        print("Item already exists!")
        return
    
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[item_name] = {"quantity": quantity, "price": price}
        print("Item added successfully!")
    except ValueError:
        print("Invalid input – use numbers for quantity and price.")


def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty!")
        return
    
    print("\n--- CURRENT INVENTORY ---")
    for name, details in inventory.items():
        print(f"{name.title()} | Quantity: {details['quantity']} | Price: {details['price']}")


def update_item(inventory):
    item_name = input("Enter name of item to update: ").lower()
    
    if item_name not in inventory:
        print("Item not found!")
        return
    
    try:
        new_quantity = int(input("Enter new quantity: "))
        inventory[item_name]["quantity"] = new_quantity
        print("Quantity updated successfully!")
    except ValueError:
        print("Invalid input – use a number for quantity.")


def remove_item(inventory):
    item_name = input("Enter name of item to remove: ").lower()
    
    if item_name in inventory:
        del inventory[item_name]
        print("Item removed successfully!")
    else:
        print("Item not found!")


def main_menu():
    inventory = load_inventory()
    
    while True:
        print("\n==== INVENTORY MENU ====")
        print("1. Add New Item")
        print("2. View All Items")
        print("3. Update Item Quantity")
        print("4. Remove Item")
        print("5. Save and Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            remove_item(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Changes saved. Goodbye!")
            break
        else:
            print("Invalid choice – please enter a number between 1 and 5.")


main_menu()

