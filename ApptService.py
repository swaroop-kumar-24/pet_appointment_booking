# ApptService.py
from ApptDbDao import ApptDbDao
from model import Appointment
class ApptService:
    def __init__(self):
        self.dao = ApptDbDao()
    def book(self, pet_id, time_slot):
        appt = Appointment(pet_id=pet_id, time_slot=time_slot)
        self.dao.book_appt(appt)
    def view(self):
        self.dao.view_appts()
    def cancel(self, appt_id):
        self.dao.delete_appt(appt_id)
