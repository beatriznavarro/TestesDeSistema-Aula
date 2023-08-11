from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutOverviewPage(PageObject):
    url = 'https://www.saucedemo.com/checkout-step-two.html'
    btn_finish = 'finish'
    text_title = 'Checkout: Overview'
    class_prod_name = 'inventory_item_name'

    def __init__(self, driver):
        super(CheckoutOverviewPage, self).__init__(driver=driver)


    def click_finish(self):
        self.driver.find_element(By.ID, self.btn_finish).click()


    def check_checkout_overview_page(self):
        return self.check_page(self.url, self.text_title)


    def check_data(self, prod_name):
        return self.driver.find_element(By.CLASS_NAME, self.class_prod_name).text == prod_name


