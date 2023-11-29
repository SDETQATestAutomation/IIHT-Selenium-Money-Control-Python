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
            all_elements_length = len(all_elements)
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
            all_elements_length = len(all_elements)
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
            all_elements_length = len(all_elements)
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


def do_javascript_click(driver, element):
    try:
        driver.execute_script("arguments[0].click();", element)
    except Exception as ex:
        print(f"ex {ex}")


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


def signin_box_click_login_button_except_error(driver):
    login_signin_box_present = False
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
        login_signin_box_present = wait_for_element_present(driver, money_control_element["login_signin_box"])
        print(f"login_signin_box_present {login_signin_box_present}")
    except Exception as ex:
        print(f"ex {ex}")
    finally:
        driver.switch_to.default_content()
        return login_signin_box_present


def signin_box_check_error(driver, error_message):
    is_error_message_checked = False
    driver.switch_to.default_content()
    switch_to_signin_iframe_succeed = switch_to_signin_iframe(driver)
    if not switch_to_signin_iframe_succeed:
        return False
    signin_box_error_div_element = find_element_use_xpath(driver,
                                                          money_control_element["signin_box_error_div"])
    if signin_box_error_div_element is None:
        return False
    signin_box_error_div_element_text = signin_box_error_div_element.text
    print(f"signin_box_error_div_element_text {signin_box_error_div_element_text}")
    if signin_box_error_div_element_text == error_message:
        is_error_message_checked = True
    return is_error_message_checked


def check_logged_in_user(driver, email):
    is_email_checked = False
    logged_in_user_link_element = find_element_use_xpath(driver,
                                                         money_control_element["logged_in_user_link"])
    if logged_in_user_link_element is None:
        return False
    logged_in_user_link_title_attribute = logged_in_user_link_element.get_attribute("title")
    print(f"logged_in_user_link_title_attribute {logged_in_user_link_title_attribute}")
    if logged_in_user_link_title_attribute.lstrip().rstrip() == email:
        is_email_checked = True
    return is_email_checked


def select_submenu_from_menu(driver, main_menu, sub_menu):
    main_menu = money_control_element["main_menu"].replace("$(main_menu)", main_menu)
    sub_menu = money_control_element["sub_menu"].replace("$(sub_menu)", sub_menu)

    main_menu_element = find_element_use_xpath(driver, main_menu)
    if main_menu_element is None:
        return False
    main_menu_element_visible = wait_for_element_visible(driver, main_menu)
    print(f"main_menu_element_visible {main_menu_element_visible}")
    if main_menu_element_visible is False:
        return False
    actions = ActionChains(driver)
    actions.move_to_element(main_menu_element).perform()
    sub_menu_element = find_element_use_xpath(driver, sub_menu)
    if sub_menu_element is None:
        return False
    sub_menu_element_visible = wait_for_element_visible(driver, sub_menu)
    print(f"sub_menu_element_visible {sub_menu_element_visible}")
    if sub_menu_element_visible is False:
        return False
    sub_menu_element.click()
    check_page_load_complete(driver)
    return True


def fixed_deposit_calculator_enter_investment_amount(driver, investment_amount):
    investment_amount_input = money_control_element["investment_amount_input"]
    investment_amount_input_element = find_element_use_xpath(driver, investment_amount_input)
    if investment_amount_input_element is None:
        return False
    investment_amount_input_element_visible = wait_for_element_visible(driver, investment_amount_input)
    print(f"investment_amount_input_element_visible {investment_amount_input_element_visible}")
    if investment_amount_input_element_visible is False:
        return False
    investment_amount_input_element.clear()
    investment_amount_input_element.send_keys(investment_amount)
    return True


def fixed_deposit_calculator_check_investment_amount(driver, investment_amount):
    investment_amount_input = money_control_element["investment_amount_input"]
    investment_amount_input_element = find_element_use_xpath(driver, investment_amount_input)
    if investment_amount_input_element is None:
        return False
    investment_amount_input_element_visible = wait_for_element_visible(driver, investment_amount_input)
    print(f"investment_amount_input_element_visible {investment_amount_input_element_visible}")
    if investment_amount_input_element_visible is False:
        return False
    investment_amount_input_element_value_attribute = investment_amount_input_element.get_attribute("value")
    print(f"investment_amount_input_element_value_attribute {investment_amount_input_element_value_attribute}")
    if investment_amount_input_element_value_attribute != investment_amount:
        return False
    return True


def fixed_deposit_calculator_enter_investment_period(driver, investment_period):
    investment_period_input = money_control_element["investment_period_input"]
    investment_period_input_element = find_element_use_xpath(driver, investment_period_input)
    if investment_period_input_element is None:
        return False
    investment_period_input_element_visible = wait_for_element_visible(driver, investment_period_input)
    print(f"investment_period_input_element_visible {investment_period_input_element_visible}")
    if investment_period_input_element_visible is False:
        return False
    investment_period_input_element.clear()
    investment_period_input_element.send_keys(investment_period)
    return True


def fixed_deposit_calculator_check_investment_period(driver, investment_period):
    investment_period_input = money_control_element["investment_period_input"]
    investment_period_input_element = find_element_use_xpath(driver, investment_period_input)
    if investment_period_input_element is None:
        return False
    investment_period_input_element_visible = wait_for_element_visible(driver, investment_period_input)
    print(f"investment_period_input_element_visible {investment_period_input_element_visible}")
    if investment_period_input_element_visible is False:
        return False
    investment_period_input_element_value_attribute = investment_period_input_element.get_attribute("value")
    print(f"investment_period_input_element_value_attribute {investment_period_input_element_value_attribute}")
    if investment_period_input_element_value_attribute != investment_period:
        return False
    return True


def fixed_deposit_calculator_enter_rate_of_return(driver, rate_of_return):
    rate_of_return_input = money_control_element["rate_of_return_input"]
    rate_of_return_input_element = find_element_use_xpath(driver, rate_of_return_input)
    if rate_of_return_input_element is None:
        return False
    rate_of_return_input_element_visible = wait_for_element_visible(driver, rate_of_return_input)
    print(f"rate_of_return_input_element_visible {rate_of_return_input_element_visible}")
    if rate_of_return_input_element_visible is False:
        return False
    rate_of_return_input_element.clear()
    rate_of_return_input_element.send_keys(rate_of_return)
    return True


