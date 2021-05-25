import time

import allure
import pytest

from ..Pages.Customers import Customers
from ..Pages.Dashboard import Dashboard
from ..Pages.LogIn import LogIn


@allure.feature('Tests Customer page')
@allure.feature('Tests Search')
@pytest.mark.regullar
def test_searchByEmail(driver):
    page = LogIn(driver)
    with allure.step("Открываем страницу"):
        page.open()
    with allure.step("Передаем Email администратора"):
        page.set_email(LogIn.email)
    with allure.step("Передаем Password администратора"):
        page.set_password(LogIn.password)
    with allure.step("Нажимаем на кнопку Login"):
        page.click_LogIn()
    with allure.step("создаем объект страницы Dashboard"):
        dash = Dashboard(driver)
    with allure.step("Нажимаем на Customers слева в списке меню"):
        dash.click_CustomerMenu()
    with allure.step("Нажимаем на Customers слева в выпадающем списке"):
        dash.click_CustomerMenuItem()
    with allure.step("создаем объект страницы Customer"):
        cust = Customers(driver)
    with allure.step("Передаем почту для поиска"):
        cust.set_email("brenda_lindgren@nopCommerce.com")
    with allure.step("Нажимаем кнопку Search"):
        cust.click_searchbtn()
    time.sleep(3)
    with allure.step("Проверяем результаты поиска"):
        cust.search_by_email_check_status("brenda_lindgren@nopCommerce.com")
