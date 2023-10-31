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
from src.main.pyhton.com.iiht.evaluation.automation import *
from src.test.python.com.iiht.evaluation.automation.testutils import *

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--remote-allow-origins=*")
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.implicitly_wait(15)

def get_href_of_link(driver):
    if driver.get_attribute("outerHTML").startswith("<a"):
        return driver.get_attribute("href")
    else:
        return driver.get_attribute("outerHTML")

@pytest.mark.order(1)
def test_mouse_over_personal_finance(driver):
    try:
        element = Helpers.getElementforMouseOver(driver)
        href = get_href_of_link(element)
        status = href == MasterData.repo[0]
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)

@pytest.mark.order(2)
def test_get_tool_for_emi_calculator(driver):
    try:
        element = Helpers.get_element_for_tool(driver)
        href = get_href_of_link(element)
        status = href == MasterData.repo[1]
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
        TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)

@pytest.mark.order(3)
def test_get_home_loan_emi_calculator(driver):
    try:
        element = Helpers.get_element_for_home_loan(driver)
        href = get_href_of_link(element)
        status = href == MasterData.repo[2]
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Home Loan')]")))
        driver.execute_script("arguments[0].click();", element)
        TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)
                            
@pytest.mark.order(4)
def test_access_loan_amount(driver):
    try:
        element = Helpers.getElementforLoanAmount(driver)
        href = get_href_of_link(element)
        status = href == MasterData.repo[3]
        TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)

@pytest.mark.order(5)
def test_set_value_for_loan_amount(driver):
    try:
        status = SubActivities.enterValueLoanAmount(driver)
        TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)

@pytest.mark.order(6)
def test_access_loan_period(driver):
    try:
        element = Helpers.getElementforLoanPeriod(driver)
        href = get_href_of_link(element)
        status = href == MasterData.repo[4]
        TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)

@pytest.mark.order(7)
def test_set_value_for_loan_period(driver):
    try:
        status = SubActivities.enterValueLoanPeriod(driver)
        TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)
        
@pytest.mark.order(9)
def test_set_value_for_emi_start_from(driver):
    try:
        status = SubActivities.selectEMIStartsFrom(driver)
        TestUtils.yakshaAssert(
            TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(
            TestUtils.currentTest(), False, TestUtils.businessTestFile)

@pytest.mark.order(10)
def test_access_interest_rate(driver):
    try:
        element = Helpers.getElementforInterestRate(driver)
        href = get_href_of_link(element)
        status = href == MasterData.repo[6]
        TestUtils.yakshaAssert(
            TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(
            TestUtils.currentTest(), False, TestUtils.businessTestFile)

@pytest.mark.order(11)
def test_set_value_for_interest_rate(driver):
    try:
        status = SubActivities.enterInterestRate(driver)
        TestUtils.yakshaAssert(
            TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(
            TestUtils.currentTest(), False, TestUtils.businessTestFile)


@pytest.mark.order(12)
def test_access_upfront_charges():
    status = False
    try:
        element = Helpers.getElementforUpfrontcharges(driver)
        href = get_href_of_link(element)
        status = href == MasterData.repo[7]
        TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)

@pytest.mark.order(13)
def test_set_value_for_upfront_charges():
    status = False
    try:
        status = SubActivities.enterValueUpfrontCharges(driver)
        TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)

@pytest.mark.order(14)
def test_get_total_payment_element():
    status = False
    try:
        element = SubActivities.getTotalPaymentElement(driver)
        if element is not None:
            TestUtils.yakshaAssert(TestUtils.currentTest(), True, TestUtils.businessTestFile)
        else:
            TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)
    except Exception as ex:
        TestUtils.yakshaAssert(TestUtils.currentTest(), False, TestUtils.businessTestFile)

@pytest.mark.order(15)
def test_get_xpath_for_7th_year_emi_payment():
    status = Helpers.getXpathfor7thYearEMIPayment().contains("sibling")
    TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)

@pytest.mark.order(16)
def test_get_xpath_for_7th_year_interest_payment():
    status = Helpers.getXpathfor7thYearInterestPayment().contains("sibling")
    TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)

@pytest.mark.order(17)
def test_get_xpath_for_7th_year_principal_payment():
    status = Helpers.getXpathfor7thYearPrincipalPayment().contains("sibling")
    TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)

@pytest.mark.order(18)
def test_get_xpath_for_5th_year_outstanding_principal_payment():
    status = Helpers.getXpathfor5thYearOutstandingPrincipalPayment().contains("sibling")
    TestUtils.yakshaAssert(TestUtils.currentTest(), status, TestUtils.businessTestFile)





@classmethod
def setup_class(cls):
    cls.driver = webdriver.Chrome('chromedriver.exe')
    
@classmethod
def teardown_class(cls):
    cls.driver.quit()
