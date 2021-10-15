import sqlite3
import json

CUSTOMERS = [
    {
      "id": 15,
      "name": "Ryan Tanay",
      "email": "ryan@tanay.com",
      
    },
    {
      "id": 16,
      "name": "Emma Beaton",
      "email": "emma@beaton.com",
      
    },
    {
      "id": 17,
      "name": "Dani Adkins",
      "email": "dani.adkins.com",
      
    },
    {
      "id": 18,
      "name": "Adam Oswalt",
      "email": "adam@oswalt.com",
      
    },
    {
      "id": 19,
      "name": "Fletcher Bangs",
      "email": "flangs@bangs.com",
      
    },
    {
      "id": 20,
      "name": "Angela Lee",
      "email": "lee@lee.com",
      
    },
    {
      "name": "mike mike",
      "email": "m@m.com",
      "id": 21,
    }
]


def get_all_customers():
    return CUSTOMERS


def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:   
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:           
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
