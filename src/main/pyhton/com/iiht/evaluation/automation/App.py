'''
Created on 29-Oct-2023

@author: pranjan
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.main.pyhton.com.iiht.evaluation.automation import Activities
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver_path = 'chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--remote-allow-origins=*")

driver = webdriver.Chrome(driver_path, options=chrome_options)
driver.implicitly_wait(15)

activities = Activities()

try:
    if activities.navigateToHomeLoanEMI(driver):
        if activities.calculateHomeLoanEMI(driver):
            print("Total Payment: ", activities.getTotalPayment(driver))
            print("EMI: ", activities.getEMI(driver))
            print("7th Year EMI Payment: ", activities.getTableDetails7thYearEMIPaymentInTheYear(driver))
            print("7th Year Interest Payment: ", activities.getTableDetails7thYearInterestPaymentInTheYear(driver))
            print("7th Year Principal Payment: ", activities.getTableDetails7thYearPrincipalPaymentInTheYear(driver))
            print("5th Year Outstanding Principal: ", activities.getTableDetails5thYearOutstandingPrincipalAtTheEndOfYear(driver))
except Exception as e:
    # Handle exception
    print(e)
finally:
    driver.quit()