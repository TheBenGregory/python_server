import sqlite3
import json
from models import Location

def get_all_locations():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)
        locations = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            location = Location(row['id'], row['name'], row['address'],
                            )

            locations.append(location.__dict__)
    return json.dumps(locations)



def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

       
        location = Location(data['id'], data['name'], data['address'],
                          )

        return json.dumps(location.__dict__)

def create_location(new_location):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Location
            ( name, address )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_location['name'], new_location['address'], ))
        id = db_cursor.lastrowid
        new_location['id'] = id

def delete_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))



def update_location(id, new_location):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Location
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                location_id = ?
        WHERE id = ?
        """, (new_location['name'], new_location['breed'],
              new_location['status'], new_location['location_id'],
              new_location['location_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
