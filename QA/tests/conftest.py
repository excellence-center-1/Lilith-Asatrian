import pytest
from configparser import ConfigParser

@pytest.fixture(scope="session")
def base_url():
    config = ConfigParser()
    config.read('config.ini')
    print(config.get('API', 'base_url'))
    return config.get('API', 'base_url')

@pytest.fixture(scope="session")
def jwt_token():
    return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NUb2tlbiI6InlhMjkuYTBBZkJfYnlDU1lmNWNwcVdTcXdGU0RYX09mVms2UXI3YXJlUGxKOTBaVEhfQkVjSHNyN2p1Q2IycUNYczJ1Q2MzTXlUbU9qbTNZNGIxWTZzSV9pQ285bjF3dkVXS1NQc2VGQmhscEZsYlI2UTZ2QlB1M0tQZHVNRjAtY244b2czUU9DeDcyRHJDaUdmZW5BdTg2ckE4VmFhR0ZrRHZYdkd4dVVDOWFDZ1lLQWNFU0FROFNGUUhHWDJNaV9WY0U4c3BSNWRyU2lpbV9VQmZEOGcwMTcxIiwiY3JlYXRlZCI6ZmFsc2UsImlhdCI6MTcwNTAwNjA2OCwiZXhwIjoxNzA1NjEwODY4fQ.owqDYAc7O-aXBXKtNxkE_dOqi1LJ-twzKPB8aEqJ9O8'

@pytest.fixture(scope="session")
def headers(jwt_token):
    return {
        'Authorization': f'Bearer {jwt_token}',
        'Content-Type': 'application/json'
    }
