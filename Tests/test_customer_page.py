import time

from ..Pages.Customers import Customers
from ..Pages.Dashboard import Dashboard
from ..Pages.LogIn import LogIn


def test_searchByEmail(driver):
    page = LogIn(driver)
    page.open()
    page.set_email(LogIn.email)
    page.set_password(LogIn.password)
    page.click_LogIn()
    dash = Dashboard(driver)
    dash.click_CustomerMenu()
    dash.click_CustomerMenuItem()
    cust = Customers(driver)
    cust.set_email("brenda_lindgren@nopCommerce.com")
    cust.click_searchbtn()
    time.sleep(3)
    cust.search_by_email_check_status("brenda_lindgren@nopCommerce.com")
