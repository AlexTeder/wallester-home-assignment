from tests.fixtures.api_fixture import api_client
from tests.fixtures.api_fixture import api_get
from tests.fixtures.api_fixture import api_put
from tests.helpers.api_request_helpers import get_call_status_200_return_json

# GET brands

_BRANDS_LIST_URL = "brandsList"


def test_get_brands_response_code_200_get_brands_list(api_client, api_get):
    """Test fetching all brands list."""
    response_json = get_call_status_200_return_json(api_get, _BRANDS_LIST_URL)
    assert response_json.get('responseCode') == 200
    assert isinstance(response_json.get('brands'), list)


def test_get_brands_number_of_brands_in_response_greater_than_zero(api_client, api_get):
    """Test that the number of brands returned in the response is greater than 0"""
    response_json = get_call_status_200_return_json(api_get, _BRANDS_LIST_URL)
    assert len(response_json['brands']) > 0


def test_get_brands_all_names_should_be_unique(api_client, api_get):
    """Test that brand names in the response are unique."""
    response_json = get_call_status_200_return_json(api_get, _BRANDS_LIST_URL)
    brands = [brand['brand'] for brand in response_json['brands']]
    assert len(brands) == len(set(brands))


def test_get_brands_ids_are_positive_integers(api_client, api_get):
    """Test that all brand IDs are positive integers."""
    response_json = get_call_status_200_return_json(api_get, _BRANDS_LIST_URL)
    for brand in response_json['brands']:
        assert isinstance(brand['id'], int)
        assert brand['id'] > 0


def test_get_brands_names_are_non_empty_strings(api_client, api_get):
    """Test that brand names are strings."""
    response_json = get_call_status_200_return_json(api_get, _BRANDS_LIST_URL)
    for brand in response_json['brands']:
        assert isinstance(brand['brand'], str)
        assert len(brand['brand']) > 0


def test_get_brands_polo_brand_in_response(api_client, api_get):
    """Test that Polo brand exists in the response."""
    response_json = get_call_status_200_return_json(api_get, _BRANDS_LIST_URL)
    brands = [brand['brand'] for brand in response_json['brands']]
    assert 'Polo' in brands


# PUT brands

def test_put_brands_method_is_not_allowed_status_code(api_client, api_put):
    """Test that PUT request to /brandsList is not allowed."""
    response = api_put(_BRANDS_LIST_URL)
    assert response.status_code == 405


def test_put_brands_error_response_is_accurate(api_client, api_put):
    """Test that PUT request to /brandsList is not allowed."""
    response = api_put(_BRANDS_LIST_URL)
    response_json = response.json()
    assert response_json.get('responseCode') == 405
    assert response_json.get('message') == 'This request method is not supported.'


def test_put_brands_response_content_type_is_json(api_client, api_put):
    """Test that the response content type is JSON."""
    response = api_put(_BRANDS_LIST_URL)
    assert response.headers.get('Content-Type') == 'application/json; charset=utf-8'


def test_put_brands_response_content_type_is_html(api_client, api_put):
    """Test that the response content type is text/html."""
    response = api_put(_BRANDS_LIST_URL)
    assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'
