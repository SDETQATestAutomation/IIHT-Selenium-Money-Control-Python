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
