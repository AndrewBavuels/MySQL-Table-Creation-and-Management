# MySQL Table Creation and Management

This document provides step-by-step instructions on creating and managing tables in MySQL, including creating databases, tables, and viewing structures and warnings.

## Installation of MySQL on Ubuntu

If you don't have MySQL installed on your system, follow the installation guide from the official MySQL website:

[Install MySQL on Ubuntu](https://dev.mysql.com/downloads/mysql/5.7.html#downloads)

In my case, I selected as you can see in the image below, regarding my Ubuntu OS version:

![1_Ubuntu](https://github.com/user-attachments/assets/8ddbe5d4-262c-4436-930a-03580ee11e36)

After installing, ensure that the MySQL service is up and running before proceeding with the following steps.

## Connecting and Creating a Database

### 1. Starting MySQL Service

To start the MySQL service, use the following command:

```sh
sudo service mysql start
```

To check the status of the MySQL service:

```sh
sudo service mysql status
```
You should see output similar to this:
```sh
 * /usr/bin/mysqladmin  Ver 8.0.37-0ubuntu0.22.04.3 for Linux on x86_64 ((Ubuntu))
Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Server version          8.0.37-0ubuntu0.22.04.3
Protocol version        10
Connection              Localhost via UNIX socket
UNIX socket             /var/run/mysqld/mysqld.sock
Uptime:                 36 sec

Threads: 2  Questions: 8  Slow queries: 0  Opens: 119  Flush tables: 3  Open tables: 38  Queries per second avg: 0.222
```


### 2. Connecting to MySQL

```sh
mysql -u <your_username> -p
Enter password:
```

You should see output similar to this:

```sh
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 29
Server version: 8.0.37-0ubuntu0.22.04.3 (Ubuntu)

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```

### 3. Creating a Database:

```sh
mysql> CREATE database holi_operations;
Query OK, 1 row affected (0.02 sec)

mysql> CREATE DATABASE IF NOT EXISTS holi_operations;
Query OK, 1 row affected, 1 warning (0.01 sec)
```
### 4. Showing warnings:

```sh
mysql> SHOW warnings;
+-------+------+----------------------------------------------------------+
| Level | Code | Message                                                  |
+-------+------+----------------------------------------------------------+
| Note  | 1007 | Can't create database 'holi_operations'; database exists |
+-------+------+----------------------------------------------------------+
1 row in set (0.00 sec)
```
### 5. Showing databases:

```sh
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| CURSOPRACTICOSQL   |
| holi_operations    |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)
```
### 6. Using the database:

```sh
mysql> use holi_operations;
Database changed
```

## Creating Tables

### 7. Create `books` Table:

```sh
CREATE TABLE IF NOT EXISTS books(
    book_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    author_id INTEGER UNSIGNED,
    title VARCHAR(100) NOT NULL,
    `year` INTEGER UNSIGNED NOT NULL DEFAULT 1900,
    `language` VARCHAR(2) NOT NULL DEFAULT 'es' COMMENT 'ISO 639-1 language',
    `cover_url` VARCHAR(500),
    price DOUBLE(6, 2) NOT NULL DEFAULT 10.0,
    sellable TINYINT(1) DEFAULT 1,
    copies INTEGER NOT NULL DEFAULT 1,
    description TEXT
);
```

### 8. Create `authors` Table:

```sh
CREATE TABLE IF NOT EXISTS authors(
    author_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    nationality VARCHAR(3)
);
```
### 9. Create `clients` Table:

```sh
CREATE TABLE clients (
    client_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    birthdate DATETIME,
    gender ENUM('F','M','ND') NOT NULL,
    active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
```

### 10. Create `operations` Table:

```sh
CREATE TABLE IF NOT EXISTS operations (
    operation_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    book_id INTEGER UNSIGNED,
    client_id INTEGER UNSIGNED,
    `type` ENUM('sold', 'lent', 'returned') NOT NULL,
    finished TINYINT(1) NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
```
## Verifying the Current Database

### 11. Show Current Database:

```sh
mysql> select database();
+-----------------+
| database()      |
+-----------------+
| holi_operations |
+-----------------+
1 row in set (0.00 sec)

Query OK, 0 rows affected, 2 warnings (0.09 sec)
```
### 12. Show Created Tables:

```sh
mysql> show tables;
+---------------------------+
| Tables_in_holi_operations |
+---------------------------+
| authors                   |
| books                     |
| clients                   |
| operations                |
+---------------------------+
4 rows in set (0.01 sec)
```

## Fixing Errors

### 13. Drop author (in singular) Table:

```sh
mysql> drop table author;
Query OK, 0 rows affected (0.07 sec)

mysql> show tables;
+---------------------------+
| Tables_in_holi_operations |
+---------------------------+
| books                     |
+---------------------------+
1 row in set (0.00 sec)
```
### 14. Recreate authors (in plural) Table:

```sh
mysql> CREATE TABLE IF NOT EXISTS authors(
    ->     author_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    ->     name VARCHAR(100) NOT NULL,
ARCHAR(3)
);    ->     nationality VARCHAR(3)
    -> );
Query OK, 0 rows affected (0.08 sec)

mysql> show tables;
+---------------------------+
| Tables_in_holi_operations |
+---------------------------+
| authors                   |
| books                     |
| clients                   |
| operations                |
+---------------------------+
4 rows in set (0.00 sec)
```
### 15. Describing Table Structure:

**Describe:** In case where we work with these databases for the first time and we need context

```sh
mysql> describe authors;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| author_id   | int unsigned | NO   | PRI | NULL    | auto_increment |
| name        | varchar(100) | NO   |     | NULL    |                |
| nationality | varchar(3)   | YES  |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
```
...also with `desc`:

```sh
mysql> desc books;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| book_id     | int unsigned | NO   | PRI | NULL    | auto_increment |
| author_id   | int unsigned | YES  |     | NULL    |                |
| title       | varchar(100) | NO   |     | NULL    |                |
| year        | int unsigned | NO   |     | 1900    |                |
| language    | varchar(2)   | NO   |     | es      |                |
| cover_url   | varchar(500) | YES  |     | NULL    |                |
| price       | double(6,2)  | NO   |     | 10.00   |                |
| sellable    | tinyint(1)   | YES  |     | 1       |                |
| copies      | int          | NO   |     | 1       |                |
| description | text         | YES  |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
10 rows in set (0.01 sec)
```
### 16. To get detailed column information:

```sh
mysql> show full columns from books;
```
## Inserting Data into Tables

### 17. Inserting Data into `authors`:

```sh
INSERT INTO `authors` (name, nationality) 
VALUES
    ('Dave Grohl', 'USA'),
    ('Aldous Huxley', 'GBR'),
    ('Eric Ries', 'USA'),
    ('Gabriel Garcia Marquez', 'COL'),
    ('J.K. Rowling', 'GBR'),
    ('George R.R. Martin', 'USA'),
    ('Stephen King', 'USA'),
    ('Jane Austen', 'GBR'),
    ('Leo Tolstoy', 'RUS'),
    ('Fyodor Dostoevsky', 'RUS'),
    ...
  ;
```
### 18. Inserting Data into `books`:

```sh
INSERT INTO `books` VALUES
    (1, 1, "The Storyteller: Tales of Life and Music", 2021, "en", NULL, 15.42, 1, 5, "A memoir by Dave Grohl, recounting his experiences as a musician and his journey through the world of rock and roll."),
    (2, 2, "Brave New World", 1932, "en", NULL, 38.45, 1, 10, "A dystopian novel set in a futuristic society characterized by technological advancements and social stability at the cost of individuality."),
    (3, 3, "The Lean Startup", 2011, "en", NULL, 40.1, 1, 7, "A guide to building successful startups through a methodology that emphasizes rapid prototyping and customer feedback."),
    (4, 4, "One Hundred Years of Solitude", 1967, "es", NULL, 37.65, 1, 8, "A multi-generational novel that explores the magical realism of the Buendía family in the fictional town of Macondo."),
    (5, 5, "Harry Potter and the Sorcerer's Stone", 1997, "en", NULL, 49.5, 1, 15, "The first book in the Harry Potter series, where young Harry discovers his magical heritage and attends Hogwarts School of Witchcraft and Wizardry."),
    (6, 9, "War and Peace", 1869, "ru", NULL, 47.48, 1, 11, "An epic historical novel that covers the Napoleonic Wars and the impact of these events on Russian aristocratic families."),
    (7, 10, "Crime and Punishment", 1866, "ru", NULL, 28.25, 1, 9, "A psychological novel that explores the moral dilemmas and consequences faced by a young man who commits a crime."),
    (8, 11, "Moby-Dick", 1851, "en", NULL, 30.51, 1, 7, "A novel about Captain Ahab's obsessive quest to hunt the white whale, Moby Dick, and the consequences of his obsession."),
    (9, 13, "Great Expectations", 1861, "en", NULL, 14.97, 1, 8, "A coming-of-age novel that tells the story of Pip and his growth from an orphan into a gentleman with great expectations."),
    (10, 14, "Murder on the Orient Express", 1934, "en", NULL, 13.58, 1, 6, "A classic mystery novel featuring detective Hercule Poirot solving a murder on a luxurious train journey."),
    ...
    ;
```
### 19. Inserting Data into `clients`:

```sh
INSERT INTO `clients` (name, email, birthdate, gender, active)
VALUES
    ('Tom Hanks', 'tom.hanks@example.com', '1956-07-09', 'M', 1),
    ('Scarlett Johansson', 'scarlett.johansson@example.com', '1984-11-22', 'F', 1),
    ('Robert Downey Jr.', 'robert.downey.jr@example.com', '1965-04-04', 'M', 1),
    ('Jennifer Lawrence', 'jennifer.lawrence@example.com', '1990-08-15', 'F', 1),
    ('Morgan Freeman', 'morgan.freeman@example.com', '1937-06-01', 'M', 1),
    ('Emma Watson', 'emma.watson@example.com', '1990-04-15', 'F', 1),
    ('Ryan Reynolds', 'ryan.reynolds@example.com', '1976-10-23', 'M', 1),
    ('Natalie Portman', 'natalie.portman@example.com', '1981-06-09', 'F', 1),
    ('Leonardo DiCaprio', 'leonardo.dicaprio@example.com', '1974-11-11', 'M', 1),
    ('Marge Simpson', 'marge.simpson@example.com', '1956-03-19', 'F', 1),
    ...
    ;
```

### 20. Inserting Data into `operations`:

```sh
INSERT INTO operations(operation_id, book_id, client_id, type, finished)
VALUES
    (1, 104, 96, 'returned' ,1),
    (2, 52, 113, 'lent' ,1),
    (3, 9, 95, 'lent' ,1),
    (4, 141, 131, 'returned' ,1),
    (5, 130, 91, 'sold' ,1),
    (6, 12, 50, 'sold' ,1),
    (7, 76, 87, 'returned' ,1),
    (8, 116, 42, 'returned' ,1),
    (9, 84, 7, 'lent' ,1),
    (10, 147, 122, 'sold' ,1),
    ...
    ;
```

## Querying Data and Viewing Results

**1. Query Example:** To query data from the clients table, you can use the following command:

```sh
mysql> SELECT * FROM clients WHERE client_id = 6;
+-----------+-------------+-------------------------+---------------------+--------+--------+---------------------+---------------------+
| client_id | name        | email                   | birthdate           | gender | active | created_at          | updated_at          |
+-----------+-------------+-------------------------+---------------------+--------+--------+---------------------+---------------------+
|         6 | Emma Watson | emma.watson@example.com | 1990-04-15 00:00:00 | F      |      1 | 2024-08-09 11:41:25 | 2024-08-09 11:41:25 |
+-----------+-------------+-------------------------+---------------------+--------+--------+---------------------+---------------------+
1 row in set (0.00 sec)
```
**2. More Readable Output:** For a more readable format, use the `\G` option at the end of your query. This will format the output vertically:

```sh
mysql> SELECT * FROM clients WHERE client_id = 6\G
*************************** 1. row ***************************
 client_id: 6
      name: Emma Watson
     email: emma.watson@example.com
 birthdate: 1990-04-15 00:00:00
    gender: F
    active: 1
created_at: 2024-08-09 11:41:25
updated_at: 2024-08-09 11:41:25
1 row in set (0.00 sec)
```


## Querying Data with SELECT

The `SELECT` statement is used to query data from a database. Below are several examples demonstrating how to use SELECT to retrieve and format data.

**1. Basic Query:** Retrieve the `name`, `email`, and `gender` columns from the `clients` table with a limit of 10 rows:

```sh
mysql> SELECT name, email, gender FROM clients
    -> LIMIT 10;
+--------------------+--------------------------------+--------+
| name               | email                          | gender |
+--------------------+--------------------------------+--------+
| Tom Hanks          | tom.hanks@example.com          | M      |
| Scarlett Johansson | scarlett.johansson@example.com | F      |
| Robert Downey Jr.  | robert.downey.jr@example.com   | M      |
| Jennifer Lawrence  | jennifer.lawrence@example.com  | F      |
| Morgan Freeman     | morgan.freeman@example.com     | M      |
| Emma Watson        | emma.watson@example.com        | F      |
| Ryan Reynolds      | ryan.reynolds@example.com      | M      |
| Natalie Portman    | natalie.portman@example.com    | F      |
| Leonardo DiCaprio  | leonardo.dicaprio@example.com  | M      |
| Marge Simpson      | marge.simpson@example.com      | F      |
+--------------------+--------------------------------+--------+
10 rows in set (0.00 sec)
```
**2. Filtering Data:** Retrieve `name`, `email`, and `gender` for female clients only, with a limit of 10 rows:

```sh
mysql> SELECT name, email, gender FROM clients WHERE gender = 'F' LIMIT 10;
+--------------------+--------------------------------+--------+
| name               | email                          | gender |
+--------------------+--------------------------------+--------+
| Scarlett Johansson | scarlett.johansson@example.com | F      |
| Jennifer Lawrence  | jennifer.lawrence@example.com  | F      |
| Emma Watson        | emma.watson@example.com        | F      |
| Natalie Portman    | natalie.portman@example.com    | F      |
| Marge Simpson      | marge.simpson@example.com      | F      |
| Jennifer Garner    | jennifer.garner@example.com    | F      |
| Meryl Streep       | meryl.streep@example.com       | F      |
| Angelina Jolie     | angelina.jolie@example.com     | F      |
| Julia Roberts      | julia.roberts@example.com      | F      |
| Charlize Theron    | charlize.theron@example.com    | F      |
+--------------------+--------------------------------+--------+
10 rows in set (0.00 sec)
```
**3. Extracting Parts of Data:** Retrieve the `name` and the birth year of clients, limiting to 10 rows:
```sh
mysql> SELECT name, YEAR(birthdate) FROM clients LIMIT 10;
+--------------------+-----------------+
| name               | year(birthdate) |
+--------------------+-----------------+
| Tom Hanks          |            1956 |
| Scarlett Johansson |            1984 |
| Robert Downey Jr.  |            1965 |
| Jennifer Lawrence  |            1990 |
| Morgan Freeman     |            1937 |
| Emma Watson        |            1990 |
| Ryan Reynolds      |            1976 |
| Natalie Portman    |            1981 |
| Leonardo DiCaprio  |            1974 |
| Marge Simpson      |            1956 |
+--------------------+-----------------+
10 rows in set (0.00 sec)
```

**4. Using Date Functions:** Retrieve the current date and time:

```sh
mysql> SELECT NOW();
+---------------------+
| now()               |
+---------------------+
| 2024-08-13 13:14:56 |
+---------------------+
1 row in set (0.00 sec)
```
**5. Calculating Values:** Calculate the age of female clients:

```sh
mysql> SELECT name, YEAR(NOW()) - YEAR(birthdate) FROM clients WHERE gender = 'F' LIMIT 10;
+--------------------+-------------------------------+
| name               | year(now()) - year(birthdate) |
+--------------------+-------------------------------+
| Scarlett Johansson |                            40 |
| Jennifer Lawrence  |                            34 |
| Emma Watson        |                            34 |
| Natalie Portman    |                            43 |
| Marge Simpson      |                            68 |
| Jennifer Garner    |                            52 |
| Meryl Streep       |                            75 |
| Angelina Jolie     |                            49 |
| Julia Roberts      |                            57 |
| Charlize Theron    |                            49 |
+--------------------+-------------------------------+
10 rows in set (0.01 sec)
```
**6. Using Patterns for Search:** Search for clients whose name contains "worth":

```sh
mysql> SELECT * FROM clients WHERE name LIKE '%worth'\G
*************************** 1. row ***************************
 client_id: 29
      name: Chris Hemsworth
     email: chris.hemsworth@example.com
 birthdate: 1983-08-11 00:00:00
    gender: M
    active: 1
created_at: 2024-08-13 11:43:55
updated_at: 2024-08-13 11:43:55
1 row in set (0.00 sec)
```
**7. Combining Conditions:** Retrieve names and ages of female clients whose names include "nifer":

```sh
mysql> SELECT name, YEAR(NOW()) - YEAR(birthdate) AS age
    -> FROM clients
    -> WHERE gender = 'F'
    -> AND name LIKE '%nifer%';
+-------------------+------+
| name              | age  |
+-------------------+------+
| Jennifer Lawrence |   34 |
| Jennifer Garner   |   52 |
+-------------------+------+
2 rows in set (0.00 sec)
```
## Combining Data with JOIN

The JOIN (or INNER JOIN) clause is used to combine rows from two or more tables based on a related column between them. Here are some examples demonstrating different types of joins in MySQL.

**1. Counting Rows in Tables:** First, let’s count the number of rows in the `books` and `authors` tables:

#### `books`:

```sh
mysql> SELECT COUNT(*) FROM books;
+----------+
| count(*) |
+----------+
|      176 |
+----------+
1 row in set (0.01 sec)
```
#### `authors`:

```sh
mysql> SELECT COUNT(*) FROM authors;
+----------+
| count(*) |
+----------+
|       99 |
+----------+
1 row in set (0.00 sec)
```

**2. Retrieving Data from Multiple Tables:**

#### 2.1. Retrieve Authors: 

Get details of authors with IDs between 1 and 5:

```sh
mysql> SELECT * FROM authors WHERE author_id > 0 AND author_id <= 5;
+-----------+------------------------+-------------+
| author_id | name                   | nationality |
+-----------+------------------------+-------------+
|         1 | Dave Grohl             | USA         |
|         2 | Aldous Huxley          | GBR         |
|         3 | Eric Ries              | USA         |
|         4 | Gabriel Garcia Marquez | COL         |
|         5 | J.K. Rowling           | GBR         |
+-----------+------------------------+-------------+
5 rows in set (0.01 sec)
```
#### 2.2. Retrieve Books: 
    
Get books with author IDs between 1 and 5:

```sh
mysql> SELECT book_id, author_id, title FROM books WHERE author_id BETWEEN 1 AND 5;
+---------+-----------+------------------------------------------+
| book_id | author_id | title                                    |
+---------+-----------+------------------------------------------+
|       1 |         1 | The Storyteller: Tales of Life and Music |
|       2 |         2 | Brave New World                          |
|       3 |         3 | The Lean Startup                         |
|       4 |         4 | One Hundred Years of Solitude            |
|       5 |         5 | Harry Potter and the Sorcerer's Stone    |
+---------+-----------+------------------------------------------+
5 rows in set (0.00 sec)
```
**3. Using INNER JOIN:**
    
#### 3.1. Combine Books and Authors: 
    
Join `books` with `authors` to get book titles along with author names for authors with IDs between 1 and 5:

```sh
SELECT b.book_id, a.name, b.title
FROM books AS b
INNER JOIN authors AS a
    ON a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 AND 5;

+---------+------------------------+------------------------------------------+
| book_id | name                   | title                                    |
+---------+------------------------+------------------------------------------+
|       1 | Dave Grohl             | The Storyteller: Tales of Life and Music |
|       2 | Aldous Huxley          | Brave New World                          |
|       3 | Eric Ries              | The Lean Startup                         |
|       4 | Gabriel Garcia Marquez | One Hundred Years of Solitude            |
|       5 | J.K. Rowling           | Harry Potter and the Sorcerer's Stone    |
+---------+------------------------+------------------------------------------+
5 rows in set (0.00 sec)
```
#### 3.2 Combine Operations, Books, Clients, and Author: 
    
Retrieve names of female clients, book titles, author names, and operation types for operations where books were sold:

```sh
SELECT c.name, b.title, a.name, o.type
FROM operations AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id
INNER JOIN clients AS c
    ON o.client_id = c.client_id
INNER JOIN authors AS a
    ON b.author_id = a.author_id
WHERE c.gender = 'F'
    AND o.type = 'sold';

+--------------------+------------------------------------------+------------------------+------+
| name               | title                                    | name                   | type |
+--------------------+------------------------------------------+------------------------+------+
| Scarlett Johansson | Brave New World                          | Aldous Huxley          | sold |
| Jennifer Lawrence  | The Lean Startup                         | Eric Ries              | sold |
| Emma Watson        | One Hundred Years of Solitude            | Gabriel Garcia Marquez | sold |
| Natalie Portman    | Harry Potter and the Sorcerer's Stone    | J.K. Rowling           | sold |
+--------------------+------------------------------------------+------------------------+------+
4 rows in set (0.01 sec)
```
#### 3.3 Filter Results Based on Conditions: 
    
Retrieve names, book titles, authors, and operation types for male clients where books were either sold or lent:

```sh
SELECT c.name, b.title, a.name, o.type
FROM operations AS o
INNER JOIN books AS b
    ON o.book_id = b.book_id
INNER JOIN clients AS c
    ON o.client_id = c.client_id
INNER JOIN authors AS a
    ON b.author_id = a.author_id
WHERE c.gender = 'M'
    AND o.type IN ('sold', 'lent');

+------------------+------------------------------------------+------------------------+------+
| name             | title                                    | name                   | type |
+------------------+------------------------------------------+------------------------+------+
| Tom Hanks        | The Storyteller: Tales of Life and Music | Dave Grohl             | sold |
| Robert Downey Jr.| Brave New World                          | Aldous Huxley          | lent |
+------------------+------------------------------------------+------------------------+------+
2 rows in set (0.00 sec)
```

## Using LEFT JOIN and Other JOIN Types

In SQL, `JOIN` operations are crucial for combining data from multiple tables. Below, we explore different types of joins, including `LEFT JOIN`, and how to use them effectively.

**1. Implicit JOIN vs. Explicit JOIN:**

#### 1.1. Implicit JOIN: 
    
Uses a comma to separate table names and combines tables based on the `WHERE` clause:


```sh
SELECT b.title, a.name
FROM authors AS a, books AS b
WHERE a.author_id = b.author_id
LIMIT 10;

+------------------------------------------+------------------------+
| title                                    | name                   |
+------------------------------------------+------------------------+
| The Storyteller: Tales of Life and Music | Dave Grohl             |
| Brave New World                          | Aldous Huxley          |
| The Lean Startup                         | Eric Ries              |
| One Hundred Years of Solitude            | Gabriel Garcia Marquez |
| Harry Potter and the Sorcerer's Stone    | J.K. Rowling           |
| War and Peace                            | Leo Tolstoy            |
| Crime and Punishment                     | Fyodor Dostoevsky      |
| Moby-Dick                                | Herman Melville        |
| Great Expectations                       | Charles Dickens        |
| Murder on the Orient Express             | Agatha Christie        |
+------------------------------------------+------------------------+
10 rows in set (0.00 sec)
```
#### 1.2 Explicit JOIN: 
    
Uses the `JOIN` keyword for better readability and understanding. The example below uses `INNER JOIN`, which is the same as `JOIN`:

```sh
SELECT b.title, a.name
FROM books AS b
INNER JOIN authors AS a
  ON a.author_id = b.author_id
LIMIT 10;

+------------------------------------------+------------------------+
| title                                    | name                   |
+------------------------------------------+------------------------+
| The Storyteller: Tales of Life and Music | Dave Grohl             |
| Brave New World                          | Aldous Huxley          |
| The Lean Startup                         | Eric Ries              |
| One Hundred Years of Solitude            | Gabriel Garcia Marquez |
| Harry Potter and the Sorcerer's Stone    | J.K. Rowling           |
| War and Peace                            | Leo Tolstoy            |
| Crime and Punishment                     | Fyodor Dostoevsky      |
| Moby-Dick                                | Herman Melville        |
| Great Expectations                       | Charles Dickens        |
| Murder on the Orient Express             | Agatha Christie        |
+------------------------------------------+------------------------+
10 rows in set (0.00 sec)
```
**2. INNER JOIN with ORDER BY:** When sorting results, you can use the `ORDER BY` clause. By default, the sorting is in ascending order (`ASC`), but you can specify descending order (`DESC`):

```sh
SELECT a.author_id, a.name, a.nationality, b.title
FROM authors AS a
INNER JOIN books AS b
  ON b.author_id = a.author_id
WHERE a.author_id BETWEEN 1 AND 5
ORDER BY a.name DESC;

+-----------+------------------------+-------------+------------------------------------------+
| author_id | name                   | nationality | title                                    |
+-----------+------------------------+-------------+------------------------------------------+
|         5 | J.K. Rowling           | GBR         | Harry Potter and the Sorcerer's Stone    |
|         4 | Gabriel Garcia Marquez | COL         | One Hundred Years of Solitude            |
|         3 | Eric Ries              | USA         | The Lean Startup                         |
|         1 | Dave Grohl             | USA         | The Storyteller: Tales of Life and Music |
|         2 | Aldous Huxley          | GBR         | Brave New World                          |
+-----------+------------------------+-------------+------------------------------------------+
5 rows in set (0.00 sec)
```
**3. LEFT JOIN:** The `LEFT JOIN` (or `LEFT OUTER JOIN`) returns all rows from the left table and the matched rows from the right table. If no match is found, NULL values are returned for columns from the right table.

#### 3.1 Example with LEFT JOIN:
    
Retrieve authors and their books. If an author does not have any books, their details will still be included:

```sh
SELECT a.author_id, a.name, a.nationality, b.title
FROM authors AS a
LEFT JOIN books AS b
  ON b.author_id = a.author_id
WHERE a.author_id BETWEEN 10 AND 15
ORDER BY a.author_id;

+-----------+-------------------+-------------+------------------------------+
| author_id | name              | nationality | title                        |
+-----------+-------------------+-------------+------------------------------+
|        10 | Fyodor Dostoevsky | RUS         | Crime and Punishment         |
|        11 | Herman Melville   | USA         | Moby-Dick                    |
|        12 | J.R.R. Tolkien    | GBR         | The Silmarillion             |
|        13 | Charles Dickens   | GBR         | Great Expectations           |
|        14 | Agatha Christie   | GBR         | Murder on the Orient Express |
|        15 | Isaac Asimov      | USA         | I, Robot                     |
+-----------+-------------------+-------------+------------------------------+
6 rows in set (0.00 sec)
```
In this example, if an author in the specified range does not have any books, the title field will be NULL.

**4. Counting Books per Author:** To count the number of books each author has, use `COUNT` along with `GROUP BY`. This counts the number of books and groups the results by author:

```sh
SELECT a.author_id, a.name, a.nationality, COUNT(b.book_id)
FROM authors AS a
LEFT JOIN books AS b
  ON b.author_id = a.author_id
WHERE a.author_id BETWEEN 20 AND 25
GROUP BY a.author_id
ORDER BY a.author_id;

+-----------+-------------------+-------------+------------------+
| author_id | name              | nationality | COUNT(b.book_id) |
+-----------+-------------------+-------------+------------------+
|        20 | Ursula K. Le Guin | USA         |                1 |
|        21 | Margaret Atwood   | CAN         |                1 |
|        22 | Neil Gaiman       | GBR         |                1 |
|        23 | Douglas Adams     | GBR         |                1 |
|        24 | Michael Moorcock  | GBR         |                2 |
|        25 | Anne Rice         | USA         |                2 |
+-----------+-------------------+-------------+------------------+
6 rows in set (0.04 sec)
```
In this query, `COUNT(b.book_id)` counts the number of books for each author, including those with no books.

## Business Cases and Queries

Here are some common business queries you can run on your database to extract meaningful insights.

**1. What Nationalities Are There?** To list all distinct nationalities from the authors and order them alphabetically:

```sh
SELECT DISTINCT nationality 
FROM authors 
ORDER BY nationality;

+-------------+
| nationality |
+-------------+
| ARG         |
| AUS         |
| CAN         |
| CHI         |
| CHN         |
| COL         |
| DEU         |
| ESP         |
| FRA         |
| GBR         |
| IND         |
| IRL         |
| ISR         |
| MEX         |
| PER         |
| RUS         |
| USA         |
+-------------+
17 rows in set (0.00 sec)
```

**2. How Many Authors Are There from Each Nationality?** To count the number of authors from each nationality, excluding `NULL` values:

```sh
SELECT nationality, COUNT(author_id) AS authors_count
FROM authors
WHERE nationality IS NOT NULL
GROUP BY nationality
ORDER BY authors_count DESC, nationality ASC;

+-------------+---------------+
| nationality | authors_count |
+-------------+---------------+
| USA         |            46 |
| GBR         |            21 |
| CAN         |             5 |
| FRA         |             5 |
| CHI         |             4 |
| MEX         |             3 |
| ARG         |             2 |
| DEU         |             2 |
| ISR         |             2 |
| RUS         |             2 |
| AUS         |             1 |
| CHN         |             1 |
| COL         |             1 |
| ESP         |             1 |
| IND         |             1 |
| IRL         |             1 |
| PER         |             1 |
+-------------+---------------+
17 rows in set (0.00 sec)
```

**3. How Many Books Are There from Each Nationality?** To count the number of books written by authors from each nationality:

```sh
SELECT a.nationality, COUNT(b.book_id) AS books_count
FROM authors AS a
INNER JOIN books AS b
    ON b.author_id = a.author_id
WHERE nationality IS NOT NULL
GROUP BY nationality
ORDER BY books_count DESC, nationality ASC;

+-------------+-------------+
| nationality | books_count |
+-------------+-------------+
| USA         |          83 |
| GBR         |          33 |
| FRA         |          10 |
| CAN         |           9 |
| CHI         |           8 |
| MEX         |           6 |
| ARG         |           4 |
| DEU         |           4 |
| ISR         |           4 |
| AUS         |           2 |
| CHN         |           2 |
| ESP         |           2 |
| IND         |           2 |
| IRL         |           2 |
| PER         |           2 |
| RUS         |           2 |
| COL         |           1 |
+-------------+-------------+
17 rows in set (0.00 sec)
```
**4. What Is the Average and Standard Deviation of Book Prices by Nationality?** To get the average price and standard deviation of book prices for each nationality:

```sh
SELECT nationality,
    COUNT(book_id) AS books_count,
    AVG(price) AS mean, 
    STDDEV(price) AS std
FROM books AS b
JOIN authors AS a
    ON a.author_id = b.author_id
GROUP BY nationality
ORDER BY mean DESC;

+-------------+-------------+-----------+---------------------+
| nationality | books_count | mean      | std                 |
+-------------+-------------+-----------+---------------------+
| RUS         |           2 | 37.865000 |   9.614999999999997 |
| IND         |           2 | 37.715000 |   8.594999999999999 |
| COL         |           1 | 37.650000 |                   0 |
| DEU         |           4 | 34.407500 |   9.246692314011536 |
| CHN         |           2 | 32.430000 |  11.729999999999999 |
| GBR         |          33 | 31.847576 |  11.947687497892263 |
| FRA         |          10 | 29.931000 |    8.29831241879938 |
| ESP         |           2 | 29.565000 |   5.484999999999999 |
| MEX         |           6 | 29.190000 |  11.678575826415367 |
| USA         |          83 | 28.929398 |  11.847953241916713 |
| ARG         |           4 | 28.895000 |   9.935322088387473 |
| CHI         |           8 | 28.135000 |   8.698124797909031 |
| ISR         |           4 | 26.105000 |   9.267822020302289 |
| CAN         |           9 | 23.967778 |  11.789122837766625 |
| AUS         |           2 | 21.280000 |  1.6400000000000006 |
| PER         |           2 | 20.200000 | 0.35000000000000053 |
| IRL         |           2 | 17.205000 |   1.174999999999998 |
+-------------+-------------+-----------+---------------------+
17 rows in set (0.00 sec)
```
**What Is the Maximum and Minimum Price of a Book?** To find the maximum and minimum price of books:

```sh
SELECT a.nationality, MAX(price) AS max_price, MIN(price) AS min_price
FROM books AS b
JOIN authors AS a
    ON a.author_id = b.author_id
GROUP BY nationality;

+-------------+-----------+-----------+
| nationality | max_price | min_price |
+-------------+-----------+-----------+
| USA         |     49.98 |     10.21 |
| GBR         |     49.87 |     12.25 |
| COL         |     37.65 |     37.65 |
| RUS         |     47.48 |     28.25 |
| IRL         |     18.38 |     16.03 |
| DEU         |     49.09 |     23.67 |
| FRA         |     41.42 |     13.32 |
| PER         |     20.55 |     19.85 |
| CHI         |     46.63 |     15.74 |
| MEX         |     46.84 |     15.78 |
| ARG         |     44.45 |     18.88 |
| CHN         |     44.16 |     20.70 |
| CAN         |     44.82 |     10.32 |
| IND         |     46.31 |     29.12 |
| ESP         |     35.05 |     24.08 |
| ISR         |     34.10 |     10.60 |
| AUS         |     22.92 |     19.64 |
+-------------+-----------+-----------+
```

**6. How Would the Loan Report Look?** To generate a report of book loans, showing the client’s name, type of operation, book title, author (with nationality), and how long ago the operation was updated:

```sh
SELECT c.name, o.type, b.title, 
    CONCAT(a.name, ' (', a.nationality, ')') AS author,
    TO_DAYS(NOW()) - TO_DAYS(o.updated_at) AS ago
FROM operations AS o
LEFT JOIN clients AS c
    ON c.client_id = o.client_id
LEFT JOIN books AS b
    ON b.book_id = o.book_id
LEFT JOIN authors AS a
    ON b.author_id = a.author_id
LIMIT 10;

+-------------------+----------+---------------------------------------------------+-------------------------+------+
| name              | type     | title                                             | author                  | ago  |
+-------------------+----------+---------------------------------------------------+-------------------------+------+
| Jodie Foster      | returned | A Farewell to Arms                                | Ernest Hemingway (USA)  |    1 |
| Maggie Gyllenhaal | lent     | Incognito: The Secret Lives of the Brain          | David Eagleman (USA)    |    1 |
| Brie Larson       | lent     | Great Expectations                                | Charles Dickens (GBR)   |    1 |
| Tig Notaro        | returned | How to Create the Future                          | Ashlee Vance (USA)      |    1 |
| Ben Barnes        | sold     | The Analytical Engine and the Future of Computing | Ada Lovelace (GBR)      |    1 |
| Rami Malek        | sold     | Ender's Game                                      | Orson Scott Card (USA)  |    1 |
| Janelle Monáe     | returned | Sapiens: A Brief History of Humankind             | Yuval Noah Harari (ISR) |    1 |
| Daniel Craig      | returned | The Plain in Flames                               | Juan Rulfo (MEX)        |    1 |
| Ryan Reynolds     | lent     | Weapons of Math Destruction                       | Cathy O’Neil (USA)      |    1 |
| Awkwafina         | sold     | The Digital Economy                               | Don Tapscott (CAN)      |    1 |
+-------------------+----------+---------------------------------------------------+-------------------------+------+
10 rows in set (0.00 sec)
```
**7. Extra: Days Calculation** to see the number of days since each client’s birthdate:

```sh
SELECT name, TO_DAYS(birthdate) AS birthdate_days
FROM clients
LIMIT 10;

+--------------------+----------------+
| name               | birthdate_days |
+--------------------+----------------+
| Tom Hanks          |         714604 |
| Scarlett Johansson |         724967 |
| Robert Downey Jr.  |         717795 |
| Jennifer Lawrence  |         727059 |
| Morgan Freeman     |         707626 |
| Emma Watson        |         726937 |
| Ryan Reynolds      |         722015 |
| Natalie Portman    |         723705 |
| Leonardo DiCaprio  |         721303 |
| Marge Simpson      |         714492 |
+--------------------+----------------+
10 rows in set (0.00 sec)
```

## Data Manipulation: UPDATE and DELETE Commands

**1. Selecting Random Records:** To randomly select a subset of authors. **Note:** Using RAND() can impact performance on large datasets:


```sh
SELECT * 
FROM authors 
ORDER BY RAND() 
LIMIT 10;

+-----------+------------------+-------------+
| author_id | name             | nationality |
+-----------+------------------+-------------+
|        50 | Bruce Sterling   | USA         |
|        99 | Richard Dawkins  | GBR         |
|        31 | Ernest Hemingway | USA         |
|        81 | Geoffrey Hinton  | CAN         |
|        11 | Herman Melville  | USA         |
|        30 | James Joyce      | IRL         |
|        22 | Neil Gaiman      | GBR         |
|        69 | Tim Berners-Lee  | GBR         |
|        64 | James Gleick     | USA         |
|        35 | Marcel Proust    | FRA         |
+-----------+------------------+-------------+
10 rows in set (0.00 sec)
```

**2. Deleting Records:** To delete a specific author by `author_id`. **Note:** Do not FORGET to add the `WHERE`clause:


```sh
DELETE FROM authors 
WHERE author_id = 200 
LIMIT 1;
```
**3. Identifying Inactive Clients:** 

```sh
SELECT client_id, name 
FROM clients 
WHERE active <> 1;
```
**4. Updating Records:** Here is the general structure of an `UPDATE` statement, which you can use to modify records in a table:

```sh
UPDATE table_name
SET
    column1 = value1,
    column2 = value2,
    ...
WHERE
    conditions
LIMIT 1;

**Example:** To activate a specific client, you could do the following:

```sh
UPDATE clients
SET
    active = 1
WHERE
    client_id = 123
LIMIT 1;
```

## Advanced SQL Techniques for Querys

In this section, you'll find a series of advanced SQL queries that demonstrate how to extract complex insights from your database. These queries go beyond basic SELECT statements, showcasing the power of SQL for data analysis.

**1. Distinct Nationalities:** Get a list of all distinct nationalities present in the authors table:

```sh
SELECT DISTINCT nationality 
FROM authors;
+-------------+
| nationality |
+-------------+
| USA         |
| GBR         |
| COL         |
| RUS         |
| CAN         |
| IRL         |
| DEU         |
| FRA         |
| PER         |
| CHI         |
| MEX         |
| ARG         |
| CHN         |
| IND         |
| ESP         |
| ISR         |
| AUS         |
+-------------+
17 rows in set (0.01 sec)
```
**2. Total Number of Books:** Count the total number of books:

```sh
SELECT COUNT(book_id) 
FROM books;
+----------------+
| COUNT(book_id) |
+----------------+
|            176 |
+----------------+
1 row in set (0.02 sec)
```
**3. Count and Sum Together:** Count the number of books and sum a constant for each record:

```sh
SELECT COUNT(book_id), SUM(1) 
FROM books;

+----------------+--------+
| COUNT(book_id) | SUM(1) |
+----------------+--------+
|            176 |    176 |
+----------------+--------+
1 row in set (0.00 sec)
```
**4. Sum of Sellable Books:** Calculate the total price of all sellable books:

```sh
SELECT SUM(price) 
FROM books 
WHERE sellable = 1;
+------------+
| SUM(price) |
+------------+
|    5155.15 |
+------------+
1 row in set (0.00 sec)
```
**5. Total Value of Sellable Books with Copies:** Calculate the total value considering the number of copies for each sellable book:

```sh
SELECT SUM(price * copies) 
FROM books 
WHERE sellable = 1;
+---------------------+
| SUM(price * copies) |
+---------------------+
|            37695.60 |
+---------------------+
1 row in set (0.00 sec)
```

**6. Grouping by Sellable Status:** Sum the total value of books grouped by whether they are sellable:

```sh
SELECT sellable, SUM(price * copies) 
FROM books 
GROUP BY sellable;
+----------+---------------------+
| sellable | SUM(price * copies) |
+----------+---------------------+
|        1 |            37695.60 |
+----------+---------------------+
1 row in set (0.01 sec)
```
**7. Books Published Before 1950:** Count the number of books published before 1950:

```sh
SELECT COUNT(book_id), SUM(IF(year < 1950, 1, 0)) AS `<1950` 
FROM books;
+----------------+-------+
| COUNT(book_id) | <1950 |
+----------------+-------+
|            176 |    31 |
+----------------+-------+
1 row in set (0.00 sec)
```

Or alternatively:

```sh
SELECT COUNT(book_id) 
FROM books 
WHERE year < 1950;
+----------------+
| COUNT(book_id) |
+----------------+
|             31 |
+----------------+
1 row in set (0.00 sec)
```
**8. Count books published before and after 1950:** 

```sh
SELECT COUNT(book_id), 
    SUM(IF(year < 1950, 1, 0)) AS `<1950`,
    SUM(IF(year >= 1950, 1, 0)) AS `>1950` 
FROM books;
+----------------+-------+-------+
| COUNT(book_id) | <1950 | >1950 |
+----------------+-------+-------+
|            176 |    31 |   145 |
+----------------+-------+-------+
1 row in set (0.00 sec)
```

**9. Books Published by Decade:** Count books by different time periods:

```sh
SELECT COUNT(book_id), 
    SUM(IF(year < 1950, 1, 0)) AS `<1950`,
    SUM(IF(year >= 1950 AND year < 1990, 1, 0)) AS `<1990`,
    SUM(IF(year >= 1990 AND year < 2000, 1, 0)) AS `<2000`,
    SUM(IF(year >= 2000, 1, 0)) AS `<today`
FROM books;
+----------------+-------+-------+-------+--------+
| COUNT(book_id) | <1950 | <1990 | <2000 | <today |
+----------------+-------+-------+-------+--------+
|            176 |    31 |    43 |    21 |     81 |
+----------------+-------+-------+-------+--------+
1 row in set (0.00 sec)
```

**10. Count books by nationality and time period:** 


```sh
SELECT a.nationality, COUNT(book_id), 
    SUM(IF(year < 1950, 1, 0)) AS `<1950`,
    SUM(IF(year >= 1950 AND year < 1990, 1, 0)) AS `<1990`,
    SUM(IF(year >= 1990 AND year < 2000, 1, 0)) AS `<2000`,
    SUM(IF(year >= 2000, 1, 0)) AS `<today`
FROM books AS b
JOIN authors AS a
    ON a.author_id = b.author_id
WHERE a.nationality IS NOT NULL
GROUP BY a.nationality;
+-------------+----------------+-------+-------+-------+--------+
| nationality | COUNT(book_id) | <1950 | <1990 | <2000 | <today |
+-------------+----------------+-------+-------+-------+--------+
| USA         |             83 |     7 |    20 |     9 |     47 |
| GBR         |             33 |     7 |    11 |     4 |     11 |
| COL         |              1 |     0 |     1 |     0 |      0 |
| RUS         |              2 |     2 |     0 |     0 |      0 |
| IRL         |              2 |     2 |     0 |     0 |      0 |
| DEU         |              4 |     2 |     0 |     0 |      2 |
| FRA         |             10 |    10 |     0 |     0 |      0 |
| PER         |              2 |     0 |     2 |     0 |      0 |
| CHI         |              8 |     1 |     1 |     3 |      3 |
| MEX         |              6 |     0 |     5 |     1 |      0 |
| ARG         |              4 |     0 |     3 |     1 |      0 |
| CHN         |              2 |     0 |     0 |     0 |      2 |
| CAN         |              9 |     0 |     0 |     1 |      8 |
| IND         |              2 |     0 |     0 |     0 |      2 |
| ESP         |              2 |     0 |     0 |     1 |      1 |
| ISR         |              4 |     0 |     0 |     0 |      4 |
| AUS         |              2 |     0 |     0 |     1 |      1 |
+-------------+----------------+-------+-------+-------+--------+
17 rows in set (0.00 sec)
```

## Data Migration

In certain scenarios, you may need to migrate data from one database to another, whether due to a system upgrade, environment change, or the need to back up and restore data.

For exporting data and schemas from a MySQL database, the `mysqldump` tool is commonly used. Below are basic examples of how `mysqldump` can be utilized as part of a data migration process.

**1. Exporting the schema only (without data):**

```sh
mysqldump -u your_username -p -d database_name > schema.sql
```
#### Example:

```sh
mysqldump -u andrewbavuels -p -d holi_operations > squema.sql
```
**2. Exporting both the schema and the data:**

```sh
mysqldump -u your_username -p database_name > database_dump.sql
```
#### Example:

```sh
mysqldump -u andrewbavuels -p holi_operations > holi_books.sql
```

These commands generate `.sql` files containing the necessary instructions to recreate the database structure and, if desired, the data in another MySQL system.

Additionally, you might need to perform certain table modifications during or after the migration process, such as:

#### Adding a column:

```sh
ALTER TABLE authors ADD COLUMN birthyear INTEGER DEFAULT 1930 AFTER name;
```
#### Modifying a column:

```sh
ALTER TABLE authors MODIFY COLUMN birthyear YEAR DEFAULT 1920;
```
#### Dropping a column:

```sh
ALTER TABLE authors DROP COLUMN birthyear;
```

**Note:** A complete data migration may involve additional steps such as transforming and validating data in the new environment.

This section provides a high-level overview of the data migration process, with a focus on how `mysqldump` can be used, making it accessible and clear for anyone reading the READ