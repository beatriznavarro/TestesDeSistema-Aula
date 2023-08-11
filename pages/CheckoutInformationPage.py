from selenium.webdriver.common.by import By
from pages.PageObject import PageObject


class CheckoutInformationPage(PageObject):
    url = 'https://www.saucedemo.com/checkout-step-one.html'
    text_title = 'Checkout: Your Information'
    css_continue_btn = '[name="continue"]'
    text_first_name_required = 'Error: First Name is required'
    css_error_message = '[data-test="error"]'
    id_first_name = 'first-name'
    id_last_name = 'last-name'
    id_zip = 'postal-code'

    def __init__(self, driver):
        super(CheckoutInformationPage, self).__init__(driver=driver)

    def check_checkout_info_page(self):
        return self.check_page(self.url, self.text_title)

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_continue_btn).click()

    def has_first_name_required_error_message(self):
        error_text = self.driver.find_element(By.CSS_SELECTOR, self.css_error_message).text
        return error_text == self.text_first_name_required

    def fill_first_name(self, first_name, ):
        self.driver.find_element(By.ID,self.id_first_name).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(By.ID,self.id_last_name).send_keys(last_name)

    def fill_zip_code(self, zip_code):
        self.driver.find_element(By.ID,self.id_zip).send_keys(zip_code)


