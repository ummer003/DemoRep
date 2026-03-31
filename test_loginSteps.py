# from selenium.webdriver.common.by import By
# class Login:
#     def __init__(self, driver):
#         self.driver = driver
#         self.userEmailLoc = (By.ID, "emailAndUserId")
#         self.nextBtnLoc = (By.CLASS_NAME, "ant-btn")
#         self.userIDLoc = (By.ID, "user_id")
#         self.userPasswordLoc = (By.ID, "password")
#         self.loginBtnLoc = (By.XPATH, "//span[text()='LOGIN']")

#     def login(self, userEmail, userID, password):
#         self.userEmail = userEmail
#         self.userID = userID
#         self.password = password
#         self.driver.find_element(*self.userEmailLoc).send_keys(self.userEmail)
#         self.driver.find_element(*self.nextBtnLoc).click()
#         self.driver.find_element(*self.userIDLoc).send_keys(self.userID)
#         self.driver.find_element(*self.userPasswordLoc).send_keys(self.password)
#         self.driver.find_element(*self.loginBtnLoc).click()

from selenium.webdriver.common.by import By        

class Login:

    def __init__(self, driver):
        self.driver = driver
        self.userEmailLoc = (By.ID, "emailAndUserId")
        self.nextBtnLoc = (By.CLASS_NAME, "ant-btn")
        self.userIDLoc = (By.ID, "user_id")
        self.userPasswordLoc = (By.ID, "password")
        self.loginBtnLoc = (By.XPATH, "//span[text()='LOGIN']")

    def login(self, userEmail, userID, password):
        self.userEmail = userEmail
        self.userID = userID
        self.password = password

        self.driver.find_element(*self.userEmailLoc).send_keys(self.userEmail)
        self.driver.find_element(*self.nextBtnLoc).click()
        self.driver.find_element(*self.userIDLoc).send_keys(self.userID)
        self.driver.find_element(*self.userPasswordLoc).send_keys(self.password)
        self.driver.find_element(*self.loginBtnLoc).click()