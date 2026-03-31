from selenium.webdriver.common.by import By

from Framework.Utils.BrowserUtils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.usernameLoc = (By.ID, "username")
        self.passwordLoc = (By.ID, "password")
        self.signInButtonLoc = (By.ID, "signInBtn")

    def login(self, username, password):
        self.username = username
        self.password = password
        self.driver.find_element(*self.usernameLoc).send_keys(self.username)
        self.driver.find_element(*self.passwordLoc).send_keys(self.password)
        self.driver.find_element(*self.signInButtonLoc).click()
    