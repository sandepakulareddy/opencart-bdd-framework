import pytest
from utils.api_client import PetAPI

pet_api = PetAPI()

@pytest.fixture
def pet_payload():
    return {
        "id": 999001,
        "name": "Doggie",
        "status": "available"
    }

def test_create_read_update_delete_pet(pet_payload):

    # CREATE
    create_response = pet_api.create_pet(pet_payload)
    assert create_response.status_code == 200
    assert create_response.json()["name"] == "Doggie"

    pet_id = pet_payload["id"]

    # READ
    get_response = pet_api.get_pet(pet_id)
    assert get_response.status_code == 200
    assert get_response.json()["id"] == pet_id

    # UPDATE
    pet_payload["status"] = "sold"
    update_response = pet_api.update_pet(pet_payload)
    assert update_response.status_code == 200
    assert update_response.json()["status"] == "sold"

    # DELETE
    delete_response = pet_api.delete_pet(pet_id)
    assert delete_response.status_code == 200

    # VERIFY DELETE
    get_deleted = pet_api.get_pet(pet_id)
    assert get_deleted.status_code == 404