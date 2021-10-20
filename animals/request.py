import sqlite3
import json
from models import Animal
from models import Location
from models import Customer


def get_all_animals():

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = l.location_id
        """)
        animals = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'])
            location = Location(row['location_id'], row['location_name'], row['location_address'])
            customer = Customer(row['customer_id']), row['customer_name'], row['customer_address'], row['customer_email'], row['customer_password']
            animal.location = location.__dict__
            animals.append(animal.__dict__)
    return json.dumps(animals)



def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

       
        animal = Animal(data['id'], data['name'], data['breed'],
                            data['status'], data['location_id'],
                            data['customer_id'])

        return json.dumps(animal.__dict__)


def create_animal(new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, status, breed, customer_id, location_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_animal['name'], new_animal['status'],
              new_animal['breed'], new_animal['customer_id'],
              new_animal['location_id'], ))
        id = db_cursor.lastrowid
        new_animal['id'] = id


    return json.dumps(new_animal)


def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))



def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True



