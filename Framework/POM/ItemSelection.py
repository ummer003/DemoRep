from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from Framework.Utils.BrowserUtils import BrowserUtils

class ItemSelection(BrowserUtils):
    def __init__(self, driver, reqItem):
        super().__init__(driver)
        self.driver = driver
        self.reqItem = reqItem
        self.addItemLoc = (By.XPATH, f"//a[text()='{self.reqItem}']//parent::h4//parent::div//parent::div/div[@class='card-footer']/button")
        self.checkoutButtonLoc = (By.PARTIAL_LINK_TEXT, "Checkout")
        
    def selectingItem(self):
        self.driver.find_element(*self.addItemLoc).click()

    def goToCart(self):
        actions = ActionChains(self.driver)
        checkout = self.driver.find_element(*self.checkoutButtonLoc)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkout)
        actions.move_to_element(checkout).click().perform()

