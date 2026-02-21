import requests
from utils.config import BASE_URL

class PetAPI:

    def create_pet(self, payload):
        return requests.post(f"{BASE_URL}/pet", json=payload)

    def get_pet(self, pet_id):
        return requests.get(f"{BASE_URL}/pet/{pet_id}")

    def update_pet(self, payload):
        return requests.put(f"{BASE_URL}/pet", json=payload)

    def delete_pet(self, pet_id):
        return requests.delete(f"{BASE_URL}/pet/{pet_id}")