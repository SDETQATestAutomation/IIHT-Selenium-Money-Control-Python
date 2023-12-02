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
from src.main.pyhton.com.iiht.evaluation.automation import SubActivities
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
    check_page_load_complete(driver)
    try:
        print("\nAfter method setup")
        yield driver
    finally:
        driver.quit()
    return driver


def check_page_load_complete(driver):
    timeout = 60  # Timeout in seconds
    interval = 10  # Retry interval in seconds
    start_time = time.time()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    while True:
        if driver.execute_script('return document.readyState') == 'complete':
            break

        if (time.time() - start_time) >= timeout:
            # Timeout reached
            break

        time.sleep(interval)

        # Check if the page has loaded completely
    is_page_loaded = driver.execute_script('return document.readyState') == 'complete'
    if is_page_loaded:
        print('Webpage loaded completely')
    else:
        print('Webpage not loaded completely')


def find_element_use_xpath(driver, xpath):
    required_element = None
    try:
        required_element = driver.find_element(By.XPATH, xpath)
    except Exception as ex:
        print(f"ex {ex}")
    finally:
        return required_element


def wait_for_element_not_present(driver, xpath):
    element_not_present = False
    driver.implicitly_wait(0)
    wait_timeout = 60
    retry_timeout = 5
    count_needed = math.floor(wait_timeout / retry_timeout)
    try:
        for i in range(count_needed):
            all_elements = driver.find_elements(By.XPATH, xpath)
            all_elements_length = len(all_elements)
            print(f"all_elements_length {all_elements_length}")
            if all_elements_length == 0:
                element_not_present = True
                break
            else:
                time.sleep(retry_timeout)

    except Exception as ex:
        print(f"ex {ex}")
    finally:
        driver.implicitly_wait(15)
        return element_not_present


def wait_for_element_present(driver, xpath):
    element_present = False
    driver.implicitly_wait(0)
    wait_timeout = 60
    retry_timeout = 5
    count_needed = math.floor(wait_timeout / retry_timeout)
    try:
        for i in range(count_needed):
            all_elements = driver.find_elements(By.XPATH, xpath)
            all_elements_length = all_elements.size()
            if all_elements_length > 0:
                element_present = True
                break
            else:
                time.sleep(retry_timeout)

    except Exception as ex:
        print(f"ex {ex}")
    finally:
        driver.implicitly_wait(15)
        return element_present


def wait_for_element_visible(driver, xpath):
    element_visible = False
    driver.implicitly_wait(0)
    wait_timeout = 60
    retry_timeout = 5
    count_needed = math.floor(wait_timeout / retry_timeout)
    try:
        for i in range(count_needed):
            all_elements = driver.find_elements(By.XPATH, xpath)
            all_elements_length = all_elements.size()
            if all_elements_length > 0:
                required_element = all_elements[0]
                required_element_display = required_element.is_displayed()
                print(f"required_element_display {required_element_display}")
                if required_element_display:
                    element_visible = True
                    break
            else:
                time.sleep(retry_timeout)

    except Exception as ex:
        print(f"ex {ex}")
    finally:
        driver.implicitly_wait(15)
        return element_visible


def wait_for_element_not_visible(driver, xpath):
    element_not_visible = False
    driver.implicitly_wait(0)
    wait_timeout = 60
    retry_timeout = 5
    count_needed = math.floor(wait_timeout / retry_timeout)
    try:
        for i in range(count_needed):
            all_elements = driver.find_elements(By.XPATH, xpath)
            all_elements_length = all_elements.size()
            if all_elements_length > 0:
                required_element = all_elements[0]
                required_element_display = required_element.is_displayed()
                print(f"required_element_display {required_element_display}")
                if not required_element_display:
                    element_not_visible = True
                    break
            else:
                time.sleep(retry_timeout)

    except Exception as ex:
        print(f"ex {ex}")
    finally:
        driver.implicitly_wait(15)
        return element_not_visible


def open_login_panel(driver):
    user_link_element = find_element_use_xpath(driver, money_control_element["login_link"])
    if user_link_element is None:
        return False
    actions = ActionChains(driver)
    actions.move_to_element(user_link_element).perform()
    login_signup_box_element = find_element_use_xpath(driver, money_control_element["login_signup_box"])
    if login_signup_box_element is None:
        return False
    login_signup_box_element_display = login_signup_box_element.is_displayed()
    print(f"login_signup_box_element_display {login_signup_box_element_display}")
    if login_signup_box_element_display is False:
        return False
    return True


