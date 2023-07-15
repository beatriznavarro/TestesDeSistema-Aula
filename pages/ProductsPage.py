from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class ProductsPage(PageObject):

    # Funções do Selenium ficam dentro da Page
    # Locators
    url = 'https://www.saucedemo.com/inventory.html'
    class_products_title = 'title'
    txt_products_title = 'Products'
    class_list_products = 'inventory_item'
    products_qtd = 6
    id_menu = "react-burger-menu-btn"


    def __init__(self, driver):
        super(ProductsPage,self).__init__(driver=driver)

    def is_url_products(self):
        return self.driver.current_url == self.url

    def has_products_title(self):
        title_page = self.driver.find_element(By.CLASS_NAME, self.class_products_title).text
        return title_page == self.txt_products_title

    def get_products_list_size(self):
        list = self.driver.find_elements(By.CLASS_NAME, self.class_list_products)
        return len(list)

    def has_menu_button(self):
        try:
            return self.driver.find_element(By.ID,self.id_menu).is_displayed()
        except NoSuchElementException:
            return False #elemento nem existe