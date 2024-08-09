# MySQL Table Creation and Management

This document provides instructions on creating and managing tables in MySQL, including creating databases, tables, and viewing structures and warnings.


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
andrewbavuels@the-Legionnaire:~/sql/2018$ mysql -u andrewbavuels -p
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

mysql> CREATE DATABASE holi_operations;
ERROR 1007 (HY000): Can't create database 'holi_operations'; database exists
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
## Fixing Errors

### 11. Drop author (in singular) Table:

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
### 12. Recreate authors (in plural) Table:

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
### 13. Describing Table Structure:

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
### 14. To get detailed column information:

```sh
mysql> show full columns from books;
```
## Inserting Data into Tables

### Inserting Data into authors:

```sh
INSERT INTO authors (name, nationality)
VALUES
    ('Dave Grohl', 'USA'),
    ('Aldous Huxley', 'GBR'),
    ('Eric Ries', 'USA'),
    ('Gabriel Garcia Marquez', 'COL'),
    ('J.K. Rowling', 'GBR'),
    ('George R.R. Martin', 'USA'),
    ('Stephen King', 'USA'),
    ('Jane Austen', 'GBR'),
    ('Mark Twain', 'USA'),
    ('Leo Tolstoy', 'RUS'),
    ('Fyodor Dostoevsky', 'RUS'),
    ('Herman Melville', 'USA'),
    ('J.R.R. Tolkien', 'GBR'),
    ('Charles Dickens', 'GBR'),
    ('Agatha Christie', 'GBR'),
    ('Isaac Asimov', 'USA'),
    ('Philip K. Dick', 'USA'),
    ('H.P. Lovecraft', 'USA'),
    ('Arthur C. Clarke', 'GBR'),
    ('Orson Scott Card', 'USA'),
    ('Ursula K. Le Guin', 'USA'),
    ('Margaret Atwood', 'CAN'),
    ('Neil Gaiman', 'GBR'),
    ('Douglas Adams', 'GBR'),
    ('Michael Moorcock', 'GBR'),
    ('Anne Rice', 'USA'),
    ('Ray Bradbury', 'USA'),
    ('J.D. Salinger', 'USA'),
    ('John Steinbeck', 'USA'),
    ('Kurt Vonnegut', 'USA'),
    ('James Joyce', 'IRL'),
    ('Ernest Hemingway', 'USA'),
    ('F. Scott Fitzgerald', 'USA'),
    ('Herman Hesse', 'DEU'),
    ('Gustave Flaubert', 'FRA'),
    ('Marcel Proust', 'FRA'),
    ('Albert Camus', 'FRA'),
    ('Victor Hugo', 'FRA'),
    ('Jules Verne', 'FRA'),
    ('Mario Vargas Llosa', 'PER'),
    ('Pablo Neruda', 'CHI'),
    ('Isabel Allende', 'CHI'),
    ('Luis Sepulveda', 'CHI'),
    ('Juan Rulfo', 'MEX'),
    ('Carlos Fuentes', 'MEX'),
    ('Octavio Paz', 'MEX'),
    ('Julio Cortázar', 'ARG'),
    ('Manuel Puig', 'ARG'),
    ('Roberto Bolaño', 'CHI');
```
