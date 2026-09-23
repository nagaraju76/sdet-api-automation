# SDET API Automation Challenge

API automation test suite for the public JSONPlaceholder Posts API using Python, Pytest, and Requests.

## API Under Test

Base URL:

https://jsonplaceholder.typicode.com

The current test suite covers:

- Getting all posts
- Getting a single post
- Response status validation
- Response content type validation
- Response structure validation
- Response data type validation

## Tech Stack

- Python 3
- Pytest
- Requests
- REST API
- Git

## Project Structure


sdet-api-automation/
├── api/
│   ├── __init__.py
│   └── posts_api.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_posts.py
├── utils/
│   ├── __init__.py
│   └── constants.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md

Setup
Prerequisites
- Python 3.8 or higher
- Git
Clone the repository
git clone https://github.com/nagaraju76/sdet-api-automation.git
cd sdet-api-automation

Create a virtual environment
Windows:
python -m venv .venv
.venv\Scripts\activate

Linux/macOS:
python3 -m venv .venv
source .venv/bin/activate

Install dependencies
python -m pip install -r requirements.txt

Run Tests
Run all tests:
pytest

Run with verbose output:
pytest -v

Test Scenarios
The first version of the test suite contains 4 tests.
Get All Posts
Validates:
- HTTP status code is 200
- Response content type is JSON
- Response is a list
- Expected number of posts is returned
Validate Post Structure and Data Types
Validates that each post contains:
- userId
- id
- title
- body
The test also validates the expected data types and basic positive values for IDs.
Get Post by Valid ID
Uses a valid post ID and validates:
- HTTP status code is 200
- Expected fields are present
- Returned post ID matches the requested ID


Expected Result
A successful test execution should show:
4 passed


