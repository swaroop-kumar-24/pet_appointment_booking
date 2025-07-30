# PetService.py
from PetDbDao import PetDbDao
from model import Pet
class PetService:
    def __init__(self):
        self.dao = PetDbDao()
    def add_pet(self, pet_id, name, breed, owner):
        pet = Pet(pet_id, name, breed, owner)
        self.dao.add_pet(pet)
    def view_pets(self):
        self.dao.view_pets()
    def delete_pet(self, pet_id):
        self.dao.delete_pet(pet_id)
