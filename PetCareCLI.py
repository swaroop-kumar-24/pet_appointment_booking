import os
from dotenv import load_dotenv
from PetService import PetService
from ApptService import ApptService

load_dotenv()
pet_svc  = PetService()
appt_svc = ApptService()

MENU = """
1. Book appointment
2. View appointments
3. Delete appointment
4. Add pet
5. View pets
6. Delete pet
Any other key to exit
"""

while True:
    print(MENU)
    choice = input("Select option: ")
    if choice == "1":
        pid  = int(input("Pet ID: "))
        when = input("Time slot (YYYY-MM-DD HH:MM): ")
        appt_svc.book(pid, when)
    elif choice == "2":
        appt_svc.view()
    elif choice == "3":
        aid = int(input("Appointment ID to delete: "))
        appt_svc.cancel(aid)
    elif choice == "4":
        pid   = int(input("New Pet ID: "))
        name  = input("Name: ")
        breed = input("Breed: ")
        owner = input("Owner: ")
        pet_svc.add_pet(pid, name, breed, owner)
    elif choice == "5":
        pet_svc.view_pets()
    elif choice == "6":
        pid = int(input("Pet ID to delete: "))
        pet_svc.delete_pet(pid)
    else:
        break
