import random
import string
import time
from selenium.webdriver.support.select import Select
from ..Pages.BasePage import BasePage
from ..Pages.Locators import DashboardLocators, AddCustomerLocators


class Dashboard(BasePage):

    def checkTitle(self):
        title = self.driver.title
        assert title == "Dashboard / nopCommerce administration", 'Wrong title'

    def click_CustomerMenu(self):
        self.driver.find_element(*DashboardLocators.LINK_Customers_menu).click()

    def click_CustomerMenuItem(self):
        self.driver.find_element(*DashboardLocators.LINK_Customers_menu_item).click()

    def click_AddNew(self):
        self.driver.find_element(*AddCustomerLocators.BTN_Add).click()

    def click_Save(self):
        self.driver.find_element(*AddCustomerLocators.BTN_Save).click()

    def random_gen(self, len=6):
        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(len))

    def set_Email(self):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_Email)
        field.clear()
        field.send_keys(self.random_gen() + '@yandex.ru')

    def set_Password(self):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_Password)
        field.clear()
        field.send_keys(self.random_gen())

    def set_FirstName(self, FirstName):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_FName)
        field.clear()
        field.send_keys(FirstName)

    def set_LastName(self, LastName):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_LName)
        field.clear()
        field.send_keys(LastName)

    def set_Gender(self, gender):
        if gender == "male":
            self.driver.find_element(*AddCustomerLocators.OPTION_GenderMale).click()
        else:
            self.driver.find_element(*AddCustomerLocators.OPTION_GenderFeMale).click()

    def set_CompanyName(self, name):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_CompanyName)
        field.clear()
        field.send_keys(name)

    def set_Dob(self, date):
        DoB = self.driver.find_element(*AddCustomerLocators.FIELD_DOB)
        DoB.send_keys(date)

    def set_Role(self, role):
        self.driver.find_element(*AddCustomerLocators.SELECT_Delete).click()
        self.driver.find_element(*AddCustomerLocators.SELECT_Roles).click()
        time.sleep(2)
        if role == "Registered":
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Registered).click()
        elif role == "Administrator":
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Administrators).click()
            time.sleep(1)
            self.driver.find_element(*AddCustomerLocators.SELECT_Roles).click()
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Guests).click()
        elif role == "Vendors":
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Vendors).click()
            time.sleep(1)
            self.driver.find_element(*AddCustomerLocators.SELECT_Roles).click()
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Guests).click()
        elif role == "Forum Moderators":
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Moderator).click()
            time.sleep(1)
            self.driver.find_element(*AddCustomerLocators.SELECT_Roles).click()
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Guests).click()
        elif role == "Guests":
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Guests).click()

    def set_Manager(self, value):
        manager = Select(self.driver.find_element(*AddCustomerLocators.SELECT_Manager))
        manager.select_by_visible_text(value)

    def set_Comment(self, text):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_Comment)
        field.clear()
        field.send_keys(text)

    def check_status(self):
        block = self.is_element_present(*AddCustomerLocators.STATUS_Good)
        assert block == True, 'block does not appear'
