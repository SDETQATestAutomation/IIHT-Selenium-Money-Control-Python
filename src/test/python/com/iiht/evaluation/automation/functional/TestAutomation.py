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


def test_failure_login(driver, email="prashant.ranjan.qa@gmail.commmmm", password="igetup@7AMmmmmmm",
                       error_message="Invalid User Id/EmailID or Password. Please try again."):
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
            signin_box_click_login_button_except_error_succeed = Activities.signin_box_click_login_button_except_error(
                driver)
            print(
                f"signin_box_click_login_button_except_error_succeed {signin_box_click_login_button_except_error_succeed}")
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


def test_fixed_deposit_calculator_interest_frequency_monthly(driver, investment_amount="2000000",
                                                             investment_period="14", rate_of_return="12",
                                                             interest_frequency="Monthly",
                                                             tax_rate="15", total_payment="2,000,000.00",
                                                             total_interest="8,641,939.64",
                                                             total_corpus="10,641,939.64",
                                                             post_tax_amount="9,293,797.05"):
    testcase_status = True
    try:
        select_submenu_from_menu_succeed = Activities.select_submenu_from_menu(driver, "Personal Finance",
                                                                               "Fixed Deposit Interest Calculator")
        print(f"select_submenu_from_menu_succeed {select_submenu_from_menu_succeed}")
        if not select_submenu_from_menu_succeed:
            testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_investment_amount_succeed = Activities.fixed_deposit_calculator_enter_investment_amount(
                driver, investment_amount)
            print(
                f"fixed_deposit_calculator_enter_investment_amount_succeed {fixed_deposit_calculator_enter_investment_amount_succeed}")
            if not fixed_deposit_calculator_enter_investment_amount_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_investment_period_succeed = Activities.fixed_deposit_calculator_enter_investment_period(
                driver, investment_period)
            print(
                f"fixed_deposit_calculator_enter_investment_period_succeed {fixed_deposit_calculator_enter_investment_period_succeed}")
            if not fixed_deposit_calculator_enter_investment_period_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_rate_of_return_succeed = Activities.fixed_deposit_calculator_enter_rate_of_return(
                driver, rate_of_return)
            print(
                f"fixed_deposit_calculator_enter_rate_of_return_succeed {fixed_deposit_calculator_enter_rate_of_return_succeed}")
            if not fixed_deposit_calculator_enter_rate_of_return_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_select_interest_frequency_succeed = Activities.fixed_deposit_calculator_select_interest_frequency(
                driver, interest_frequency)
            print(
                f"fixed_deposit_calculator_select_interest_frequency_succeed {fixed_deposit_calculator_select_interest_frequency_succeed}")
            if not fixed_deposit_calculator_select_interest_frequency_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_tax_rate_succeed = Activities.fixed_deposit_calculator_enter_tax_rate(driver,
                                                                                                                 tax_rate)
            print(f"fixed_deposit_calculator_enter_tax_rate_succeed {fixed_deposit_calculator_enter_tax_rate_succeed}")
            if not fixed_deposit_calculator_enter_tax_rate_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_click_submit_button_succeed = Activities.fixed_deposit_calculator_click_submit_button(
                driver)
            print(
                f"fixed_deposit_calculator_click_submit_button_succeed {fixed_deposit_calculator_click_submit_button_succeed}")
            if not fixed_deposit_calculator_click_submit_button_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_payment_succeed = Activities.fixed_deposit_calculator_check_total_payment(
                driver, total_payment)
            print(
                f"fixed_deposit_calculator_check_total_payment_succeed {fixed_deposit_calculator_check_total_payment_succeed}")
            if not fixed_deposit_calculator_check_total_payment_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_interest_succeed = Activities.fixed_deposit_calculator_check_total_interest(
                driver, total_interest)
            print(
                f"fixed_deposit_calculator_check_total_interest_succeed {fixed_deposit_calculator_check_total_interest_succeed}")
            if not fixed_deposit_calculator_check_total_interest_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_corpus_succeed = Activities.fixed_deposit_calculator_check_total_corpus(
                driver, total_corpus)
            print(
                f"fixed_deposit_calculator_check_total_corpus_succeed {fixed_deposit_calculator_check_total_corpus_succeed}")
            if not fixed_deposit_calculator_check_total_corpus_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_post_tax_amount_succeed = Activities.fixed_deposit_calculator_check_post_tax_amount(
                driver, post_tax_amount)
            print(
                f"fixed_deposit_calculator_check_post_tax_amount_succeed {fixed_deposit_calculator_check_post_tax_amount_succeed}")
            if not fixed_deposit_calculator_check_post_tax_amount_succeed:
                testcase_status = False
        print(f"testcase_status {testcase_status}")

    except Exception as ex:
        print(ex)


