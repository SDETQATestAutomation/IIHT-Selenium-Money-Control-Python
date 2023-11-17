'''
Created on 29-Oct-2023

@author: pranjan
'''
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.main.pyhton.com.iiht.evaluation.automation import Helpers
from src.main.pyhton.com.iiht.evaluation.automation import SubActivities
from src.test.python.com.iiht.evaluation.automation.testutils.MasterData import MasterData
from src.test.python.com.iiht.evaluation.automation.testutils.TestUtils import TestUtils
from root_path import get_project_root


@pytest.fixture(scope="session")
def driver(request):
    req_root_path=get_project_root();
    print(f"${req_root_path}")
    req_chrome_driver_path=req_root_path+"/binaries/chromedriver.exe"
    print(f"{req_chrome_driver_path}")
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
    service = Service(req_chrome_driver_path)
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


def get_href_of_link(driver):
    if driver.get_attribute("outerHTML").startswith("<a"):
        return driver.get_attribute("href")
    else:
        return driver.get_attribute("outerHTML")


@pytest.mark.order(1)
def test_mouse_over_personal_finance(driver):
    utils = TestUtils()
    master_data = MasterData()
    try:
        element = Helpers.getElementforMouseOver(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[0]
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(2)
def test_get_tool_for_emi_calculator(driver):
    utils = TestUtils()
    master_data = MasterData()
    try:
        element = Helpers.getElementforTool(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[1]
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(3)
def test_get_home_loan_emi_calculator(driver):
    utils = TestUtils()
    master_data = MasterData()
    try:
        element = Helpers.getElementforHomeLoan(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[2]
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Home Loan')]")))
        driver.execute_script("arguments[0].click();", element)
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(4)
def test_access_loan_amount(driver):
    utils = TestUtils()
    master_data = MasterData()
    try:
        element = Helpers.getElementforLoanAmount(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[3]
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(5)
def test_set_value_for_loan_amount(driver):
    utils = TestUtils()
    try:
        status = SubActivities.enterValueLoanAmount(driver)
        # utils.yakshaAssert(utils.currentTest(), status,"Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(6)
def test_access_loan_period(driver):
    utils = TestUtils()
    master_data = MasterData()
    try:
        element = Helpers.getElementforLoanPeriod(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[4]
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")

@pytest.mark.order(7)
def test_set_value_for_loan_period(driver):
    utils = TestUtils()
    try:
        status = SubActivities.enterValueLoanPeriod(driver)
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(9)
def test_set_value_for_emi_start_from(driver):
    utils = TestUtils()
    try:
        status = SubActivities.selectEMIStartsFrom(driver)
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(10)
def test_access_interest_rate(driver):
    utils = TestUtils()
    master_data = MasterData()
    try:
        element = Helpers.getElementforInterestRate(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[6]
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(11)
def test_set_value_for_interest_rate(driver):
    utils = TestUtils()
    try:
        status = SubActivities.enterInterestRate(driver)
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(12)
def test_access_upfront_charges(driver):
    utils = TestUtils()
    master_data = MasterData()
    status = False
    try:
        element = Helpers.getElementforUpfrontcharges(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[7]
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(13)
def test_set_value_for_upfront_charges(driver):
    utils = TestUtils()
    status = False
    try:
        status = SubActivities.enterValueUpfrontCharges(driver)
        # utils.yakshaAssert(utils.currentTest(), status, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(14)
def test_get_total_payment_element(driver):
    utils = TestUtils()
    try:
        element = SubActivities.getTotalPaymentElement(driver)
        if element is not None:
            print(True)
            # utils.yakshaAssert(utils.currentTest(), True, "Business")
        else:
            print(False)
            # utils.yakshaAssert(utils.currentTest(), False, "Business")
    except Exception as ex:
        print(ex)
        # utils.yakshaAssert(utils.currentTest(), False, "Business")


@pytest.mark.order(15)
def test_get_xpath_for_7th_year_emi_payment(driver):
    utils = TestUtils()
    status = Helpers.getXpathfor7thYearEMIPayment().find("sibling")
    # utils.yakshaAssert(utils.currentTest(), status, "Business")


@pytest.mark.order(16)
def test_get_xpath_for_7th_year_interest_payment(driver):
    utils = TestUtils()
    status = Helpers.getXpathfor7thYearInterestPayment().find("sibling")
    # utils.yakshaAssert(utils.currentTest(), status, "Business")


@pytest.mark.order(17)
def test_get_xpath_for_7th_year_principal_payment(driver):
    utils = TestUtils()
    status = Helpers.getXpathfor7thYearPrincipalPayment().find("sibling")
    # utils.yakshaAssert(utils.currentTest(), status, "Business")


@pytest.mark.order(18)
def test_get_xpath_for_5th_year_outstanding_principal_payment(driver):
    utils = TestUtils()
    status = Helpers.getXpathfor5thYearOutstandingPrincipalPayment().find("sibling")
    # utils.yakshaAssert(utils.currentTest(), status, "Business")


@pytest.mark.parametrize("test_input", ["test_mouse_over_personal_finance", "test_get_tool_for_emi_calculator","test_get_home_loan_emi_calculator",
                                        "test_access_loan_amount","test_set_value_for_loan_amount"])
def test_suite(driver, test_input):
    # Your test code here
    print(f"Running {test_input}")


if __name__ == "__main__":
    pytest.main([__file__])
