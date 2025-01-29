from tests.fixtures.api_fixture import api_client
from tests.fixtures.api_fixture import api_delete
from tests.fixtures.api_fixture import api_post
from tests.fixtures.api_fixture import api_put
from tests.helpers.api_request_helpers import get_email_and_password_params
from tests.helpers.api_request_helpers import get_user_account_request_params

_CREATE_ACCOUNT_URL = "createAccount"
_DELETE_ACCOUNT_URL = "deleteAccount"
_UPDATE_ACCOUNT_URL = "updateAccount"


# POST user account creation

def test_post_create_account_success(api_client, api_post):
    """Test successful account creation."""
    request_params = get_user_account_request_params()
    response = api_post(_CREATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 200
    response_json = response.json()

    print(response_json)
    assert response_json["responseCode"] == 200
    assert response_json["message"] == "User created!"


def test_post_create_account_missing_required_parameters_bad_request(api_client, api_post):
    """Test trying to create account with missing required parameters."""
    request_params = get_user_account_request_params(name=None)
    response = api_post(_CREATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400


def test_post_create_account_missing_required_parameters_response_bad_request(api_client, api_post):
    """Test trying to create account with missing required parameters."""
    request_params = get_user_account_request_params(name=None)
    response = api_post(_CREATE_ACCOUNT_URL, request_params=request_params)

    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, name parameter is missing in POST request."


def test_post_create_account_invalid_email_format(api_client, api_post):
    """Test trying to create account with invalid email format."""
    request_params = get_user_account_request_params(email="invalid.email")
    response = api_post(_CREATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, Invalid email address."


def test_post_create_account_password_too_short(api_client, api_post):
    """Test trying to create account with password that is too short."""
    request_params = get_user_account_request_params(password="short")
    response = api_post(_CREATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, Password too short."


def test_post_create_account_invalid_birth_date(api_client, api_post):
    """Test trying to create account with invalid birthdate."""
    request_params = get_user_account_request_params(birth_date="-2")
    response = api_post(_CREATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, Invalid birth date"


def test_post_create_account_missing_country(api_client, api_post):
    """Test trying to create account with missing country parameter."""
    request_params = get_user_account_request_params(country=None)
    response = api_post(_CREATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, Country is required"


def test_post_create_account_missing_zipcode(api_client, api_post):
    """Test trying to create account with missing zipcode parameter."""
    request_params = get_user_account_request_params(zipcode=None)
    response = api_post(_CREATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, Zipcode is required"


# DELETE user account

def test_delete_account_success(api_client, api_delete):
    """Test successful account deletion."""
    request_params = get_email_and_password_params()
    response = api_delete(_DELETE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    assert response_json["message"] == "Account deleted!"


def test_delete_account_non_existent_email(api_client, api_delete):
    """Test using non-existent email for account deletion."""
    request_params = get_email_and_password_params(email="nonexistent@mail.com")
    response = api_delete(_DELETE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["message"] == "Bad request, Email not found"


def test_delete_account_missing_email(api_client, api_delete):
    """Test trying to delete account with missing email parameter."""
    request_params = get_email_and_password_params(email=None)
    response = api_delete(_DELETE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, email parameter is missing in DELETE request."


def test_delete_account_missing_password(api_client, api_delete):
    """Test trying to delete account with missing password parameter."""
    request_params = get_email_and_password_params(password=None)
    response = api_delete(_DELETE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, password parameter is missing in DELETE request."


# PUT user account

def test_put_update_account_success(api_client, api_put):
    """Test successful account update."""
    request_params = get_user_account_request_params()
    response = api_put(_UPDATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    assert response_json["message"] == "User updated!"


def test_put_update_account_invalid_email(api_client, api_put):
    """Test trying to update account with invalid email format."""
    request_params = get_user_account_request_params(email="invalid.email")
    response = api_put(_UPDATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, Invalid email format"


def test_put_update_account_missing_name(api_client, api_put):
    """Test trying to update account with missing name parameter."""
    request_params = get_user_account_request_params(name=None)
    response = api_put(_UPDATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Name is required"


def test_put_update_account_missing_email_status_code_400(api_client, api_put):
    """Test trying to update account with missing email parameter returns code 400."""
    request_params = get_user_account_request_params(email=None)
    response = api_put(_UPDATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400


def test_put_update_account_missing_email_response_bad_request(api_client, api_put):
    """Test trying to update account with missing email parameter returns bad request response."""
    request_params = get_user_account_request_params(email=None)
    response = api_put(_UPDATE_ACCOUNT_URL, request_params=request_params)

    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, email parameter is missing in PUT request."


def test_put_update_account_missing_password_status_code_400(api_client, api_put):
    """Test trying to update account with missing password parameter returns code 400."""
    request_params = get_user_account_request_params(password=None)
    response = api_put(_UPDATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400


def test_put_update_account_missing_password_response_bad_request(api_client, api_put):
    """Test trying to update account with missing password parameter returns bad request response."""
    request_params = get_user_account_request_params(password=None)
    response = api_put(_UPDATE_ACCOUNT_URL, request_params=request_params)

    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, password parameter is missing in PUT request."


def test_put_update_account_invalid_country_response_bad_request(api_client, api_put):
    """Test trying to update account with invalid country returns bad request response."""
    request_params = get_user_account_request_params(country="InvalidCountry")

    response = api_put(_UPDATE_ACCOUNT_URL, request_params=request_params)

    assert response.status_code == 400
    response_json = response.json()
    assert response_json["responseCode"] == 400
    assert response_json["message"] == "Bad request, Invalid country"
