from ..Pages.LogIn import LogIn

def test_LogInPage_title(driver):
    page = LogIn(driver)
    page.open()
    page.check_title()


def test_GoToDashboard(driver):
    page = LogIn(driver)
    page.open()
    page.set_email(LogIn.email)
    page.set_password(LogIn.password)
    page.click_LogIn()


def test_GoToDashboard_Error(driver):
    page = LogIn(driver)
    page.open()
    page.set_email(LogIn.email)
    page.set_password(LogIn.password_error)
    page.click_LogIn_Error()
