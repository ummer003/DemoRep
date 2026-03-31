import json
import time
import pytest
from test_loginSteps import Login

# # testDataPath = "D:\Program\Python\SampleTestFilePractice\test_login.json"
# with open("test_login.json") as d:
#     testData = json.load(d)
#     testDataList = testData["data"]

# @pytest.mark.parametrize("testDataItems", testDataList)
# def test_login(browserInstance, testDataItems):
#     driver = browserInstance
#     driver.get(testDataItems['url'])
#     loginTest = Login(driver)
#     loginTest.login(testDataItems["userEmail"], testDataItems["userID"], testDataItems["userPassword"])
#     time.sleep(3)


with open("test_login.json") as d:
    testData = json.load(d)
    testDataList = testData["data"]

@pytest.mark.parametrize("testDataItems", testDataList)
def test_login(browserInstance, testDataItems):
    driver = browserInstance
    driver.get(testDataItems["url"])
    loginTest = Login(driver)
    loginTest.login(testDataItems["userEmail"], testDataItems["userID"], testDataItems["userPassword"])    
    time.sleep(3)