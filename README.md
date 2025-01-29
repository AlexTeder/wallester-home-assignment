# Test Automation Home Assignment

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