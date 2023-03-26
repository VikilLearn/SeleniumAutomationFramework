# conftest_167: Generate html test report.
# Cmd line - py.test -v test_class_demo2_165_ref.py --browser chrome --html=report1.html
# "-s": This option enables outputting print statements from the tests to the console.  But this does not print on html
# "-v": This option enables verbose output, meaning that pytest will print more detailed information about the tests that are run.
    #   Specifically, pytest will print the names of each test being run, and whether each test passed or failed.

# If you want to run the cases from start i.e. opening the browser and routing it to desired location then do not use oneTimeSetup at class level (i.e. scope = 'class')
# rather use oneTimeSetup without any scope and on login_tests.py use only the setup which is available in conftest (i.e. @pytest.mark.usefixtures("oneTimeSetUp"))

import time

import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser='chrome'):                ## Adding default value to browser allows us to run on pycharm and debug here if needed.
    print("Running one time setUp")

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")
    time.sleep(1)

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")