from tests.fixtures.api_fixture import api_client
from tests.fixtures.api_fixture import api_get
from tests.fixtures.api_fixture import api_post
from tests.helpers.api_request_helpers import get_call_status_200_return_json
import pytest
import re

_PRODUCTS_LIST_URL = "productsList"


# GET products

def test_get_products_returns_all_products_list(api_client, api_get):
    """Test getting all products returns list of all products."""
    response_json = get_call_status_200_return_json(api_get, _PRODUCTS_LIST_URL)
    assert response_json.get('responseCode') == 200
    assert isinstance(response_json.get('products'), list)


def test_get_products_non_empty_products_list(api_client, api_get):
    """Test getting all products list returns non-empty list of products."""
    response_json = get_call_status_200_return_json(api_get, _PRODUCTS_LIST_URL)

    products_list = response_json.get('products', [])
    assert len(products_list) > 0, "Expected at least one product in the response"


@pytest.mark.parametrize("field", ["id", "name", "price", "brand", "category"])
def test_get_products_each_product_has_expected_fields(api_client, api_get, field):
    """Test that each product has the expected fields: if, name, price, brand and category."""
    response_json = get_call_status_200_return_json(api_get, _PRODUCTS_LIST_URL)

    for product in response_json.get('products', []):
        assert field in product, f"Missing '{field}' field in product"


@pytest.mark.parametrize("nested_field", ["usertype", "category"])
def test_get_products_each_product_category_contains_expected_fields(api_client, api_get, nested_field):
    """Test that each product's category contains the expected fields: usertype, category."""
    response_json = get_call_status_200_return_json(api_get, _PRODUCTS_LIST_URL)

    for product in response_json.get('products', []):
        assert 'category' in product, "Missing 'category' field in product"
        assert isinstance(product['category'], dict), "Field 'category' should be of dict type"
        assert nested_field in product['category'], f"Missing '{nested_field}' in category"


def test_get_products_price_format_is_correct(api_client, api_get):
    """Test that the price field follows the expected format (Rs. <amount>)."""
    response_json = get_call_status_200_return_json(api_get, _PRODUCTS_LIST_URL)

    # Check the price format (example: Rs. 500)
    for product in response_json.get('products', []):
        assert re.match(r"^Rs\.\s\d+(\.\d{1,2})?$", product['price']), \
            f"Invalid price format: {product['price']}, expected Rs. <amount>"


def test_get_products_each_product_has_positive_price_value(api_client, api_get):
    """Test that all prices of each product are positive numbers."""
    response_json = get_call_status_200_return_json(api_get, _PRODUCTS_LIST_URL)

    for product in response_json.get('products', []):
        price = product['price']
        price_value = float(price.split()[1])  # Extract the numeric value from the 'Rs. <amount>'
        assert price_value > 0, f"Price for product {product['name']} is not positive: {price_value}"


def test_get_products_each_product_has_unique_product_id(api_client, api_get):
    """Test that all each product's ID is unique."""
    response_json = get_call_status_200_return_json(api_get, _PRODUCTS_LIST_URL)

    product_ids = [product['id'] for product in response_json.get('products', [])]
    assert len(product_ids) == len(set(product_ids)), "Product IDs are not unique"


# POST to all product list tests

def test_post_products_list_method_is_not_allowed_status_code_405(api_client, api_post):
    """Test that POST request to /productsList is not allowed."""
    response = api_post(_PRODUCTS_LIST_URL)

    assert response.status_code == 405


def test_post_products_list_error_response_method_not_supported(api_client, api_post):
    """Test that POST request to /productsList is not allowed."""
    response = api_post(_PRODUCTS_LIST_URL)
    response_json = response.json()

    assert response_json.get('responseCode') == 405
    assert response_json.get('message') == 'This request method is not supported.'
