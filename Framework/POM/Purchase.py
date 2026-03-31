from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Framework.Utils.BrowserUtils import BrowserUtils

class Purchase(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.countryLoc = (By.ID, "country")
        self.inputCountryLoc = (By.CSS_SELECTOR, ".suggestions")
        self.countryListLoc = (By.CSS_SELECTOR, ".suggestions li")
        self.tcCheckboxLoc = (By.CSS_SELECTOR, "div[class*='checkbox']")
        self.purchaseButtonLoc = (By.CSS_SELECTOR, "input[value='Purchase']")
        self.successMessageLoc = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def purchase(self, reqCountry):
        self.reqCountry = reqCountry
        self.driver.find_element(*self.countryLoc).send_keys(self.reqCountry)
        WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(self.inputCountryLoc))

        countries = self.driver.find_elements(*self.countryListLoc)

        for country in countries:
            if country.text == self.reqCountry:
                # self.driver.find_element(By.XPATH, f"//li/a[text()='{country.text}']").click()
                country.click()
                break

        self.driver.find_element(*self.tcCheckboxLoc).click()
        self.driver.find_element(*self.purchaseButtonLoc).click()

        successMessage = self.driver.find_element(*self.successMessageLoc).text
        print(successMessage)
        assert "Success" in successMessage

        