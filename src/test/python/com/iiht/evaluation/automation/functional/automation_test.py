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