def test_fixed_deposit_calculator_interest_frequency_quaterly(driver, investment_amount="2000000",
                                                              investment_period="14", rate_of_return="12",
                                                              interest_frequency="Quaterly",
                                                              tax_rate="15", total_payment="2,000,000.00",
                                                              total_interest="8,223,373.39",
                                                              total_corpus="10,469,226.10",
                                                              post_tax_amount="9,148,026.83"):
    testcase_status = True
    try:
        select_submenu_from_menu_succeed = Activities.select_submenu_from_menu(driver, "Personal Finance",
                                                                               "Fixed Deposit Interest Calculator")
        print(f"select_submenu_from_menu_succeed {select_submenu_from_menu_succeed}")
        if not select_submenu_from_menu_succeed:
            testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_investment_amount_succeed = Activities.fixed_deposit_calculator_enter_investment_amount(
                driver, investment_amount)
            print(
                f"fixed_deposit_calculator_enter_investment_amount_succeed {fixed_deposit_calculator_enter_investment_amount_succeed}")
            if not fixed_deposit_calculator_enter_investment_amount_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_investment_period_succeed = Activities.fixed_deposit_calculator_enter_investment_period(
                driver, investment_period)
            print(
                f"fixed_deposit_calculator_enter_investment_period_succeed {fixed_deposit_calculator_enter_investment_period_succeed}")
            if not fixed_deposit_calculator_enter_investment_period_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_rate_of_return_succeed = Activities.fixed_deposit_calculator_enter_rate_of_return(
                driver, rate_of_return)
            print(
                f"fixed_deposit_calculator_enter_rate_of_return_succeed {fixed_deposit_calculator_enter_rate_of_return_succeed}")
            if not fixed_deposit_calculator_enter_rate_of_return_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_select_interest_frequency_succeed = Activities.fixed_deposit_calculator_select_interest_frequency(
                driver, interest_frequency)
            print(
                f"fixed_deposit_calculator_select_interest_frequency_succeed {fixed_deposit_calculator_select_interest_frequency_succeed}")
            if not fixed_deposit_calculator_select_interest_frequency_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_tax_rate_succeed = Activities.fixed_deposit_calculator_enter_tax_rate(driver,
                                                                                                                 tax_rate)
            print(f"fixed_deposit_calculator_enter_tax_rate_succeed {fixed_deposit_calculator_enter_tax_rate_succeed}")
            if not fixed_deposit_calculator_enter_tax_rate_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_click_submit_button_succeed = Activities.fixed_deposit_calculator_click_submit_button(
                driver)
            print(
                f"fixed_deposit_calculator_click_submit_button_succeed {fixed_deposit_calculator_click_submit_button_succeed}")
            if not fixed_deposit_calculator_click_submit_button_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_payment_succeed = Activities.fixed_deposit_calculator_check_total_payment(
                driver, total_payment)
            print(
                f"fixed_deposit_calculator_check_total_payment_succeed {fixed_deposit_calculator_check_total_payment_succeed}")
            if not fixed_deposit_calculator_check_total_payment_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_interest_succeed = Activities.fixed_deposit_calculator_check_total_interest(
                driver, total_interest)
            print(
                f"fixed_deposit_calculator_check_total_interest_succeed {fixed_deposit_calculator_check_total_interest_succeed}")
            if not fixed_deposit_calculator_check_total_interest_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_corpus_succeed = Activities.fixed_deposit_calculator_check_total_corpus(
                driver, total_corpus)
            print(
                f"fixed_deposit_calculator_check_total_corpus_succeed {fixed_deposit_calculator_check_total_corpus_succeed}")
            if not fixed_deposit_calculator_check_total_corpus_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_post_tax_amount_succeed = Activities.fixed_deposit_calculator_check_post_tax_amount(
                driver, post_tax_amount)
            print(
                f"fixed_deposit_calculator_check_post_tax_amount_succeed {fixed_deposit_calculator_check_post_tax_amount_succeed}")
            if not fixed_deposit_calculator_check_post_tax_amount_succeed:
                testcase_status = False
        print(f"testcase_status {testcase_status}")

    except Exception as ex:
        print(ex)


