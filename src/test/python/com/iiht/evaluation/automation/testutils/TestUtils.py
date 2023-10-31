'''
Created on 29-Oct-2023

@author: pranjan
'''
import requests
import json
import inspect

class TestUtils:
    TEXT_RESET = "\033[0m"
    RED_BOLD_BRIGHT = "\033[1;91m" # RED
    GREEN_BOLD_BRIGHT = "\033[1;92m" # GREEN
    YELLOW_BOLD_BRIGHT = "\033[1;93m" # YELLOW
    BLUE_BOLD_BRIGHT = "\033[1;94m" # BLUE

    testResult = ""

    total = 0
    passed = 0
    failed = 0

    businessTestFile = None
    boundaryTestFile = None
    exceptionTestFile = None
    xmlFile = None
    
    GUID = "6ed39465-d6d3-4ec4-b27d-1dcb870b2992"
    customData = ""
    URL = "https://yaksha-prod-sbfn.azurewebsites.net/api/YakshaMFAEnqueue?code=jSTWTxtQ8kZgQ5FC0oLgoSgZG7UoU9Asnmxgp6hLLvYId/GW9ccoLw=="

    def __init__(self):
        self.total = 0
        self.passed = 0
        self.failed = 0

        self.testResult = ""

        self.businessTestFile = open("./output_revised.txt", "w")
        self.businessTestFile.close()

        self.boundaryTestFile = open("./output_boundary_revised.txt", "w")
        self.boundaryTestFile.close()

        self.exceptionTestFile = open("./output_exception_revised.txt", "w")
        self.exceptionTestFile.close()

    @staticmethod
    def readData(filePath):
        with open(filePath, "r") as file:
            return file.read()

    def yakshaAssert(self, testName, result, file):
        testCaseResults = {}

        self.customData = self.readData("../custom.ih")
        resultStatus = "Failed"
        resultScore = 0
        if result == True:
            resultScore = 1
            resultStatus = "Passed"

        try:
            testType = "functional"

            if "boundary" in file.name:
                testType = "boundary"

            if "exception" in file.name:
                testType = "exception"
                testCaseResults[self.GUID] = {
                "testCaseId": testName,
                "testType": testType,
                "maxMarks": 1,
                "score": resultScore,
                "resultStatus": resultStatus,
                "executionStatus": True,
                "remarks": ""
            }

        except Exception as e:
            print(e)

        testResults = {
            "testCaseResults": testCaseResults,
            "customData": self.customData
        }

        try:
            response = requests.post(self.URL, json=testResults)
            print(response.text)
        except Exception as e:
            print(e)

        self.total += 1
        r = testName.split("(?=[A-Z])")[1:]
        print("\n" + self.BLUE_BOLD_BRIGHT + "=>", end="")
        print(self.BLUE_BOLD_BRIGHT + "Test For:", end="")
        for word in r:
            print(self.BLUE_BOLD_BRIGHT + word, end=" ")
        print(":", end=" ")
        if result == True:
            print(self.GREEN_BOLD_BRIGHT + "PASSED" + self.TEXT_RESET)
            self.passed += 1
        else:
            print(self.RED_BOLD_BRIGHT + "FAILED" + self.TEXT_RESET)
            self.failed += 1

    def testReport(self):
        print("\n" + self.BLUE_BOLD_BRIGHT + "TEST CASES EVALUATED : " + str(self.total) + self.TEXT_RESET)
        print(self.GREEN_BOLD_BRIGHT + "PASSED : " + str(self.passed) + self.TEXT_RESET)
        print(self.RED_BOLD_BRIGHT + "FAILED : " + str(self.failed) + self.TEXT_RESET)

    @staticmethod
    def currentTest():
        return inspect.stack()[1][3]

    def asJsonString(self, obj):
        return json.dumps(obj)

                
                