import sqlite3
import json
from models import Employee

def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        """)
        employees = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'],)
            employees.append(employee.__dict__)
    return json.dumps(employees)



def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

       
        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'],
                            )

        return json.dumps(employee.__dict__)

def create_employee(new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, address,location_id )
        VALUES
            ( ?, ?, ?,);
        """, (new_employee['name'], new_employee['address'],
              new_employee['location_id'], ))
        id = db_cursor.lastrowid
        new_employee['id'] = id


    return json.dumps(new_employee)

def delete_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))



def update_employee(id, new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                employee_id = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['breed'],
              new_employee['status'], new_employee['location_id'],
              new_employee['employee_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
