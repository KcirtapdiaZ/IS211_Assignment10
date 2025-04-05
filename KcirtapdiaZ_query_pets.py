# RUN THIS AFTER RUNNING LOAD_PETS.PY
import sqlite3

def get_person_and_pets(person_id):
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    # Query to get person data
    cursor.execute('SELECT * FROM person WHERE id = ?', (person_id,))
    person = cursor.fetchone()

    if person:
        print(f"{person[1]} {person[2]}, {person[3]} years old")
        
        # Query to get the pets of the person
        cursor.execute('''
            SELECT p.name, p.breed, p.age 
            FROM pet p
            JOIN person_pet pp ON p.id = pp.pet_id
            WHERE pp.person_id = ?
        ''', (person_id,))
        
        pets = cursor.fetchall()
        
        if pets:
            for pet in pets:
                print(f"{person[1]} {person[2]} owned {pet[0]}, a {pet[1]} that was {pet[2]} years old.")
        else:
            print(f"{person[1]} {person[2]} does not own any pets.")
    else:
        print("Error: Person not found!")

    conn.close()

while True:
    person_id = int(input("Enter a person's ID (or -1 to exit): "))
    if person_id == -1:
        break
    get_person_and_pets(person_id)
