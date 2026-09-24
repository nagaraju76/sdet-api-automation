# SDET API Automation Challenge

API automation test suite for the public JSONPlaceholder Posts API using Python, Pytest, and Requests.

## API Under Test

Base URL:

https://jsonplaceholder.typicode.com

The test suite covers:

- Getting all posts
- Getting a single post
- Response status validation
- Response content type validation
- Response structure validation
- Response data type validation
- Non-existent post
- Invalid post ID
- Negative post ID

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

Clone the Repository
git clone https://github.com/nagaraju76/sdet-api-automation.git
cd sdet-api-automation
Create a Virtual Environment

Windows:

python -m venv .venv
.venv\Scripts\activate

Linux/macOS:

python3 -m venv .venv
source .venv/bin/activate
Install Dependencies
python -m pip install -r requirements.txt
Run Tests

Run all tests:

pytest

Run with verbose output:

pytest -v
Test Scenarios

The test suite contains 7 tests.

Get All Posts

Validates:

HTTP status code is 200
Response content type is JSON
Response is a list
Expected number of posts is returned
Validate Post Structure and Data Types

Validates that each post contains:

userId
id
title
body

The test also validates the expected data types and basic positive values for IDs.

Get Post by Valid ID

Uses a valid post ID and validates:

HTTP status code is 200
Expected fields are present
Returned post ID matches the requested ID
Negative Scenarios

The suite also covers invalid resource requests.

Non-existent Post ID

Uses a post ID that does not exist and validates:

HTTP status code is 404
Invalid Post ID

Uses a non-numeric post ID such as abc and validates:

HTTP status code is 404
Negative Post ID

Uses -1 and validates:

HTTP status code is 404


Design Approach

The API request logic is separated from the test cases.

API Layer

api/posts_api.py contains the API client and request methods.

The tests use the API client instead of directly calling requests.get().

Test Layer

tests/test_posts.py contains the test scenarios and assertions.

The tests focus on validating API behavior and responses.

Fixtures

tests/conftest.py provides the PostsAPI object through a Pytest fixture.

This allows the API client to be reused across tests.

Constants

utils/constants.py contains common test values such as:

Expected post count
Valid post ID
Non-existent post ID
Expected response fields

Keeping these values in one place makes the tests easier to maintain.

Negative Testing

Negative scenarios are included to verify how the API behaves when the requested resource is invalid or unavailable.

The current negative scenarios are:

Non-existent post ID
Non-numeric post ID
Negative post ID

The expected behavior was verified against the public API.

Maintainability

The framework follows a simple separation:

Test Cases
    |
    v
PostsAPI Client
    |
    v
JSONPlaceholder API
