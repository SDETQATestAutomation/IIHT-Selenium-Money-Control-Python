'''
Created on 29-Oct-2023

@author: pranjan
'''
import math

from selenium import webdriver
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
from src.test.python.com.iiht.evaluation.automation.locators.object_repository import money_control_element
from src.test.python.com.iiht.evaluation.automation.testutils.MasterData import MasterData
from src.test.python.com.iiht.evaluation.automation.testutils.TestUtils import TestUtils


class SubActivities:
    @staticmethod
    def check_page_load_complete(driver: webdriver):
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

    @staticmethod
    def find_element_use_xpath(driver: webdriver, xpath):
        required_element = None
        try:
            required_element = driver.find_element(By.XPATH, xpath)
        except Exception as ex:
            print(f"ex {ex}")
        finally:
            return required_element

    @staticmethod
    def wait_for_element_not_present(driver: webdriver, xpath):
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

    @staticmethod
    def wait_for_element_present(driver: webdriver, xpath):
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

    @staticmethod
    def wait_for_element_visible(driver: webdriver, xpath):
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

    @staticmethod
    def wait_for_element_not_visible(driver: webdriver, xpath):
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

    @staticmethod
    def do_javascript_click(driver: webdriver, element):
        try:
            driver.execute_script("arguments[0].click();", element)
        except Exception as ex:
            print(f"ex {ex}")
