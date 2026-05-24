# Inventory Management System - Pseudocode

## Program Flow Overview

```
START PROGRAM
    Initialize empty inventory
    Load existing inventory from file (if exists)
    
    DO WHILE user hasn't exited:
        Display main menu
        Get user choice
        
        IF choice == 1 THEN
            CALL add_item()
        ELSE IF choice == 2 THEN
            CALL view_inventory()
        ELSE IF choice == 3 THEN
            CALL update_item()
        ELSE IF choice == 4 THEN
            CALL remove_item()
        ELSE IF choice == 5 THEN
            CALL search_item()
        ELSE IF choice == 6 THEN
            CALL save_inventory()
            Display "Goodbye" message
            EXIT loop
        ELSE
            Display "Invalid choice" error
        END IF
    END DO
END PROGRAM
```

---

## Function: load_inventory()

```
FUNCTION load_inventory():
    IF inventory file exists THEN
        TRY
            Open file in read mode
            Parse JSON content
            Return parsed inventory dictionary
        CATCH JSONDecodeError OR IOError
            Display error message
            Return empty dictionary
        END TRY
    ELSE
        Return empty dictionary
    END IF
END FUNCTION
```

---

## Function: save_inventory(inventory)

```
FUNCTION save_inventory(inventory):
    TRY
        Open file in write mode
        Convert inventory dictionary to JSON format
        Write JSON to file with 4-space indentation
        Display success message
    CATCH IOError
        Display error message
    END TRY
END FUNCTION
```

---

## Function: add_item(inventory)

```
FUNCTION add_item(inventory):
    Get item_name from user input
    Convert to lowercase and remove whitespace
    
    IF item_name is empty THEN
        Display "Item name cannot be empty" error
        RETURN
    END IF
    
    IF item_name exists in inventory THEN
        Display "Item already exists" error
        RETURN
    END IF
    
    TRY
        Get quantity from user (convert to integer)
        Get price from user (convert to float)
        
        IF quantity < 0 OR price < 0 THEN
            Display "Values must be non-negative" error
            RETURN
        END IF
        
        Add new entry to inventory:
            inventory[item_name] = {quantity: quantity, price: price}
        
        CALL save_inventory(inventory)
        Display "Item added successfully" message
    CATCH ValueError
        Display "Invalid input" error
    END TRY
END FUNCTION
```

---

## Function: view_inventory(inventory)

```
FUNCTION view_inventory(inventory):
    IF inventory is empty THEN
        Display "Inventory is empty" message
        RETURN
    END IF
    
    Display header: "--- CURRENT INVENTORY ---"
    Set total_value = 0
    
    FOR EACH item in inventory:
        Get item name and details (quantity, price)
        Calculate item_value = quantity × price
        Add item_value to total_value
        
        Display formatted row:
            [Item Name] | Qty: [quantity] | Price: $[price] | Total: $[item_value]
    END FOR
    
    Display separator line
    Display total inventory value
    Display blank line
END FUNCTION
```

---

## Function: update_item(inventory)

```
FUNCTION update_item(inventory):
    Get item_name from user input
    Convert to lowercase and remove whitespace
    
    IF item_name NOT in inventory THEN
        Display "Item not found" error
        RETURN
    END IF
    
    TRY
        Get new_quantity from user (convert to integer)
        
        IF new_quantity < 0 THEN
            Display "Quantity must be non-negative" error
            RETURN
        END IF
        
        Update inventory[item_name]["quantity"] = new_quantity
        CALL save_inventory(inventory)
        Display "Quantity updated successfully" message
    CATCH ValueError
        Display "Invalid input" error
    END TRY
END FUNCTION
```

---

## Function: remove_item(inventory)

```
FUNCTION remove_item(inventory):
    Get item_name from user input
    Convert to lowercase and remove whitespace
    
    IF item_name EXISTS in inventory THEN
        Delete inventory[item_name]
        CALL save_inventory(inventory)
        Display "Item removed successfully" message
    ELSE
        Display "Item not found" error
    END IF
END FUNCTION
```

---

## Function: search_item(inventory)

```
FUNCTION search_item(inventory):
    Get search_term from user input
    Convert to lowercase and remove whitespace
    
    IF search_term is empty THEN
        Display "Search term cannot be empty" error
        RETURN
    END IF
    
    Create results dictionary = {}
    
    FOR EACH item in inventory:
        IF search_term is contained in item name THEN
            Add item to results dictionary
        END IF
    END FOR
    
    IF results is NOT empty THEN
        Display header: "--- SEARCH RESULTS FOR '[search_term]' ---"
        
        FOR EACH result in results:
            Get item details (quantity, price)
            Calculate item_value = quantity × price
            Display formatted row:
                [Item Name] | Qty: [quantity] | Price: $[price] | Total: $[item_value]
        END FOR
    ELSE
        Display "No items found matching '[search_term]'" message
    END IF
END FUNCTION
```

---

## Data Structure

### Inventory Dictionary
```
inventory = {
    "item_name": {
        "quantity": integer_value,
        "price": float_value
    },
    "item_name2": {
        "quantity": integer_value,
        "price": float_value
    }
}
```

### JSON File Format (inventory.json)
```json
{
    "item_name": {
        "quantity": 10,
        "price": 25.99
    },
    "item_name2": {
        "quantity": 5,
        "price": 15.50
    }
}
```
