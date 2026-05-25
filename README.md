# Inventory Management System

## Project Information

**Course:** BS Information Technology 1C  
**Project Type:** Group Project  
**Language:** Python 3  
**Status:** ✅ Functional and Complete

---

## 👥 Group Members

- *[Marcky Cielo A.Cañete]*
- *[Justin Sam G. Cantiga]*
- *[Member 3 Name]*
- *[Additional Members]*

---

## Project Description

The **Inventory Management System** a command-line application designed to help users efficiently manage their inventory of items. The system allows users to add, view, update, search, and remove items in the storage in JSON format.

---

## Features

### 1. Add New Item
- Input item name, quantity, and price
- Automatic validation of inputs
- Prevents duplicate item entries
- Case-insensitive duplicate checking

### 2. View All Items
- Display all items in organized table format
- Shows quantity and price for each item
- Calculates individual item totals (quantity × price)
- Displays total inventory value
- Formatted output with alignment

### 3. Update Item Quantity
- Search for item by name
- Update quantity with validation
- Prevents negative quantities
- Automatic data continuation

### 4. Remove Item
- Delete items from inventory
- Confirmation that item was removed
- Immediate data continuation

### 5. Search Item
- Find items by partial name match
- Case-insensitive search
- Displays all matching results
- Shows detailed information for each match

### 6. Data Persistence
- Automatic saving after each operation
- JSON file storage for easy access
- Error recovery for corrupted files
- Automatic file creation on first run

---

## Technologies & Libraries Used

### Core Language
- **Python 3.x** - Programming language

### Libraries
- **json** - JSON file serialization and deserialization
- **os** - Operating system interface (file existence checking)

### Storage
- **JSON (inventory.json)** - Human-readable data storage format

---

### Main Menu

When you run the program, you'll see:

```
==== INVENTORY MENU ====
1. Add New Item
2. View All Items
3. Update Item Quantity
4. Remove Item
5. Search Item
6. Save and Exit

Choose an option (1-6):
```


#### Add a New Item

```
Choose an option (1-6): 1
Enter item name: Laptop
Enter quantity: 5
Enter price: 999.99
Item added successfully!
Inventory saved successfully!
```

#### View All Items

```
Choose an option (1-6): 2

--- CURRENT INVENTORY ---
Laptop               | Qty:     5 | Price: $  999.99 | Total: $ 4999.95
Mouse                | Qty:    20 | Price: $   25.50 | Total: $  510.00
----------------------------------------------------------------------
TOTAL INVENTORY VALUE                                  | Total: $ 5509.95
```

#### Update Item Quantity

```
Choose an option (1-6): 3
Enter name of item to update: Laptop
Enter new quantity: 3
Quantity updated successfully!
Inventory saved successfully!
```

#### Search Item

```
Choose an option (1-6): 5
Enter item name to search: lap

--- SEARCH RESULTS FOR 'lap' ---
Laptop | Qty: 3 | Price: $999.99 | Total: $2999.97
```

#### Remove Item

```
Choose an option (1-6): 4
Enter name of item to remove: Mouse
Item removed successfully!
Inventory saved successfully!
```

#### Exit

```
Choose an option (1-6): 6
Inventory saved successfully!
Changes saved. Goodbye!
```

---

## Data Storage Format

### File Location

```
Inventory/
├── source/
│   ├── inventory.py
│   └── inventory.json  ← Created on first run
└── ...
```

### JSON Structure

```json
{
    "laptop": {
        "quantity": 5,
        "price": 999.99
    },
    "mouse": {
        "quantity": 20,
        "price": 25.50
    },
    "keyboard": {
        "quantity": 15,
        "price": 79.99
    }
}
```

---

## Error Handling

### Validation Errors

```
❌ Item name cannot be empty!
❌ Item already exists!
❌ Quantity and price must be non-negative!
❌ Invalid input – use numbers for quantity and price.
```

### File System Errors

```
❌ Error loading inventory: [details]
❌ Error saving inventory: [details]
```

### Not Found Errors

```
❌ Item not found!
❌ No items found matching '[search_term]'
```

---

## Screenshots

See the `/images` folder for:
- Program startup screenshot
- Main menu interface
- Sample inventory view
- Add item process
- Search functionality
- Program output examples

---

## Documentation

For detailed documentation, see:

- **Pseudocode:** `/documentation/PSEUDOCODE.md`
  - Complete algorithm pseudocode for all functions
  - Data structure specifications
  
- **Flowchart:** `/documentation/FLOWCHART.md`
  - Visual flowchart of program flow
  - Decision trees for each menu option
  - Error handling flows

- **Program Logic:** `/documentation/PROGRAM_LOGIC.md`
  - Detailed explanation of each function
  - Design decisions and rationale
  - Data flow diagrams
  - Testing considerations

---

## Code Structure

### Functions Overview

| Function | Purpose | Input | Output |
|----------|---------|-------|--------|
| `load_inventory()` | Load data from JSON file | None | Dictionary |
| `save_inventory()` | Save data to JSON file | Dictionary | None |
| `add_item()` | Add new item to inventory | User input | Success/Error message |
| `view_inventory()` | Display all items | Dictionary | Formatted table |
| `update_item()` | Modify item quantity | User input | Success/Error message |
| `remove_item()` | Delete item | User input | Success/Error message |
| `search_item()` | Find items by name | User input | Matching items |
| `main_menu()` | Main program loop | None | Program control |

### Code Quality Features

✅ **Proper File Handling** - Uses `with` statements for automatic resource cleanup  
✅ **Input Validation** - Comprehensive validation of all user inputs  
✅ **Error Handling** - Try-except blocks for graceful error management  
✅ **Documentation** - Docstrings for all functions  
✅ **Clean Code** - Readable variable names and proper spacing  
✅ **DRY Principle** - No code duplication  

---

## Known Issues

None currently. The program is still being tested.

---

## Future Enhancements

- [ ] Graphical User Interface (GUI) with Tkinter
- [ ] SQLite database instead of JSON for scalability
- [ ] Price update functionality
- [ ] Stock alert system (low inventory warnings)
- [ ] Inventory reports (CSV/PDF export)
- [ ] Undo/Redo functionality
- [ ] Multi-user support with authentication
- [ ] Backup and restore features
- [ ] Barcode scanning integration
- [ ] Statistical analysis and trends


---

## Support & Contact

For questions or issues regarding this project:
1. Check the `/documentation` folder for detailed guides
2. Review the code comments in `inventory.py`
3. Test with the examples provided in this README

---

## Learning Outcomes

This project teaches:

1. **File I/O Operations**
   - Reading and writing files
   - JSON format handling
   - Error recovery

2. **Data Structures**
   - Dictionary usage
   - Nested data structures
   - Data organization

3. **Input Validation**
   - User input checking
   - Type conversion
   - Error prevention

4. **Error Handling**
   - Try-except blocks
   - Custom error messages
   - Graceful degradation

5. **Program Design**
   - Modular function design
   - Menu-driven interfaces
   - Program flow control

6. **Best Practices**
   - Code organization
   - Documentation
   - Testing methodology

---

## Checklist for Submission

- [x] Source code in `/source` folder
- [x] Pseudocode in `/documentation`
- [x] Flowchart in `/documentation`
- [x] Program logic documentation
- [x] Screenshot examples in `/images` folder
- [x] Comprehensive README.md
- [x] Code is functional and tested
- [x] Repository is public
- [x] All files properly organized
- [x] Commit history shows group contributions

---

**Project Version:** 1.0  
**Last Updated:** 2026-05-24  
**Repository:** https://github.com/marckyaz09-ship-it/Inventory