def fixed_deposit_calculator_check_rate_of_return(driver, rate_of_return):
    rate_of_return_input = money_control_element["rate_of_return_input"]
    rate_of_return_input_element = find_element_use_xpath(driver, rate_of_return_input)
    if rate_of_return_input_element is None:
        return False
    rate_of_return_input_element_visible = wait_for_element_visible(driver, rate_of_return_input)
    print(f"rate_of_return_input_element_visible {rate_of_return_input_element_visible}")
    if rate_of_return_input_element_visible is False:
        return False
    rate_of_return_input_element_value_attribute = rate_of_return_input_element.get_attribute("value")
    print(f"rate_of_return_input_element_value_attribute {rate_of_return_input_element_value_attribute}")
    if rate_of_return_input_element_value_attribute != rate_of_return:
        return False
    return True


def fixed_deposit_calculator_select_interest_frequency(driver, interest_frequency):
    interest_frequency_radio = money_control_element["interest_frequency_radio"].replace("$(interest_frequency)",
                                                                                         interest_frequency)
    interest_frequency_radio_element = find_element_use_xpath(driver, interest_frequency_radio)
    if interest_frequency_radio_element is None:
        return False
    do_javascript_click(driver, interest_frequency_radio_element)
    interest_frequency_radio_checked_attribute = interest_frequency_radio_element.get_attribute("checked")
    print(f"interest_frequency_radio_checked_attribute {interest_frequency_radio_checked_attribute}")
    if interest_frequency_radio_checked_attribute != "checked":
        return False
    return True


def fixed_deposit_calculator_enter_tax_rate(driver, tax_rate):
    tax_rate_input = money_control_element["tax_rate_input"]
    tax_rate_input_element = find_element_use_xpath(driver, tax_rate_input)
    if tax_rate_input_element is None:
        return False
    tax_rate_input_element_visible = wait_for_element_visible(driver, tax_rate_input)
    print(f"tax_rate_input_element_visible {tax_rate_input_element_visible}")
    if tax_rate_input_element_visible is False:
        return False
    tax_rate_input_element.clear()
    tax_rate_input_element.send_keys(tax_rate)
    return True


def fixed_deposit_calculator_check_tax_rate(driver, tax_rate):
    tax_rate_input = money_control_element["tax_rate_input"]
    tax_rate_input_element = find_element_use_xpath(driver, tax_rate_input)
    if tax_rate_input_element is None:
        return False
    tax_rate_input_element_visible = wait_for_element_visible(driver, tax_rate_input)
    print(f"tax_rate_input_element_visible {tax_rate_input_element_visible}")
    if tax_rate_input_element_visible is False:
        return False
    tax_rate_input_element_value_attribute=tax_rate_input_element.get_attribute("value")
    print(f"tax_rate_input_element_value_attribute {tax_rate_input_element_value_attribute}")
    if tax_rate_input_element_value_attribute != tax_rate:
        return False
    return True


def fixed_deposit_calculator_click_submit_button(driver):
    submit_button = money_control_element["submit_button"]
    submit_button_element = find_element_use_xpath(driver, submit_button)
    if submit_button_element is None:
        return False
    submit_button_element_visible = wait_for_element_visible(driver, submit_button)
    print(f"submit_button_element_visible {submit_button_element_visible}")
    if submit_button_element_visible is False:
        return False
    submit_button_element.click()
    return True


def fixed_deposit_calculator_click_reset_button(driver):
    reset_button = money_control_element["reset_button"]
    reset_button_element = find_element_use_xpath(driver, reset_button)
    if reset_button_element is None:
        return False
    reset_button_element_visible = wait_for_element_visible(driver, reset_button)
    print(f"reset_button_element_visible {reset_button_element_visible}")
    if reset_button_element_visible is False:
        return False
    reset_button_element.click()
    return True


def fixed_deposit_calculator_check_total_payment(driver, total_payment):
    total_payment_span = money_control_element["total_payment_span"]
    total_payment_span_element = find_element_use_xpath(driver, total_payment_span)
    if total_payment_span_element is None:
        return False
    total_payment_span_element_visible = wait_for_element_visible(driver, total_payment_span)
    print(f"total_payment_span_element_visible {total_payment_span_element_visible}")
    if total_payment_span_element_visible is False:
        return False
    total_payment_span_element_text = total_payment_span_element.text
    print(f"total_payment_span_element_text {total_payment_span_element_text}")
    if total_payment_span_element_text != total_payment:
        return False
    return True


def fixed_deposit_calculator_check_total_interest(driver, total_interest):
    total_interest_span = money_control_element["total_interest_span"]
    total_interest_span_element = find_element_use_xpath(driver, total_interest_span)
    if total_interest_span_element is None:
        return False
    total_interest_span_element_visible = wait_for_element_visible(driver, total_interest_span)
    print(f"total_interest_span_element_visible {total_interest_span_element_visible}")
    if total_interest_span_element_visible is False:
        return False
    total_interest_span_element_text = total_interest_span_element.text
    print(f"total_interest_span_element_text {total_interest_span_element_text}")
    if total_interest_span_element_text != total_interest:
        return False
    return True


def fixed_deposit_calculator_check_total_corpus(driver, total_corpus):
    total_corpus_span = money_control_element["total_corpus_span"]
    total_corpus_span_element = find_element_use_xpath(driver, total_corpus_span)
    if total_corpus_span_element is None:
        return False
    total_corpus_span_element_visible = wait_for_element_visible(driver, total_corpus_span)
    print(f"total_corpus_span_element_visible {total_corpus_span_element_visible}")
    if total_corpus_span_element_visible is False:
        return False
    total_corpus_span_element_text = total_corpus_span_element.text
    print(f"total_corpus_span_element_text {total_corpus_span_element_text}")
    if total_corpus_span_element_text != total_corpus:
        return False
    return True


