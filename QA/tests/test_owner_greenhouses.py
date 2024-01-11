import pytest
import requests

@pytest.mark.api
class TestAPIWithJWTToken:
    @pytest.mark.get
    def test_api_with_jwt_token(self, base_url, headers):
        api_endpoint = base_url
        response = requests.get(api_endpoint, headers=headers)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

@pytest.mark.api
class TestGetGreenhouses:
    @pytest.mark.get
    def test_get_greenhouses(self, base_url, headers):
        api_endpoint = f'{base_url}/greenhouses'
        response = requests.get(api_endpoint, headers=headers)
        assert response.status_code == 200
        greenhouses = response.json()
        assert all(field in greenhouses[0] for field in ['id', 'greenhouse_name', 'greenhouse_size', 'measurement', 'greenhouse_description', 'greenhouse_location', 'created_at', 'updated_at']), "The response is missing some expected fields"

    @pytest.mark.get
    def test_content_type_in_response(self, base_url, headers):
        api_endpoint = f'{base_url}/greenhouses'
        response = requests.get(api_endpoint, headers=headers)
        assert 'Content-Type' in response.headers, "Unexpected Content-Type header"

    @pytest.mark.get
    def test_timout_in_response(self, base_url, headers):
        api_endpoint = f'{base_url}/greenhouses'
        response = requests.get(api_endpoint, headers=headers)
        assert response.elapsed.total_seconds() < 1, "Response took longer than expected"

    @pytest.mark.get
    def test_api_with_invalid_token(self, base_url):
        api_endpoint = f'{base_url}/greenhouses'
        invalid_header = { 
            'Authorization': 'Bearer invalid_token',
            'Content-Type': 'application/json'
        }
        response = requests.get(api_endpoint, headers=invalid_header)
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    
    @pytest.mark.get
    def test_get_nonexistent_greenhouse(self, base_url, headers):
        greenhouse_id=999
        api_endpoint = f'{base_url}/greenhouses/{greenhouse_id}'
        response = requests.get(api_endpoint, headers=headers)
        assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

@pytest.mark.api
class TestPostGreenhouse:
    @pytest.mark.post
    def test_create_greenhouse(self, base_url, headers):
        api_endpoint = f'{base_url}/greenhouses/create'
        payload = {
            'name': 'Greenhouse 300',
            'size': 2,
            'measurement': 3,
            'description': 'A new greenhouse',
            'location': 'Somewhere',
            'created_at': '2024-01-11T12:30:45.678Z'
        }
        response = requests.post(api_endpoint, json=payload, headers=headers)
        assert response.status_code == 200, f"The status code should be 200, but got {response.status_code}"
    
    @pytest.mark.post
    def test_create_the_same_name_greenhouse(self, base_url, headers):
        api_endpoint = f'{base_url}/greenhouses/create'
        payload = {
            'name': 'Greenhouse 300',
            'size': 2,
            'measurement': 3,
            'description': 'A new greenhouse',
            'location': 'Somewhere',
            'created_at': '2024-01-11T12:30:45.678Z'
        }
        response = requests.post(api_endpoint, json=payload, headers=headers)
        assert response.status_code == 400, f"The expected status code should be 400, but got {response.status_code}"

    @pytest.mark.post
    def test_create_greenhouse_with_missing_field(self, base_url, headers):
        api_endpoint = f'{base_url}/greenhouses/create'
        payload = {
            'name': 'Yay Greenhouse',
            'measurement': 3,
            'description': 'A new greenhouse',
            'location': 'Somewhere',
            'created_at': '2024-01-11T12:30:45.678Z'
        }
        response = requests.post(api_endpoint, json=payload, headers=headers)
        assert response.status_code == 500, f"Status code should be 500, but got {response.status_code}"

@pytest.mark.api
class TestUpdateGreenhouse:
    @pytest.mark.put
    def test_update_greenhouse(self, base_url, headers):
        greenhouse_id = 14
        api_endpoint = f'{base_url}/greenhouses/{greenhouse_id}'
        payload = {
            'name': 'Hey',
            'description': 'description',
            'location': 'Updated location'
        }
        response = requests.put(api_endpoint, json=payload, headers=headers)
        assert response.status_code == 200

    @pytest.mark.put
    def test_update_nonexistent_greenhouse(self, base_url, headers):
        greenhouse_id = 800
        api_endpoint = f'{base_url}/greenhouses/{greenhouse_id}'
        payload = {
            'name': 'Hey',
            'description': 'description',
            'location': 'Updated location'
        }
        response = requests.put(api_endpoint, json=payload, headers=headers)
        assert response.status_code == 404, f"The expected status code should be 404, but got {response.status_code}"

@pytest.mark.api
class TestDeleteGreenhouse:
    @pytest.mark.delete
    def test_delete_greenhouse(self, base_url, headers):
        greenhouse_id=11
        api_endpoint = f'{base_url}/greenhouses/{greenhouse_id}'
        response = requests.delete(api_endpoint, headers=headers)
        assert response.status_code == 204
