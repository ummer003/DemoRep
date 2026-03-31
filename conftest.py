# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# def pytest_addoption(parser):
#     parser.addoption(
#         "--browserName", action="store", default="chrome", help="Browser Selection"
#     )

# @pytest.fixture(scope="function")
# def browserInstance(request):
#     browser_name = request.config.getoption("browserName")
    
#     if browser_name == "chrome":
#         chromeOptions = Options()
#         chromeOptions.add_experimental_option("detach", True)
#         driver = webdriver.Chrome(options=chromeOptions)
#     elif browser_name == "firefox":
#         driver = webdriver.Firefox()
    
#     driver.maximize_window()
#     driver.implicitly_wait(5)

#     yield driver

#     driver.quit()