def switch_to_signin_iframe(driver):
    login_signin_iframe_element = find_element_use_xpath(driver, money_control_element["login_signin_iframe"])
    if login_signin_iframe_element is None:
        return False
    driver.switch_to.frame(login_signin_iframe_element)
    return True


def open_signin_box(driver):
    signup_box_login_link_element = find_element_use_xpath(driver,
                                                           money_control_element["signup_box_login_link"])
    if signup_box_login_link_element is None:
        return False
    signup_box_login_link_element.click()
    switch_to_signin_iframe_succeed = switch_to_signin_iframe(driver)
    if not switch_to_signin_iframe_succeed:
        return False
    login_signin_box_element = find_element_use_xpath(driver,
                                                      money_control_element["login_signin_box"])
    if login_signin_box_element is None:
        return False
    return True


def signin_box_enter_email(driver, email):
    driver.switch_to.default_content()
    switch_to_signin_iframe_succeed = switch_to_signin_iframe(driver)
    if not switch_to_signin_iframe_succeed:
        return False
    signin_box_email_field_element = find_element_use_xpath(driver,
                                                            money_control_element["signin_box_email_field"])
    if signin_box_email_field_element is None:
        return False
    signin_box_email_field_element.send_keys(email)
    return True


def signin_box_enter_password(driver, password):
    driver.switch_to.default_content()
    switch_to_signin_iframe_succeed = switch_to_signin_iframe(driver)
    if not switch_to_signin_iframe_succeed:
        return False
    signin_box_password_field_element = find_element_use_xpath(driver,
                                                               money_control_element["signin_box_password_field"])
    if signin_box_password_field_element is None:
        return False
    signin_box_password_field_element.send_keys(password)
    return True


def signin_box_click_login_button(driver):
    login_signin_box_not_present = False
    driver.switch_to.default_content()
    switch_to_signin_iframe_succeed = switch_to_signin_iframe(driver)
    if not switch_to_signin_iframe_succeed:
        return False
    signin_box_login_button_element = find_element_use_xpath(driver,
                                                             money_control_element["signin_box_login_button"])
    if signin_box_login_button_element is None:
        return False
    signin_box_login_button_element.click()

    try:
        login_signin_box_not_present = wait_for_element_not_present(driver, money_control_element["login_signin_box"])
        print(f"login_signin_box_not_present {login_signin_box_not_present}")
    except Exception as ex:
        print(f"ex {ex}")
    finally:
        driver.switch_to.default_content()
        return login_signin_box_not_present


def test_login(driver):
    open_login_panel(driver)
    open_signin_box(driver)
    signin_box_enter_email(driver, "prashant.ranjan.qa@gmail.com")
    signin_box_enter_password(driver, "igetup@7AM")
    signin_box_click_login_button(driver)