def fixed_deposit_calculator_check_post_tax_amount(driver, post_tax_amount):
    post_tax_amount_span = money_control_element["post_tax_amount_span"]
    post_tax_amount_span_element = find_element_use_xpath(driver, post_tax_amount_span)
    if post_tax_amount_span_element is None:
        return False
    post_tax_amount_span_element_visible = wait_for_element_visible(driver, post_tax_amount_span)
    print(f"post_tax_amount_span_element_visible {post_tax_amount_span_element_visible}")
    if post_tax_amount_span_element_visible is False:
        return False
    post_tax_amount_span_element_text = post_tax_amount_span_element.text
    print(f"post_tax_amount_span_element_text {post_tax_amount_span_element_text}")
    if post_tax_amount_span_element_text != post_tax_amount:
        return False
    return True

def emergency_fund_calculator_enter_medical_dental_cost(driver,medical_dental_cost):
    medical_dental_cost_input = money_control_element["medical_dental_cost_input"]
    medical_dental_cost_input_element = find_element_use_xpath(driver, medical_dental_cost_input)
    if medical_dental_cost_input_element is None:
        return False
    medical_dental_cost_input_element_visible = wait_for_element_visible(driver, medical_dental_cost_input)
    print(f"medical_dental_cost_input_element_visible {medical_dental_cost_input_element_visible}")
    if medical_dental_cost_input_element_visible is False:
        return False
    medical_dental_cost_input_element.clear()
    medical_dental_cost_input_element.send_keys(medical_dental_cost)
    return True

def emergency_fund_calculator_check_medical_dental_cost(driver,medical_dental_cost):
    medical_dental_cost_input = money_control_element["medical_dental_cost_input"]
    medical_dental_cost_input_element = find_element_use_xpath(driver, medical_dental_cost_input)
    if medical_dental_cost_input_element is None:
        return False
    medical_dental_cost_input_element_visible = wait_for_element_visible(driver, medical_dental_cost_input)
    print(f"medical_dental_cost_input_element_visible {medical_dental_cost_input_element_visible}")
    if medical_dental_cost_input_element_visible is False:
        return False
    medical_dental_cost_input_element_value_attribute = medical_dental_cost_input_element.get_attribute("value")
    print(f"medical_dental_cost_input_element_value_attribute {medical_dental_cost_input_element_value_attribute}")
    if medical_dental_cost_input_element_value_attribute != medical_dental_cost:
        return False
    return True

def emergency_fund_calculator_enter_vehicle_repair(driver,vehicle_repair):
    vehicle_repair_input = money_control_element["vehicle_repair_input"]
    vehicle_repair_input_element = find_element_use_xpath(driver, vehicle_repair_input)
    if vehicle_repair_input_element is None:
        return False
    vehicle_repair_input_element_visible = wait_for_element_visible(driver, vehicle_repair_input)
    print(f"vehicle_repair_input_element_visible {vehicle_repair_input_element_visible}")
    if vehicle_repair_input_element_visible is False:
        return False
    vehicle_repair_input_element.clear()
    vehicle_repair_input_element.send_keys(vehicle_repair)
    return True


def emergency_fund_calculator_check_vehicle_repair(driver,vehicle_repair):
    vehicle_repair_input = money_control_element["vehicle_repair_input"]
    vehicle_repair_input_element = find_element_use_xpath(driver, vehicle_repair_input)
    if vehicle_repair_input_element is None:
        return False
    vehicle_repair_input_element_visible = wait_for_element_visible(driver, vehicle_repair_input)
    print(f"vehicle_repair_input_element_visible {vehicle_repair_input_element_visible}")
    if vehicle_repair_input_element_visible is False:
        return False
    vehicle_repair_input_element_value_attribute = vehicle_repair_input_element.get_attribute("value")
    print(f"vehicle_repair_input_element_value_attribute {vehicle_repair_input_element_value_attribute}")
    if vehicle_repair_input_element_value_attribute != vehicle_repair:
        return False
    return True

def emergency_fund_calculator_enter_others(driver,others):
    others_input = money_control_element["others_input"]
    others_input_element = find_element_use_xpath(driver, others_input)
    if others_input_element is None:
        return False
    others_input_element_visible = wait_for_element_visible(driver, others_input)
    print(f"others_input_element_visible {others_input_element_visible}")
    if others_input_element_visible is False:
        return False
    others_input_element.clear()
    others_input_element.send_keys(others)
    return True

def emergency_fund_calculator_check_others(driver,others):
    others_input = money_control_element["others_input"]
    others_input_element = find_element_use_xpath(driver, others_input)
    if others_input_element is None:
        return False
    others_input_element_visible = wait_for_element_visible(driver, others_input)
    print(f"others_input_element_visible {others_input_element_visible}")
    if others_input_element_visible is False:
        return False
    others_input_element_value_attribute = others_input_element.get_attribute("value")
    print(f"others_input_element_value_attribute {others_input_element_value_attribute}")
    if others_input_element_value_attribute != others:
        return False
    return True

def emergency_fund_calculator_enter_life_health_insurance_premium(driver,life_health_insurance_premium):
    life_health_insurance_premium_input = money_control_element["life_health_insurance_premium_input"]
    life_health_insurance_premium_input_element = find_element_use_xpath(driver, life_health_insurance_premium_input)
    if life_health_insurance_premium_input_element is None:
        return False
    life_health_insurance_premium_input_element_visible = wait_for_element_visible(driver, life_health_insurance_premium_input)
    print(f"life_health_insurance_premium_input_element_visible {life_health_insurance_premium_input_element_visible}")
    if life_health_insurance_premium_input_element_visible is False:
        return False
    life_health_insurance_premium_input_element.clear()
    life_health_insurance_premium_input_element.send_keys(life_health_insurance_premium)
    return True

