from ..Pages.BasePage import BasePage
from ..Pages.Locators import LoginPageLocators


class LogIn(BasePage):

    def check_title(self):
        title = self.driver.title
        assert title == "Your store. Login", 'Wrong title'

    def set_email(self, username):
        email = self.driver.find_element(*LoginPageLocators.FIELD_Email)
        email.clear()
        email.send_keys(username)

    def set_password(self, userpassword):
        password = self.driver.find_element(*LoginPageLocators.FIELD_Password)
        password.clear()
        password.send_keys(userpassword)

    def click_LogIn(self):
        btn = self.driver.find_element(*LoginPageLocators.BTN_LogIn)
        btn.click()
        act_title = self.driver.title
        assert act_title == "Dashboard / nopCommerce administration", 'Wrong title'

    def click_LogIn_Error(self):
        self.driver.find_element(*LoginPageLocators.BTN_LogIn).click()
        error = self.is_element_present(*LoginPageLocators.BLOCK_Error)
        assert error == True, "Block doesn't appears"