# def get_href_of_link(driver):
#     if driver.get_attribute("outerHTML").startswith("<a"):
#         return driver.get_attribute("href")
#     else:
#         return driver.get_attribute("outerHTML")
#
#
# def test_mouse_over_personal_finance(driver):
#     utils = TestUtils()
#     master_data = MasterData()
#     try:
#         element = Helpers.getElementforMouseOver(driver)
#         href = get_href_of_link(element)
#         status = href == master_data.repo[0]
#         actions = ActionChains(driver)
#         actions.move_to_element(element).perform()
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(2)
# def test_get_tool_for_emi_calculator(driver):
#     utils = TestUtils()
#     master_data = MasterData()
#     try:
#         element = Helpers.getElementforTool(driver)
#         href = get_href_of_link(element)
#         status = href == master_data.repo[1]
#         actions = ActionChains(driver)
#         actions.move_to_element(element).click().perform()
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(3)
# def test_get_home_loan_emi_calculator(driver):
#     utils = TestUtils()
#     master_data = MasterData()
#     try:
#         element = Helpers.getElementforHomeLoan(driver)
#         href = get_href_of_link(element)
#         status = href == master_data.repo[2]
#         wait = WebDriverWait(driver, 10)
#         wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Home Loan')]")))
#         driver.execute_script("arguments[0].click();", element)
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(4)
# def test_access_loan_amount(driver):
#     utils = TestUtils()
#     master_data = MasterData()
#     try:
#         element = Helpers.getElementforLoanAmount(driver)
#         href = get_href_of_link(element)
#         status = href == master_data.repo[3]
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(5)
# def test_set_value_for_loan_amount(driver):
#     utils = TestUtils()
#     try:
#         status = SubActivities.enterValueLoanAmount(driver)
#         # utils.yakshaAssert(utils.currentTest(), status,"Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(6)
# def test_access_loan_period(driver):
#     utils = TestUtils()
#     master_data = MasterData()
#     try:
#         element = Helpers.getElementforLoanPeriod(driver)
#         href = get_href_of_link(element)
#         status = href == master_data.repo[4]
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(7)
# def test_set_value_for_loan_period(driver):
#     utils = TestUtils()
#     try:
#         status = SubActivities.enterValueLoanPeriod(driver)
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(8)
# def test_set_value_for_emi_start_from(driver):
#     utils = TestUtils()
#     try:
#         status = SubActivities.selectEMIStartsFrom(driver)
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(9)
# def test_access_interest_rate(driver):
#     utils = TestUtils()
#     master_data = MasterData()
#     try:
#         element = Helpers.getElementforInterestRate(driver)
#         href = get_href_of_link(element)
#         status = href == master_data.repo[6]
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(10)
# def test_set_value_for_interest_rate(driver):
#     utils = TestUtils()
#     try:
#         status = SubActivities.enterInterestRate(driver)
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(11)
# def test_access_upfront_charges(driver):
#     utils = TestUtils()
#     master_data = MasterData()
#     status = False
#     try:
#         element = Helpers.getElementforUpfrontcharges(driver)
#         href = get_href_of_link(element)
#         status = href == master_data.repo[7]
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(12)
# def test_set_value_for_upfront_charges(driver):
#     utils = TestUtils()
#     status = False
#     try:
#         status = SubActivities.enterValueUpfrontCharges(driver)
#         # utils.yakshaAssert(utils.currentTest(), status, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(13)
# def test_get_total_payment_element(driver):
#     utils = TestUtils()
#     try:
#         element = SubActivities.getTotalPaymentElement(driver)
#         if element is not None:
#             print(True)
#             # utils.yakshaAssert(utils.currentTest(), True, "Business")
#         else:
#             print(False)
#             # utils.yakshaAssert(utils.currentTest(), False, "Business")
#     except Exception as ex:
#         print(ex)
#         # utils.yakshaAssert(utils.currentTest(), False, "Business")
#
#
# @pytest.mark.order(14)
# def test_get_xpath_for_7th_year_emi_payment(driver):
#     utils = TestUtils()
#     status = Helpers.getXpathfor7thYearEMIPayment().find("sibling")
#     # utils.yakshaAssert(utils.currentTest(), status, "Business")
#
#
# @pytest.mark.order(15)
# def test_get_xpath_for_7th_year_interest_payment(driver):
#     utils = TestUtils()
#     status = Helpers.getXpathfor7thYearInterestPayment().find("sibling")
#     # utils.yakshaAssert(utils.currentTest(), status, "Business")
#
#
# @pytest.mark.order(16)
# def test_get_xpath_for_7th_year_principal_payment(driver):
#     utils = TestUtils()
#     status = Helpers.getXpathfor7thYearPrincipalPayment().find("sibling")
#     # utils.yakshaAssert(utils.currentTest(), status, "Business")
#
#
# @pytest.mark.order(17)
# def test_get_xpath_for_5th_year_outstanding_principal_payment(driver):
#     utils = TestUtils()
#     status = Helpers.getXpathfor5thYearOutstandingPrincipalPayment().find("sibling")
# utils.yakshaAssert(utils.currentTest(), status, "Business")

# @pytest.mark.parametrize("test_input", ["test_mouse_over_personal_finance", "test_get_tool_for_emi_calculator",
#                                         "test_get_home_loan_emi_calculator",
#                                         "test_access_loan_amount", "test_set_value_for_loan_amount"])
# def test_suite(driver, test_input):
#     # Your test code here
#     print(f"Running {test_input}")
#
#
# if __name__ == "__main__":
#     pytest.main([__file__])
