'''
Created on 29-Oct-2023

@author: pranjan
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import StaleElementReferenceException
# from datetime import datetime

def mouseOverPersonalFinance(driver: webdriver, baseUrl: str) -> bool:
    return False

def clickTools(driver: webdriver, actions: ActionChains) -> bool:
    return False

def clickOnHomeLoanEMICalculator(driver: webdriver) -> bool:
    return False

def enterValueLoanAmount(driver: webdriver) -> bool:
    return False

def enterValueLoanPeriod(driver: webdriver) -> bool:
    return False

def selectEMIStartsFrom(driver: webdriver) -> bool:
    return False

def enterInterestRate(driver: webdriver) -> bool:
    return False

def enterValueUpfrontCharges(driver: webdriver) -> bool:
    return False

def getTotalPaymentElement(driver: webdriver) -> WebElement:
    return None

def clickSubmit(driver: webdriver) -> bool:
    return False