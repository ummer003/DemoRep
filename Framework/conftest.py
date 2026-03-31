import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browserName",
        action="store",
        default="chrome",
        help="Browser Selection"
    )

@pytest.fixture(scope='function')
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browserName")
    if browser_name == "chrome":
        chromeOptions = Options()
        chromeOptions.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chromeOptions)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            if driver:
                screenshot = driver.get_screenshot_as_base64()
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screenshot
                extra.append(pytest_html.extras.html(html))
        report.extras = extra