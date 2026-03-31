import json
import pytest
from POM.Purchase import Purchase
from POM.Cart import Cart
from POM.ItemSelection import ItemSelection
from POM.Login import LoginPage

testDataPath = "Data/test_e2e.json"

with open(testDataPath) as d:
    loadData = json.load(d)
    dataList = loadData['data']

@pytest.mark.e2e
@pytest.mark.parametrize("testData", dataList)
def test_e2e(browserInstance, testData):
    driver = browserInstance
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(testData["url"])

    loginPage = LoginPage(driver)
    loginPage.login(testData["username"], testData["password"])
    print(f"Login page tile: {loginPage.getTitle()}")

    addToCart = ItemSelection(driver, testData["itemName"])
    addToCart.selectingItem()
    addToCart.goToCart()
    print(f"Item Selection page tile: {addToCart.getTitle()}")

    cartCheck = Cart(driver)
    cartCheck.cart(testData["itemName"])
    print(f"Cart page title: {cartCheck.getTitle()}")

    finalPurchase = Purchase(driver)
    finalPurchase.purchase(testData["countryName"])
    print(f"Final page title: {finalPurchase.getTitle()}")
