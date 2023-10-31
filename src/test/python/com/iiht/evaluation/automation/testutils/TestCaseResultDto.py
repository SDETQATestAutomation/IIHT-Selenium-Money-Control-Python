'''
Created on 29-Oct-2023

@author: pranjan
'''


class TestCaseResultDto:
    def __init__(self, methodName, methodType, actualScore, earnedScore, status, isMandatory, erroMessage):
        self.methodName = methodName
        self.methodType = methodType
        self.actualScore = actualScore
        self.earnedScore = earnedScore
        self.status = status
        self.isMandatory = isMandatory
        self.erroMessage = erroMessage

    def getMethodName(self):
        return self.methodName

    def setMethodName(self, methodName):
        self.methodName = methodName

    def getMethodType(self):
        return self.methodType

    def setMethodType(self, methodType):
        self.methodType = methodType

    def getActualScore(self):
        return self.actualScore

    def setActualScore(self, actualScore):
        self.actualScore = actualScore

    def getEarnedScore(self):
        return self.earnedScore

    def setEarnedScore(self, earnedScore):
        self.earnedScore = earnedScore

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getIsMandatory(self):
        return self.isMandatory

    def setIsMandatory(self, isMandatory):
        self.isMandatory = isMandatory

    def getErrorMessage(self):
        return self.errorMessage

    def setErrorMessage(self, errorMessage):
        self.errorMessage = errorMessage