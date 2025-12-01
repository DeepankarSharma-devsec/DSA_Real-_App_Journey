# Personal Notes: MySQL ALTER TABLE Operations

------------------------------------------------------------------------

## 1. Overview

The `ALTER TABLE` command is all about changing the **structure** of an
existing table.\
Unlike `UPDATE` (which edits row data), `ALTER TABLE` modifies the table
layout itself.

### What I can do with ALTER TABLE:

-   Add new columns
-   Modify existing columns (change datatype, size)
-   Rename columns
-   Remove (drop) columns

------------------------------------------------------------------------

## 2. Adding Columns

### ✔️ Add a Single Column

``` sql
ALTER TABLE employees 
ADD COLUMN phone_number VARCHAR(25);
```

### ✔️ Add Multiple Columns

I can add several new fields at once:

``` sql
ALTER TABLE employees 
ADD COLUMN middle_name VARCHAR(25),
ADD COLUMN date_of_birth DATE;
```

------------------------------------------------------------------------

## 3. Modifying Columns (Changing Data Types)

Useful when increasing text size, changing number precision, or
adjusting field type.

### ✔️ General Syntax

``` sql
ALTER TABLE table_name 
MODIFY COLUMN column_name new_datatype;
```

### ✔️ Examples

**Reduce phone number length:**

``` sql
ALTER TABLE employees 
MODIFY COLUMN phone_number VARCHAR(20);
```

**Change salary from DECIMAL → INT:**\
(Decimal precision is removed.)

``` sql
ALTER TABLE employees 
MODIFY COLUMN salary INT;
```

------------------------------------------------------------------------

## 4. Renaming Columns

For renaming, I must use `CHANGE COLUMN`.\
Important: I must restate the datatype even if it stays the same.

### ✔️ Example

Rename `middle_name` → `middleName`:

``` sql
ALTER TABLE employees 
CHANGE COLUMN middle_name middleName VARCHAR(25);
```

------------------------------------------------------------------------

## 5. Dropping Columns

### ✔️ Drop a Single Column

``` sql
ALTER TABLE employees 
DROP COLUMN date_of_birth;
```

### ✔️ Drop Multiple Columns

``` sql
ALTER TABLE employees 
DROP COLUMN phone_number,
DROP COLUMN middleName;
```

------------------------------------------------------------------------

## 6. Quick Keyword Summary

  ------------------------------------------------------------------------
  Action           SQL Keyword                What It Does
  ---------------- -------------------------- ----------------------------
  Add Column       `ADD COLUMN`               Creates a new field

  Modify Column    `MODIFY COLUMN`            Changes datatype or size

  Rename Column    `CHANGE COLUMN`            Renames the field (datatype
                                              required)

  Delete Column    `DROP COLUMN`              Removes a column permanently
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## My Personal Takeaways

-   ALTER TABLE is powerful --- but destructive if not used carefully.\
-   When renaming, always remember to include the datatype.\
-   Adding and dropping multiple columns at once is cleaner than writing
    many queries.\
-   COLUMN changes happen instantly, so I should double-check before
    executing.

These notes should help me quickly recall how to reshape a table
structure in MySQL.
