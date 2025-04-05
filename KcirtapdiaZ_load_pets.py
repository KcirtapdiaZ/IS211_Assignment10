import sqlite3

# Connect to the database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

# Create tables (if they don't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS person_pet (
    person_id INTEGER,
    pet_id INTEGER,
    FOREIGN KEY (person_id) REFERENCES person(id),
    FOREIGN KEY (pet_id) REFERENCES pet(id)
);
''')

# Inserting data into Person Table
cursor.executemany('''
    INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?)
''', [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
])

# Inserting data into Pet Table
cursor.executemany('''
    INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'AlaskanMalamute', 3, 0),
    (3, 'Max', 'CockerSpaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'CockerSpaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
])

# Inserting data into Person_Pet Table
cursor.executemany('''
    INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)
''', [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
])

# Commit the changes and close the connection
conn.commit()
conn.close()