def emergency_fund_calculator_check_life_health_insurance_premium(driver,life_health_insurance_premium):
    life_health_insurance_premium_input = money_control_element["life_health_insurance_premium_input"]
    life_health_insurance_premium_input_element = find_element_use_xpath(driver, life_health_insurance_premium_input)
    if life_health_insurance_premium_input_element is None:
        return False
    life_health_insurance_premium_input_element_visible = wait_for_element_visible(driver, life_health_insurance_premium_input)
    print(f"life_health_insurance_premium_input_element_visible {life_health_insurance_premium_input_element_visible}")
    if life_health_insurance_premium_input_element_visible is False:
        return False
    life_health_insurance_premium_input_element_value_attribute = life_health_insurance_premium_input_element.get_attribute("value")
    print(f"life_health_insurance_premium_input_element_value_attribute {life_health_insurance_premium_input_element_value_attribute}")
    if life_health_insurance_premium_input_element_value_attribute != life_health_insurance_premium:
        return False
    return True

def emergency_fund_calculator_enter_home_auto_insurance_premium(driver,home_auto_insurance_premium):
    home_auto_insurance_premium_input = money_control_element["home_auto_insurance_premium_input"]
    home_auto_insurance_premium_input_element = find_element_use_xpath(driver, home_auto_insurance_premium_input)
    if home_auto_insurance_premium_input_element is None:
        return False
    home_auto_insurance_premium_input_element_visible = wait_for_element_visible(driver,
                                                                                   home_auto_insurance_premium_input)
    print(f"home_auto_insurance_premium_input_element_visible {home_auto_insurance_premium_input_element_visible}")
    if home_auto_insurance_premium_input_element_visible is False:
        return False
    home_auto_insurance_premium_input_element.clear()
    home_auto_insurance_premium_input_element.send_keys(home_auto_insurance_premium)
    return True


def emergency_fund_calculator_check_home_auto_insurance_premium(driver,home_auto_insurance_premium):
    home_auto_insurance_premium_input = money_control_element["home_auto_insurance_premium_input"]
    home_auto_insurance_premium_input_element = find_element_use_xpath(driver, home_auto_insurance_premium_input)
    if home_auto_insurance_premium_input_element is None:
        return False
    home_auto_insurance_premium_input_element_visible = wait_for_element_visible(driver,
                                                                                   home_auto_insurance_premium_input)
    print(f"home_auto_insurance_premium_input_element_visible {home_auto_insurance_premium_input_element_visible}")
    if home_auto_insurance_premium_input_element_visible is False:
        return False
    home_auto_insurance_premium_input_element_value_attribute = home_auto_insurance_premium_input_element.get_attribute(
        "value")
    print(
        f"home_auto_insurance_premium_input_element_value_attribute {home_auto_insurance_premium_input_element_value_attribute}")
    if home_auto_insurance_premium_input_element_value_attribute != home_auto_insurance_premium:
        return False
    return True

def emergency_fund_calculator_enter_home_loan_other_important_emis(driver,home_loan_other_important_emis):
    home_loan_other_important_emis_input = money_control_element["home_loan_other_important_emis_input"]
    home_loan_other_important_emis_input_element = find_element_use_xpath(driver, home_loan_other_important_emis_input)
    if home_loan_other_important_emis_input_element is None:
        return False
    home_loan_other_important_emis_input_element_visible = wait_for_element_visible(driver,
                                                                                 home_loan_other_important_emis_input)
    print(f"home_loan_other_important_emis_input_element_visible {home_loan_other_important_emis_input_element_visible}")
    if home_loan_other_important_emis_input_element_visible is False:
        return False
    home_loan_other_important_emis_input_element.clear()
    home_loan_other_important_emis_input_element.send_keys(home_loan_other_important_emis)
    return True

def emergency_fund_calculator_check_home_loan_other_important_emis(driver,home_loan_other_important_emis):
    home_loan_other_important_emis_input = money_control_element["home_loan_other_important_emis_input"]
    home_loan_other_important_emis_input_element = find_element_use_xpath(driver, home_loan_other_important_emis_input)
    if home_loan_other_important_emis_input_element is None:
        return False
    home_loan_other_important_emis_input_element_visible = wait_for_element_visible(driver,
                                                                                 home_loan_other_important_emis_input)
    print(f"home_loan_other_important_emis_input_element_visible {home_loan_other_important_emis_input_element_visible}")
    if home_loan_other_important_emis_input_element_visible is False:
        return False
    home_loan_other_important_emis_input_element_value_attribute = home_loan_other_important_emis_input_element.get_attribute(
        "value")
    print(
        f"home_loan_other_important_emis_input_element_value_attribute {home_loan_other_important_emis_input_element_value_attribute}")
    if home_loan_other_important_emis_input_element_value_attribute != home_loan_other_important_emis:
        return False
    return True


def emergency_fund_calculator_enter_monthly_living_expenses(driver,monthly_living_expenses):
    monthly_living_expenses_input = money_control_element["monthly_living_expenses_input"]
    monthly_living_expenses_input_element = find_element_use_xpath(driver, monthly_living_expenses_input)
    if monthly_living_expenses_input_element is None:
        return False
    monthly_living_expenses_input_element_visible = wait_for_element_visible(driver,
                                                                             monthly_living_expenses_input)
    print(f"monthly_living_expenses_input_element_visible {monthly_living_expenses_input_element_visible}")
    if monthly_living_expenses_input_element_visible is False:
        return False
    monthly_living_expenses_input_element.clear()
    monthly_living_expenses_input_element.send_keys(monthly_living_expenses)
    return True

def emergency_fund_calculator_check_monthly_living_expenses(driver,monthly_living_expenses):
    monthly_living_expenses_input = money_control_element["monthly_living_expenses_input"]
    monthly_living_expenses_input_element = find_element_use_xpath(driver, monthly_living_expenses_input)
    if monthly_living_expenses_input_element is None:
        return False
    monthly_living_expenses_input_element_visible = wait_for_element_visible(driver,
                                                                             monthly_living_expenses_input)
    print(f"monthly_living_expenses_input_element_visible {monthly_living_expenses_input_element_visible}")
    if monthly_living_expenses_input_element_visible is False:
        return False
    monthly_living_expenses_input_element_value_attribute = monthly_living_expenses_input_element.get_attribute(
        "value")
    print(
        f"monthly_living_expenses_input_element_value_attribute {monthly_living_expenses_input_element_value_attribute}")
    if monthly_living_expenses_input_element_value_attribute != monthly_living_expenses:
        return False
    return True

