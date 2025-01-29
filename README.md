# Test Automation Home Assignment

Idea of the home assignment was to cover provided application with sufficient test cases.
Application has variety of functionalities described by different methods. For instance, data creation, data deletion, 
data retrieval, etc.

The functionality of the application demonstrates range of issues that in real life scenario could be easily discovered
at the very early stages of development process. Some of the issues are, for example, inconsistent response codes 
in case of status code of response itself and the response code inside the response body.
In addition, insufficient validation for such fields as email, password, etc.
Also, request parameters are not being processed and are simply ignored in the request. Therefore, some parts of the
functionality could not be properly investigated and tested for receivable result.

In addition to the issues mentioned above, the REST structure and practical usage does not follow all the REST principles.
For example in user_account API there are three different endpoints for account creation, deletion and update.
However, in RESTful API, there should be only one endpoint for each entity, and the action should be defined by the HTTP method.

Taking my notes and investigations into account, I have created not only test cases that support existing functionality  
and explains its logic, but also intentionally failing tests that demonstrate the issues mentioned above.

## Technologies
- Python 3.13
- PyTest 8.3.4

## Installation
1. Clone the [repository](https://github.com/AlexTeder/wallester-home-assignment)
2. Create Python virtual environment by running
```
python -m venv your-env
source your-env/bin/activate 
```
### Set up virtual environment in PyCharm
1. Go to File -> Settings -> Project -> Python Interpreter
2. Choose Add Interpreter -> Add Local Interpreter
3. If you have created your own env as described below, choose "Select existing"
4. Otherwise, choose "Generate new one" and specify the path to the Python executable, as well as location for .venv

## Install dependencies
```
pip install -r requirements.txt
```

## Running tests
Run tests
```
pytest
```

Run tests and generate HTML report
```
pytest --html=reports/test_report.html --self-contained-html
```

Run tests with logs
```
pytest -v --log-cli-level=INFO
```

## Ongoing developments
In case if any more plugins/libs have been added during development, the `requirements.txt` file should be updated.

To generate up-to-date requirements.txt
```
pip freeze > requirements.txt 
```