def test_fixed_deposit_calculator_interest_frequency_half_yearly(driver, investment_amount="2000000",
                                                                 investment_period="14", rate_of_return="12",
                                                                 interest_frequency="Half Yearly",
                                                                 tax_rate="15", total_payment="2,000,000.00",
                                                                 total_interest="8,223,373.39",
                                                                 total_corpus="10,223,373.39",
                                                                 post_tax_amount="8,940,527.14"):
    testcase_status = True
    try:
        select_submenu_from_menu_succeed = Activities.select_submenu_from_menu(driver, "Personal Finance",
                                                                               "Fixed Deposit Interest Calculator")
        print(f"select_submenu_from_menu_succeed {select_submenu_from_menu_succeed}")
        if not select_submenu_from_menu_succeed:
            testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_investment_amount_succeed = Activities.fixed_deposit_calculator_enter_investment_amount(
                driver, investment_amount)
            print(
                f"fixed_deposit_calculator_enter_investment_amount_succeed {fixed_deposit_calculator_enter_investment_amount_succeed}")
            if not fixed_deposit_calculator_enter_investment_amount_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_investment_period_succeed = Activities.fixed_deposit_calculator_enter_investment_period(
                driver, investment_period)
            print(
                f"fixed_deposit_calculator_enter_investment_period_succeed {fixed_deposit_calculator_enter_investment_period_succeed}")
            if not fixed_deposit_calculator_enter_investment_period_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_rate_of_return_succeed = Activities.fixed_deposit_calculator_enter_rate_of_return(
                driver, rate_of_return)
            print(
                f"fixed_deposit_calculator_enter_rate_of_return_succeed {fixed_deposit_calculator_enter_rate_of_return_succeed}")
            if not fixed_deposit_calculator_enter_rate_of_return_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_select_interest_frequency_succeed = Activities.fixed_deposit_calculator_select_interest_frequency(
                driver, interest_frequency)
            print(
                f"fixed_deposit_calculator_select_interest_frequency_succeed {fixed_deposit_calculator_select_interest_frequency_succeed}")
            if not fixed_deposit_calculator_select_interest_frequency_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_tax_rate_succeed = Activities.fixed_deposit_calculator_enter_tax_rate(driver,
                                                                                                                 tax_rate)
            print(f"fixed_deposit_calculator_enter_tax_rate_succeed {fixed_deposit_calculator_enter_tax_rate_succeed}")
            if not fixed_deposit_calculator_enter_tax_rate_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_click_submit_button_succeed = Activities.fixed_deposit_calculator_click_submit_button(
                driver)
            print(
                f"fixed_deposit_calculator_click_submit_button_succeed {fixed_deposit_calculator_click_submit_button_succeed}")
            if not fixed_deposit_calculator_click_submit_button_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_payment_succeed = Activities.fixed_deposit_calculator_check_total_payment(
                driver, total_payment)
            print(
                f"fixed_deposit_calculator_check_total_payment_succeed {fixed_deposit_calculator_check_total_payment_succeed}")
            if not fixed_deposit_calculator_check_total_payment_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_interest_succeed = Activities.fixed_deposit_calculator_check_total_interest(
                driver, total_interest)
            print(
                f"fixed_deposit_calculator_check_total_interest_succeed {fixed_deposit_calculator_check_total_interest_succeed}")
            if not fixed_deposit_calculator_check_total_interest_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_corpus_succeed = Activities.fixed_deposit_calculator_check_total_corpus(
                driver, total_corpus)
            print(
                f"fixed_deposit_calculator_check_total_corpus_succeed {fixed_deposit_calculator_check_total_corpus_succeed}")
            if not fixed_deposit_calculator_check_total_corpus_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_post_tax_amount_succeed = Activities.fixed_deposit_calculator_check_post_tax_amount(
                driver, post_tax_amount)
            print(
                f"fixed_deposit_calculator_check_post_tax_amount_succeed {fixed_deposit_calculator_check_post_tax_amount_succeed}")
            if not fixed_deposit_calculator_check_post_tax_amount_succeed:
                testcase_status = False
        print(f"testcase_status {testcase_status}")

    except Exception as ex:
        print(ex)


