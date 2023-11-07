'''
Created on 29-Oct-2023

@author: pranjan
'''
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.main.pyhton.com.iiht.evaluation.automation import Helpers
from src.main.pyhton.com.iiht.evaluation.automation import SubActivities
from src.test.python.com.iiht.evaluation.automation.testutils.MasterData import MasterData
from src.test.python.com.iiht.evaluation.automation.testutils.TestUtils import TestUtils


@pytest.fixture(scope="module")
def driver():
    baseUrl = "https://www.moneycontrol.com/"; 
    options = Options()
    options.add_argument("--remote-allow-origins=*")
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
    prefs = {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    },
    'extentions': {},
    'download': {
        'prompt_for_download': False,
        'directory_upgrade': True,
        'default_directory': '/downloads'
    }
    }
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options)
    driver.implicitly_wait(15)
    driver.get(baseUrl);
    return driver


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
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


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
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


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
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(4)
def test_access_loan_amount(driver):
    utils = TestUtils()
    master_data = MasterData()
    try:
        element = Helpers.getElementforLoanAmount(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[3]
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(5)
def test_set_value_for_loan_amount(driver):
    utils = TestUtils()
    try:
        status = SubActivities.enterValueLoanAmount(driver)
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(6)
def test_access_loan_period(driver):
    utils = TestUtils()
    master_data = MasterData()
    try:
        element = Helpers.getElementforLoanPeriod(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[4]
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(7)
def test_set_value_for_loan_period(driver):
    utils = TestUtils()
    try:
        status = SubActivities.enterValueLoanPeriod(driver)
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(9)
def test_set_value_for_emi_start_from(driver):
    utils = TestUtils()
    try:
        status = SubActivities.selectEMIStartsFrom(driver)
        utils.yakshaAssert(
            utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(10)
def test_access_interest_rate(driver):
    utils = TestUtils()
    master_data = MasterData()
    try:
        element = Helpers.getElementforInterestRate(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[6]
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(11)
def test_set_value_for_interest_rate(driver):
    utils = TestUtils()
    try:
        status = SubActivities.enterInterestRate(driver)
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(12)
def test_access_upfront_charges():
    utils = TestUtils()
    master_data = MasterData()
    status = False
    try:
        element = Helpers.getElementforUpfrontcharges(driver)
        href = get_href_of_link(element)
        status = href == master_data.repo[7]
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(13)
def test_set_value_for_upfront_charges():
    utils = TestUtils()
    status = False
    try:
        status = SubActivities.enterValueUpfrontCharges(driver)
        utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(14)
def test_get_total_payment_element():
    utils = TestUtils()
    try:
        element = SubActivities.getTotalPaymentElement(driver)
        if element is not None:
            utils.yakshaAssert(utils.currentTest(), True, utils.businessTestFile)
        else:
            utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)
    except Exception as ex:
        print(ex)
        utils.yakshaAssert(utils.currentTest(), False, utils.businessTestFile)


@pytest.mark.order(15)
def test_get_xpath_for_7th_year_emi_payment():
    utils = TestUtils()
    status = Helpers.getXpathfor7thYearEMIPayment().contains("sibling")
    utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)


@pytest.mark.order(16)
def test_get_xpath_for_7th_year_interest_payment():
    utils = TestUtils()
    status = Helpers.getXpathfor7thYearInterestPayment().contains("sibling")
    utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)


@pytest.mark.order(17)
def test_get_xpath_for_7th_year_principal_payment():
    utils = TestUtils()
    status = Helpers.getXpathfor7thYearPrincipalPayment().contains("sibling")
    utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)


@pytest.mark.order(18)
def test_get_xpath_for_5th_year_outstanding_principal_payment():
    utils = TestUtils()
    status = Helpers.getXpathfor5thYearOutstandingPrincipalPayment().contains("sibling")
    utils.yakshaAssert(utils.currentTest(), status, utils.businessTestFile)


@classmethod
def setup_class(cls):
    cls.driver = webdriver.Chrome('chromedriver.exe')


@classmethod
def teardown_class(cls):
    cls.driver.quit()

    
if __name__ == "__main__":
    pytest.main([__file__])