def emergency_fund_calculator_enter_month_unemployed(driver,month_unemployed):
    month_unemployed_input = money_control_element["month_unemployed_input"]
    month_unemployed_input_element = find_element_use_xpath(driver, month_unemployed_input)
    if month_unemployed_input_element is None:
        return False
    month_unemployed_input_element_visible = wait_for_element_visible(driver,
                                                                             month_unemployed_input)
    print(f"month_unemployed_input_element_visible {month_unemployed_input_element_visible}")
    if month_unemployed_input_element_visible is False:
        return False
    month_unemployed_input_element.clear()
    month_unemployed_input_element.send_keys(month_unemployed)
    return True

def emergency_fund_calculator_check_month_unemployed(driver,month_unemployed):
    month_unemployed_input = money_control_element["month_unemployed_input"]
    month_unemployed_input_element = find_element_use_xpath(driver, month_unemployed_input)
    if month_unemployed_input_element is None:
        return False
    month_unemployed_input_element_visible = wait_for_element_visible(driver,
                                                                             month_unemployed_input)
    print(f"month_unemployed_input_element_visible {month_unemployed_input_element_visible}")
    if month_unemployed_input_element_visible is False:
        return False
    month_unemployed_input_element_value_attribute = month_unemployed_input_element.get_attribute(
        "value")
    print(
        f"month_unemployed_input_element_value_attribute {month_unemployed_input_element_value_attribute}")
    if month_unemployed_input_element_value_attribute != month_unemployed:
        return False
    return True


def emergency_fund_calculator_click_calculate_button(driver):
    calculate_button = money_control_element["calculate_button"]
    calculate_button_element = find_element_use_xpath(driver, calculate_button)
    if calculate_button_element is None:
        return False
    calculate_button_element_visible = wait_for_element_visible(driver, calculate_button)
    print(f"calculate_button_element_visible {calculate_button_element_visible}")
    if calculate_button_element_visible is False:
        return False
    calculate_button_element.click()
    return True


def emergency_fund_calculator_check_uninsured_unexpected_emergencies_total(driver,uninsured_unexpected_emergencies_total):
    uninsured_unexpected_emergencies_total_div = money_control_element["uninsured_unexpected_emergencies_total_div"]
    uninsured_unexpected_emergencies_total_div_element = find_element_use_xpath(driver, uninsured_unexpected_emergencies_total_div)
    if uninsured_unexpected_emergencies_total_div_element is None:
        return False
    uninsured_unexpected_emergencies_total_div_element_visible = wait_for_element_visible(driver, uninsured_unexpected_emergencies_total_div)
    print(f"uninsured_unexpected_emergencies_total_div_element_visible {uninsured_unexpected_emergencies_total_div_element_visible}")
    if uninsured_unexpected_emergencies_total_div_element_visible is False:
        return False
    uninsured_unexpected_emergencies_total_div_element_text = uninsured_unexpected_emergencies_total_div_element.text
    print(f"uninsured_unexpected_emergencies_total_div_element_text {uninsured_unexpected_emergencies_total_div_element_text}")
    if uninsured_unexpected_emergencies_total_div_element_text != uninsured_unexpected_emergencies_total:
        return False
    return True

def emergency_fund_calculator_check_annual_amount_of_fixed_payments_total(driver,annual_amount_of_fixed_payments_total):
    annual_amount_of_fixed_payments_total_div = money_control_element["annual_amount_of_fixed_payments_total_div"]
    annual_amount_of_fixed_payments_total_div_element = find_element_use_xpath(driver,
                                                                                annual_amount_of_fixed_payments_total_div)
    if annual_amount_of_fixed_payments_total_div_element is None:
        return False
    annual_amount_of_fixed_payments_total_div_element_visible = wait_for_element_visible(driver,
                                                                                          annual_amount_of_fixed_payments_total_div)
    print(
        f"annual_amount_of_fixed_payments_total_div_element_visible {annual_amount_of_fixed_payments_total_div_element_visible}")
    if annual_amount_of_fixed_payments_total_div_element_visible is False:
        return False
    annual_amount_of_fixed_payments_total_div_element_text = annual_amount_of_fixed_payments_total_div_element.text
    print(
        f"annual_amount_of_fixed_payments_total_div_element_text {annual_amount_of_fixed_payments_total_div_element_text}")
    if annual_amount_of_fixed_payments_total_div_element_text != annual_amount_of_fixed_payments_total:
        return False
    return True

def emergency_fund_calculator_check_build_reserve_to_pay_for_job_loss(driver,build_reserve_to_pay_for_job_loss):
    build_reserve_to_pay_for_job_loss_div = money_control_element["build_reserve_to_pay_for_job_loss_div"]
    build_reserve_to_pay_for_job_loss_div_element = find_element_use_xpath(driver,
                                                                               build_reserve_to_pay_for_job_loss_div)
    if build_reserve_to_pay_for_job_loss_div_element is None:
        return False
    build_reserve_to_pay_for_job_loss_div_element_visible = wait_for_element_visible(driver,
                                                                                         build_reserve_to_pay_for_job_loss_div)
    print(
        f"build_reserve_to_pay_for_job_loss_div_element_visible {build_reserve_to_pay_for_job_loss_div_element_visible}")
    if build_reserve_to_pay_for_job_loss_div_element_visible is False:
        return False
    build_reserve_to_pay_for_job_loss_div_element_text = build_reserve_to_pay_for_job_loss_div_element.text
    print(
        f"build_reserve_to_pay_for_job_loss_div_element_text {build_reserve_to_pay_for_job_loss_div_element_text}")
    if build_reserve_to_pay_for_job_loss_div_element_text != build_reserve_to_pay_for_job_loss:
        return False
    return True