def test_fixed_deposit_calculator_interest_frequency_yearly(driver, investment_amount="2000000",
                                                            investment_period="14", rate_of_return="12",
                                                            interest_frequency="Yearly",
                                                            tax_rate="15", total_payment="2,000,000.00",
                                                            total_interest="7,774,224.57",
                                                            total_corpus="9,774,224.57",
                                                            post_tax_amount="8,561,445.54"):
    testcase_status = True
    try:
        select_submenu_from_menu_succeed = Activities.select_submenu_from_menu(driver, "Personal Finance",
                                                                               "Fixed Deposit Interest Calculator")
        print(f"select_submenu_from_menu_succeed {select_submenu_from_menu_succeed}")
        if not select_submenu_from_menu_succeed:
            testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_investment_amount_succeed = Activities.fixed_deposit_calculator_enter_investment_amount(
                driver, investment_amount)
            print(
                f"fixed_deposit_calculator_enter_investment_amount_succeed {fixed_deposit_calculator_enter_investment_amount_succeed}")
            if not fixed_deposit_calculator_enter_investment_amount_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_investment_period_succeed = Activities.fixed_deposit_calculator_enter_investment_period(
                driver, investment_period)
            print(
                f"fixed_deposit_calculator_enter_investment_period_succeed {fixed_deposit_calculator_enter_investment_period_succeed}")
            if not fixed_deposit_calculator_enter_investment_period_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_rate_of_return_succeed = Activities.fixed_deposit_calculator_enter_rate_of_return(
                driver, rate_of_return)
            print(
                f"fixed_deposit_calculator_enter_rate_of_return_succeed {fixed_deposit_calculator_enter_rate_of_return_succeed}")
            if not fixed_deposit_calculator_enter_rate_of_return_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_select_interest_frequency_succeed = Activities.fixed_deposit_calculator_select_interest_frequency(
                driver, interest_frequency)
            print(
                f"fixed_deposit_calculator_select_interest_frequency_succeed {fixed_deposit_calculator_select_interest_frequency_succeed}")
            if not fixed_deposit_calculator_select_interest_frequency_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_tax_rate_succeed = Activities.fixed_deposit_calculator_enter_tax_rate(driver,
                                                                                                                 tax_rate)
            print(f"fixed_deposit_calculator_enter_tax_rate_succeed {fixed_deposit_calculator_enter_tax_rate_succeed}")
            if not fixed_deposit_calculator_enter_tax_rate_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_click_submit_button_succeed = Activities.fixed_deposit_calculator_click_submit_button(
                driver)
            print(
                f"fixed_deposit_calculator_click_submit_button_succeed {fixed_deposit_calculator_click_submit_button_succeed}")
            if not fixed_deposit_calculator_click_submit_button_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_payment_succeed = Activities.fixed_deposit_calculator_check_total_payment(
                driver, total_payment)
            print(
                f"fixed_deposit_calculator_check_total_payment_succeed {fixed_deposit_calculator_check_total_payment_succeed}")
            if not fixed_deposit_calculator_check_total_payment_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_interest_succeed = Activities.fixed_deposit_calculator_check_total_interest(
                driver, total_interest)
            print(
                f"fixed_deposit_calculator_check_total_interest_succeed {fixed_deposit_calculator_check_total_interest_succeed}")
            if not fixed_deposit_calculator_check_total_interest_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_total_corpus_succeed = Activities.fixed_deposit_calculator_check_total_corpus(
                driver, total_corpus)
            print(
                f"fixed_deposit_calculator_check_total_corpus_succeed {fixed_deposit_calculator_check_total_corpus_succeed}")
            if not fixed_deposit_calculator_check_total_corpus_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_post_tax_amount_succeed = Activities.fixed_deposit_calculator_check_post_tax_amount(
                driver, post_tax_amount)
            print(
                f"fixed_deposit_calculator_check_post_tax_amount_succeed {fixed_deposit_calculator_check_post_tax_amount_succeed}")
            if not fixed_deposit_calculator_check_post_tax_amount_succeed:
                testcase_status = False
        print(f"testcase_status {testcase_status}")

    except Exception as ex:
        print(ex)


