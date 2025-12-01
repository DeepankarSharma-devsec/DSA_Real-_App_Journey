# Personal Notes: MySQL Data Manipulation (DML)

------------------------------------------------------------------------

## 1. Database & Table Setup

Before working with data, I created a fresh database and an `employees`
table.

### ✔️ Create and Select Database

``` sql
CREATE DATABASE companyDB;
USE companyDB; -- Must select the DB before creating tables
```

### ✔️ Create Table (Initial Version)

The employees table includes fields for ID, name, email, hire date, and
salary.

``` sql
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10,2)
);
```

------------------------------------------------------------------------

## 2. Understanding SQL NULL Values

A **NULL** value means *no value*, *unknown*, or *missing information*.\
It's not the same as `0` or an empty string `''`.

### ✔️ Insert Records Containing NULL

``` sql
INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, salary)
VALUES (5, 'Krish', NULL, 'krishna@gmail.com', NULL, 55000.00);
```

### ✔️ Retrieve Records With NULL Values

I cannot use `=` or `!=` with NULL.\
Instead, I must use `IS NULL`.

``` sql
SELECT * FROM employees WHERE last_name IS NULL;
```

Check multiple fields:

``` sql
SELECT * FROM employees 
WHERE last_name IS NULL OR hire_date IS NULL;
```

------------------------------------------------------------------------

## 3. UPDATE Statement

The `UPDATE` statement modifies existing rows in the table.

### ✔️ General Syntax

``` sql
UPDATE table_name
SET column_name = new_value
WHERE condition;
```

### ✔️ Fix Missing Data (Updating NULL)

``` sql
UPDATE employees
SET last_name = 'Nayak'
WHERE employee_id = 5;
```

### ✔️ Arithmetic Update Example

Increasing salary:

``` sql
UPDATE employees
SET salary = salary + 10000
WHERE employee_id = 5;
```

------------------------------------------------------------------------

## 4. DELETE Statement

Used to remove specific records.

### ✔️ Delete One Record

``` sql
DELETE FROM employees WHERE employee_id = 1;
```

### ✔️ Delete Multiple Records

``` sql
DELETE FROM employees WHERE salary < 66000;
```

------------------------------------------------------------------------

## 5. Safe Update Mode (Common MySQL Workbench Error)

I ran into an error:\
**"You are using Safe Update mode..."**

### ✔️ Why It Happens

Workbench blocks updates/deletes unless: - A **PRIMARY KEY** is used in
`WHERE`, or\
- A `LIMIT` clause is included.

This prevents accidental mass deletion.

------------------------------------------------------------------------

## 6. Fixing the Safe Update Issue

### **Solution A (Recommended): Add a Primary Key**

Recreating table with a PK:

``` sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10,2)
);
```

### **Solution B: Turn Off Safe Update Mode**

Steps inside MySQL Workbench:

1.  Edit\
2.  Preferences\
3.  SQL Editor\
4.  Uncheck "Safe Updates (rejects UPDATEs and DELETEs without a key)"\
5.  Apply\
6.  Reconnect to DB

------------------------------------------------------------------------

## Final Thoughts (My Personal Takeaways)

-   Always define a **Primary Key**---saves headaches later.\
-   NULL handling is super important.\
-   Safe Update Mode is useful but can block valid queries, so I must
    understand when to keep it on/off.\
-   UPDATE and DELETE without proper conditions can be dangerous.

These notes should help me quickly revise DML fundamentals whenever
needed.
