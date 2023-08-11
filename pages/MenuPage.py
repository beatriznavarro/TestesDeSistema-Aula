from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.PageObject import PageObject
from selenium.webdriver.support import expected_conditions as EC


class MenuPage(PageObject):
    # Locators
    id_menu_button = 'react-burger-menu-btn'
    id_logout = 'logout_sidebar_link'
    id_menu_close_btn = 'react-burger-cross-btn'
    class_menu_items = 'bm-item-list'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def click_menu_btn(self):
        self.driver.find_element(By.ID, self.id_menu_button).click()

    # professor
    def logout(self):
        logout_menu_item = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.id_logout)))
        logout_menu_item.click()

    # professor
    def is_menu_open(self):
        try:
            self.driver.find_element(By.ID, self.id_menu_close_btn)
            self.driver.find_element(By.CLASS_NAME, self.class_menu_items)
            return True
        except NoSuchElementException:
            return False
