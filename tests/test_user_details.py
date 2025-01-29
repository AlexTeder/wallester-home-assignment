import json
import pytest

from tests.fixtures.api_fixture import api_client
from tests.fixtures.api_fixture import api_get
from tests.helpers.api_request_helpers import get_call_status_200_return_json

_GET_USER_DETAIL_URL = "getUserDetailByEmail"


def test_get_user_details_success(api_client, api_get):
    """Test getting user details by email user exists."""
    params = {"email": "email"}
    response_json = get_call_status_200_return_json(api_get, _GET_USER_DETAIL_URL, params)

    assert response_json.get('responseCode') == 200
    assert isinstance(response_json.get('user'), dict)


def test_get_user_details_valid_email_returns_user_data(api_client, api_get):
    """Test getting user details by email result is correct."""
    params = {"email": "email"}
    response_json = get_call_status_200_return_json(api_get, _GET_USER_DETAIL_URL, params)

    assert response_json.get('responseCode') == 200
    assert isinstance(response_json.get('user'), dict)
    assert response_json['user'] == json.loads("""
    {
      "id": 5911,
      "name": "user",
      "email": "email",
      "title": "Mr",
      "birth_day": "13/10/97",
      "birth_month": "10",
      "birth_year": "1997",
      "first_name": "Fran",
      "last_name": "Saez",
      "company": "Everis",
      "address1": "alameda",
      "address2": "de la iglesia",
      "country": "España",
      "state": "Albacete",
      "city": "Hellin",
      "zipcode": "02409"
    }
    """)


def test_get_user_details_missing_email_status_code_400(api_client, api_get):
    """Test trying to get user details with missing email status code 400."""
    response = api_get(_GET_USER_DETAIL_URL)
    assert response.status_code == 400


def test_get_user_details_missing_email_response_bad_request(api_client, api_get):
    """Test trying to get user details with missing email returns response bad request."""
    response = api_get(_GET_USER_DETAIL_URL)

    response_json = response.json()
    assert response_json.get('responseCode') == 400
    assert response_json.get('message') == 'Bad request, email parameter is missing in GET request.'


def test_get_user_details_email_not_found_status_code_400(api_client, api_get):
    """Trying to get user details by non-existent email returns status code 400."""
    params = {"email": "nonexistentemail@example.com"}
    response = api_get(_GET_USER_DETAIL_URL, params)

    assert response.status_code == 404


def test_get_user_details_email_not_found_response(api_client, api_get):
    """Trying to get user details by non-existent email returns not found response."""
    params = {"email": "nonexistentemail@example.com"}
    response = api_get(_GET_USER_DETAIL_URL, params)

    response_json = response.json()
    assert response_json.get('responseCode') == 404
    assert response_json.get('message') == 'Account not found with this email, try another email!'


def test_get_user_details_invalid_email_format_no_user_data(api_client, api_get):
    """Trying to get user details with invalid email returns no user data."""
    params = {"email": "invalid-email-format"}
    response_json = get_call_status_200_return_json(api_get, _GET_USER_DETAIL_URL, params)

    assert response_json.get('responseCode') != 200
    assert 'user' not in response_json


@pytest.mark.parametrize(
    "field",
    [
        ("id"),
        ("name"),
        ("email"),
        ("first_name"),
        ("last_name"),
        ("birth_day"),
        ("company")
    ]
)
def test_get_user_details_response_fields_are_present(api_client, api_get, field):
    """Test getting user details user data contains expected fields:
     id, name, email, first_name, last_name, birth_day, company."""
    params = {"email": "email"}
    response_json = get_call_status_200_return_json(api_get, _GET_USER_DETAIL_URL, params)

    user_data = response_json.get('user')
    assert field in user_data


def test_get_user_details_invalid_request_parameter_status_code_400(api_client, api_get):
    """Test trying to get user data by invalid request parameter returns bad request status code 400."""
    params = {"invalid_param": "value"}
    response = api_get(_GET_USER_DETAIL_URL, params)

    assert response.status_code == 400


def test_get_user_details_invalid_request_parameter_empty_response(api_client, api_get):
    """Test trying to get user data by invalid request parameter returns status code 400 bad request empty response."""
    params = {"invalid_param": "value"}
    response = api_get(_GET_USER_DETAIL_URL, params)

    response_json = response.json()
    assert response_json.get('responseCode') == 400
    assert 'user' not in response_json


def test_get_user_details_correct_case_insensitive_email_returns_data(api_client, api_get):
    """Test trying to get user data by valid email in different case returns user data."""
    params = {"email": "EMAIL"}
    response_json = get_call_status_200_return_json(api_get, _GET_USER_DETAIL_URL, params)

    assert response_json.get('responseCode') == 200
    assert isinstance(response_json.get('user'), dict)
    assert response_json['user'].get('email').lower() == "email"
