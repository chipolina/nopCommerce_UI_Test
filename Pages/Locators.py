from selenium.webdriver.common.by import By


# Список элементов на страницах
class LoginPageLocators:
    FIELD_Email = (By.ID, 'Email')
    FIELD_Password = (By.ID, 'Password')
    BTN_LogIn = (By.XPATH, "//button[@type='submit']")
    CHECK_Remember = (By.XPATH, "//label[@for='RememberMe']")
    CHECK_Remember_Check = (By.ID, "RememberMe")
    BLOCK_Error = (By.XPATH, "//div[contains(@class, 'message-error validation-summary-errors')]")


class DashboardLocators:
    BTN_LogOut = (By.XPATH, "//a[normalize-space()='Logout']")
    LINK_Customers_menu = (By.XPATH, "//a[@href='#']//p[contains(text(), 'Customers')]")
    LINK_Customers_menu_item = (
        By.XPATH, "//a[@class='nav-link'][@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")


class CustomerLocators:
    FIELD_Email = (By.XPATH, "//*[@id='SearchEmail']")
    BTN_Search = (By.XPATH, "//*[@id='search-customers']")
    TBL_Rows = (By.XPATH, "//*[@id='customers-grid']//tbody/tr")
    TBL_Collumns = (By.XPATH, "//*[@id='customers-grid']//tbody/tr/td")


class AddCustomerLocators:
    BTN_Add = (By.XPATH, "//a[@href='/Admin/Customer/Create']")
    BTN_Save = (By.XPATH, "//button[@name='save']")
    FIELD_Email = (By.ID, "Email")
    FIELD_Password = (By.ID, "Password")
    FIELD_FName = (By.ID, "FirstName")
    FIELD_LName = (By.ID, "LastName")
    OPTION_GenderMale = (By.XPATH, "//label[contains(@for, 'Gender_Male')]")
    OPTION_GenderFeMale = (By.XPATH, "//label[contains(@for, 'Gender_FeMale')]")
    FIELD_DOB = (By.XPATH, "//input[@role='combobox']")
    SELECT_DOB = (By.XPATH, "//span[contains(@class,'k-select') and @role='button']")
    FIELD_CompanyName = (By.ID, "Company")
    CHECK_Tax = (By.ID, "IsTaxExempt")
    SELECT_Roles = (By.XPATH, "//div[contains(@class, 'input-group-append input-group-required')]")
    SELECT_Role_Registered = (By.XPATH, "//*[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(), 'Registered')]")
    SELECT_Role_Moderator = (
        By.XPATH, "//*[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(), 'Forum Moderators')]")
    SELECT_Role_Administrators = (
        By.XPATH, "//*[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(), 'Administrators')]")
    SELECT_Role_Guests = (By.XPATH, "//li[normalize-space()='Guests']")
    SELECT_Role_Vendors = (By.XPATH, "//*[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(), 'Vendors')]")
    SELECT_Delete = (By.XPATH, "//span[@title='delete']")
    SELECT_Manager = (By.ID, "VendorId")
    CHECK_Active = (By.ID, "Active")
    FIELD_Comment = (By.ID, "AdminComment")
    STATUS_Good = (By.XPATH, "//div[contains(@class,'alert alert-success alert-dismissable')]")
