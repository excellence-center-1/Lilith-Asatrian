import pytest
from configparser import ConfigParser
import psycopg2

@pytest.fixture(scope="session")
def config():
    config = ConfigParser()
    config.read('config.ini')
    return config

@pytest.fixture(scope="session")
def base_url(config):
    return config.get('API', 'base_url')

@pytest.fixture(scope="session")
def jwt_token(config):
    return config.get('API', 'jwt_token').strip('"')

@pytest.fixture(scope="session")
def headers(jwt_token):
    return {
        'Authorization': f'Bearer {jwt_token}',
        'Content-Type': 'application/json'
    }

@pytest.fixture(scope="function")
def db_connection(config):
    db_params={
        'dbname': config.get("Database, db_name"),
        'user': config.get("Database, db_user"),
        'password': config.get('Database', 'db_password'),
        'host': config.get('Database', 'db_host'),
        'port': config.get('Database', 'db_port')
    }
    conn = psycopg2.connect(**db_params)
    yield
    conn.close()

@pytest.fixture(scope="function")
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()