import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
from ..Utility.CurrentTime import curr_time
from ..Utility.ReadProp import ReadConfig


class BasePage:
    link = ReadConfig.getUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    password_error = ReadConfig.getPassword_error()

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.link)
        self.driver.maximize_window()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def screen(self):
        allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot_' + str(curr_time()),
                      attachment_type=AttachmentType.PNG)
