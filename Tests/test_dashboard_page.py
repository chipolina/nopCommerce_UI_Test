import allure
from ..Pages.Dashboard import Dashboard
from ..Pages.LogIn import LogIn


def test_GoToDashboard(driver):
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
    with allure.step("Нажимаем на кнопку Add New"):
        dash.click_AddNew()
    with allure.step("Передаем сгенерированную почту"):
        dash.set_Email()
    with allure.step("Передаем сгенерированный пароль"):
        dash.set_Password()
    with allure.step("Передаем Имя"):
        dash.set_FirstName('Denis')
    with allure.step("Передаем Фамилию"):
        dash.set_LastName('Sudakov')
    with allure.step("Передаем пол"):
        dash.set_Gender('male')
    with allure.step("Передаем дату рождения"):
        dash.set_Dob('09/03/1988')
    with allure.step("Передаем имя компании"):
        dash.set_CompanyName('My company')
    with allure.step("Передаем роль"):
        dash.set_Role("Vendors")
    with allure.step("Передаем комментарий"):
        dash.set_Comment('Test comment')
    with allure.step("Нажимаем Save"):
        dash.click_Save()
    with allure.step("Проверяем успешно ли создался ползователь"):
        dash.check_status()
