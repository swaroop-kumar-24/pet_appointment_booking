import os
from dotenv import load_dotenv
from mysql.connector import connect, errors

# Load environment variables
load_dotenv()

class ApptDbDao:
    def __init__(self):
        # Initialize DB connection
        self.conn = connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE")
        )
        self.cur = self.conn.cursor(dictionary=True)
        self.table = os.getenv("DB_APPT_TABLE")
        self._ensure_table()

    def _ensure_table(self):
        # Create appointments table if it doesn't exist
        create_query = f"""
        CREATE TABLE IF NOT EXISTS {self.table} (
            appt_id    INT AUTO_INCREMENT PRIMARY KEY,
            pet_id     INT,
            time_slot  DATETIME,
            FOREIGN KEY (pet_id) REFERENCES {os.getenv("DB_PET_TABLE")}(pet_id)
        );
        """
        self.cur.execute(create_query)
        self.conn.commit()
        print(os.getenv("MSG_TABLE_OK"))

    def book_appt(self, appt):
        # 1) Check slot availability
        check_q = f"SELECT COUNT(*) AS cnt FROM {self.table} WHERE time_slot = %s"
        self.cur.execute(check_q, (appt.time_slot,))
        if self.cur.fetchone()["cnt"] > 0:
            print(os.getenv("MSG_SLOT_UNAVAILABLE").format(time_slot=appt.time_slot))
            return None

        # 2) Attempt to book
        try:
            insert_q = f"INSERT INTO {self.table} (pet_id, time_slot) VALUES (%s, %s)"
            self.cur.execute(insert_q, (appt.pet_id, appt.time_slot))
            self.conn.commit()
            appt_id = self.cur.lastrowid
            print(os.getenv("MSG_BOOK_OK").format(
                appt_id=appt_id,
                pet_id=appt.pet_id,
                time_slot=appt.time_slot
            ))
            return appt_id
        except errors.IntegrityError:
            print(os.getenv("MSG_BOOK_FAIL").format(pet_id=appt.pet_id))
            return None

    def view_appts(self):
        # Display all appointments
        print(os.getenv("MSG_VIEW_APPTS"))
        select_q = f"SELECT * FROM {self.table}"
        self.cur.execute(select_q)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def delete_appt(self, appt_id):
        # Delete an appointment by ID
        try:
            delete_q = f"DELETE FROM {self.table} WHERE appt_id = %s"
            self.cur.execute(delete_q, (appt_id,))
            self.conn.commit()
            if self.cur.rowcount:
                print(os.getenv("MSG_APPT_DELETE_OK").format(appt_id=appt_id))
            else:
                print(os.getenv("MSG_APPT_DELETE_FAIL").format(appt_id=appt_id))
        except errors.Error:
            print(os.getenv("MSG_APPT_DELETE_FAIL").format(appt_id=appt_id))