def test_fixed_deposit_calculator_reset(driver, investment_amount="2000000",
                                        investment_period="14", rate_of_return="12",
                                        interest_frequency="Yearly",
                                        tax_rate="15",
                                        default_investment_amount="10000000",
                                        default_investment_period="10",
                                        default_rate_of_return="10",
                                        ):
    testcase_status = True
    try:
        select_submenu_from_menu_succeed = Activities.select_submenu_from_menu(driver, "Personal Finance",
                                                                               "Fixed Deposit Interest Calculator")
        print(f"select_submenu_from_menu_succeed {select_submenu_from_menu_succeed}")
        if not select_submenu_from_menu_succeed:
            testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_investment_amount_succeed = Activities.fixed_deposit_calculator_enter_investment_amount(
                driver, investment_amount)
            print(
                f"fixed_deposit_calculator_enter_investment_amount_succeed {fixed_deposit_calculator_enter_investment_amount_succeed}")
            if not fixed_deposit_calculator_enter_investment_amount_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_investment_period_succeed = Activities.fixed_deposit_calculator_enter_investment_period(
                driver, investment_period)
            print(
                f"fixed_deposit_calculator_enter_investment_period_succeed {fixed_deposit_calculator_enter_investment_period_succeed}")
            if not fixed_deposit_calculator_enter_investment_period_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_rate_of_return_succeed = Activities.fixed_deposit_calculator_enter_rate_of_return(
                driver, rate_of_return)
            print(
                f"fixed_deposit_calculator_enter_rate_of_return_succeed {fixed_deposit_calculator_enter_rate_of_return_succeed}")
            if not fixed_deposit_calculator_enter_rate_of_return_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_select_interest_frequency_succeed = Activities.fixed_deposit_calculator_select_interest_frequency(
                driver, interest_frequency)
            print(
                f"fixed_deposit_calculator_select_interest_frequency_succeed {fixed_deposit_calculator_select_interest_frequency_succeed}")
            if not fixed_deposit_calculator_select_interest_frequency_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_enter_tax_rate_succeed = Activities.fixed_deposit_calculator_enter_tax_rate(driver,
                                                                                                                 tax_rate)
            print(f"fixed_deposit_calculator_enter_tax_rate_succeed {fixed_deposit_calculator_enter_tax_rate_succeed}")
            if not fixed_deposit_calculator_enter_tax_rate_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_click_reset_button_succeed = Activities.fixed_deposit_calculator_click_reset_button(
                driver)
            print(
                f"fixed_deposit_calculator_click_reset_button_succeed {fixed_deposit_calculator_click_reset_button_succeed}")
            if not fixed_deposit_calculator_click_reset_button_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_investment_amount_succeed = Activities.fixed_deposit_calculator_check_investment_amount(
                driver, default_investment_amount)
            print(
                f"fixed_deposit_calculator_check_investment_amount_succeed {fixed_deposit_calculator_check_investment_amount_succeed}")
            if not fixed_deposit_calculator_check_investment_amount_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_investment_period_succeed = Activities.fixed_deposit_calculator_check_investment_period(
                driver, default_investment_period)
            print(
                f"fixed_deposit_calculator_check_investment_period_succeed {fixed_deposit_calculator_check_investment_period_succeed}")
            if not fixed_deposit_calculator_check_investment_period_succeed:
                testcase_status = False
        if testcase_status:
            fixed_deposit_calculator_check_rate_of_return_succeed = Activities.fixed_deposit_calculator_check_rate_of_return(
                driver, default_rate_of_return)
            print(
                f"fixed_deposit_calculator_check_rate_of_return_succeed {fixed_deposit_calculator_check_rate_of_return_succeed}")
            if not fixed_deposit_calculator_check_rate_of_return_succeed:
                testcase_status = False
        print(f"testcase_status {testcase_status}")

    except Exception as ex:
        print(ex)


