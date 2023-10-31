'''
Created on 29-Oct-2023

@author: pranjan
'''
class TestResults:
    def __init__(self):
        self.testCaseResults = ""
        self.customData = ""

    def getTestCaseResults(self):
        return self.testCaseResults

    def setTestCaseResults(self, testCaseResults):
        self.testCaseResults = testCaseResults

    def getCustomData(self):
        return self.customData

    def setCustomData(self, customData):
        self.customData = customData