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


def test_success_login(driver, email="prashant.ranjan.qa@gmail.com", password="igetup@7AM"):
    testcase_status = True
    try:
        open_login_panel_succeed = Activities.open_login_panel(driver)
        print(f"open_login_panel_succeed {open_login_panel_succeed}")
        if not open_login_panel_succeed:
            testcase_status = False
        if testcase_status:
            open_signin_box_succeed = Activities.open_signin_box(driver)
            print(f"open_signin_box_succeed {open_signin_box_succeed}")
            if not open_signin_box_succeed:
                testcase_status = False
        if testcase_status:
            signin_box_enter_email_succeed = Activities.signin_box_enter_email(driver, email)
            print(f"signin_box_enter_email_succeed {signin_box_enter_email_succeed}")
            if not signin_box_enter_email_succeed:
                testcase_status = False
        if testcase_status:
            signin_box_enter_password_succeed = Activities.signin_box_enter_password(driver, password)
            print(f"signin_box_enter_password_succeed {signin_box_enter_password_succeed}")
            if not signin_box_enter_password_succeed:
                testcase_status = False
        if testcase_status:
            signin_box_click_login_button_succeed = Activities.signin_box_click_login_button(driver)
            print(f"signin_box_click_login_button_succeed {signin_box_click_login_button_succeed}")
            if not signin_box_click_login_button_succeed:
                testcase_status = False
        if testcase_status:
            check_logged_in_user_succeed = Activities.check_logged_in_user(driver, email)
            print(f"check_logged_in_user_succeed {check_logged_in_user_succeed}")
            if not check_logged_in_user_succeed:
                testcase_status = False
        print(f"testcase_status {testcase_status}")

    except Exception as ex:
        print(ex)


def test_failure_login(driver, email="prashant.ranjan.qa@gmail.commmmm", password="igetup@7AMmmmmmm",error_message="Invalid User Id/EmailID or Password. Please try again."):
    testcase_status = True
    try:
        open_login_panel_succeed = Activities.open_login_panel(driver)
        print(f"open_login_panel_succeed {open_login_panel_succeed}")
        if not open_login_panel_succeed:
            testcase_status = False
        if testcase_status:
            open_signin_box_succeed = Activities.open_signin_box(driver)
            print(f"open_signin_box_succeed {open_signin_box_succeed}")
            if not open_signin_box_succeed:
                testcase_status = False
        if testcase_status:
            signin_box_enter_email_succeed = Activities.signin_box_enter_email(driver, email)
            print(f"signin_box_enter_email_succeed {signin_box_enter_email_succeed}")
            if not signin_box_enter_email_succeed:
                testcase_status = False
        if testcase_status:
            signin_box_enter_password_succeed = Activities.signin_box_enter_password(driver, password)
            print(f"signin_box_enter_password_succeed {signin_box_enter_password_succeed}")
            if not signin_box_enter_password_succeed:
                testcase_status = False
        if testcase_status:
            signin_box_click_login_button_except_error_succeed = Activities.signin_box_click_login_button_except_error(driver)
            print(f"signin_box_click_login_button_except_error_succeed {signin_box_click_login_button_except_error_succeed}")
            if not signin_box_click_login_button_except_error_succeed:
                testcase_status = False
        if testcase_status:
            signin_box_check_error_succeed = Activities.signin_box_check_error(driver, error_message)
            print(f"signin_box_check_error_succeed {signin_box_check_error_succeed}")
            if not signin_box_check_error_succeed:
                testcase_status = False
        print(f"testcase_status {testcase_status}")

    except Exception as ex:
        print(ex)
