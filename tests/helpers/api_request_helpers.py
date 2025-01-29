def get_call_status_200_return_json(api_get, url, params=None):
    response = api_get(url, request_params=params)
    assert response.status_code == 200
    return response.json()


def get_user_account_request_params(name=None, email=None, password=None, birth_date=None, country=None, zipcode=None):
    """Helper function to generate request params dynamically."""
    return {
        "name": name or "Alex Doe",
        "email": email or "valid@example.com",
        "password": password or "validPassword123",
        "title": "Mr",
        "birth_date": birth_date or "15",
        "birth_month": "March",
        "birth_year": "1994",
        "firstname": "Alex",
        "lastname": "Doe",
        "company": "Example Corp",
        "address1": "123 Example St.",
        "address2": "Suite 101",
        "country": country or "Estonia",
        "zipcode": zipcode or "12345",
        "state": "Harju",
        "city": "Tallinn",
        "mobile_number": "+12345671890"
    }


def get_email_and_password_params(email=None, password=None):
    """Helper function to generate request params dynamically."""
    return {
        "email": email or "valid@example.com",
        "password": password or "validPassword123",
    }
