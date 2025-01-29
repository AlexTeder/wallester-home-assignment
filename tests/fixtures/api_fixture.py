import pytest
import requests
from urllib.parse import urlencode

BASE_URL = "https://automationexercise.com/api/"


@pytest.fixture(scope="session")
def api_client():
    """Fixture to create a reusable API client for sending HTTP requests."""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()


@pytest.fixture
def api_get(api_client):
    """Fixture to perform GET call"""

    def _get(url, request_params=None):
        if request_params:
            query_string = urlencode(request_params)
            url_with_params = f"{BASE_URL}/{url}?{query_string}"
        else:
            url_with_params = f"{BASE_URL}/{url}"
        response = api_client.get(url_with_params)
        return response

    return _get


@pytest.fixture
def api_post(api_client):
    """Fixture to perform a dynamic POST call."""

    def _post(url, body=None, request_params=None):
        """Helper function for making POST requests."""
        if body is not None:
            return api_client.post(f"{BASE_URL}/{url}", data=body)
        if request_params is not None:
            return api_client.post(f"{BASE_URL}/{url}?{request_params}")
        return api_client.post(f"{BASE_URL}/{url}")

    return _post


@pytest.fixture
def api_put(api_client):
    """Fixture to perform a dynamic PUT call."""

    def _put(url, body=None, request_params=None):
        full_url = f"{BASE_URL}/{url}"
        if request_params:
            full_url += f"?{request_params}"
        response = api_client.put(full_url, data=body)
        return response

    return _put


@pytest.fixture
def api_delete(api_client):
    """Fixture to perform a dynamic DELETE call."""

    def _delete(url, request_params=None):
        """Helper function for making DELETE requests."""
        if request_params is not None:
            return api_client.delete(f"{BASE_URL}/{url}?{request_params}")
        return api_client.delete(f"{BASE_URL}/{url}")

    return _delete
