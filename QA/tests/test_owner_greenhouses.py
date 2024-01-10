import pytest
import requests

jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NUb2tlbiI6InlhMjkuYTBBZkJfYnlBdURzV3h4Szk2ZnJ2Ui1KalJXMkE0UjI4VTBReF8zbkx3R0xZb2tRSUdvT01aOXYwYXdPN3VPb3RYWU13Zm5XTWVIazJ1SmxDMTNBa3QzVnBxOUZvdzZuUGlYTjlFZmpwb0h0ZHVVVy00UkZadUkxODN0dGR5bmd5N29iUjl0Ukp1M25NOE9HaDRqM2Q2T09pb2hxQ0VtU3dBbDkySGFDZ1lLQVFZU0FROFNGUUhHWDJNaWpFY19tOW5TblRXUEFWVFFjM3l6eUEwMTcxIiwiY3JlYXRlZCI6ZmFsc2UsImlhdCI6MTcwNDg3MDgzMCwiZXhwIjoxNzA1NDc1NjMwfQ.KwKbW5WgBXRaMUyi-8E_NkqEESbqjMt9LfwAnQ-wE64'
headers = {
    'Authorization': f'Bearer {jwt_token}',
    'Content-Type': 'application/json'
}

@pytest.mark.api_get
def test_api_with_jwt_token():
    api_endpoint = 'http://localhost:5000'
    response = requests.get(api_endpoint, headers=headers)
    assert response.status_code == 200

@pytest.mark.get
def test_get_greenhouses():
    api_endpoint = 'http://localhost:5000/greenhouses'
    response = requests.get(api_endpoint, headers=headers)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

@pytest.mark.post
def test_create_greenhouse():
    api_endpoint = 'http://localhost:5000/greenhouses/create'
    data = {
        'name': 'New Greenhouse',
        'size': 100,
        'measurement': 'sqm',
        'description': 'A new greenhouse',
        'location': 'Somewhere',
        'created_at': '2024-01-09T12:00:00Z'
    }
    response = requests.post(api_endpoint, data=data, headers=headers)
    assert response.status_code == 200

@pytest.mark.put
def test_update_greenhouse():
    greenhouse_id = 11
    api_endpoint = f'http://localhost:5000/greenhouses/{greenhouse_id}'
    payload = {
        'name': 'Updated Greenhouse Name',
        'description': 'Updated description',
        'location': 'Updated location'
    }
    response = requests.put(api_endpoint, json=payload, headers=headers)
    assert response.status_code == 200
