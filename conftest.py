import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, edge"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
