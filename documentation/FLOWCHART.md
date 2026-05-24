# Inventory Management System - Flowchart

## Main Program Flow

```
┌─────────────────────────┐
│   START PROGRAM         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Load Inventory from    │
│  inventory.json file    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Display Main Menu      │
│  1. Add Item            │
│  2. View Inventory      │
│  3. Update Item         │
│  4. Remove Item         │
│  5. Search Item         │
│  6. Save & Exit         │
└────────────┬────────────┘
             │
             ▼
        ┌────────────┐
        │ Get Choice │
        └─────┬──────┘
              │
      ┌───────┼───────┐
      │       │       │
      ▼       ▼       ▼
    Choice = 1, 2, 3, 4, 5, or 6?
      │       │       │
      ├───────┼───────┼───────┬───────┬─────┐
      │       │       │       │       │     │
      ▼       ▼       ▼       ▼       ▼     ▼
     [1]    [2]    [3]    [4]    [5]   [6]
```

---

## Choice 1: Add Item

```
┌─────────────────────────┐
│  ADD ITEM FUNCTION      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Input: Item Name        │
└────────────┬────────────┘
             │
             ▼
       ┌─────────────┐
       │Name Empty?  │
       └─────┬───────┘
         YES │ NO
            │  │
            ▼  ▼
          [X] Input: Quantity & Price
              │
              ▼
          ┌────────────────┐
          │Valid Numbers?  │
          └────┬───────┬───┘
          NO  │  YES   │
             │        │
             ▼        ▼
           [X]    Item Name Exists?
                  │        │
                YES│       NO
                  │        │
                  ▼        ▼
                [X]    Add to Dictionary
                       │
                       ▼
                  Save to File
                       │
                       ▼
                 Success Message
                       │
                       ▼
               Return to Menu Loop
```

---

## Choice 2: View Inventory

```
┌──────────────────────────┐
│  VIEW INVENTORY FUNCTION │
└────────────┬─────────────┘
             │
             ▼
        ┌─────────────┐
        │Empty Check? │
        └────┬────┬───┘
         YES │    NO
            │    │
            ▼    ▼
          [X]  Display Header
               │
               ▼
           For each item:
               │
               ▼
          Calculate total value
          (quantity × price)
               │
               ▼
          Display formatted row
               │
               ▼
          Display total sum
               │
               ▼
        Return to Menu Loop
```

---

## Choice 3: Update Item

```
┌──────────────────────────┐
│  UPDATE ITEM FUNCTION    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Input: Item Name to Update
└────────────┬─────────────┘
             │
             ▼
        ┌──────────────┐
        │Item Exists?  │
        └────┬─────┬───┘
         YES │     NO
            │      │
            ▼      ▼
        Input New  [X] Error:
        Quantity   Item not found
            │
            ▼
        ┌──────────────┐
        │Valid Number? │
        └────┬─────┬───┘
         YES │     NO
            │      │
            ▼      ▼
        Update  [X] Error:
        Value   Invalid input
            │
            ▼
        Save to File
            │
            ▼
        Success Message
            │
            ▼
        Return to Menu Loop
```

---

## Choice 4: Remove Item

```
┌──────────────────────────┐
│  REMOVE ITEM FUNCTION    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Input: Item Name to Remove
└────────────┬─────────────┘
             │
             ▼
        ┌──────────────┐
        │Item Exists?  │
        └────┬─────┬───┘
         YES │     NO
            │      │
            ▼      ▼
        Delete  [X] Error:
        Item    Item not found
            │
            ▼
        Save to File
            │
            ▼
        Success Message
            │
            ▼
        Return to Menu Loop
```

---

## Choice 5: Search Item

```
┌──────────────────────────┐
│  SEARCH ITEM FUNCTION    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Input: Search Term       │
└────────────┬─────────────┘
             │
             ▼
       ┌─────────────┐
       │Empty Term?  │
       └─────┬───────┘
         YES │ NO
            │  │
            ▼  ▼
          [X]  Search through all items
               (matching substring)
               │
               ▼
          ┌──────────────┐
          │Results Found?│
          └────┬─────┬───┘
           YES │     NO
              │      │
              ▼      ▼
           Display  [X] No items
           Results   found message
              │
              ▼
           Return to Menu Loop
```

---

## Choice 6: Save & Exit

```
┌──────────────────────────┐
│  SAVE & EXIT FUNCTION    │
└────────────┬─────────────┘
             │
             ▼
        Save Inventory
        to JSON File
             │
             ▼
        Display "Goodbye"
        Message
             │
             ▼
        Exit Menu Loop
             │
             ▼
        ┌─────────────┐
        │ END PROGRAM │
        └─────────────┘
```

---

## Error Handling Flow

```
┌────────────────────────┐
│  TRY-EXCEPT BLOCK      │
└────────────┬───────────┘
             │
             ▼
    Execute User Input
             │
      ┌──────┴──────┐
      │             │
      ▼             ▼
   Success      Exception?
      │             │
      ▼             ▼
   Continue     Display Error
   Operation    Message
      │             │
      └──────┬──────┘
             │
             ▼
        Return to
        Menu Loop
```
