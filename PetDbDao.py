# PetDbDao.py
import os
from dotenv import load_dotenv
from mysql.connector import connect

load_dotenv()
class PetDbDao:
    def __init__(self):
        self.conn   = connect(
            host     = os.getenv("DB_HOST"),
            user     = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_DATABASE")
        )
        self.cur    = self.conn.cursor(dictionary=True)
        self.table  = os.getenv("DB_PET_TABLE")
        self._ensure_table()
    def _ensure_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS pets ("
            "pet_id INT PRIMARY KEY, name VARCHAR(100), "
            "breed VARCHAR(100), owner VARCHAR(100))"
        )
        self.conn.commit()
    def add_pet(self, pet):
        qry = f"INSERT INTO {self.table} VALUES (%s,%s,%s,%s)"
        self.cur.execute(qry, (pet.pet_id, pet.name, pet.breed, pet.owner))
        self.conn.commit()
    def view_pets(self):
        self.cur.execute(f"SELECT * FROM {self.table}")
        for row in self.cur.fetchall():
            print(row)
    def delete_pet(self, pet_id):
        self.cur.execute(f"DELETE FROM {self.table} WHERE pet_id=%s", (pet_id,))
        self.conn.commit()
