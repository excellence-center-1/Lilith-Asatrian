import pytest
import requests
import allure

@allure.title("Test API")
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
    @allure.title("Test Get Greenhouse")
    @allure.description("This test attempts to get all greenhouses")
    @allure.tag("Get")
    def test_get_greenhouses(self, base_url, headers):
        api_endpoint = f'{base_url}/greenhouses'
        response = requests.get(api_endpoint, headers=headers)
        assert response.status_code == 200
        #greenhouses = response.json()
        # assert all(field in greenhouses[0] for field in ['id', 'greenhouse_name', 'greenhouse_size', 'measurement', 'greenhouse_description', 'greenhouse_location', 'created_at', 'updated_at']), "The response is missing some expected fields"

    # @pytest.mark.get
    # def test_content_type_in_response(self, base_url, headers):
    #     api_endpoint = f'{base_url}/greenhouses'
    #     response = requests.get(api_endpoint, headers=headers)
    #     assert 'Content-Type' in response.headers, "Unexpected Content-Type header"

    @pytest.mark.get
    @allure.title("Get Greenhouse in fixed time")
    @allure.description("This test attempts to get all greenhouses in less than one second")
    @allure.tag("Get", "timeout")
    def test_timout_in_response(self, base_url, headers):
        api_endpoint = f'{base_url}/greenhouses'
        response = requests.get(api_endpoint, headers=headers)
        assert response.elapsed.total_seconds() < 1, "Response took longer than expected"

    @pytest.mark.get
    @allure.title("Get Greenhouse with invalid JWT token")
    @allure.description("This test attempts to get all greenhouses with invalid token")
    @allure.tag("Get", "invalid")
    @pytest.mark.get
    def test_api_with_invalid_token(self, base_url):
        api_endpoint = f'{base_url}/greenhouses'
        invalid_header = { 
            'Authorization': 'Bearer invalid_token',
            'Content-Type': 'application/json'
        }
        response = requests.get(api_endpoint, headers=invalid_header)
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    
    # @pytest.mark.get
    # def test_get_nonexistent_greenhouse(self, base_url, headers):
    #     greenhouse_id=999
    #     api_endpoint = f'{base_url}/greenhouses/{greenhouse_id}'
    #     response = requests.get(api_endpoint, headers=headers)
    #     assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

@allure.title("Post API")
@pytest.mark.api
class TestPostGreenhouse:

    allure.title("Create greenhouses")
    @allure.description("This test case intends to create multiple greenhouses, and valid credentails are provided.")
    @pytest.mark.post
    @pytest.mark.parametrize("name, size", [("Greenhouse 1", 500), ("Greenhouse 2", 1000), ("Greenhouse 3", 400)])
    def test_create_greenhouse(self, base_url, headers, name, size, db_cursor):
        api_endpoint = f'{base_url}/greenhouses/create'
        payload = {
            'name': name,
            'size': size,
            'measurement': 3,
            'description': 'A new greenhouse',
            'location': 'Somewhere',
            'created_at': '2024-01-11T12:30:45.678Z'
        }
        response = requests.post(api_endpoint, json=payload, headers=headers)
        assert response.status_code == 200, f"The status code should be 200, but got {response.status_code}"
        created_data = response.json()
        print("################", created_data)
        db_cursor.execute("SELECT * FROM greenhouses WHERE id = %s", (created_data['id'],))
        result = db_cursor.fetchone()
        assert result is not None, "The created data is not found in the database"
        
    @allure.title("Create greenhouses with already existing names")
    @allure.description("This test case intends to create multiple greenhouses, but already existing names are used")
    @pytest.mark.post
    @pytest.mark.parametrize("name, size", [("Greenhouse 1", 500), ("Greenhouse 2", 1000), ("Greenhouse 3", 400)])
    def test_create_the_same_name_greenhouse(self, base_url, headers, name, size):
        api_endpoint = f'{base_url}/greenhouses/create'
        payload = {
            'name': name, 
            'size': size,
            'measurement': 3,
            'description': 'A new greenhouse',
            'location': 'Somewhere',
            'created_at': '2024-01-11T12:30:45.678Z'
        }
        response = requests.post(api_endpoint, json=payload, headers=headers)
        assert response.status_code == 400, f"The expected status code should be 400, but got {response.status_code}"

    @allure.title("Create greenhouses with missing fields")
    @allure.description("This test case intends to check the creation of greenhouses with missing fields, here only name and measurement are provided.")
    @allure.tag("missing")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("name, size", [("Greenhouse 4", 500), ("Greenhouse 5", 1000), ("Greenhouse 6", 400)])
    @pytest.mark.post
    def test_create_greenhouse_with_missing_field(self, base_url, headers, name, size):
        api_endpoint = f'{base_url}/greenhouses/create'
        payload = {
            'name': name, 
            'measurement': size,
        }
        response = requests.post(api_endpoint, json=payload, headers=headers)
        assert response.status_code == 500, f"Status code should be 500, but got {response.status_code}"

@pytest.mark.api
class TestUpdateGreenhouse:
    @allure.title("Update existing greenhouse with valid credentials")
    @pytest.mark.put
    def test_update_greenhouse(self, base_url, headers):
        greenhouse_id = 3
        api_endpoint = f'{base_url}/greenhouses/{greenhouse_id}'
        payload = {
            'name': 'Hey',
            'description': 'description',
            'location': 'Updated location'
        }
        response = requests.put(api_endpoint, json=payload, headers=headers)
        assert response.status_code == 200

    # @pytest.mark.put
    # def test_update_nonexistent_greenhouse(self, base_url, headers):
    #     greenhouse_id = 800
    #     api_endpoint = f'{base_url}/greenhouses/{greenhouse_id}'
    #     payload = {
    #         'name': 'Hey',
    #         'description': 'description',
    #         'location': 'Updated location'
    #     }
    #     response = requests.put(api_endpoint, json=payload, headers=headers)
    #     assert response.status_code == 404, f"The expected status code should be 404, but got {response.status_code}"
    
    @allure.title("Update greenhouse with invalid credentials")
    @pytest.mark.xfail(run=False)
    @pytest.mark.invalid_input
    @pytest.mark.put
    @pytest.mark.parametrize("name, size", [("Invalid name 1", -1), ("Invalid name 2", -5)])
    def test_update_greenhouse_with_invalid_credentials(self, base_url, headers, name, size):
        greenhouse_id = 2
        api_endpoint=f'{base_url}/greenhouses/{greenhouse_id}'
        payload = {
            'name': name,
            'size': size,
        }
        response = requests.put(api_endpoint, json=payload, headers=headers)
        assert response.status_code == 400, f"The expected status code should be 400, but got {response.status_code}"

@allure.title("Delete greenhouse")
@pytest.mark.xfail()
@pytest.mark.api
class TestDeleteGreenhouse:
   @pytest.mark.delete
   def test_delete_greenhouse(self, base_url, headers):
       greenhouse_id=11
       api_endpoint = f'{base_url}/greenhouses/{greenhouse_id}'
       response = requests.delete(api_endpoint, headers=headers)
       assert response.status_code == 204