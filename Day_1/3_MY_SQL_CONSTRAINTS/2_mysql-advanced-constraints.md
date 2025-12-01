# Personal Notes: Advanced MySQL Constraints (Default, Index & Composite Keys)

------------------------------------------------------------------------

## 1. Default Constraint

The **DEFAULT** constraint helps MySQL fill in a value automatically
when I don't provide one.\
Super useful when a field is optional or when forms don't always send
data for every column.

### ✔️ Example: Members Table With Default Salary

``` sql
CREATE TABLE members (
    id INT PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    email VARCHAR(25) UNIQUE,
    salary INT DEFAULT 22000
);
```

If I insert a row without the salary:

``` sql
INSERT INTO members (id, first_name, last_name, email)
VALUES (1, 'Chris', 'Nick', 'example@example.com');
```

MySQL automatically sets salary = **22000**.\
Good reminder that defaults keep databases consistent without forcing
extra input.

------------------------------------------------------------------------

## 2. Index Constraint

Indexes drastically improve search performance.\
If a table has thousands of rows and I frequently filter by a specific
column, adding an index makes queries way faster.

### ✔️ Creating an Index

``` sql
CREATE INDEX index_first_name ON members (first_name);
```

Now when I run:

``` sql
SELECT * FROM members WHERE first_name = 'Krish';
```

The engine uses the index instead of scanning the whole table.\
In large systems, this makes a massive difference.

------------------------------------------------------------------------

## 3. Composite Key

A **Composite Key** is a Primary Key made from multiple columns.\
It ensures uniqueness based on the **combination** of values, not
individual columns.

### ✔️ Where It's Useful

Example: A student can take many courses, and a course has many
students.\
But the same student shouldn't be enrolled in the same course twice.

### ✔️ Enrollment Table Example

``` sql
CREATE TABLE enrollment (
    studentID INT,
    courseID INT,
    enrollment_date DATE,
    PRIMARY KEY (studentID, courseID)
);
```

### ✔️ Behavior Notes

-   (1,1) → Allowed once\
-   (1,2) → Allowed\
-   (2,1) → Allowed\
-   (1,1) again → ❌ Duplicate error

### ✔️ Testing It

``` sql
INSERT INTO enrollment (studentID, courseID, enrollment_date)
VALUES (1, 1, '2024-09-09'); -- Works

INSERT INTO enrollment (studentID, courseID, enrollment_date)
VALUES (1, 1, '2025-01-01'); -- Fails
```

MySQL rejects the second insert because the combination already exists.

------------------------------------------------------------------------

## Summary Table

  -----------------------------------------------------------------------
  Constraint                 What It Ensures
  -------------------------- --------------------------------------------
  **DEFAULT**                Auto-fills values when none are provided

  **INDEX**                  Makes searches much faster

  **COMPOSITE KEY**          Ensures uniqueness across multiple columns
                             together
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## My Takeaways

-   DEFAULT values reduce errors and missing data.
-   Indexes are essential once tables grow large --- they're like
    performance boosters.
-   Composite keys help model real-world relationships cleanly.
-   Always think about how data will *actually* be used before deciding
    constraints.

These notes help me remember how and when to use these advanced
constraints.