def test_emergency_fund_calculator(driver, medical_dental_cost="2000000",
                                   vehicle_repair="100000",
                                   others="50000",
                                   life_health_insurance_premium="250000",
                                   home_auto_insurance_premium="300000",
                                   home_loan_other_important_emis="50000",
                                   monthly_living_expenses="75000",
                                   month_unemployed="5",
                                   uninsured_unexpected_emergencies_total="21,50,000",
                                   annual_amount_of_fixed_payments_total="6,00,000",
                                   build_reserve_to_pay_for_job_loss="3,75,000",
                                   final_result="31,25,000"):
    testcase_status = True
    try:
        select_submenu_from_menu_succeed = Activities.select_submenu_from_menu(driver, "Personal Finance",
                                                                               "Emergency Fund Calculator")
        print(f"select_submenu_from_menu_succeed {select_submenu_from_menu_succeed}")
        if not select_submenu_from_menu_succeed:
            testcase_status = False
        if testcase_status:
            emergency_fund_calculator_enter_medical_dental_cost_succeed = Activities.emergency_fund_calculator_enter_medical_dental_cost(
                driver, medical_dental_cost)
            print(
                f"emergency_fund_calculator_enter_medical_dental_cost_succeed {emergency_fund_calculator_enter_medical_dental_cost_succeed}")
            if not emergency_fund_calculator_enter_medical_dental_cost_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_enter_vehicle_repair_succeed = Activities.emergency_fund_calculator_enter_vehicle_repair(
                driver, vehicle_repair)
            print(
                f"emergency_fund_calculator_enter_vehicle_repair_succeed {emergency_fund_calculator_enter_vehicle_repair_succeed}")
            if not emergency_fund_calculator_enter_vehicle_repair_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_enter_others_succeed = Activities.emergency_fund_calculator_enter_others(
                driver, others)
            print(
                f"emergency_fund_calculator_enter_others_succeed {emergency_fund_calculator_enter_others_succeed}")
            if not emergency_fund_calculator_enter_others_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_enter_life_health_insurance_premium_succeed = Activities.emergency_fund_calculator_enter_life_health_insurance_premium(
                driver, life_health_insurance_premium)
            print(
                f"emergency_fund_calculator_enter_life_health_insurance_premium_succeed {emergency_fund_calculator_enter_life_health_insurance_premium_succeed}")
            if not emergency_fund_calculator_enter_life_health_insurance_premium_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_enter_home_auto_insurance_premium_succeed = Activities.emergency_fund_calculator_enter_home_auto_insurance_premium(
                driver,
                home_auto_insurance_premium)
            print(
                f"emergency_fund_calculator_enter_home_auto_insurance_premium_succeed {emergency_fund_calculator_enter_home_auto_insurance_premium_succeed}")
            if not emergency_fund_calculator_enter_home_auto_insurance_premium_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_enter_home_loan_other_important_emis_succeed = Activities.emergency_fund_calculator_enter_home_loan_other_important_emis(
                driver,
                home_loan_other_important_emis)
            print(
                f"emergency_fund_calculator_enter_home_loan_other_important_emis_succeed {emergency_fund_calculator_enter_home_loan_other_important_emis_succeed}")
            if not emergency_fund_calculator_enter_home_loan_other_important_emis_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_enter_monthly_living_expenses_succeed = Activities.emergency_fund_calculator_enter_monthly_living_expenses(
                driver,
                monthly_living_expenses)
            print(
                f"emergency_fund_calculator_enter_monthly_living_expenses_succeed {emergency_fund_calculator_enter_monthly_living_expenses_succeed}")
            if not emergency_fund_calculator_enter_monthly_living_expenses_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_enter_month_unemployed_succeed = Activities.emergency_fund_calculator_enter_month_unemployed(
                driver,
                month_unemployed)
            print(
                f"emergency_fund_calculator_enter_month_unemployed_succeed {emergency_fund_calculator_enter_month_unemployed_succeed}")
            if not emergency_fund_calculator_enter_month_unemployed_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_click_calculate_button_succeed = Activities.emergency_fund_calculator_click_calculate_button(
                driver)
            print(
                f"emergency_fund_calculator_click_calculate_button_succeed {emergency_fund_calculator_click_calculate_button_succeed}")
            if not emergency_fund_calculator_click_calculate_button_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_check_uninsured_unexpected_emergencies_total_succeed = Activities.emergency_fund_calculator_check_uninsured_unexpected_emergencies_total(
                driver, uninsured_unexpected_emergencies_total)
            print(
                f"emergency_fund_calculator_check_uninsured_unexpected_emergencies_total_succeed {emergency_fund_calculator_check_uninsured_unexpected_emergencies_total_succeed}")
            if not emergency_fund_calculator_check_uninsured_unexpected_emergencies_total_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_check_annual_amount_of_fixed_payments_total_succeed = Activities.emergency_fund_calculator_check_annual_amount_of_fixed_payments_total(
                driver, annual_amount_of_fixed_payments_total)
            print(
                f"emergency_fund_calculator_check_annual_amount_of_fixed_payments_total_succeed {emergency_fund_calculator_check_annual_amount_of_fixed_payments_total_succeed}")
            if not emergency_fund_calculator_check_annual_amount_of_fixed_payments_total_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_check_build_reserve_to_pay_for_job_loss_succeed = Activities.emergency_fund_calculator_check_build_reserve_to_pay_for_job_loss(
                driver, build_reserve_to_pay_for_job_loss)
            print(
                f"emergency_fund_calculator_check_build_reserve_to_pay_for_job_loss_succeed {emergency_fund_calculator_check_build_reserve_to_pay_for_job_loss_succeed}")
            if not emergency_fund_calculator_check_build_reserve_to_pay_for_job_loss_succeed:
                testcase_status = False
        if testcase_status:
            emergency_fund_calculator_check_result_succeed = Activities.emergency_fund_calculator_check_result(
                driver, final_result)
            print(
                f"emergency_fund_calculator_check_result_succeed {emergency_fund_calculator_check_result_succeed}")
            if not emergency_fund_calculator_check_result_succeed:
                testcase_status = False
        print(f"testcase_status {testcase_status}")

    except Exception as ex:
        print(ex)


