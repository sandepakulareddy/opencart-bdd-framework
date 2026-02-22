# OpenCart BDD Framework

Python-based test automation framework that combines:
- UI test flow for OpenCart demo site using Selenium + `pytest-bdd`
- API CRUD/negative testing for Swagger Petstore using `requests` + `pytest`

## Tech Stack

- Python 3.10+
- pytest
- pytest-bdd
- Selenium WebDriver
- requests

## Project Structure

```text
opencart-bdd-framework/
|-- features/
|   `-- checkout.feature
|-- pages/
|   |-- base_page.py
|   |-- home_page.py
|   |-- cart_page.py
|   `-- checkout_page.py
|-- tests/
|   |-- test_checkout_steps.py
|   |-- test_pet_crud.py
|   `-- test_negative_cases.py
|-- utils/
|   |-- api_client.py
|   `-- config.py
|-- conftest.py
|-- requirements.txt
`-- README.md
```

## What Is Covered

### UI BDD Scenario

Feature file: `features/checkout.feature`

Flow covered:
1. Open OpenCart demo home page
2. Select product (`MacBook`)
3. Add product to cart
4. Proceed to checkout

### API Tests

API client: `utils/api_client.py`
Base URL: `https://petstore.swagger.io/v2`

Covered API validations:
- Create, read, update, delete pet (`tests/test_pet_crud.py`)
- Negative scenarios for non-existing/invalid data (`tests/test_negative_cases.py`)

## Setup

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

## Run Tests

### Run all tests

```powershell
pytest -v
```

### Run only UI BDD tests

```powershell
pytest tests/test_checkout_steps.py -v
```

### Run only API tests

```powershell
pytest tests/test_pet_crud.py tests/test_negative_cases.py -v
```

### Run tests on a specific browser

Supported via `conftest.py`: `chrome`, `firefox`, `edge`

```powershell
pytest tests/test_checkout_steps.py --browser chrome -v
```

## Notes

- UI tests require a locally available browser driver (`chromedriver`, `geckodriver`, or `msedgedriver`) accessible on your system PATH.
- UI scenario uses `https://tutorialsninja.com/demo/`.
- API tests hit a public demo service; occasional external instability can affect results.

## Troubleshooting

- `Browser not supported`: pass one of `--browser chrome|firefox|edge`
- `WebDriver` errors: ensure matching browser/driver versions and PATH setup
- API failures with 5xx/timeout: retry later; public sandbox service may be unstable

## Future Improvements

- Add environment-based config (`.env` or config file) for UI/API endpoints
- Add HTML/JUnit reports in CI
- Add explicit assertions for checkout page verification step in BDD flow
- Add test data management for stable API IDs
