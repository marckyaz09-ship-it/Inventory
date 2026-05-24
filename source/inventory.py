import json
import os

INVENTORY_FILE = "inventory.json"


def load_inventory():
    """Load inventory from JSON file with proper error handling."""
    if os.path.exists(INVENTORY_FILE):
        try:
            with open(INVENTORY_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading inventory: {e}. Starting with empty inventory.")
            return {}
    return {}


def save_inventory(inventory):
    """Save inventory to JSON file with proper error handling."""
    try:
        with open(INVENTORY_FILE, "w") as f:
            json.dump(inventory, f, indent=4)
        print("Inventory saved successfully!")
    except IOError as e:
        print(f"Error saving inventory: {e}")


def add_item(inventory):
    """Add a new item to inventory with validation."""
    item_name = input("Enter item name: ").lower().strip()
    
    if not item_name:
        print("Item name cannot be empty!")
        return
    
    if item_name in inventory:
        print("Item already exists!")
        return
    
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        
        if quantity < 0 or price < 0:
            print("Quantity and price must be non-negative!")
            return
        
        inventory[item_name] = {"quantity": quantity, "price": price}
        save_inventory(inventory)
        print("Item added successfully!")
    except ValueError:
        print("Invalid input – use numbers for quantity and price.")


def view_inventory(inventory):
    """Display all items in inventory with totals."""
    if not inventory:
        print("Inventory is empty!")
        return
    
    print("\n--- CURRENT INVENTORY ---")
    total_value = 0
    for name, details in inventory.items():
        item_value = details['quantity'] * details['price']
        total_value += item_value
        print(f"{name.title():20} | Qty: {details['quantity']:5} | Price: ${details['price']:8.2f} | Total: ${item_value:8.2f}")
    
    print("-" * 70)
    print(f"{'TOTAL INVENTORY VALUE':20} | {'':<5} | {'':<8} | {'':<8} | Total: ${total_value:8.2f}\n")


def update_item(inventory):
    """Update item quantity with validation."""
    item_name = input("Enter name of item to update: ").lower().strip()
    
    if item_name not in inventory:
        print("Item not found!")
        return
    
    try:
        new_quantity = int(input("Enter new quantity: "))
        if new_quantity < 0:
            print("Quantity must be non-negative!")
            return
        inventory[item_name]["quantity"] = new_quantity
        save_inventory(inventory)
        print("Quantity updated successfully!")
    except ValueError:
        print("Invalid input – use a number for quantity.")


def remove_item(inventory):
    """Remove an item from inventory."""
    item_name = input("Enter name of item to remove: ").lower().strip()
    
    if item_name in inventory:
        del inventory[item_name]
        save_inventory(inventory)
        print("Item removed successfully!")
    else:
        print("Item not found!")


def search_item(inventory):
    """Search for items by name."""
    search_term = input("Enter item name to search: ").lower().strip()
    
    if not search_term:
        print("Search term cannot be empty!")
        return
    
    results = {name: details for name, details in inventory.items() if search_term in name}
    
    if results:
        print(f"\n--- SEARCH RESULTS FOR '{search_term}' ---")
        for name, details in results.items():
            item_value = details['quantity'] * details['price']
            print(f"{name.title()} | Qty: {details['quantity']} | Price: ${details['price']:.2f} | Total: ${item_value:.2f}")
    else:
        print(f"No items found matching '{search_term}'")


def main_menu():
    """Main menu loop."""
    inventory = load_inventory()
    
    while True:
        print("\n==== INVENTORY MENU ====")
        print("1. Add New Item")
        print("2. View All Items")
        print("3. Update Item Quantity")
        print("4. Remove Item")
        print("5. Search Item")
        print("6. Save and Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            view_inventory(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            remove_item(inventory)
        elif choice == "5":
            search_item(inventory)
        elif choice == "6":
            save_inventory(inventory)
            print("Changes saved. Goodbye!")
            break
        else:
            print("Invalid choice – please enter a number between 1 and 6.")


if __name__ == "__main__":
    main_menu()
