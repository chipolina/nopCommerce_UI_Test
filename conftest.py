import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Функция для 3 разных драйверов под Chrome, Firefox, Opera. При запуске тесто необходимо указывать имя драйвера
# --browser = chrome|firefox|opera
@pytest.fixture()
def driver(request):
    browser = request.config.getoption("browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
    elif browser == 'opera':
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        driver.maximize_window()
    else:
        raise pytest.UsageError("--browser should be chrome, firefox or opera")
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=None, help="Choose browser chrome, firefox or opera")
