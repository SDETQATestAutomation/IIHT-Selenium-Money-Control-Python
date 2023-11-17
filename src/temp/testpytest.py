
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.main.root_path import get_project_root



@pytest.fixture(scope="session")
def driver(request):
    root = get_project_root()
    print(f"${root}")
    req_chrome_driver_path=root+"/src/binaries/chromedriver.exe"
    print(f"${req_chrome_driver_path}")
    baseUrl = "https://www.moneycontrol.com/"
    options = Options()
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-cross-origin-auth-prompt")
    options.add_argument("--allow-control-allow-origin")
    options.add_argument("-–allow-file-access-from-files")
    options.add_argument("--test-type")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
    options.add_argument("--lang=en")
    options.add_argument("--no-sandbox")
    options.add_argument("disable-popup-blocking")

    options.set_capability("goog:loggingPrefs", {'driver': 'INFO','server': 'OFF','browser': 'INFO'})
    options.set_capability("elementScrollBehavior", 1)
    options.set_capability("acceptInsecureCerts", True)
    options.set_capability("javascriptEnabled", True)
    service = Service("req_chrome_driver_path")
    driver = webdriver.Chrome(service=service,options=options)
    driver.implicitly_wait(15)
    driver.get(baseUrl)
    def teardown():
        # Quit chromedriver
        driver.quit()

    request.addfinalizer(teardown)
    return driver

@pytest.fixture(autouse=True)
def setup_teardown(driver):
    # Executes before each test
    # Add any setup steps here
    yield

    # Executes after each test
    # Add any teardown steps here

@pytest.mark.parametrize("test_input", ["Test 1", "Test 2"])
def test_example(driver, test_input):
    # Your test code here
    print(f"Running {test_input}")
    # driver.get("https://www.example.com")
    # assert driver.title == "Example Domain"

def test_google(driver):
    # Test accessing Google
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_search(driver):
    # Test searching on Google
    driver.get("https://www.google.com")
    search_input = driver.find_element("name", "q")
    search_input.send_keys("Selenium")
    search_input.submit()
    assert "Selenium" in driver.title

if __name__ == "__main__":
    pytest.main()