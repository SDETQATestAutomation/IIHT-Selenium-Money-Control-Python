'''
Created on 29-Oct-2023

@author: pranjan
'''
import math

import pytest
import os
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from root_path import get_project_root
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.main.pyhton.com.iiht.evaluation.automation import Helpers
from src.main.pyhton.com.iiht.evaluation.automation.SubActivities import SubActivities
from src.main.pyhton.com.iiht.evaluation.automation.Activities import Activities
from src.test.python.com.iiht.evaluation.automation.locators.object_repository import money_control_element
from src.test.python.com.iiht.evaluation.automation.testutils.MasterData import MasterData
from src.test.python.com.iiht.evaluation.automation.testutils.TestUtils import TestUtils


@pytest.fixture()
def driver(request):
    print("\nBefore method setup")
    req_root_path = get_project_root()
    print(f"${req_root_path}")
    req_chrome_driver_path = req_root_path + "/binaries/chromedriver.exe"
    print(f"{req_chrome_driver_path}")
    base_url = "https://www.moneycontrol.com/"
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
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")

    options.set_capability("goog:loggingPrefs", {'driver': 'INFO', 'server': 'OFF', 'browser': 'INFO'})
    options.set_capability("elementScrollBehavior", 1)
    options.set_capability("acceptInsecureCerts", True)
    options.set_capability("javascriptEnabled", True)
    service = Service(req_chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(15)
    # driver.get(base_url)
    SubActivities.check_page_load_complete(driver)
    try:
        print("\nAfter method setup")
        yield driver
    finally:
        driver.quit()
    return driver


def test_login(driver):
    Activities.open_login_panel(driver)
    Activities.open_signin_box(driver)
    Activities.signin_box_enter_email(driver, "prashant.ranjan.qa@gmail.com")
    Activities.signin_box_enter_password(driver, "igetup@7AM")
    Activities.signin_box_click_login_button(driver)
    Activities.check_logged_in_user(driver, "Prashant.ranjan.qa@gmail.com")
    # Activities.signin_box_check_error(driver, "Invalid User Id/EmailID or Password. Please try again.")
# select_submenu_from_menu(driver, "Personal Finance", "Fixed Deposit Interest Calculator")
# fixed_deposit_calculator_enter_investment_amount(driver, 300000)
# fixed_deposit_calculator_enter_investment_period(driver, 5)
# fixed_deposit_calculator_enter_rate_of_return(driver, 12)
# fixed_deposit_calculator_select_interest_frequency(driver, "Monthly")
# fixed_deposit_calculator_enter_tax_rate(driver, 15)
# fixed_deposit_calculator_click_submit_button(driver)
# fixed_deposit_calculator_check_total_payment(driver, "300,000.00")
# fixed_deposit_calculator_check_total_interest(driver, "245,009.01")
# fixed_deposit_calculator_check_total_corpus(driver, "545,009.01")
# fixed_deposit_calculator_check_post_tax_amount(driver, "506,787.60")
# fixed_deposit_calculator_check_investment_amount(driver,"10000000")
# fixed_deposit_calculator_check_investment_period(driver,"10")
# fixed_deposit_calculator_check_rate_of_return(driver,"10")
# fixed_deposit_calculator_check_tax_rate(driver,"15")
