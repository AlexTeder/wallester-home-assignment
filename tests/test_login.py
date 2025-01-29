from tests.fixtures.api_fixture import api_client
from tests.fixtures.api_fixture import api_post
from tests.fixtures.api_fixture import api_delete
from tests.helpers.api_request_helpers import get_email_and_password_params

_VERIFY_LOGIN_URL = "verifyLogin"


# POST Verify Login

def test_post_verify_valid_login_user_exists(api_client, api_post):
    """Test verify provided login credentials are valid and user exists."""
    request_params = get_email_and_password_params()
    response = api_post(_VERIFY_LOGIN_URL, request_params=request_params)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    assert response_json["message"] == "User exists!"


def test_post_verify_login_non_existent_email(api_client, api_post):
    """Test login with not registered email."""
    request_params = get_email_and_password_params(email="nonexistent@mail.com")
    response = api_post(_VERIFY_LOGIN_URL, request_params=request_params)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 404
    assert response_json["message"] == "User not found!"


def test_post_verify_login_invalid_email_format(api_client, api_post):
    """Test login with invalid format of email."""
    request_params = get_email_and_password_params(email="abc.xyz")
    response = api_post(_VERIFY_LOGIN_URL, request_params=request_params)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Invalid email format!"


def test_post_verify_login_missing_email_status_code_400(api_client, api_post):
    """Test login with missing email."""
    request_params = get_email_and_password_params(email=None)
    response = api_post(_VERIFY_LOGIN_URL, request_params=request_params)

    assert response.status_code == 400


def test_post_verify_login_missing_email_response_bad_request(api_client, api_post):
    """Test login with missing email bad request."""
    request_params = get_email_and_password_params(email=None)
    response = api_post(_VERIFY_LOGIN_URL, request_params=request_params)

    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, email or password parameter is missing in POST request."


def test_post_verify_login_missing_password_status_code_400(api_client, api_post):
    """Test login with missing password."""
    request_params = get_email_and_password_params(password=None)
    response = api_post(_VERIFY_LOGIN_URL, request_params=request_params)

    assert response.status_code == 400


def test_post_verify_login_missing_password_response_bad_request(api_client, api_post):
    """Test login with missing password bad request."""
    request_params = get_email_and_password_params(password=None)
    response = api_post(_VERIFY_LOGIN_URL, request_params=request_params)

    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, email or password parameter is missing in POST request."


# DELETE Verify Login

def test_delete_verify_login_expected_status_code_405(api_client, api_delete):
    """Test verify login DELETE method not supported."""
    response = api_delete(_VERIFY_LOGIN_URL)

    assert response.status_code == 405


def test_delete_verify_login_response_method_not_supported(api_client, api_delete):
    """Test verify login DELETE method not supported."""
    response = api_delete(_VERIFY_LOGIN_URL)

    response_json = response.json()
    assert response_json["responseCode"] == 405
    assert response_json["message"] == "This request method is not supported."
