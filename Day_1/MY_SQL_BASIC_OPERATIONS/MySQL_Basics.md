# MySQL Basics: Databases, Tables, and CRUD Operations

------------------------------------------------------------------------

## 1. Introduction to Databases

**Database:**\
An organized collection of data stored and accessed electronically.
Databases allow efficient data retrieval, manipulation, and storage.

**MySQL:**\
A popular Relational Database Management System (RDBMS) that stores data
in **tables** containing rows and columns.

------------------------------------------------------------------------

## 2. Managing Databases (DDL)

### ▶️ Creating a Database

Use `CREATE DATABASE` to make a new container for your data.

**Syntax:**

``` sql
CREATE DATABASE database_name;
```

**Example:**

``` sql
CREATE DATABASE LibraryDB;
```

**Note:**\
Reserved words like `CREATE`, `DATABASE`, and `INT` should not be used
as names.

------------------------------------------------------------------------

### ▶️ Naming Conventions & Case Sensitivity

-   Use meaningful names.
-   Write SQL keywords in uppercase.
-   Windows: Case-insensitive
-   Linux/Unix: Case-sensitive

------------------------------------------------------------------------

### ▶️ Selecting a Database

``` sql
USE LibraryDB;
```

------------------------------------------------------------------------

### ▶️ Viewing All Databases

``` sql
SHOW DATABASES;
```

------------------------------------------------------------------------

### ▶️ Dropping a Database

Deletes the database permanently.

``` sql
DROP DATABASE database_name;
```

------------------------------------------------------------------------

## 3. Managing Tables

### ▶️ Creating a Table (Without Constraints)

Tables store the actual data.

**Syntax:**

``` sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype
);
```

**Common Data Types:** - `INT` - `VARCHAR(n)`

**Example:**

``` sql
CREATE TABLE books (
    book_id INT,
    title VARCHAR(25),
    author VARCHAR(25),
    genre VARCHAR(25),
    publication_year INT
);
```

------------------------------------------------------------------------

### ▶️ Dropping a Table

``` sql
DROP TABLE books;
```

------------------------------------------------------------------------

## 4. Manipulating Data (DML)

### ▶️ Inserting Data

**Syntax:**

``` sql
INSERT INTO table_name (col1, col2)
VALUES (val1, val2);
```

**Example:**

``` sql
INSERT INTO books (book_id, title, author, genre, publication_year)
VALUES (1, 'Twilight', 'Stephenie Meyer', 'Romance', 2020),
       (2, 'Harry Potter', 'J.K. Rowling', 'Sci-Fi', 2018);
```

------------------------------------------------------------------------

### ▶️ Retrieving Data

``` sql
SELECT * FROM books;
```

------------------------------------------------------------------------

## 5. Shortcuts & Comments

  Feature               Description   Syntax/Key
  --------------------- ------------- -----------------
  Execute Query         Run SQL       Ctrl + Enter
  Single-Line Comment   One line      -- comment
  Multi-line Comment    Block         /\* comment \*/
  End Statement         End query     ;

------------------------------------------------------------------------

## 6. Workflow Recap

1.  Create DB\
2.  Use DB\
3.  Create Table\
4.  Insert Data\
5.  Select Data\
6.  Drop Table or Drop DB