def emergency_fund_calculator_check_result(driver,result):
    emergency_fund_calculator_result_div = money_control_element["emergency_fund_calculator_result_div"]
    emergency_fund_calculator_result_div_element = find_element_use_xpath(driver,
                                                                       emergency_fund_calculator_result_div)
    if emergency_fund_calculator_result_div_element is None:
        return False
    emergency_fund_calculator_result_div_element_visible = wait_for_element_visible(driver,
                                                                                 emergency_fund_calculator_result_div)
    print(
        f"emergency_fund_calculator_result_div_element_visible {emergency_fund_calculator_result_div_element_visible}")
    if emergency_fund_calculator_result_div_element_visible is False:
        return False
    emergency_fund_calculator_result_div_element_text = emergency_fund_calculator_result_div_element.text
    print(
        f"emergency_fund_calculator_result_div_element_text {emergency_fund_calculator_result_div_element_text}")

    if result not in emergency_fund_calculator_result_div_element_text:
        return False
    return True

def provident_fund_calculator_enter_your_age(driver,your_age):
    your_age_input = money_control_element["your_age_input"]
    your_age_input_element = find_element_use_xpath(driver, your_age_input)
    if your_age_input_element is None:
        return False
    your_age_input_element_visible = wait_for_element_visible(driver, your_age_input)
    print(f"your_age_input_element_visible {your_age_input_element_visible}")
    if your_age_input_element_visible is False:
        return False
    your_age_input_element.clear()
    your_age_input_element.send_keys(your_age)
    return True

def provident_fund_calculator_check_your_age(driver,your_age):
    your_age_input = money_control_element["your_age_input"]
    your_age_input_element = find_element_use_xpath(driver, your_age_input)
    if your_age_input_element is None:
        return False
    your_age_input_element_visible = wait_for_element_visible(driver, your_age_input)
    print(f"your_age_input_element_visible {your_age_input_element_visible}")
    if your_age_input_element_visible is False:
        return False
    your_age_input_element_value_attribute = your_age_input_element.get_attribute("value")
    print(f"your_age_input_element_value_attribute {your_age_input_element_value_attribute}")
    if your_age_input_element_value_attribute != your_age:
        return False
    return True

def provident_fund_calculator_enter_your_basic_salary_monthly(driver,your_basic_salary_monthly):
    your_basic_salary_monthly_input = money_control_element["your_basic_salary_monthly_input"]
    your_basic_salary_monthly_input_element = find_element_use_xpath(driver, your_basic_salary_monthly_input)
    if your_basic_salary_monthly_input_element is None:
        return False
    your_basic_salary_monthly_input_element_visible = wait_for_element_visible(driver, your_basic_salary_monthly_input)
    print(f"your_basic_salary_monthly_input_element_visible {your_basic_salary_monthly_input_element_visible}")
    if your_basic_salary_monthly_input_element_visible is False:
        return False
    your_basic_salary_monthly_input_element.clear()
    your_basic_salary_monthly_input_element.send_keys(your_basic_salary_monthly)
    return True

def provident_fund_calculator_check_your_basic_salary_monthly(driver,your_basic_salary_monthly):
    your_basic_salary_monthly_input = money_control_element["your_basic_salary_monthly_input"]
    your_basic_salary_monthly_input_element = find_element_use_xpath(driver, your_basic_salary_monthly_input)
    if your_basic_salary_monthly_input_element is None:
        return False
    your_basic_salary_monthly_input_element_visible = wait_for_element_visible(driver, your_basic_salary_monthly_input)
    print(f"your_basic_salary_monthly_input_element_visible {your_basic_salary_monthly_input_element_visible}")
    if your_basic_salary_monthly_input_element_visible is False:
        return False
    your_basic_salary_monthly_input_element_value_attribute = your_basic_salary_monthly_input_element.get_attribute("value")
    print(f"your_basic_salary_monthly_input_element_value_attribute {your_basic_salary_monthly_input_element_value_attribute}")
    if your_basic_salary_monthly_input_element_value_attribute != your_basic_salary_monthly:
        return False
    return True

def provident_fund_calculator_enter_your_contribution_to_epf(driver,your_contribution_to_epf):
    your_contribution_to_epf_input = money_control_element["your_contribution_to_epf_input"]
    your_contribution_to_epf_input_element = find_element_use_xpath(driver, your_contribution_to_epf_input)
    if your_contribution_to_epf_input_element is None:
        return False
    your_contribution_to_epf_input_element_visible = wait_for_element_visible(driver, your_contribution_to_epf_input)
    print(f"your_contribution_to_epf_input_element_visible {your_contribution_to_epf_input_element_visible}")
    if your_contribution_to_epf_input_element_visible is False:
        return False
    your_contribution_to_epf_input_element.clear()
    your_contribution_to_epf_input_element.send_keys(your_contribution_to_epf)
    return True

def provident_fund_calculator_check_your_contribution_to_epf(driver,your_contribution_to_epf):
    your_contribution_to_epf_input = money_control_element["your_contribution_to_epf_input"]
    your_contribution_to_epf_input_element = find_element_use_xpath(driver, your_contribution_to_epf_input)
    if your_contribution_to_epf_input_element is None:
        return False
    your_contribution_to_epf_input_element_visible = wait_for_element_visible(driver, your_contribution_to_epf_input)
    print(f"your_contribution_to_epf_input_element_visible {your_contribution_to_epf_input_element_visible}")
    if your_contribution_to_epf_input_element_visible is False:
        return False
    your_contribution_to_epf_input_element_value_attribute = your_contribution_to_epf_input_element.get_attribute(
        "value")
    print(
        f"your_contribution_to_epf_input_element_value_attribute {your_contribution_to_epf_input_element_value_attribute}")
    if your_contribution_to_epf_input_element_value_attribute != your_contribution_to_epf:
        return False
    return True