def test_provident_fund_calculator(driver, your_age="50",
                                   your_basic_salary_monthly="75000",
                                   your_contribution_to_epf="10",
                                   your_employer_contribution_to_epf="12",
                                   average_annual_increase_in_salary_you_expect="12",
                                   age_when_you_intend_to_retire="60",
                                   current_epf_balance_if_any="5000000",
                                   current_interest_rate="9",
                                   final_result="1,62,14,311"):
    testcase_status = True
    try:
        select_submenu_from_menu_succeed = Activities.select_submenu_from_menu(driver, "Personal Finance",
                                                                               "Provident Fund Calculator")
        print(f"select_submenu_from_menu_succeed {select_submenu_from_menu_succeed}")
        if not select_submenu_from_menu_succeed:
            testcase_status = False
        if testcase_status:
            provident_fund_calculator_enter_your_age_succeed = Activities.provident_fund_calculator_enter_your_age(
                driver, your_age)
            print(
                f"provident_fund_calculator_enter_your_age_succeed {provident_fund_calculator_enter_your_age_succeed}")
            if not provident_fund_calculator_enter_your_age_succeed:
                testcase_status = False
        if testcase_status:
            provident_fund_calculator_enter_your_basic_salary_monthly_succeed = Activities.provident_fund_calculator_enter_your_basic_salary_monthly(
                driver, your_basic_salary_monthly)
            print(
                f"provident_fund_calculator_enter_your_basic_salary_monthly_succeed {provident_fund_calculator_enter_your_basic_salary_monthly_succeed}")
            if not provident_fund_calculator_enter_your_basic_salary_monthly_succeed:
                testcase_status = False
        if testcase_status:
            provident_fund_calculator_enter_your_contribution_to_epf_succeed = Activities.provident_fund_calculator_enter_your_contribution_to_epf(
                driver, your_contribution_to_epf)
            print(
                f"provident_fund_calculator_enter_your_contribution_to_epf_succeed {provident_fund_calculator_enter_your_contribution_to_epf_succeed}")
            if not provident_fund_calculator_enter_your_contribution_to_epf_succeed:
                testcase_status = False
        if testcase_status:
            provident_fund_calculator_enter_your_employer_contribution_to_epf_succeed = Activities.provident_fund_calculator_enter_your_employer_contribution_to_epf(
                driver, your_employer_contribution_to_epf)
            print(
                f"provident_fund_calculator_enter_your_employer_contribution_to_epf_succeed {provident_fund_calculator_enter_your_employer_contribution_to_epf_succeed}")
            if not provident_fund_calculator_enter_your_employer_contribution_to_epf_succeed:
                testcase_status = False
        if testcase_status:
            provident_fund_calculator_enter_average_annual_increase_in_salary_you_expect_succeed = Activities.provident_fund_calculator_enter_average_annual_increase_in_salary_you_expect(
                driver,
                average_annual_increase_in_salary_you_expect)
            print(
                f"provident_fund_calculator_enter_average_annual_increase_in_salary_you_expect_succeed {provident_fund_calculator_enter_average_annual_increase_in_salary_you_expect_succeed}")
            if not provident_fund_calculator_enter_average_annual_increase_in_salary_you_expect_succeed:
                testcase_status = False
        if testcase_status:
            provident_fund_calculator_enter_age_when_you_intend_to_retire_succeed = Activities.provident_fund_calculator_enter_age_when_you_intend_to_retire(
                driver,
                age_when_you_intend_to_retire)
            print(
                f"provident_fund_calculator_enter_age_when_you_intend_to_retire_succeed {provident_fund_calculator_enter_age_when_you_intend_to_retire_succeed}")
            if not provident_fund_calculator_enter_age_when_you_intend_to_retire_succeed:
                testcase_status = False
        if testcase_status:
            provident_fund_calculator_enter_current_epf_balance_if_any_succeed = Activities.provident_fund_calculator_enter_current_epf_balance_if_any(
                driver,
                current_epf_balance_if_any)
            print(
                f"provident_fund_calculator_enter_current_epf_balance_if_any_succeed {provident_fund_calculator_enter_current_epf_balance_if_any_succeed}")
            if not provident_fund_calculator_enter_current_epf_balance_if_any_succeed:
                testcase_status = False
        if testcase_status:
            provident_fund_calculator_enter_current_interest_rate_succeed = Activities.provident_fund_calculator_enter_current_interest_rate(
                driver,
                current_interest_rate)
            print(
                f"provident_fund_calculator_enter_current_interest_rate_succeed {provident_fund_calculator_enter_current_interest_rate_succeed}")
            if not provident_fund_calculator_enter_current_interest_rate_succeed:
                testcase_status = False
        if testcase_status:
            provident_fund_calculator_click_submit_button_succeed = Activities.provident_fund_calculator_click_submit_button(
                driver)
            print(
                f"provident_fund_calculator_click_submit_button_succeed {provident_fund_calculator_click_submit_button_succeed}")
            if not provident_fund_calculator_click_submit_button_succeed:
                testcase_status = False
        if testcase_status:
            provident_fund_calculator_check_result_succeed = Activities.provident_fund_calculator_check_result(
                driver, final_result)
            print(
                f"provident_fund_calculator_check_result_succeed {provident_fund_calculator_check_result_succeed}")
            if not provident_fund_calculator_check_result_succeed:
                testcase_status = False
        print(f"testcase_status {testcase_status}")

    except Exception as ex:
        print(ex)


