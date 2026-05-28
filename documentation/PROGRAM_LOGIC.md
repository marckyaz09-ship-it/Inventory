# Inventory Management System - Program Logic Explanation

---

## Core Components

### 1. Data Storage

**File Format:** JSON (JavaScript Object Notation)  
**File Name:** `inventory.json`  
**Data Structure:** Dictionary of items with quantity and price

```json
{
    "laptop": {
        "quantity": 5,
        "price": 999.99
    },
    "mouse": {
        "quantity": 20,
        "price": 25.50
    }
}
```

**Advantages:**
- Human-readable format
- Easy to parse and manipulate
- Universal compatibility
- Native support in Python

---

### 2. File Operations

#### Load Inventory
- **Purpose:** Retrieve existing inventory data from file
- **Process:**
  1. Check if `inventory.json` file exists
  2. If exists, open and read the file
  3. Parse JSON content into Python dictionary
  4. Return dictionary to memory
  5. If file doesn't exist, return empty dictionary
  6. Handle errors gracefully (corrupted JSON, permission issues)

#### Save Inventory
- **Purpose:** Persist inventory changes to file
- **Process:**
  1. Convert inventory dictionary to JSON format
  2. Open file in write mode (creates if doesn't exist)
  3. Write formatted JSON with proper indentation
  4. Close file automatically (using `with` statement)
  5. Display success confirmation
  6. Handle IOError if write operation fails

**Best Practices:**
- Uses `with` statement for automatic file closing
- Prevents file corruption from improper closure
- Error handling prevents crashes on file system errors

---

### 3. User Input Validation

#### Item Name Validation
- **Normalization:** Convert to lowercase, remove whitespace
- **Rules:**
  - Cannot be empty
  - Must be unique (no duplicates)
  - Case-insensitive ("Laptop" = "laptop")

#### Numeric Input Validation
- **Quantity:** Must be integer, non-negative
- **Price:** Must be float/decimal, non-negative
- **Error Handling:** Try-catch blocks catch `ValueError` exceptions

#### Why This Matters
- Prevents invalid data entry
- Ensures data consistency
- Improves user experience with clear error messages

---

### 4. Core Functions Logic

#### ADD ITEM
1. Request item name from user
2. Normalize input (lowercase, trim)
3. Validate:
   - Name not empty
   - Name not already in inventory
4. Request quantity and price
5. Validate numeric inputs
6. Add to inventory dictionary
7. Save to file
8. Confirm success

**Example:**
```
User enters: "Laptop"
Stored as: "laptop" (normalized)
Data: {"laptop": {"quantity": 5, "price": 999.99}}
```

#### VIEW INVENTORY
1. Check if inventory is empty
2. Display header
3. For each item:
   - Calculate item total value (quantity × price)
   - Format and display as table row
   - Add to running total
4. Display separator line
5. Display total inventory value

**Formatting Example:**
```
--- CURRENT INVENTORY ---
Laptop               | Qty:     5 | Price: $  999.99 | Total: $ 4999.95
Mouse                | Qty:    20 | Price: $   25.50 | Total: $  510.00
----------------------------------------------------------------------
TOTAL INVENTORY VALUE                                  | Total: $ 5509.95
```
#### UPDATE ITEM
1. Request item name from user
2. Normalize input
3. Verify item exists in inventory
4. Request new quantity
5. Validate numeric input
6. Update quantity value
7. Save to file
8. Confirm success

#### REMOVE ITEM
1. Request item name from user
2. Normalize input
3. Check if item exists
4. Delete from dictionary
5. Save to file
6. Confirm success

#### SEARCH ITEM
1. Request search term from user
2. Validate input not empty
3. Create empty results dictionary
4. Loop through all items:
   - Check if search term is substring of item name
   - Add matching items to results
5. Display results with formatting
6. Handle case where no items match

**Example:**
```
Search term: "lap"
Matches: "laptop" (because "lap" is in "laptop")
```

---

### 5. Error Handling Strategy

#### Try-Except Blocks
- **Purpose:** Catch and handle runtime errors gracefully
- **Exceptions Caught:**
  - `ValueError`: Invalid numeric input
  - `JSONDecodeError`: Corrupted JSON file
  - `IOError`: File system issues

#### User-Friendly Messages
- Clear error descriptions
- Guidance on how to fix (e.g., "use numbers for quantity")
- Program continues running instead of crashing

---

### 6. Main Menu Loop

#### Purpose
- Continuously display menu until user exits
- Route user choice to appropriate function
- Maintain inventory state in memory

#### Flow
```
1. Load inventory from file
2. LOOP:
   - Display menu
   - Get user choice
   - Route to function based on choice
   - Function modifies inventory and saves
   - Return to menu
3. Exit loop on choice "6"
4. Program ends
```

---

## Data Flow Diagram

```
┌─────────────────────┐
│   inventory.json    │
│   (Persistent       │
│    Storage)         │
└──────────┬──────────┘
           │
      LOAD │ SAVE
           │
           ▼
┌─────────────────────┐
│   Inventory Dict    │
│   (In Memory)       │
└──────────┬──────────┘
           │
    ┌──────┴──────────────┬─────────┬───────┬──────┐
    │                     │         │       │      │
    ▼                     ▼         ▼       ▼      ▼
  ADD_ITEM         UPDATE_ITEM  REMOVE_ITEM VIEW  SEARCH
    │                     │         │       │      │
    └──────────┬──────────┴─────────┴───────┴──────┘
               │
               ▼
        SAVE to File
```

---

## Key Design Decisions

### 1. Auto-Save After Each Operation
- **Benefit:** Prevents data loss from crashes
- **Trade-off:** Slightly slower operations (file I/O)

### 2. Lowercase Item Names
- **Benefit:** Prevents duplicate items with different cases
- **Trade-off:** Display uses `.title()` for proper capitalization

### 3. JSON for Storage
- **Benefit:** Human-readable, easy to debug, portable
- **Alternative:** SQLite (overkill for small project)

### 4. In-Memory Dictionary
- **Benefit:** Fast operations during session
- **Trade-off:** Changes lost if not saved before exit

---

## Testing Considerations

### Unit Test Examples

**Test 1: Add Valid Item**
```
Input: name="laptop", quantity=5, price=999.99
Expected: Item added to inventory, file saved
Actual: ✓ Passed
```

**Test 2: Add Duplicate Item**
```
Input: name="laptop" (already exists)
Expected: Error message, item not added
Actual: ✓ Passed
```

**Test 3: Invalid Quantity**
```
Input: quantity="abc"
Expected: ValueError caught, error message displayed
Actual: ✓ Passed
```

**Test 4: Negative Price**
```
Input: price=-10
Expected: Validation error, item not added
Actual: ✓ Passed
```

---
