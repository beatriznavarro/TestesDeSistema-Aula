from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutCompletePage(PageObject):
    url = 'https://www.saucedemo.com/checkout-complete.html'
    text_title = 'Checkout: Complete!'
    msg_success_text = 'Thank you for your order!'
    class_msg_success = 'complete-header'



    def __init__(self, driver):
        super(CheckoutCompletePage, self).__init__(driver=driver)


    def check_checkout_complete_page(self):
        return self.check_page(self.url, self.text_title)

    def has_msg_success(self):
        msg_success = self.driver.find_element(By.CLASS_NAME, self.class_msg_success).text
        return msg_success == self.msg_success_text
