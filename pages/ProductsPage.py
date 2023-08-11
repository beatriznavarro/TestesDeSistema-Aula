from random import randint
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.PageObject import PageObject


class ProductsPage(PageObject):
    url = 'https://www.saucedemo.com/inventory.html'
    txt_products_title = 'Products'
    class_product_item = 'inventory_item'
    id_menu_btn = "react-burger-menu-btn"
    class_product_card = 'inventory_item'
    class_add_to_cart_btn = 'btn_primary'
    class_cart_badge = 'shopping_cart_badge'
    class_cart_btn = 'shopping_cart_link'
    class_product_name = 'inventory_item_name'
    class_remove_btn = 'btn_secondary'
    text_remove_btn = 'Remove'
    text_add_to_cart_btn = 'Add to cart'
    css_filter_price_low_to_high = '[value="lohi"]'
    css_filter_select = '[data-test="product_sort_container"]'
    class_prices = 'inventory_item_price'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_url_products(self):
        return self.is_url(self.url)

    def has_products_title(self):
        return self.has_title(self.txt_products_title)

    def validate_products_in_page(self):
        products_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)
        return len(products_list) == 6

    def has_menu_button(self):
        try:
            return self.driver.find_element(By.ID, self.id_menu_btn).is_displayed()
        except NoSuchElementException:
            return False

    def add_random_product_to_cart(self):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_card)
        random_product = randint(0, len(product_list) - 1)
        product_element = product_list[random_product]
        add_to_cart_text = product_element.find_element(By.CLASS_NAME, self.class_add_to_cart_btn).text
        if add_to_cart_text != self.text_add_to_cart_btn:
            raise Exception('Add to cart button not found!')
        product_element.find_element(By.CLASS_NAME, self.class_add_to_cart_btn).click()
        button_remove_text = product_element.find_element(By.CLASS_NAME, self.class_remove_btn).text
        if button_remove_text != self.text_remove_btn:
            raise Exception('Remove button not found!')
        return product_element.find_element(By.CLASS_NAME, self.class_product_name).text

    def get_cart_badge_number(self):
        return int(self.driver.find_element(By.CLASS_NAME, self.class_cart_badge).text)

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.class_cart_btn).click()

    def filter(self):
       self.driver.find_element(By.CSS_SELECTOR, self.css_filter_select).click()
       self.driver.find_element(By.CSS_SELECTOR,self.css_filter_price_low_to_high).click()

    def filter_validate_low_to_high(self):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.class_prices)
        for p in range(len(product_list)-1):
            current_price = float(product_list[p].text.replace('$', ''))
            next_price = float(product_list[p+1].text.replace('$', ''))
            if (current_price > next_price):
                return False
        return True












