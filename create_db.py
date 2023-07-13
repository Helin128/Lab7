"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from datetime import datetime
from faker import Faker
import random

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'sn.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"
    conn = sqlite3.connect('sn.db')
    cur = conn.cursor()
    
    create_people_table_query = """
        CREATE TABLE IF NOT EXISTS people
        (
            id         INTEGER PRIMARY KEY,
            name       TEXT NOT NULL,
            email      TEXT NOT NULL,
            address    TEXT NOT NULL,
            city       TEXT NOT NULL,
            province   TEXT NOT NULL,
            bio        TEXT,
            age        INTEGER,
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL
        );
"""
    cur.execute(create_people_table_query)
    conn.commit()
    conn.close()
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    # Use Faker to generate fake data
conn = sqlite3.connect('sn.db')
cur = conn.cursor()

    # Create people table
add_human_query = """
    INSERT INTO people
      (
      name, 
      email,
      address,
      city, 
      age, 
      created_at, 
      updated_at
      )
      VALUES (?, ?, ?, ?, ?, ?, ?);
    """
     # Insert 200 fake people into the people table
fake = Faker()

for _ in range(200):
  fake.name(),
  fake.email(),
  fake.address(),
  fake.city(),
  random.randint(1, 100),
  datetime.now(),
  datetime.now()      
     
cur.execute(add_human_query,fake)
conn.commit()
conn.close()
    
if __name__ == '__main__':
   main()