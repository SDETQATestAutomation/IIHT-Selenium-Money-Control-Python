'''
Created on 29-Oct-2023

@author: pranjan
'''

class MasterData:
    repo = []
    repo.append("https://www.moneycontrol.com/personal-finance/")  # Mouse over Personal Finance (0)
    repo.append("https://www.moneycontrol.com/personal-finance/tools/")  # Click Tools (1)
    repo.append("https://www.moneycontrol.com/personal-finance/tools/emi-calculator.html")  # Home Loan Calculator (2)
    repo.append("<input class=\"sipslidervalue\" id=\"carhome_loan\" maxlength=\"20000\" value=\"10000\" oninput=\"javascript: if (this.value > 5000000) this.value = '5000000';this.value.replace(/[^\\d]/g,'');\" type=\"number\">")  # Loan Amount (3)
    repo.append("<input id=\"loan_period\" class=\"sipslidervalue month_input\" oninput=\"javascript: if (this.value > 35) this.value = '20';\" type=\"number\">")  # Loan Period (4)
    repo.append("<select class=\"custselect\" id=\"emi_start_from\">" +
                "  <option value=\"0\">At the time of loan disbursement</option>" +
                "  <option value=\"1\">From next month after disbursement</option>" +
                "</select>")  # EMI Start (5)
    repo.append("<input id=\"interest_rate\" class=\"sipslidervalue\" oninput=\"javascript: (this.value > 99.99 ) ? this.value = '' :this.value=this.value.slice(0,5);\" type=\"number\">")  # Interest Rate (6)
    repo.append("<input id=\"upfront_charges\" class=\"sipslidervalue\" oninput=\"javascript: if (this.value > 1000000) this.value = '10000';\" type=\"number\">")  # Upfront charges (7)