def test_debt_reduction_plan_calculator(driver,
                                        total_debt_outstanding="1500000",
                                        rate_of_interest_per_annum="15",
                                        how_much_can_you_repay_every_month="50000",
                                        final_result="15,00,000"):
    testcase_status = True
    try:
        select_submenu_from_menu_succeed = Activities.select_submenu_from_menu(driver, "Personal Finance",
                                                                               "Debt Reduction Planner")
        print(f"select_submenu_from_menu_succeed {select_submenu_from_menu_succeed}")
        if not select_submenu_from_menu_succeed:
            testcase_status = False
        if testcase_status:
            debt_reduction_plan_calculator_enter_total_debt_outstanding_succeed = Activities.debt_reduction_plan_calculator_enter_total_debt_outstanding(
                driver, total_debt_outstanding)
            print(
                f"debt_reduction_plan_calculator_enter_total_debt_outstanding_succeed {debt_reduction_plan_calculator_enter_total_debt_outstanding_succeed}")
            if not debt_reduction_plan_calculator_enter_total_debt_outstanding_succeed:
                testcase_status = False
        if testcase_status:
            debt_reduction_plan_calculator_enter_rate_of_interest_per_annum_succeed = Activities.debt_reduction_plan_calculator_enter_rate_of_interest_per_annum(
                driver, rate_of_interest_per_annum)
            print(
                f"debt_reduction_plan_calculator_enter_rate_of_interest_per_annum_succeed {debt_reduction_plan_calculator_enter_rate_of_interest_per_annum_succeed}")
            if not debt_reduction_plan_calculator_enter_rate_of_interest_per_annum_succeed:
                testcase_status = False
        if testcase_status:
            debt_reduction_plan_calculator_enter_how_much_can_you_repay_every_month_succeed = Activities.debt_reduction_plan_calculator_enter_how_much_can_you_repay_every_month(
                driver, how_much_can_you_repay_every_month)
            print(
                f"debt_reduction_plan_calculator_enter_how_much_can_you_repay_every_month_succeed {debt_reduction_plan_calculator_enter_how_much_can_you_repay_every_month_succeed}")
            if not debt_reduction_plan_calculator_enter_how_much_can_you_repay_every_month_succeed:
                testcase_status = False
        if testcase_status:
            debt_reduction_plan_calculator_click_calculate_button_succeed = Activities.debt_reduction_plan_calculator_click_calculate_button(
                driver)
            print(
                f"debt_reduction_plan_calculator_click_calculate_button_succeed {debt_reduction_plan_calculator_click_calculate_button_succeed}")
            if not debt_reduction_plan_calculator_click_calculate_button_succeed:
                testcase_status = False
        if testcase_status:
            debt_reduction_plan_calculator_check_result_succeed = Activities.debt_reduction_plan_calculator_check_result(
                driver, final_result)
            print(
                f"debt_reduction_plan_calculator_check_result_succeed {debt_reduction_plan_calculator_check_result_succeed}")
            if not debt_reduction_plan_calculator_check_result_succeed:
                testcase_status = False
        print(f"testcase_status {testcase_status}")

    except Exception as ex:
        print(ex)
