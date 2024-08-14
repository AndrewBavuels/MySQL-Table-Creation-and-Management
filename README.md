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
    ('Roberto Bolaño', 'CHI'),
    ('William Gibson', 'USA'),
    ('Bruce Sterling', 'USA'),
    ('Neal Stephenson', 'USA'),
    ('John Brunner', 'GBR'),
    ('Alastair Reynolds', 'GBR'),
    ('Iain M. Banks', 'GBR'),
    ('Liu Cixin', 'CHN'),
    ('Cory Doctorow', 'CAN'),
    ('Ada Lovelace', 'GBR'),
    ('Alan Turing', 'GBR'),
    ('Douglas Rushkoff', 'USA'),
    ('Clay Shirky', 'USA'),
    ('Nicholas Carr', 'USA'),
    ('Shoshana Zuboff', 'USA'),
    ('David Eagleman', 'USA'),
    ('James Gleick', 'USA'),
    ('Michael Lewis', 'USA'),
    ('Eric Schmidt', 'USA'),
    ('Sundar Pichai', 'IND'),
    ('Ashlee Vance', 'USA'),
    ('Tim Berners-Lee', 'GBR'),
    ('Jaron Lanier', 'USA'),
    ('Stewart Brand', 'USA'),
    ('Howard Rheingold', 'USA'),
    ('Manuel Castells', 'ESP'),
    ('Don Tapscott', 'CAN'),
    ('Kevin Kelly', 'USA'),
    ('Ray Kurzweil', 'USA'),
    ('Michio Kaku', 'USA'),
    ('Ralph Merkle', 'USA'),
    ('Gerd Leonhard', 'DEU'),
    ('David Weinberger', 'USA'),
    ('Geoffrey Hinton', 'CAN'),
    ('Andrew Ng', 'USA'),
    ('Yoshua Bengio', 'CAN'),
    ('Demis Hassabis', 'GBR'),
    ('Daniel Kahneman', 'ISR'),
    ('Steven Pinker', 'USA'),
    ('Yuval Noah Harari', 'ISR'),
    ('Daniel Dennett', 'USA'),
    ('David Chalmers', 'AUS'),
    ('Nick Bostrom', 'GBR'),
    ('Nassim Nicholas Taleb', 'USA'),
    ('Judy Wajcman', 'GBR'),
    ('Sherry Turkle', 'USA'),
    ('Angela Saini', 'GBR'),
    ('Cathy O’Neil', 'USA'),
    ('Chris Anderson', 'USA'),
    ('Tom Friedman', 'USA'),
    ('Peter Thiel', 'USA'),
    ('Richard Dawkins', 'GBR');
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
(11, 17, "The Call of Cthulhu", 1928, "en", NULL, 29.75, 1, 5, "A horror novella that introduces the cosmic entity Cthulhu and explores the theme of forbidden knowledge."),
(12, 19, "Ender's Game", 1985, "en", NULL, 49.2, 1, 11, "A science fiction novel about a young boy trained to become a military leader in a future war against alien invaders."),
(13, 24, "Elric of Melnibone", 1972, "en", NULL, 40.7, 1, 6, "The first novel in the Elric series, introducing the anti-hero Elric and his cursed sword Stormbringer."),
(14, 25, "Interview with the Vampire", 1976, "en", NULL, 42.59, 1, 8, "A novel that tells the story of Louis, a vampire recounting his life and experiences to a reporter."),
(15, 26, "Fahrenheit 451", 1953, "en", NULL, 13.58, 1, 10, "A dystopian novel about a future where books are banned and 'firemen' burn any that are found."),
(16, 27, "The Catcher in the Rye", 1951, "en", NULL, 19.53, 1, 11, "A novel about the teenage angst and alienation experienced by Holden Caulfield, a young man in post-war New York City."),
(17, 28, "The Grapes of Wrath", 1939, "en", NULL, 23.81, 1, 7, "A novel about the struggles of an impoverished family during the Great Depression as they migrate west in search of a better life."),
(18, 29, "Slaughterhouse-Five", 1969, "en", NULL, 18.85, 1, 9, "A satirical novel that follows Billy Pilgrim's experiences during World War II and his encounters with time travel and extraterrestrials."),
(19, 30, "Ulysses", 1922, "en", NULL, 18.38, 1, 10, "A modernist novel that parallels Homer's Odyssey through the experiences of Leopold Bloom in Dublin."),
(20, 31, "The Old Man and the Sea", 1952, "en", NULL, 11, 1, 6, "A novella about an aging fisherman who struggles to catch a giant marlin, symbolizing his battle with nature and personal pride."),
(21, 32, "The Great Gatsby", 1925, "en", NULL, 13.7, 1, 8, "A novel about the decadence of the Jazz Age and the disillusionment of the American Dream through the character of Jay Gatsby."),
(22, 33, "Siddhartha", 1922, "de", NULL, 33.73, 1, 7, "A philosophical novel about a man's journey to enlightenment and self-discovery in ancient India."),
(23, 34, "Madame Bovary", 1857, "fr", NULL, 27.22, 1, 8, "A novel about a woman's dissatisfaction with her provincial life and her quest for romantic fulfillment."),
(24, 35, "In Search of Lost Time", 1913, "fr", NULL, 33.75, 1, 10, "A monumental novel exploring memory and social change through the experiences of the narrator, Marcel."),
(25, 36, "The Stranger", 1942, "fr", NULL, 40.9, 1, 7, "A novel about an emotionally detached man who becomes entangled in a murder trial and existential reflections on life and death."),
(26, 37, "Les Misérables", 1862, "fr", NULL, 23.65, 1, 11, "An epic novel about the struggles of various characters in post-revolutionary France and their search for justice and redemption."),
(27, 38, "Twenty Thousand Leagues Under the Sea", 1870, "fr", NULL, 35.5, 1, 8, "A science fiction adventure novel about Captain Nemo and his submarine, the Nautilus, exploring the depths of the ocean."),
(28, 39, "The Time of the Hero", 1963, "es", NULL, 20.55, 1, 6, "A novel about life in a military academy in Peru and the corruption and rebellion that occur among the cadets."),
(29, 40, "Twenty Love Poems and a Song of Despair", 1924, "es", NULL, 28.17, 1, 7, "A collection of passionate and lyrical poems exploring themes of love and loss."),
(30, 41, "The House of the Spirits", 1982, "es", NULL, 29.79, 1, 8, "A novel blending magical realism and historical fiction, chronicling the lives of the Trueba family in Chile."),
(31, 42, "The Old Man Who Read Love Stories", 1992, "es", NULL, 24, 1, 6, "A novel about an elderly man in the Amazon who reads romance novels and contends with the changes brought by modernization."),
(32, 43, "Pedro Páramo", 1955, "es", NULL, 18.25, 1, 7, "A novel about a man's quest to find his father in a ghostly town filled with echoes of the past."),
(33, 44, "The Death of Artemio Cruz", 1962, "es", NULL, 35.05, 1, 8, "A novel exploring Mexican history and politics through the reflections of a dying man."),
(34, 45, "The Labyrinth of Solitude", 1950, "es", NULL, 38.9, 1, 7, "A collection of essays reflecting on Mexican identity and culture."),
(35, 46, "Hopscotch", 1963, "es", NULL, 30.44, 1, 6, "A novel known for its experimental narrative structure and exploration of existential themes."),
(36, 47, "Kiss of the Spider Woman", 1976, "es", NULL, 18.88, 1, 7, "A novel set in an Argentine prison, focusing on the relationship between two men who bond over stories of film and love."),
(37, 48, "2666", 2004, "es", NULL, 29.35, 1, 9, "A sprawling novel that interweaves various stories and characters connected to the mysterious disappearance of a writer."),
(38, 49, "Neuromancer", 1984, "en", NULL, 27.97, 1, 10, "A cyberpunk novel that follows a washed-up computer hacker hired for one last job in a dystopian future."),
(39, 50, "Islands in the Net", 1988, "en", NULL, 14.78, 1, 6, "A novel set in a future of high-tech crime and corporate intrigue, focusing on the battle over control of information."),
(40, 51, "Snow Crash", 1992, "en", NULL, 18.24, 1, 8, "A novel that combines cyberpunk and satire, following a pizza delivery driver who uncovers a dangerous virtual drug."),
(41, 52, "Stand on Zanzibar", 1968, "en", NULL, 31.61, 1, 7, "A science fiction novel that explores overpopulation and social change through multiple perspectives."),
(42, 53, "Revelation Space", 2000, "en", NULL, 27.07, 1, 6, "A space opera that follows a crew investigating a mysterious alien artifact and the consequences of their discoveries."),
(43, 54, "Consider Phlebas", 1987, "en", NULL, 25.94, 1, 7, "The first book in the Culture series, focusing on a mercenary's adventures in a conflict between two civilizations."),
(44, 55, "The Three-Body Problem", 2008, "zh", NULL, 20.7, 1, 9, "A science fiction novel about first contact with an alien civilization and the consequences for humanity."),
(45, 56, "Little Brother", 2008, "en", NULL, 19.44, 1, 6, "A novel about a teenager's fight against government surveillance and authoritarianism in a near-future dystopia."),
(46, 57, "Notes by Ada Lovelace on the Analytical Engine", 1843, "en", NULL, 45.4, 1, 5, "A collection of notes and annotations by Ada Lovelace on Charles Babbage's early mechanical computer, the Analytical Engine."),
(47, 58, "Computing Machinery and Intelligence", 1950, "en", NULL, 49.87, 1, 6, "An influential paper by Alan Turing discussing the concept of artificial intelligence and the Turing Test."),
(48, 59, "Present Shock", 2013, "en", NULL, 12.5, 1, 7, "A book examining the effects of living in a constantly connected, instant-gratification culture."),
(49, 60, "Here Comes Everybody", 2008, "en", NULL, 10.27, 1, 8, "A book about the impact of social media on communication and organizing in the digital age."),
(50, 61, "The Shallows", 2010, "en", NULL, 35.8, 1, 7, "A book exploring how the internet is affecting our cognitive processes and attention spans."),
(51, 62, "The Age of Surveillance Capitalism", 2019, "en", NULL, 47.36, 1, 9, "A critical analysis of how major tech companies exploit personal data for profit."),
(52, 63, "Incognito: The Secret Lives of the Brain", 2011, "en", NULL, 42.94, 1, 6, "A book exploring the mysteries of the subconscious mind and how it shapes our behavior."),
(53, 64, "The Information", 2011, "en", NULL, 19.34, 1, 7, "A history of information technology and its impact on human society."),
(54, 65, "The Big Short", 2010, "en", NULL, 35.81, 1, 8, "A non-fiction book about the events leading up to the 2008 financial crisis and the individuals who predicted it."),
(55, 66, "How Google Works", 2014, "en", NULL, 39.39, 1, 6, "A book offering insights into the strategies and culture behind Google's success."),
(56, 67, "The Making of a Leader", 2022, "en", NULL, 29.12, 1, 7, "A memoir by Sundar Pichai detailing his journey from India to becoming CEO of Google."),
(57, 68, "Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future", 2015, "en", NULL, 20.9, 1, 9, "A biography of Elon Musk, exploring his ventures and impact on technology and space exploration."),
(58, 69, "Weaving the Web", 1999, "en", NULL, 16.27, 1, 6, "A book by the inventor of the World Wide Web detailing its creation and future."),
(59, 70, "You Are Not a Gadget", 2010, "en", NULL, 12.58, 1, 7, "A critique of the digital age and its impact on individuality and creativity."),
(60, 71, "How Buildings Learn", 1994, "en", NULL, 48, 1, 6, "A book about the evolution of buildings and the concept of design that accommodates change."),
(61, 72, "The Virtual Community", 1993, "en", NULL, 41.01, 1, 7, "A book exploring online communities and their impact on human interaction and society."),
(62, 73, "The Rise of the Network Society", 1996, "es", NULL, 35.05, 1, 8, "A sociological study of how networked technologies are transforming society and the economy."),
(63, 74, "Blockchain Revolution", 2016, "en", NULL, 35.12, 1, 6, "A book about how blockchain technology is changing business and society."),
(64, 75, "What Technology Wants", 2010, "en", NULL, 20.94, 1, 7, "A book exploring the future of technology and its role in shaping human evolution."),
(65, 76, "The Singularity Is Near", 2005, "en", NULL, 41.29, 1, 9, "A book predicting the future of technological advancements and their potential impact on humanity."),
(66, 77, "The Future of the Mind", 2014, "en", NULL, 37.93, 1, 7, "A book exploring the possibilities of brain-computer interfaces and the future of human consciousness."),
(67, 78, "The Age of Nanotechnology", 2000, "en", NULL, 23.49, 1, 5, "A book about the potential and implications of nanotechnology in various fields."),
(68, 79, "Technology vs. Humanity", 2016, "de", NULL, 31.14, 1, 6, "A book examining the impact of technology on human values and the future of humanity."),
(69, 80, "Too Big to Know", 2011, "en", NULL, 25.15, 1, 7, "A book about how the internet is changing our understanding of knowledge and information."),
(70, 81, "Neural Networks for Machine Learning", 2012, "en", NULL, 11.13, 1, 8, "A comprehensive guide to neural networks and their applications in machine learning."),
(71, 82, "Machine Learning Yearning", 2018, "en", NULL, 19.59, 1, 7, "A book providing practical advice for building machine learning systems."),
(72, 83, "Deep Learning", 2016, "en", NULL, 10.32, 1, 9, "A foundational text on deep learning, written by leading experts in the field."),
(73, 84, "AlphaGo and the Future of Artificial Intelligence", 2018, "en", NULL, 15.75, 1, 6, "A book discussing the development of AlphaGo and its implications for the future of AI."),
(74, 85, "Thinking, Fast and Slow", 2011, "he", NULL, 10.6, 1, 8, "A groundbreaking book on human decision-making and cognitive biases."),
(75, 86, "Enlightenment Now", 2018, "en", NULL, 39.47, 1, 7, "A book advocating for the benefits of Enlightenment values and progress in human societies."),
(76, 87, "Sapiens: A Brief History of Humankind", 2011, "he", NULL, 34.1, 1, 9, "A sweeping history of the human species from the emergence of Homo sapiens to the present."),
(77, 88, "Consciousness Explained", 1991, "en", NULL, 21.21, 1, 6, "A book offering a theory of consciousness and the nature of subjective experience."),
(78, 89, "The Conscious Mind", 1996, "en", NULL, 22.92, 1, 7, "A philosophical exploration of the nature of consciousness and the 'hard problem' of subjective experience."),
(79, 90, "Superintelligence", 2014, "en", NULL, 25.89, 1, 8, "A book exploring the potential risks and benefits of advanced artificial intelligence."),
(80, 91, "The Black Swan", 2007, "en", NULL, 30.07, 1, 9, "A book about the impact of rare and unpredictable events on our lives and decision-making."),
(81, 92, "Pressed for Time", 2015, "en", NULL, 44.45, 1, 7, "A book examining how technological advancements affect our perception of time and work."),
(82, 93, "Alone Together", 2011, "en", NULL, 19.22, 1, 6, "A book exploring the impact of technology on human relationships and social interactions."),
(83, 94, "Inferior", 2017, "en", NULL, 12.25, 1, 7, "A book challenging myths about gender differences and highlighting the impact of scientific research on gender equality."),
(84, 95, "Weapons of Math Destruction", 2016, "en", NULL, 44.71, 1, 8, "A book examining how big data and algorithms can perpetuate inequality and injustice."),
(85, 96, "The Long Tail", 2006, "en", NULL, 46.74, 1, 7, "A book about how the internet and digital technology are changing the economics of supply and demand."),
(86, 97, "The World is Flat", 2005, "en", NULL, 29.16, 1, 6, "A book discussing globalization and the ways in which technology has leveled the playing field for businesses and individuals."),
(87, 98, "Zero to One", 2014, "en", NULL, 36.9, 1, 8, "A book about innovation and creating startups that build new technologies and markets."),
(88, 99, "The Selfish Gene", 1976, "en", NULL, 14.16, 1, 7, "A book presenting the gene-centered view of evolution and the concept of 'selfish' genes."),
(89, 22, "Neverwhere", 1996, "en", NULL, 38.51, 1, 7, "A novel about a man who discovers a hidden, magical world beneath London after helping a mysterious girl."),
(90, 20, "The Dispossessed", 1974, "en", NULL, 43.26, 1, 8, "A science fiction novel exploring anarchist and capitalist societies through the life of a physicist from an isolated planet."),
(91, 16, "A Scanner Darkly", 1977, "en", NULL, 34.39, 1, 6, "A dystopian novel about a drug-enforced surveillance society and the blurred lines between reality and identity."),
(92, 15, "I, Robot", 1950, "en", NULL, 23.16, 1, 7, "A collection of interconnected short stories about robots and the ethical dilemmas of artificial intelligence."),
(93, 18, "Childhood's End", 1953, "en", NULL, 35.53, 1, 9, "A science fiction novel about the peaceful alien invasion of Earth and the subsequent evolution of humanity."),
(94, 19, "Speaker for the Dead", 1986, "en", NULL, 33.69, 1, 8, "The second book in the Ender's Game series, exploring themes of xenology and the complexities of interspecies communication."),
(95, 21, "Oryx and Crake", 2003, "en", NULL, 20.19, 1, 7, "A dystopian novel set in a future where genetic engineering has led to ecological collapse and social upheaval."),
(96, 23, "Dirk Gently's Holistic Detective Agency", 1987, "en", NULL, 38.65, 1, 6, "A comedic novel featuring a detective who solves cases based on a holistic view of interconnectedness."),
(97, 24, "The Eternal Champion", 1970, "en", NULL, 40.74, 1, 7, "A novel introducing the concept of the Eternal Champion, a recurring hero across multiple fantasy and science fiction settings."),
(98, 25, "The Vampire Lestat", 1985, "en", NULL, 24.49, 1, 8, "The second book in The Vampire Chronicles series, focusing on the life and adventures of the vampire Lestat."),
(99, 26, "Something Wicked This Way Comes", 1962, "en", NULL, 12.03, 1, 6, "A horror novel about two boys who encounter a sinister traveling carnival with dark intentions."),
(100, 27, "Franny and Zooey", 1961, "en", NULL, 28.68, 1, 7, "A novel consisting of two connected stories about the Glass family and their philosophical and existential struggles."),
(101, 28, "Of Mice and Men", 1937, "en", NULL, 44.54, 1, 8, "A novella about two displaced migrant ranch workers during the Great Depression and their dreams of a better future."),
(102, 29, "Cat's Cradle", 1963, "en", NULL, 37.18, 1, 6, "A satirical novel about the creation of a substance that can destroy the world and the absurdities of human behavior."),
(103, 30, "Dubliners", 1914, "en", NULL, 16.03, 1, 7, "A collection of short stories capturing the everyday life and struggles of Dubliners in the early 20th century."),
(104, 31, "A Farewell to Arms", 1929, "en", NULL, 30.84, 1, 8, "A novel about the love affair between an American ambulance driver and a British nurse during World War I."),
(105, 32, "Tender Is the Night", 1934, "en", NULL, 48.76, 1, 6, "A novel about the lives of a glamorous couple and their disintegration amidst personal and financial troubles."),
(106, 33, "Steppenwolf", 1927, "de", NULL, 49.09, 1, 8, "A novel exploring the dual nature of the protagonist's psyche and his quest for self-understanding and transformation."),
(107, 34, "Bouvard et Pécuchet", 1881, "fr", NULL, 32.75, 1, 7, "A satirical novel about two clerks who attempt to master various professions and end up failing comically."),
(108, 35, "Swann's Way", 1913, "fr", NULL, 41.42, 1, 7, "The first volume of In Search of Lost Time, focusing on the narrator's reflections on love and memory."),
(109, 36, "The Myth of Sisyphus", 1942, "fr", NULL, 13.32, 1, 6, "A philosophical essay exploring the concept of the absurd and the human condition."),
(110, 37, "The Hunchback of Notre-Dame", 1831, "fr", NULL, 22.32, 1, 8, "A novel about the tragic love story of the hunchback Quasimodo and the beautiful gypsy Esmeralda."),
(111, 38, "Journey to the Center of the Earth", 1864, "fr", NULL, 28.48, 1, 7, "A science fiction adventure about an expedition to the Earth's core and the strange discoveries made along the way."),
(112, 39, "Conversation in the Cathedral", 1969, "es", NULL, 19.85, 1, 6, "A novel that delves into the corruption and political turmoil of 20th-century Peru through a conversation between two men."),
(113, 40, "The Book of Questions", 1991, "es", NULL, 19.52, 1, 7, "A poetic exploration of life's profound questions and existential themes through a series of poetic inquiries."),
(114, 41, "The Japanese Lover", 2015, "es", NULL, 31.88, 1, 8, "A novel that interweaves the stories of a Jewish woman and her secret Japanese lover during World War II."),
(115, 42, "The Shadow of What We Were", 2019, "es", NULL, 46.63, 1, 6, "A novel about the political and personal consequences of dictatorship in Chile."),
(116, 43, "The Plain in Flames", 1963, "es", NULL, 46.84, 1, 7, "A collection of short stories capturing the harsh realities and mystical elements of rural Mexico."),
(117, 44, "Aura", 1962, "es", NULL, 15.78, 1, 8, "A novella about a young man's mysterious encounter with an elderly woman and her enigmatic niece."),
(118, 45, "In Light of India", 1995, "es", NULL, 20.32, 1, 6, "A collection of essays reflecting on the cultural and political landscape of India."),
(119, 46, "Blow-Up and Other Stories", 1962, "es", NULL, 21.81, 1, 7, "A collection of short stories blending the fantastical and the ordinary in innovative narrative forms."),
(120, 47, "The Buenos Aires Affair", 1998, "es", NULL, 44.45, 1, 7, "A novel featuring a complex narrative about political intrigue and personal relationships in Argentina."),
(121, 48, "The Savage Detectives", 1998, "es", NULL, 15.74, 1, 8, "A novel following the lives of two poets and their quest for a mysterious figure in the literary world."),
(122, 49, "Count Zero", 1986, "en", NULL, 36.48, 1, 7, "A sequel to Neuromancer, continuing the exploration of cyberspace and corporate espionage."),
(123, 50, "Schismatrix", 1985, "en", NULL, 15.69, 1, 6, "A science fiction novel about the conflicts between post-human factions and their visions of future evolution."),
(124, 51, "The Diamond Age", 1995, "en", NULL, 13.28, 1, 7, "A novel set in a nanotech future, focusing on a young girl's journey and her interaction with advanced technology."),
(125, 52, "The Shockwave Rider", 1975, "en", NULL, 41.25, 1, 6, "A novel exploring themes of surveillance and resistance in a dystopian future controlled by powerful corporations."),
(126, 53, "House of Suns", 2008, "en", NULL, 18.19, 1, 7, "A space opera featuring a group of post-human entities traveling through the galaxy in search of lost civilizations."),
(127, 54, "The Player of Games", 1988, "en", NULL, 43.66, 1, 6, "The second book in the Culture series, focusing on a game player who becomes embroiled in interstellar politics."),
(128, 55, "The Dark Forest", 2008, "zh", NULL, 44.16, 1, 8, "The sequel to The Three-Body Problem, continuing the story of humanity's struggle with an alien threat."),
(129, 56, "Homeland", 2013, "en", NULL, 36.75, 1, 7, "A sequel to Little Brother, dealing with themes of surveillance and personal freedom in a digital age."),
(130, 57, "The Analytical Engine and the Future of Computing", 1844, "en", NULL, 25.75, 1, 5, "A collection of Ada Lovelace's writings on Charles Babbage's Analytical Engine and its potential."),
(131, 58, "On Computable Numbers", 1936, "en", NULL, 36.12, 1, 6, "A groundbreaking paper by Alan Turing establishing the foundations of computation and the concept of a Turing machine."),
(132, 59, "Throwing Rocks at the Google Bus", 2016, "en", NULL, 19.97, 1, 7, "A critique of the economic impact of digital technology and the need for a more equitable digital economy."),
(133, 60, "Cognitive Surplus", 2010, "en", NULL, 42.08, 1, 8, "A book examining how the internet has transformed leisure time into productive and collaborative activities."),
(134, 61, "The Glass Cage", 2014, "en", NULL, 33.4, 1, 7, "A book exploring the effects of automation on human skills and cognition."),
(135, 62, "The Digital Person", 2006, "en", NULL, 29.52, 1, 6, "A book analyzing the impact of digital technology on privacy and personal identity."),
(136, 63, "Livewired: The Inside Story of the Ever-Changing Brain", 2020, "en", NULL, 41.45, 1, 7, "A book about the brain's adaptability and its ability to rewire itself in response to new experiences."),
(137, 64, "Chaos: Making a New Science", 1987, "en", NULL, 49.98, 1, 8, "A book introducing the concept of chaos theory and its implications for understanding complex systems."),
(138, 65, "Moneyball", 2003, "en", NULL, 17.42, 1, 7, "A non-fiction book about the use of statistical analysis in baseball to build a competitive team."),
(139, 66, "The New Digital Age", 2013, "en", NULL, 35.18, 1, 6, "A book discussing the impact of digital technology on society and the future of the internet."),
(140, 67, "Innovation and Leadership", 2023, "en", NULL, 46.31, 1, 7, "A book exploring the principles of innovation and leadership in the tech industry."),
(141, 68, "How to Create the Future", 2019, "en", NULL, 18.04, 1, 8, "A book about the strategies and vision of leading tech innovators shaping the future."),
(142, 69, "The Web We Want", 2018, "en", NULL, 16.28, 1, 6, "A book advocating for the open web and addressing the challenges facing the future of the internet."),
(143, 70, "Dawn of the New Everything", 2017, "en", NULL, 12.43, 1, 7, "A memoir and reflection on virtual reality and its impact on technology and society."),
(144, 71, "The Clock of the Long Now", 1999, "en", NULL, 40.33, 1, 6, "A book about the creation of a clock designed to last 10,000 years and its implications for long-term thinking."),
(145, 72, "Smart Mobs", 2002, "en", NULL, 19.02, 1, 7, "A book about the rise of collective intelligence and how new technologies enable smart mobs to collaborate and act."),
(146, 73, "Communication Power", 2009, "es", NULL, 24.08, 1, 8, "A study of the role of communication in power dynamics and its impact on modern societies."),
(147, 74, "The Digital Economy", 1995, "en", NULL, 25.77, 1, 7, "A book analyzing the transformative impact of digital technology on business and economic practices."),
(148, 75, "The Inevitable", 2016, "en", NULL, 19.52, 1, 6, "A book about the twelve technological forces shaping our future and their implications for society."),
(149, 76, "How to Create a Mind", 2012, "en", NULL, 38, 1, 7, "A book exploring the workings of the human brain and how to replicate its processes in artificial intelligence."),
(150, 77, "Parallel Worlds", 2004, "en", NULL, 39.67, 1, 6, "A book about the possibility of parallel universes and their implications for our understanding of the cosmos."),
(151, 78, "The Molecular Repair of the Brain", 2005, "en", NULL, 22.27, 1, 5, "A book exploring the potential for molecular nanotechnology to repair and enhance brain functions."),
(152, 79, "The Future of Work", 2019, "de", NULL, 23.67, 1, 7, "A book examining how emerging technologies will shape the future of work and employment."),
(153, 80, "The Internet Is Not the Answer", 2015, "en", NULL, 27.54, 1, 8, "A book critiquing the idealized view of the internet and its impact on society and democracy."),
(154, 81, "Deep Learning for Computer Vision", 2018, "en", NULL, 44.82, 1, 7, "A practical guide to applying deep learning techniques to computer vision tasks."),
(155, 82, "Deep Learning Specialization", 2020, "en", NULL, 42.16, 1, 7, "A comprehensive guide to deep learning techniques and applications, based on Ng's popular online courses."),
(156, 83, "Artificial Intelligence: A Modern Approach", 2020, "en", NULL, 12.17, 1, 9, "A textbook providing a thorough overview of modern AI techniques and research."),
(157, 84, "AI: The Future of Intelligence", 2021, "en", NULL, 41.12, 1, 6, "A book discussing the potential future developments in artificial intelligence and their societal impact."),
(158, 85, "Noise: A Flaw in Human Judgment", 2021, "he", NULL, 32.21, 1, 8, "A book exploring how variability in human judgment affects decision-making and ways to mitigate it."),
(159, 86, "The Better Angels of Our Nature", 2011, "en", NULL, 20.61, 1, 7, "A book arguing that violence has been decreasing over time and that human societies are becoming more peaceful."),
(160, 87, "Homo Deus: A Brief History of Tomorrow", 2015, "he", NULL, 27.51, 1, 9, "A speculative look at the future of humanity and the potential directions for technological and societal evolution."),
(161, 88, "Darwin's Dangerous Idea", 1995, "en", NULL, 10.59, 1, 6, "A book exploring the far-reaching implications of Darwinian evolution on philosophy and science."),
(162, 89, "The Character of Consciousness", 2010, "en", NULL, 19.64, 1, 7, "A collection of essays examining the nature of consciousness and the 'hard problem' from various philosophical perspectives."),
(163, 90, "Global Catastrophic Risks", 2013, "en", NULL, 48.36, 1, 8, "A book analyzing the potential risks that could threaten the future of humanity and strategies for mitigating them."),
(164, 91, "Antifragile", 2012, "en", NULL, 31.61, 1, 7, "A book about how systems and entities can benefit from disorder and stress, becoming stronger in the process."),
(165, 92, "The Technology of Utopia", 2019, "en", NULL, 44.6, 1, 6, "A book exploring the role of technology in shaping utopian and dystopian visions of society."),
(166, 93, "Reclaiming Conversation", 2015, "en", NULL, 45.55, 1, 7, "A book about the importance of face-to-face conversation and how digital communication affects our interactions."),
(167, 94, "Superior", 2019, "en", NULL, 33.89, 1, 8, "A book challenging the myths of racial superiority and examining the science behind human diversity."),
(168, 95, "The Problem with Math Is Me", 2016, "en", NULL, 49.72, 1, 7, "A book discussing how mathematical models can perpetuate inequality and the need for ethical considerations in data science."),
(169, 96, "Free", 2009, "en", NULL, 10.21, 1, 8, "A book about the impact of free and open-source content on the economy and business models."),
(170, 97, "Thank You for Being Late", 2016, "en", NULL, 18.34, 1, 6, "A book exploring the intersection of technology, globalization, and climate change and its implications for the future."),
(171, 98, "The Diversity Myth", 1995, "en", NULL, 33.56, 1, 7, "A critique of the political correctness and diversity policies in higher education and their impact on academic freedom."),
(172, 99, "Climbing Mount Improbable", 1996, "en", NULL, 35.51, 1, 7, "A book about the gradual process of evolution and how complex biological features emerge over time."),
(173, 7, "It", 1986, "en", NULL, 16.91, 1, 6, "A horror novel about a group of friends confronting a malevolent entity that preys on children in their small town."),
(174, 8, "Emma", 1815, "en", NULL, 15.58, 1, 7, "A novel about a young woman’s matchmaking efforts and her eventual self-discovery and growth."),
(175, 6, "A Clash of Kings", 1998, "en", NULL, 18.79, 1, 7, "The second book in A Song of Ice and Fire series, continuing the epic saga of political intrigue and warfare in the Seven Kingdoms."),
(176, 12, "The Silmarillion", 1977, "en", NULL, 31.37, 1, 8, "A collection of mythopoeic stories providing the background and history of Middle-earth before The Hobbit and The Lord of the Rings.");
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
('Leonardo da Vinci', 'leonardo.da.vinci@example.com', '1452-04-15', 'M', 1),
('Jennifer Garner', 'jennifer.garner@example.com', '1972-04-17', 'F', 1),
('Keanu Reeves', 'keanu.reeves@example.com', '1964-09-02', 'M', 1),
('Meryl Streep', 'meryl.streep@example.com', '1949-06-22', 'F', 1),
('Brad Pitt', 'brad.pitt@example.com', '1963-12-18', 'M', 1),
('Angelina Jolie', 'angelina.jolie@example.com', '1975-06-04', 'F', 1),
('Will Smith', 'will.smith@example.com', '1968-09-25', 'M', 1),
('Hugh Jackman', 'hugh.jackman@example.com', '1968-10-12', 'M', 1),
('Julia Roberts', 'julia.roberts@example.com', '1967-10-28', 'F', 1),
('Johnny Depp', 'johnny.depp@example.com', '1963-06-09', 'M', 1),
('Charlize Theron', 'charlize.theron@example.com', '1975-08-07', 'F', 1),
('Tom Cruise', 'tom.cruise@example.com', '1962-07-03', 'M', 1),
('Harrison Ford', 'harrison.ford@example.com', '1942-07-13', 'M', 1),
('Cate Blanchett', 'cate.blanchett@example.com', '1969-05-14', 'F', 1),
('Denzel Washington', 'denzel.washington@example.com', '1954-12-28', 'M', 1),
('Jessica Chastain', 'jessica.chastain@example.com', '1977-03-24', 'F', 1),
('Ryan Gosling', 'ryan.gosling@example.com', '1980-11-12', 'M', 1),
('Saoirse Ronan', 'saoirse.ronan@example.com', '1994-04-12', 'F', 1),
('Chris Hemsworth', 'chris.hemsworth@example.com', '1983-08-11', 'M', 1),
('Natalie Dormer', 'natalie.dormer@example.com', '1982-02-11', 'F', 1),
('Matthew McConaughey', 'matthew.mcconaughey@example.com', '1969-11-04', 'M', 1),
('Naomi Watts', 'naomi.watts@example.com', '1968-09-28', 'F', 1),
('Daisy Ridley', 'daisy.ridley@example.com', '1992-04-10', 'F', 1),
('Chris Evans', 'chris.evans@example.com', '1981-06-13', 'M', 1),
('Tessa Thompson', 'tessa.thompson@example.com', '1983-10-03', 'F', 1),
('Paul Rudd', 'paul.rudd@example.com', '1969-04-06', 'M', 1),
('Zendaya', 'zendaya@example.com', '1996-09-01', 'F', 1),
('John Boyega', 'john.boyega@example.com', '1992-03-17', 'M', 1),
('Ana de Armas', 'ana.de.armas@example.com', '1988-04-30', 'F', 1),
('Mads Mikkelsen', 'mads.mikkelsen@example.com', '1965-11-22', 'M', 1),
('Michelle Yeoh', 'michelle.yeoh@example.com', '1962-08-06', 'F', 1),
('Daniel Craig', 'daniel.craig@example.com', '1968-03-02', 'M', 1),
('Emma Stone', 'emma.stone@example.com', '1988-11-06', 'F', 1),
('James Franco', 'james.franco@example.com', '1978-04-19', 'M', 1),
('Mila Kunis', 'mila.kunis@example.com', '1983-08-14', 'F', 1),
('Ben Affleck', 'ben.affleck@example.com', '1972-08-15', 'M', 1),
('Sienna Miller', 'sienna.miller@example.com', '1981-12-28', 'F', 1),
('Jake Gyllenhaal', 'jake.gyllenhaal@example.com', '1980-12-19', 'M', 1),
('Eiza González', 'eiza.gonzalez@example.com', '1990-01-30', 'F', 1),
('Rami Malek', 'rami.malek@example.com', '1981-05-12', 'M', 1),
('Kerry Washington', 'kerry.washington@example.com', '1977-01-31', 'F', 1),
('David Oyelowo', 'david.oyelowo@example.com', '1976-04-01', 'M', 1),
('John Legend', 'john.legend@example.com', '1978-12-28', 'M', 1),
('Priyanka Chopra', 'priyanka.chopra@example.com', '1982-07-18', 'F', 1),
('Jason Momoa', 'jason.momoa@example.com', '1979-08-01', 'M', 1),
('Alison Brie', 'alison.brie@example.com', '1982-12-29', 'F', 1),
('Maya Rudolph', 'maya.rudolph@example.com', '1972-07-27', 'F', 1),
('Zoe Saldana', 'zoe.saldana@example.com', '1978-06-19', 'F', 1),
('Matthew Fox', 'matthew.fox@example.com', '1966-07-14', 'M', 1),
('Sophie Turner', 'sophie.turner@example.com', '1996-02-21', 'F', 1),
('Lena Headey', 'lena.headey@example.com', '1973-10-03', 'F', 1),
('Clive Owen', 'clive.owen@example.com', '1964-10-03', 'M', 1),
('Jodie Comer', 'jodie.comer@example.com', '1993-03-11', 'F', 1),
('David Tennant', 'david.tennant@example.com', '1971-04-18', 'M', 1),
('Ruth Wilson', 'ruth.wilson@example.com', '1982-01-13', 'F', 1),
('Jude Law', 'jude.law@example.com', '1972-12-29', 'M', 1),
('Rachel Weisz', 'rachel.weisz@example.com', '1970-03-07', 'F', 1),
('Hugh Grant', 'hugh.grant@example.com', '1960-09-09', 'M', 1),
('Imelda Staunton', 'imelda.staunton@example.com', '1956-01-09', 'F', 1),
('Tilda Swinton', 'tilda.swinton@example.com', '1960-11-05', 'F', 1),
('Mark Ruffalo', 'mark.ruffalo@example.com', '1967-11-22', 'M', 1),
('Josh Brolin', 'josh.brolin@example.com', '1968-02-12', 'M', 1),
('Christina Hendricks', 'christina.hendricks@example.com', '1975-05-03', 'F', 1),
('Steve Carell', 'steve.carell@example.com', '1962-08-16', 'M', 1),
('Jason Bateman', 'jason.bateman@example.com', '1969-01-14', 'M', 1),
('Anna Kendrick', 'anna.kendrick@example.com', '1985-08-09', 'F', 1),
('Bill Hader', 'bill.hader@example.com', '1978-06-07', 'M', 1),
('Mindy Kaling', 'mindy.kaling@example.com', '1979-06-24', 'F', 1),
('Aziz Ansari', 'aziz.ansari@example.com', '1983-02-23', 'M', 1),
('Parker Posey', 'parker.posey@example.com', '1968-11-08', 'F', 1),
('Kumail Nanjiani', 'kumail.nanjiani@example.com', '1978-02-21', 'M', 1),
('Leslie Mann', 'leslie.mann@example.com', '1972-03-26', 'F', 1),
('Adam Driver', 'adam.driver@example.com', '1983-11-19', 'M', 1),
('John C. Reilly', 'john.c.reilly@example.com', '1965-05-24', 'M', 1),
('Connie Britton', 'connie.britton@example.com', '1967-03-06', 'F', 1),
('Gina Rodriguez', 'gina.rodriguez@example.com', '1984-07-30', 'F', 1),
('Janelle Monáe', 'janelle.monae@example.com', '1985-12-01', 'F', 1),
('Jon Bernthal', 'jon.bernthal@example.com', '1976-09-20', 'M', 1),
('Ricky Martin', 'ricky.martin@example.com', '1971-12-24', 'M', 1),
('Gisele Bündchen', 'gisele.bundchen@example.com', '1980-07-20', 'F', 1),
('Ben Barnes', 'ben.barnes@example.com', '1981-08-20', 'M', 1),
('Florence Pugh', 'florence.pugh@example.com', '1996-01-03', 'F', 1),
('Henry Cavill', 'henry.cavill@example.com', '1983-05-05', 'M', 1),
('Elizabeth Debicki', 'elizabeth.debicki@example.com', '1990-08-24', 'F', 1),
('Brie Larson', 'brie.larson@example.com', '1989-10-01', 'F', 1),
('Jodie Foster', 'jodie.foster@example.com', '1962-11-19', 'F', 1),
('Daniel Radcliffe', 'daniel.radcliffe@example.com', '1989-07-23', 'M', 1),
('Viggo Mortensen', 'viggo.mortensen@example.com', '1958-10-20', 'M', 1),
('Taron Egerton', 'taron.egerton@example.com', '1989-11-10', 'M', 1),
('Dylan O’Brien', 'dylan.obrien@example.com', '1991-08-26', 'M', 1),
('Shailene Woodley', 'shailene.woodley@example.com', '1991-11-15', 'F', 1),
('Josh Hutcherson', 'josh.hutcherson@example.com', '1992-10-12', 'M', 1),
('Lily Collins', 'lily.collins@example.com', '1989-03-18', 'F', 1),
('Anya Taylor-Joy', 'anya.taylor-joy@example.com', '1996-04-16', 'F', 1),
('Logan Lerman', 'logan.lerman@example.com', '1992-01-19', 'M', 1),
('Emma Roberts', 'emma.roberts@example.com', '1991-02-10', 'F', 1),
('Michael B. Jordan', 'michael.b.jordan@example.com', '1987-02-09', 'M', 1),
('Alicia Vikander', 'alicia.vikander@example.com', '1988-10-03', 'F', 1),
('James McAvoy', 'james.mcavoy@example.com', '1979-04-21', 'M', 1),
('Rachel McAdams', 'rachel.mcadams@example.com', '1978-11-17', 'F', 1),
('Gerard Butler', 'gerard.butler@example.com', '1969-11-13', 'M', 1),
('Rose Byrne', 'rose.byrne@example.com', '1979-07-24', 'F', 1),
('Maggie Gyllenhaal', 'maggie.gyllenhaal@example.com', '1977-10-16', 'F', 1),
('Jason Sudeikis', 'jason.sudeikis@example.com', '1975-09-18', 'M', 1),
('Kate Winslet', 'kate.winslet@example.com', '1975-10-05', 'F', 1),
('Chris Pratt', 'chris.pratt@example.com', '1979-06-21', 'M', 1),
('Olivia Wilde', 'olivia.wilde@example.com', '1984-03-10', 'F', 1),
('Jenna Ortega', 'jenna.ortega@example.com', '2002-09-27', 'F', 1),
('Henry Golding', 'henry.golding@example.com', '1987-02-05', 'M', 1),
('Gemma Chan', 'gemma.chan@example.com', '1982-11-29', 'F', 1),
('Simu Liu', 'simu.liu@example.com', '1989-04-19', 'M', 1),
('Awkwafina', 'awkwafina@example.com', '1988-06-02', 'F', 1),
('Keegan-Michael Key', 'keegan-michael.key@example.com', '1971-03-22', 'M', 1),
('Kenan Thompson', 'kenan.thompson@example.com', '1978-05-10', 'M', 1),
('Nick Kroll', 'nick.kroll@example.com', '1978-06-05', 'M', 1),
('Tiffany Haddish', 'tiffany.haddish@example.com', '1979-12-03', 'F', 1),
('Aubrey Plaza', 'aubrey.plaza@example.com', '1984-06-26', 'F', 1),
('Riki Lindhome', 'riki.lindhome@example.com', '1979-03-05', 'F', 1),
('David Cross', 'david.cross@example.com', '1964-04-04', 'M', 1),
('Paul Scheer', 'paul.scheer@example.com', '1976-01-31', 'M', 1),
('Tig Notaro', 'tig.notaro@example.com', '1971-03-24', 'F', 1),
('Jemaine Clement', 'jemaine.clement@example.com', '1974-01-10', 'M', 1),
('Taika Waititi', 'taika.waititi@example.com', '1975-08-16', 'M', 1),
('Steve Zahn', 'steve.zahn@example.com', '1967-11-13', 'M', 1),
('Zach Galifianakis', 'zach.galifianakis@example.com', '1969-10-01', 'M', 1);
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
    (11, 144, 118, 'returned' ,1),
    (12, 86, 29, 'returned' ,1),
    (13, 51, 104, 'sold' ,1),
    (14, 78, 115, 'sold' ,1),
    (15, 14, 29, 'sold' ,1),
    (16, 148, 31, 'sold' ,1),
    (17, 168, 108, 'sold' ,0),
    (18, 104, 117, 'returned' ,1),
    (19, 91, 7, 'sold' ,1),
    (20, 16, 130, 'sold' ,0),
    (21, 1, 101, 'returned' ,0),
    (22, 64, 104, 'sold' ,1),
    (23, 176, 32, 'returned' ,0),
    (24, 142, 96, 'sold' ,1),
    (25, 168, 121, 'returned' ,1),
    (26, 43, 97, 'lent' ,1),
    (27, 107, 126, 'lent' ,1),
    (28, 80, 96, 'returned' ,1),
    (29, 31, 75, 'lent' ,0),
    (30, 144, 19, 'returned' ,0),
    (31, 98, 123, 'sold' ,1),
    (32, 86, 70, 'sold' ,1),
    (33, 14, 82, 'sold' ,1),
    (34, 86, 9, 'sold' ,1),
    (35, 22, 4, 'lent' ,1),
    (36, 5, 86, 'returned' ,1),
    (37, 63, 72, 'lent' ,1),
    (38, 111, 91, 'returned' ,1),
    (39, 33, 58, 'returned' ,1),
    (40, 164, 20, 'sold' ,1),
    (41, 140, 115, 'sold' ,1),
    (42, 15, 32, 'lent' ,1),
    (43, 117, 92, 'returned' ,1),
    (44, 53, 31, 'returned' ,1),
    (45, 152, 49, 'returned' ,0),
    (46, 172, 16, 'sold' ,1),
    (47, 105, 24, 'sold' ,0),
    (48, 105, 87, 'returned' ,1),
    (49, 4, 77, 'lent' ,1),
    (50, 158, 73, 'returned' ,0),
    (51, 156, 65, 'lent' ,1),
    (52, 77, 43, 'returned' ,1),
    (53, 13, 133, 'returned' ,1),
    (54, 11, 82, 'returned' ,1),
    (55, 117, 56, 'sold' ,1),
    (56, 156, 78, 'sold' ,1),
    (57, 108, 29, 'returned' ,1),
    (58, 167, 126, 'lent' ,1),
    (59, 171, 76, 'returned' ,1),
    (60, 42, 6, 'sold' ,0),
    (61, 159, 26, 'returned' ,1),
    (62, 78, 130, 'sold' ,1),
    (63, 77, 127, 'returned' ,1),
    (64, 18, 13, 'lent' ,0),
    (65, 118, 20, 'returned' ,1),
    (66, 58, 32, 'sold' ,1),
    (67, 29, 66, 'lent' ,1),
    (68, 165, 57, 'returned' ,1),
    (69, 164, 84, 'lent' ,1),
    (70, 108, 124, 'lent' ,0),
    (71, 60, 66, 'lent' ,1),
    (72, 24, 109, 'lent' ,1),
    (73, 107, 65, 'returned' ,0),
    (74, 87, 122, 'sold' ,1),
    (75, 103, 7, 'sold' ,1),
    (76, 40, 122, 'returned' ,1),
    (77, 89, 3, 'returned' ,0),
    (78, 89, 59, 'returned' ,1),
    (79, 162, 11, 'lent' ,1),
    (80, 79, 126, 'lent' ,0),
    (81, 66, 2, 'lent' ,1),
    (82, 168, 56, 'sold' ,1),
    (83, 25, 91, 'lent' ,1),
    (84, 51, 94, 'sold' ,1),
    (85, 129, 114, 'sold' ,0),
    (86, 131, 19, 'lent' ,1),
    (87, 101, 35, 'returned' ,0),
    (88, 99, 1, 'sold' ,1),
    (89, 134, 9, 'returned' ,1),
    (90, 140, 90, 'returned' ,0),
    (91, 74, 128, 'sold' ,1),
    (92, 35, 86, 'sold' ,1),
    (93, 110, 70, 'lent' ,1),
    (94, 116, 96, 'sold' ,1),
    (95, 49, 118, 'lent' ,1),
    (96, 136, 69, 'returned' ,0),
    (97, 67, 2, 'returned' ,0),
    (98, 101, 25, 'lent' ,1),
    (99, 126, 37, 'sold' ,0),
    (100, 9, 65, 'returned' ,1),
    (101, 30, 71, 'lent' ,0),
    (102, 150, 125, 'sold' ,1),
    (103, 7, 89, 'returned' ,1),
    (104, 9, 41, 'lent' ,1),
    (105, 149, 11, 'lent' ,1),
    (106, 59, 130, 'returned' ,0),
    (107, 96, 8, 'lent' ,1),
    (108, 61, 45, 'lent' ,0),
    (109, 105, 34, 'returned' ,1),
    (110, 47, 92, 'sold' ,1),
    (111, 168, 23, 'sold' ,0),
    (112, 47, 52, 'returned' ,1),
    (113, 1, 49, 'returned' ,1),
    (114, 3, 53, 'lent' ,0),
    (115, 162, 101, 'sold' ,1),
    (116, 104, 106, 'returned' ,1),
    (117, 101, 129, 'sold' ,0),
    (118, 72, 63, 'returned' ,1),
    (119, 105, 30, 'returned' ,1),
    (120, 8, 15, 'sold' ,1),
    (121, 17, 132, 'sold' ,1),
    (122, 60, 49, 'returned' ,1),
    (123, 145, 95, 'sold' ,1),
    (124, 7, 84, 'lent' ,1),
    (125, 94, 19, 'sold' ,0),
    (126, 176, 134, 'sold' ,1),
    (127, 42, 112, 'lent' ,1),
    (128, 99, 40, 'sold' ,1),
    (129, 40, 41, 'returned' ,0),
    (130, 139, 45, 'sold' ,1),
    (131, 31, 105, 'lent' ,1),
    (132, 90, 130, 'lent' ,0),
    (133, 5, 6, 'lent' ,0),
    (134, 63, 118, 'sold' ,1),
    (135, 117, 59, 'returned' ,1),
    (136, 26, 84, 'returned' ,1),
    (137, 49, 7, 'sold' ,1),
    (138, 115, 124, 'sold' ,1),
    (139, 157, 1, 'sold' ,1),
    (140, 40, 83, 'lent' ,1),
    (141, 158, 131, 'lent' ,1),
    (142, 126, 100, 'lent' ,1),
    (143, 51, 106, 'sold' ,1),
    (144, 118, 112, 'lent' ,1),
    (145, 122, 66, 'lent' ,1),
    (146, 78, 64, 'returned' ,1),
    (147, 154, 39, 'sold' ,1),
    (148, 147, 112, 'sold' ,1),
    (149, 137, 35, 'lent' ,1),
    (150, 146, 115, 'lent' ,1),
    (151, 139, 103, 'lent' ,1),
    (152, 58, 7, 'lent' ,1),
    (153, 128, 61, 'lent' ,0),
    (154, 106, 24, 'lent' ,0),
    (155, 56, 55, 'sold' ,1),
    (156, 6, 37, 'lent' ,1),
    (157, 63, 70, 'sold' ,1),
    (158, 47, 134, 'returned' ,1),
    (159, 92, 43, 'lent' ,1),
    (160, 38, 52, 'sold' ,1),
    (161, 124, 91, 'returned' ,1),
    (162, 148, 80, 'sold' ,1),
    (163, 92, 41, 'lent' ,1),
    (164, 111, 96, 'sold' ,1),
    (165, 18, 29, 'lent' ,0),
    (166, 68, 130, 'returned' ,1),
    (167, 10, 97, 'returned' ,0),
    (168, 95, 76, 'lent' ,1),
    (169, 64, 124, 'lent' ,1),
    (170, 107, 62, 'lent' ,1),
    (171, 89, 23, 'lent' ,1),
    (172, 87, 118, 'returned' ,1),
    (173, 88, 35, 'lent' ,1),
    (174, 21, 40, 'sold' ,1),
    (175, 97, 38, 'sold' ,1),
    (176, 141, 126, 'sold' ,1),
    (177, 85, 134, 'returned' ,1),
    (178, 43, 94, 'sold' ,1),
    (179, 81, 68, 'sold' ,1),
    (180, 34, 20, 'returned' ,1),
    (181, 133, 61, 'returned' ,1),
    (182, 59, 17, 'returned' ,1),
    (183, 6, 96, 'lent' ,1),
    (184, 57, 105, 'returned' ,1),
    (185, 111, 67, 'sold' ,1),
    (186, 174, 47, 'lent' ,1),
    (187, 57, 96, 'returned' ,1),
    (188, 26, 29, 'lent' ,1),
    (189, 48, 5, 'returned' ,1),
    (190, 57, 90, 'lent' ,1),
    (191, 140, 132, 'lent' ,1),
    (192, 83, 131, 'returned' ,1),
    (193, 8, 111, 'sold' ,1),
    (194, 166, 95, 'returned' ,1),
    (195, 31, 52, 'sold' ,1),
    (196, 75, 55, 'returned' ,1),
    (197, 78, 21, 'returned' ,1),
    (198, 14, 61, 'sold' ,1),
    (199, 137, 91, 'returned' ,1),
    (200, 128, 24, 'sold' ,1),
    (201, 24, 104, 'sold' ,1),
    (202, 6, 7, 'returned' ,0),
    (203, 16, 31, 'lent' ,1),
    (204, 140, 66, 'sold' ,1),
    (205, 45, 102, 'lent' ,1),
    (206, 81, 66, 'returned' ,1),
    (207, 48, 97, 'sold' ,1),
    (208, 67, 57, 'lent' ,1),
    (209, 139, 106, 'lent' ,0),
    (210, 168, 51, 'lent' ,1),
    (211, 141, 134, 'lent' ,1),
    (212, 141, 90, 'returned' ,1),
    (213, 38, 64, 'sold' ,0),
    (214, 156, 46, 'sold' ,0),
    (215, 45, 6, 'lent' ,1),
    (216, 117, 54, 'lent' ,1),
    (217, 56, 83, 'lent' ,0),
    (218, 152, 48, 'lent' ,1),
    (219, 49, 87, 'sold' ,0),
    (220, 123, 110, 'sold' ,0),
    (221, 76, 8, 'sold' ,1),
    (222, 161, 131, 'lent' ,1),
    (223, 24, 132, 'lent' ,0),
    (224, 112, 19, 'returned' ,1),
    (225, 48, 129, 'returned' ,1),
    (226, 2, 85, 'lent' ,1),
    (227, 126, 115, 'sold' ,1),
    (228, 176, 37, 'returned' ,1),
    (229, 99, 77, 'sold' ,1),
    (230, 43, 134, 'returned' ,0),
    (231, 166, 75, 'returned' ,1),
    (232, 161, 46, 'returned' ,1),
    (233, 171, 17, 'sold' ,1),
    (234, 31, 64, 'sold' ,1),
    (235, 81, 65, 'sold' ,1),
    (236, 36, 63, 'sold' ,1),
    (237, 99, 119, 'lent' ,1),
    (238, 155, 72, 'sold' ,1),
    (239, 118, 42, 'sold' ,1),
    (240, 101, 17, 'returned' ,1),
    (241, 97, 59, 'lent' ,1),
    (242, 11, 6, 'returned' ,1),
    (243, 44, 122, 'lent' ,1),
    (244, 53, 107, 'lent' ,1),
    (245, 150, 62, 'returned' ,1),
    (246, 73, 40, 'lent' ,0),
    (247, 122, 35, 'lent' ,1),
    (248, 21, 37, 'sold' ,0),
    (249, 172, 35, 'sold' ,1),
    (250, 89, 42, 'returned' ,1),
    (251, 9, 54, 'sold' ,1),
    (252, 1, 86, 'returned' ,1),
    (253, 123, 52, 'returned' ,1),
    (254, 44, 59, 'sold' ,1),
    (255, 50, 69, 'lent' ,1),
    (256, 98, 12, 'sold' ,1),
    (257, 144, 26, 'sold' ,1),
    (258, 68, 79, 'sold' ,0),
    (259, 174, 8, 'sold' ,1),
    (260, 71, 25, 'sold' ,1),
    (261, 16, 94, 'sold' ,0),
    (262, 67, 14, 'sold' ,1),
    (263, 116, 98, 'returned' ,0),
    (264, 120, 11, 'sold' ,1),
    (265, 98, 43, 'returned' ,1),
    (266, 33, 38, 'returned' ,1),
    (267, 40, 43, 'returned' ,1),
    (268, 133, 55, 'lent' ,1),
    (269, 44, 22, 'returned' ,0),
    (270, 62, 22, 'lent' ,1),
    (271, 93, 73, 'lent' ,1),
    (272, 28, 124, 'lent' ,1),
    (273, 51, 90, 'returned' ,1),
    (274, 37, 118, 'sold' ,1),
    (275, 158, 81, 'sold' ,1),
    (276, 30, 62, 'sold' ,0),
    (277, 72, 36, 'lent' ,1),
    (278, 76, 23, 'lent' ,1),
    (279, 14, 73, 'sold' ,0),
    (280, 160, 4, 'returned' ,1),
    (281, 149, 113, 'lent' ,1),
    (282, 130, 24, 'returned' ,0),
    (283, 76, 58, 'lent' ,1),
    (284, 107, 126, 'returned' ,1),
    (285, 109, 90, 'sold' ,1),
    (286, 139, 14, 'sold' ,1),
    (287, 37, 59, 'sold' ,1),
    (288, 6, 58, 'returned' ,1),
    (289, 43, 113, 'sold' ,1),
    (290, 14, 125, 'returned' ,0),
    (291, 104, 82, 'returned' ,0),
    (292, 46, 112, 'returned' ,1),
    (293, 144, 120, 'sold' ,1),
    (294, 145, 17, 'sold' ,1),
    (295, 168, 90, 'returned' ,1),
    (296, 100, 66, 'lent' ,1),
    (297, 39, 135, 'returned' ,0),
    (298, 71, 18, 'returned' ,1),
    (299, 36, 90, 'lent' ,1),
    (300, 117, 42, 'lent' ,1),
    (301, 63, 105, 'sold' ,1),
    (302, 64, 119, 'returned' ,1),
    (303, 117, 69, 'returned' ,1),
    (304, 6, 11, 'lent' ,1),
    (305, 1, 119, 'sold' ,0),
    (306, 70, 132, 'sold' ,1),
    (307, 22, 18, 'lent' ,1),
    (308, 9, 51, 'sold' ,1),
    (309, 93, 25, 'returned' ,1),
    (310, 112, 71, 'lent' ,1),
    (311, 174, 61, 'sold' ,1),
    (312, 10, 103, 'returned' ,1),
    (313, 84, 78, 'lent' ,1),
    (314, 91, 11, 'sold' ,1),
    (315, 24, 94, 'sold' ,1),
    (316, 49, 127, 'returned' ,0),
    (317, 108, 68, 'lent' ,0),
    (318, 158, 64, 'sold' ,1),
    (319, 48, 26, 'returned' ,1),
    (320, 14, 134, 'lent' ,1),
    (321, 37, 98, 'returned' ,1),
    (322, 130, 65, 'sold' ,1),
    (323, 33, 116, 'sold' ,1),
    (324, 97, 72, 'sold' ,1),
    (325, 31, 71, 'sold' ,1),
    (326, 106, 102, 'sold' ,1),
    (327, 14, 89, 'returned' ,0),
    (328, 61, 72, 'lent' ,1),
    (329, 114, 74, 'lent' ,1),
    (330, 114, 88, 'returned' ,1),
    (331, 41, 116, 'sold' ,1),
    (332, 149, 73, 'lent' ,1),
    (333, 17, 124, 'sold' ,1),
    (334, 70, 57, 'lent' ,1),
    (335, 11, 61, 'returned' ,1),
    (336, 72, 48, 'returned' ,1),
    (337, 172, 48, 'sold' ,1),
    (338, 86, 71, 'sold' ,1),
    (339, 12, 22, 'lent' ,1),
    (340, 142, 12, 'sold' ,0),
    (341, 64, 2, 'returned' ,1),
    (342, 89, 101, 'returned' ,1),
    (343, 173, 17, 'returned' ,1),
    (344, 161, 100, 'returned' ,1),
    (345, 144, 135, 'returned' ,1),
    (346, 10, 89, 'sold' ,1),
    (347, 43, 91, 'sold' ,0),
    (348, 66, 54, 'lent' ,1),
    (349, 80, 99, 'lent' ,1),
    (350, 45, 90, 'lent' ,1)
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

    - `books`:
```sh
mysql> SELECT COUNT(*) FROM books;
+----------+
| count(*) |
+----------+
|      176 |
+----------+
1 row in set (0.01 sec)
```
    - `authors`:
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

    2.1. Retrieve Authors: 
    
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
    2.2. Retrieve Books: 
    
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
    
    3.1. Combine Books and Authors: 
    
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
    3.2 Combine Operations, Books, Clients, and Author: 
    
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
    3.3 Filter Results Based on Conditions: 
    
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

    1.1. Implicit JOIN: 
    
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
    1.2 Explicit JOIN: 
    
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

    3.1 Example with LEFT JOIN:
    
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