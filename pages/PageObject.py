from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:
    class_title = 'title'

    def __init__(self, driver=None, browser=None):
        # Singleton
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise Exception('Browser não suportado!')

        self.driver.maximize_window()
        #self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def is_url(self, url):
        return self.driver.current_url == url

    def has_title(self, title_text):
        title_page = self.driver.find_element(By.CLASS_NAME, self.class_title).text
        return title_page == title_text

    def check_page(self, url, title_text):
        return self.is_url(url) and self.has_title(title_text)
