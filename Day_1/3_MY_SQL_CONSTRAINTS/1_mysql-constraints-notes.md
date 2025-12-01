# Personal Notes: MySQL Constraints

------------------------------------------------------------------------

## 1. Understanding Constraints

Constraints are basically **rules** MySQL uses to protect the quality of
data.\
If any of these rules are violated during an INSERT/UPDATE, MySQL
immediately blocks the operation.

### ✔️ Checking Table Structure (Schema + Constraints)

``` sql
DESCRIBE table_name;
-- or
DESC table_name;
```

I use this often to confirm if a Primary Key, Unique, or Foreign Key is
applied correctly.

------------------------------------------------------------------------

## 2. Primary Key (PK)

A **Primary Key** uniquely identifies each record.\
It has 3 strict rules:

1.  Must be **unique**\
2.  Cannot be **NULL**\
3.  Only **one** PK per table

### ✔️ My Example Table with PK

``` sql
CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    email VARCHAR(25)
);
```

If I try to insert duplicate `author_id` values, MySQL throws a
**Duplicate entry** error.\
Good reminder of why PK is important.

------------------------------------------------------------------------

## 3. Foreign Key (FK)

A **Foreign Key** links two tables together.\
It enforces **Referential Integrity**---meaning I cannot insert a value
into the child table that doesn't exist in the parent table.

### ✔️ Example Relationship

Parent table → `authors`\
Child table → `books`

``` sql
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(25) NOT NULL,
    author_id INT,
    publication_year INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
```

If I try:

``` sql
INSERT INTO books (book_id, title, author_id)
VALUES (1, 'Sample Book', 999);
```

It will fail because `author_id = 999` does not exist in the `authors`
table.

------------------------------------------------------------------------

## 4. NOT NULL Constraint

Forces a column to always have a value.

### ✔️ During Creation

``` sql
CREATE TABLE student (
    id INT NOT NULL,
    first_name VARCHAR(25) NOT NULL,
    age INT
);
```

### ✔️ Adding NOT NULL Later

``` sql
ALTER TABLE student 
MODIFY age INT NOT NULL;
```

------------------------------------------------------------------------

## 5. CHECK Constraint

The `CHECK` constraint ensures that values follow a meaningful rule.

Example: publication year cannot be negative.

``` sql
CREATE TABLE books (
    book_id INT,
    title VARCHAR(25),
    publication_year INT,
    CHECK (publication_year > 0)
);
```

------------------------------------------------------------------------

## 6. UNIQUE Constraint

Ensures that values in a column are different from each other.

``` sql
CREATE TABLE person (
    id INT PRIMARY KEY,
    last_name VARCHAR(25) UNIQUE,
    age INT
);
```

### ✔️ Difference: PRIMARY KEY vs UNIQUE

  Feature               Primary Key      Unique Key
  --------------------- ---------------- ------------------
  Duplicates            ❌ Not allowed   ❌ Not allowed
  NULL allowed?         ❌ No            ✔️ Yes
  How many per table?   1 only           Multiple allowed

This is a simple but powerful distinction.

------------------------------------------------------------------------

## 7. AUTO_INCREMENT

Used mostly with Primary Keys to generate IDs automatically.

``` sql
CREATE TABLE person (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(25)
);
```

I don't have to manually insert `id` anymore---MySQL handles it.

------------------------------------------------------------------------

## 8. Altering Constraints (Add / Drop)

### ✔️ Adding Primary Key Later

``` sql
ALTER TABLE student 
MODIFY id INT NOT NULL PRIMARY KEY;
```

### ✔️ Dropping a Primary Key

``` sql
ALTER TABLE student 
DROP PRIMARY KEY;
```

### ✔️ Adding a UNIQUE Constraint Later

``` sql
ALTER TABLE person 
ADD CONSTRAINT unique_last_name UNIQUE (last_name);
```

------------------------------------------------------------------------

## My Personal Takeaways

-   Constraints make the table **safe and reliable**.\
-   Primary Key + Auto Increment is a combo I use frequently.\
-   UNIQUE allows NULLs (a detail I always remind myself).\
-   Foreign Keys prevent "orphan" records---super useful in relational
    design.\
-   `DESCRIBE table_name;` is my quick way to confirm everything is set
    properly.

These notes help me keep constraint rules clear whenever I'm designing
tables or debugging relational issues.
