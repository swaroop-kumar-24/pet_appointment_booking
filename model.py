class Pet:
    def __init__(self, pet_id, name=None, breed=None, owner=None):
        self.pet_id = pet_id
        self.name    = name
        self.breed   = breed
        self.owner   = owner
    def __str__(self):
        return f"Pet[{self.pet_id}]: {self.name}, {self.breed}, owner={self.owner}"

class Appointment:
    def __init__(self, appt_id=None, pet_id=None, time_slot=None):
        self.appt_id   = appt_id
        self.pet_id    = pet_id
        self.time_slot = time_slot
    def __str__(self):
        return f"Appt[{self.appt_id}]: Pet {self.pet_id} at {self.time_slot}"