def provident_fund_calculator_enter_your_employer_contribution_to_epf(driver,your_employer_contribution_to_epf):
    your_employer_contribution_to_epf_input = money_control_element["your_employer_contribution_to_epf_input"]
    your_employer_contribution_to_epf_input_element = find_element_use_xpath(driver, your_employer_contribution_to_epf_input)
    if your_employer_contribution_to_epf_input_element is None:
        return False
    your_employer_contribution_to_epf_input_element_visible = wait_for_element_visible(driver, your_employer_contribution_to_epf_input)
    print(f"your_employer_contribution_to_epf_input_element_visible {your_employer_contribution_to_epf_input_element_visible}")
    if your_employer_contribution_to_epf_input_element_visible is False:
        return False
    your_employer_contribution_to_epf_input_element.clear()
    your_employer_contribution_to_epf_input_element.send_keys(your_employer_contribution_to_epf)
    return True

def provident_fund_calculator_check_your_employer_contribution_to_epf(driver,your_employer_contribution_to_epf):
    your_employer_contribution_to_epf_input = money_control_element["your_employer_contribution_to_epf_input"]
    your_employer_contribution_to_epf_input_element = find_element_use_xpath(driver, your_employer_contribution_to_epf_input)
    if your_employer_contribution_to_epf_input_element is None:
        return False
    your_employer_contribution_to_epf_input_element_visible = wait_for_element_visible(driver, your_employer_contribution_to_epf_input)
    print(f"your_employer_contribution_to_epf_input_element_visible {your_employer_contribution_to_epf_input_element_visible}")
    if your_employer_contribution_to_epf_input_element_visible is False:
        return False
    your_employer_contribution_to_epf_input_element_value_attribute = your_employer_contribution_to_epf_input_element.get_attribute(
        "value")
    print(
        f"your_employer_contribution_to_epf_input_element_value_attribute {your_employer_contribution_to_epf_input_element_value_attribute}")
    if your_employer_contribution_to_epf_input_element_value_attribute != your_employer_contribution_to_epf:
        return False
    return True

def provident_fund_calculator_enter_average_annual_increase_in_salary_you_expect(driver,average_annual_increase_in_salary_you_expect):
    average_annual_increase_in_salary_you_expect_input = money_control_element["average_annual_increase_in_salary_you_expect_input"]
    average_annual_increase_in_salary_you_expect_input_element = find_element_use_xpath(driver,
                                                                             average_annual_increase_in_salary_you_expect_input)
    if average_annual_increase_in_salary_you_expect_input_element is None:
        return False
    average_annual_increase_in_salary_you_expect_input_element_visible = wait_for_element_visible(driver,
                                                                                       average_annual_increase_in_salary_you_expect_input)
    print(
        f"average_annual_increase_in_salary_you_expect_input_element_visible {average_annual_increase_in_salary_you_expect_input_element_visible}")
    if average_annual_increase_in_salary_you_expect_input_element_visible is False:
        return False
    average_annual_increase_in_salary_you_expect_input_element.clear()
    average_annual_increase_in_salary_you_expect_input_element.send_keys(average_annual_increase_in_salary_you_expect)
    return True

def provident_fund_calculator_check_average_annual_increase_in_salary_you_expect(driver,average_annual_increase_in_salary_you_expect):
    average_annual_increase_in_salary_you_expect_input = money_control_element["average_annual_increase_in_salary_you_expect_input"]
    average_annual_increase_in_salary_you_expect_input_element = find_element_use_xpath(driver,
                                                                             average_annual_increase_in_salary_you_expect_input)
    if average_annual_increase_in_salary_you_expect_input_element is None:
        return False
    average_annual_increase_in_salary_you_expect_input_element_visible = wait_for_element_visible(driver,
                                                                                       average_annual_increase_in_salary_you_expect_input)
    print(
        f"average_annual_increase_in_salary_you_expect_input_element_visible {average_annual_increase_in_salary_you_expect_input_element_visible}")
    if average_annual_increase_in_salary_you_expect_input_element_visible is False:
        return False
    average_annual_increase_in_salary_you_expect_input_element_value_attribute = average_annual_increase_in_salary_you_expect_input_element.get_attribute(
        "value")
    print(
        f"average_annual_increase_in_salary_you_expect_input_element_value_attribute {average_annual_increase_in_salary_you_expect_input_element_value_attribute}")
    if average_annual_increase_in_salary_you_expect_input_element_value_attribute != average_annual_increase_in_salary_you_expect:
        return False
    return True

def provident_fund_calculator_enter_age_when_you_intend_to_retire(driver,age_when_you_intend_to_retire):
    age_when_you_intend_to_retire_input = money_control_element[
        "age_when_you_intend_to_retire_input"]
    age_when_you_intend_to_retire_input_element = find_element_use_xpath(driver,
                                                                                        age_when_you_intend_to_retire_input)
    if age_when_you_intend_to_retire_input_element is None:
        return False
    age_when_you_intend_to_retire_input_element_visible = wait_for_element_visible(driver,
                                                                                                  age_when_you_intend_to_retire_input)
    print(
        f"age_when_you_intend_to_retire_input_element_visible {age_when_you_intend_to_retire_input_element_visible}")
    if age_when_you_intend_to_retire_input_element_visible is False:
        return False
    age_when_you_intend_to_retire_input_element.clear()
    age_when_you_intend_to_retire_input_element.send_keys(age_when_you_intend_to_retire)
    return True

def provident_fund_calculator_check_age_when_you_intend_to_retire(driver,age_when_you_intend_to_retire):
    age_when_you_intend_to_retire_input = money_control_element[
        "age_when_you_intend_to_retire_input"]
    age_when_you_intend_to_retire_input_element = find_element_use_xpath(driver,
                                                                                        age_when_you_intend_to_retire_input)
    if age_when_you_intend_to_retire_input_element is None:
        return False
    age_when_you_intend_to_retire_input_element_visible = wait_for_element_visible(driver,
                                                                                                  age_when_you_intend_to_retire_input)
    print(
        f"age_when_you_intend_to_retire_input_element_visible {age_when_you_intend_to_retire_input_element_visible}")
    if age_when_you_intend_to_retire_input_element_visible is False:
        return False
    age_when_you_intend_to_retire_input_element_value_attribute = age_when_you_intend_to_retire_input_element.get_attribute(
        "value")
    print(
        f"age_when_you_intend_to_retire_input_element_value_attribute {age_when_you_intend_to_retire_input_element_value_attribute}")
    if age_when_you_intend_to_retire_input_element_value_attribute != age_when_you_intend_to_retire:
        return False
    return True

