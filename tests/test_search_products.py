from tests.fixtures.api_fixture import api_client
from tests.fixtures.api_fixture import api_post

_SEARCH_PRODUCT_URL = "searchProduct"

# Search product tests


def test_post_search_product_without_search_product_parameter_is_forbidden(api_client, api_post):
    """Test sending POST request to /searchProduct without search parameter is not allowed."""
    response = api_post(_SEARCH_PRODUCT_URL)
    assert response.status_code == 400


def test_post_search_product_without_search_product_parameter_response_bad_request(api_client, api_post):
    """Test searching products without search_product parameter returns bad request."""
    response = api_post(_SEARCH_PRODUCT_URL)
    response_json = response.json()
    assert response_json.get('responseCode') == 400
    assert response_json.get('message') == 'Bad request, search_product parameter is missing in POST request.'


def test_post_search_product_jean_returns_products(api_client, api_post):
    """Test searching products with search_product parameter 'jean'."""
    request_params = "search_product=jean"
    response = api_post(_SEARCH_PRODUCT_URL, request_params=request_params)

    assert response.status_code == 200
    response_json = response.json()

    assert response_json.get('responseCode') == 200
    assert "products" in response_json
    assert isinstance(response_json["products"], list)
    assert len(response_json["products"]) > 0
    assert any("jean" in product["name"].lower() for product in response_json["products"])


def test_post_search_product_search_for_unknown_product(api_client, api_post):
    """Test searching for a product that does not exist returns empty result."""
    request_params = "search_product=unknownproduct"
    response = api_post(_SEARCH_PRODUCT_URL, request_params=request_params)

    assert response.status_code == 200
    response_json = response.json()

    assert response_json.get('responseCode') == 200
    assert "products" in response_json
    assert isinstance(response_json["products"], list)
    assert len(response_json["products"]) == 0


def test_post_search_product_empty_value_parameter(api_client, api_post):
    """Test searching with an empty query string returns empty result."""
    request_params = "search_product=''"
    response = api_post(_SEARCH_PRODUCT_URL, request_params=request_params)

    assert response.status_code == 200
    response_json = response.json()

    assert response_json["responseCode"] == 200
    assert "products" in response_json
    assert isinstance(response_json["products"], list)


def test_post_search_product_parameter_as_numeric_input_is_allowed(api_client, api_post):
    """Test searching with a numeric value provides OK response with empy result."""
    request_params = "search_product=12345"
    response = api_post(_SEARCH_PRODUCT_URL, request_params=request_params)

    assert response.status_code == 200
    response_json = response.json()

    assert response_json["responseCode"] == 200
    assert "products" in response_json
    assert isinstance(response_json["products"], list)
    assert len(response_json["products"]) == 0


def test_post_search_product_parameter_case_insensitive_should_return_result(api_client, api_post):
    """Test searching with different letter casing to ensure case insensitivity."""
    request_params = "search_product=JeAn"
    response = api_post(_SEARCH_PRODUCT_URL, request_params=request_params)

    assert response.status_code == 200
    response_json = response.json()

    assert response_json["responseCode"] == 200
    assert "products" in response_json
    assert isinstance(response_json["products"], list)
    assert len(response_json["products"]) > 0
    assert any("jean" in product["name"].lower() for product in response_json["products"])
