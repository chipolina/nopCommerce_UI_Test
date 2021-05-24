import random
import string
import time

import allure
from selenium.webdriver.support.select import Select
from ..Pages.BasePage import BasePage
from ..Pages.Locators import DashboardLocators, AddCustomerLocators


class Dashboard(BasePage):

    def checkTitle(self):
        act_title = self.driver.title
        title = "Dashboard / nopCommerce administration"
        with allure.step("Проверяем совпадает ли title с {}".format(title)):
            if act_title != title:
                self.screen()
        assert title == title, 'Wrong title'

    def click_CustomerMenu(self):
        self.driver.find_element(*DashboardLocators.LINK_Customers_menu).click()

    def click_CustomerMenuItem(self):
        self.driver.find_element(*DashboardLocators.LINK_Customers_menu_item).click()

    def click_AddNew(self):
        self.driver.find_element(*AddCustomerLocators.BTN_Add).click()

    def click_Save(self):
        self.driver.find_element(*AddCustomerLocators.BTN_Save).click()

    # Генерация случайного Email и Password длинной 6 символов из прописных и строчных букв и цифр.
    def random_gen(self, len=6):
        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(len))

    # Передаем сгенерированный Email из функции random_gen и конкатенируем с доменом yandex.ru
    def set_Email(self):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_Email)
        field.clear()
        field.send_keys(self.random_gen() + '@yandex.ru')

    # Передаем сгенерированный Password из функции random_gen
    def set_Password(self):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_Password)
        field.clear()
        field.send_keys(self.random_gen())

    # Передаем значение Имени
    def set_FirstName(self, FirstName):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_FName)
        field.clear()
        field.send_keys(FirstName)

    # Передаем значение Фамилии
    def set_LastName(self, LastName):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_LName)
        field.clear()
        field.send_keys(LastName)

    # Указываем пол. Если указан пол отличный от male, то выбирается значение Female
    def set_Gender(self, gender):
        if gender == "male":
            self.driver.find_element(*AddCustomerLocators.OPTION_GenderMale).click()
        else:
            self.driver.find_element(*AddCustomerLocators.OPTION_GenderFeMale).click()

    # Передаем имя компании
    def set_CompanyName(self, name):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_CompanyName)
        field.clear()
        field.send_keys(name)

    # Передаем дату рождения
    def set_Dob(self, date):
        DoB = self.driver.find_element(*AddCustomerLocators.FIELD_DOB)
        DoB.send_keys(date)

    # Выбираем роль пользователя
    def set_Role(self, role):
        with allure.step("Удаляем выбранную роль по умолчанию"):
            self.driver.find_element(*AddCustomerLocators.SELECT_Delete).click()
        with allure.step("Нажимаем на поле с Ролями"):
            self.driver.find_element(*AddCustomerLocators.SELECT_Roles).click()
        time.sleep(2)
        # Поле роль может быть либо Registered, либо Guests, либо Administrator or Vendors or Forum Moderators в
        # комбинации с Registered или Guests Здесь описана логика для выбора любого из ролей вместе с Guests
        if role == "Registered":
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Registered).click()
        elif role == "Administrator":
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Administrators).click()
            # Ждем 1 секунду чтобы второй раз нажать на поле
            time.sleep(1)
            self.driver.find_element(*AddCustomerLocators.SELECT_Roles).click()
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Guests).click()
        elif role == "Vendors":
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Vendors).click()
            # Ждем 1 секунду чтобы второй раз нажать на поле
            time.sleep(1)
            self.driver.find_element(*AddCustomerLocators.SELECT_Roles).click()
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Guests).click()
        elif role == "Forum Moderators":
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Moderator).click()
            # Ждем 1 секунду чтобы второй раз нажать на поле
            time.sleep(1)
            self.driver.find_element(*AddCustomerLocators.SELECT_Roles).click()
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Guests).click()
        elif role == "Guests":
            self.driver.find_element(*AddCustomerLocators.SELECT_Role_Guests).click()

    # Выбор значения по видимому тексту из элемента Select
    def set_Manager(self, value):
        manager = Select(self.driver.find_element(*AddCustomerLocators.SELECT_Manager))
        manager.select_by_visible_text(value)

    # Передаем текст комментария
    def set_Comment(self, text):
        field = self.driver.find_element(*AddCustomerLocators.FIELD_Comment)
        field.clear()
        field.send_keys(text)

    # Проверяем появился ли блок с текстом об успешной регистрации
    def check_status(self):
        block = self.is_element_present(*AddCustomerLocators.STATUS_Good)
        if block != True:
            self.screen()
        assert block == True, 'block does not appear'