def provident_fund_calculator_enter_current_epf_balance_if_any(driver,current_epf_balance_if_any):
    current_epf_balance_if_any_input = money_control_element[
        "current_epf_balance_if_any_input"]
    current_epf_balance_if_any_input_element = find_element_use_xpath(driver,
                                                                         current_epf_balance_if_any_input)
    if current_epf_balance_if_any_input_element is None:
        return False
    current_epf_balance_if_any_input_element_visible = wait_for_element_visible(driver,
                                                                                   current_epf_balance_if_any_input)
    print(
        f"current_epf_balance_if_any_input_element_visible {current_epf_balance_if_any_input_element_visible}")
    if current_epf_balance_if_any_input_element_visible is False:
        return False
    current_epf_balance_if_any_input_element.clear()
    current_epf_balance_if_any_input_element.send_keys(current_epf_balance_if_any)
    return True

def provident_fund_calculator_check_current_epf_balance_if_any(driver,current_epf_balance_if_any):
    current_epf_balance_if_any_input = money_control_element[
        "current_epf_balance_if_any_input"]
    current_epf_balance_if_any_input_element = find_element_use_xpath(driver,
                                                                         current_epf_balance_if_any_input)
    if current_epf_balance_if_any_input_element is None:
        return False
    current_epf_balance_if_any_input_element_visible = wait_for_element_visible(driver,
                                                                                   current_epf_balance_if_any_input)
    print(
        f"current_epf_balance_if_any_input_element_visible {current_epf_balance_if_any_input_element_visible}")
    if current_epf_balance_if_any_input_element_visible is False:
        return False
    current_epf_balance_if_any_input_element_value_attribute = current_epf_balance_if_any_input_element.get_attribute(
        "value")
    print(
        f"current_epf_balance_if_any_input_element_value_attribute {current_epf_balance_if_any_input_element_value_attribute}")
    if current_epf_balance_if_any_input_element_value_attribute != current_epf_balance_if_any:
        return False
    return True

def provident_fund_calculator_enter_current_interest_rate(driver,current_interest_rate):
    current_interest_rate_input = money_control_element[
        "current_interest_rate_input"]
    current_interest_rate_input_element = find_element_use_xpath(driver,
                                                                      current_interest_rate_input)
    if current_interest_rate_input_element is None:
        return False
    current_interest_rate_input_element_visible = wait_for_element_visible(driver,
                                                                                current_interest_rate_input)
    print(
        f"current_interest_rate_input_element_visible {current_interest_rate_input_element_visible}")
    if current_interest_rate_input_element_visible is False:
        return False
    current_interest_rate_input_element.clear()
    current_interest_rate_input_element.send_keys(current_interest_rate)
    return True

def provident_fund_calculator_check_current_interest_rate(driver,current_interest_rate):
    current_interest_rate_input = money_control_element[
        "current_interest_rate_input"]
    current_interest_rate_input_element = find_element_use_xpath(driver,
                                                                      current_interest_rate_input)
    if current_interest_rate_input_element is None:
        return False
    current_interest_rate_input_element_visible = wait_for_element_visible(driver,
                                                                                current_interest_rate_input)
    print(
        f"current_interest_rate_input_element_visible {current_interest_rate_input_element_visible}")
    if current_interest_rate_input_element_visible is False:
        return False
    current_interest_rate_input_element_value_attribute = current_interest_rate_input_element.get_attribute(
        "value")
    print(
        f"current_interest_rate_input_element_value_attribute {current_interest_rate_input_element_value_attribute}")
    if current_interest_rate_input_element_value_attribute != current_interest_rate:
        return False
    return True

def provident_fund_calculator_click_submit_button(driver):
    pf_calculator_calculate_button = money_control_element["pf_calculator_calculate_button"]
    pf_calculator_calculate_button_element = find_element_use_xpath(driver, pf_calculator_calculate_button)
    if pf_calculator_calculate_button_element is None:
        return False
    pf_calculator_calculate_button_element_visible = wait_for_element_visible(driver, pf_calculator_calculate_button)
    print(f"pf_calculator_calculate_button_element_visible {pf_calculator_calculate_button_element_visible}")
    if pf_calculator_calculate_button_element_visible is False:
        return False
    pf_calculator_calculate_button_element.click()
    return True

def provident_fund_calculator_check_result(driver,result):
    pf_cal_result_div = money_control_element["pf_cal_result_div"]
    pf_cal_result_div_element = find_element_use_xpath(driver,
                                                                       pf_cal_result_div)
    if pf_cal_result_div_element is None:
        return False
    pf_cal_result_div_element_visible = wait_for_element_visible(driver,
                                                                                 pf_cal_result_div)
    print(
        f"pf_cal_result_div_element_visible {pf_cal_result_div_element_visible}")
    if pf_cal_result_div_element_visible is False:
        return False
    pf_cal_result_div_element_text = pf_cal_result_div_element.text
    print(
        f"pf_cal_result_div_element_text {pf_cal_result_div_element_text}")

    if result not in pf_cal_result_div_element_text:
        return False
    return True




def test_login(driver):
    # open_login_panel(driver)
    # open_signin_box(driver)
    # signin_box_enter_email(driver, "prashant.ranjan.qa@gmail.com")
    # signin_box_enter_password(driver, "igetup@7AM")
    # signin_box_click_login_button(driver)
    # signin_box_check_error(driver, "Invalid User Id/EmailID or Password. Please try again.")
    # check_logged_in_user(driver, "Prashant.ranjan.qa@gmail.com")
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

