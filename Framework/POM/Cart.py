from selenium.webdriver.common.by import By

from Framework.Utils.BrowserUtils import BrowserUtils

class Cart(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ItemNameLoc = (By.XPATH, "//h4[@class='media-heading']/a")
        self.checkoutBtnLoc = (By.XPATH, "//button[@class='btn btn-success']")

    def cart(self, reqItem):
        self.reqItem = reqItem
        itemNameinCheckout = self.driver.find_element(*self.ItemNameLoc).text
        if self.reqItem == itemNameinCheckout:
            self.driver.find_element(*self.checkoutBtnLoc).click()
        