from utils.api_client import PetAPI

pet_api = PetAPI()

def test_get_non_existing_pet():
    response = pet_api.get_pet(123456789)
    assert response.status_code == 404

def test_create_pet_invalid_data():
    payload = {
        "id": "invalid_id",
        "name": 12345
    }
    response = pet_api.create_pet(payload)
    assert response.status_code in [400, 500]

def test_delete_non_existing_pet():
    response = pet_api.delete_pet(987654321)
    assert response.status_code == 404