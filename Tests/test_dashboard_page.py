import time

from ..Pages.Dashboard import Dashboard
from ..Pages.LogIn import LogIn


def test_GoToDashboard(driver):
    page = LogIn(driver)
    page.open()
    page.set_email(LogIn.email)
    page.set_password(LogIn.password)
    page.click_LogIn()
    dash = Dashboard(driver)
    dash.click_CustomerMenu()
    dash.click_CustomerMenuItem()
    dash.click_AddNew()
    dash.set_Email()
    dash.set_Password()
    dash.set_FirstName('Denis')
    dash.set_LastName('Sudakov')
    dash.set_Gender('male')
    dash.set_Dob('09/03/1988')
    dash.set_CompanyName('My company')
    dash.set_Role("Vendors")
    dash.set_Comment('Test comment')
    dash.click_Save()
    dash.check_status()
    time.sleep(20)


