import allure

from ..Pages.LogIn import LogIn


@allure.feature('Tests Login Page')
@allure.story('Check Title')
def test_LogInPage_title(driver):
    page = LogIn(driver)
    with allure.step("Открываем страницу"):
        page.open()
    with allure.step("Првоеряем Title"):
        page.check_title()


@allure.feature('Tests Login Page')
@allure.story('Check Dashboard title')
def test_GoToDashboard(driver):
    page = LogIn(driver)
    with allure.step("Открываем страницу"):
        page.open()
    with allure.step("Передаем Email"):
        page.set_email(LogIn.email)
    with allure.step("Передаем корректный Password"):
        page.set_password(LogIn.password)
    with allure.step("Нажимаем на кнопку Login"):
        page.click_LogIn()


@allure.feature('Tests Login Page')
@allure.story('Check error block appearence')
def test_GoToDashboard_Error(driver):
    page = LogIn(driver)
    with allure.step("Открываем страницу"):
        page.open()
    with allure.step("Передаем Email"):
        page.set_email(LogIn.email)
    with allure.step("Передаем Password"):
        page.set_password(LogIn.password_error)
    with allure.step("Нажимаем на кнопку Login. Проверяем появился ли блок с предупреждением"):
        page.click_LogIn_Error()
