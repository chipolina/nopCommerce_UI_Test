import allure
from ..Pages.BasePage import BasePage
from ..Pages.Locators import LoginPageLocators


class LogIn(BasePage):

    def check_title(self):
        with allure.step('Записываем title страницы в переменную'):
            title = "Your store. Login"
            act_title = self.driver.title
        with allure.step('Проверяем совпадает ли title c {}'.format(title)):
            if act_title != title:
                self.screen()
        assert act_title == title, "Wrong title"

    def set_email(self, username):
        email = self.driver.find_element(*LoginPageLocators.FIELD_Email)
        email.clear()
        email.send_keys(username)

    def set_password(self, userpassword):
        password = self.driver.find_element(*LoginPageLocators.FIELD_Password)
        password.clear()
        password.send_keys(userpassword)

    def click_LogIn(self):
        self.driver.find_element(*LoginPageLocators.BTN_LogIn).click()
        title = "Dashboard / nopCommerce administration"
        act_title = self.driver.title
        with allure.step('Проверяем совпадает ли title c {}'.format(title)):
            if act_title != title:
                self.screen()
        assert act_title == title, 'Wrong title'

    def click_LogIn_Error(self):
        self.driver.find_element(*LoginPageLocators.BTN_LogIn).click()
        error = self.is_element_present(*LoginPageLocators.BLOCK_Error)
        assert error == True, "Block doesn't appears"
