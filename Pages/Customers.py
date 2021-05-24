from ..Pages.Locators import CustomerLocators
from ..Pages.BasePage import BasePage


class Customers(BasePage):

    def set_email(self, email):
        field = self.driver.find_element(*CustomerLocators.FIELD_Email)
        field.clear()
        field.send_keys(email)

    def click_searchbtn(self):
        self.driver.find_element(*CustomerLocators.BTN_Search).click()

    def rowsNum(self):
        return len(self.driver.find_elements(*CustomerLocators.TBL_Rows))

    def columnNum(self):
        return len(self.driver.find_elements(*CustomerLocators.TBL_Collumns))

    def search_by_email_check_status(self, email):
        flag = False
        for i in range(1, self.rowsNum() + 1):
            emailID = self.driver.find_element_by_xpath("//*[@id='customers-grid']//tbody/tr[" + str(i) + "]/td[2]").text
            if emailID == email:
                flag = True
                break
        assert flag == True, "No customer"
        return flag

