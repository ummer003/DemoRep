import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

reqItem = "Samsung Note 8"

#Click on shop button
driver.find_element(By.LINK_TEXT, "Shop").click()


driver.find_element(By.XPATH, f"//a[text()='{reqItem}']//parent::h4//parent::div//parent::div/div[@class='card-footer']/button").click()



#finding item name elements

#moving to checkout element
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout")).click().perform()

#verifying item name in checkout
itemNameinCheckout = driver.find_element(By.XPATH, "//h4[@class='media-heading']/a").text

#checking out only if item name matches
if reqItem == itemNameinCheckout:
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

#Entering country
driver.find_element(By.ID, "country").send_keys("Ger")
WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".suggestions")))

#iterating through suggestions to select required option
countries = driver.find_elements(By.CSS_SELECTOR, ".suggestions li")

for country in countries:
    if country.text == "Germany":
        driver.find_element(By.XPATH, f"//li/a[text()='{country.text}']").click()
        break


driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox']").click()

#clicking on purchase
driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()

successMessage = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text

print(successMessage)
assert "Success" in successMessage
# time.sleep(5)
driver.quit()

