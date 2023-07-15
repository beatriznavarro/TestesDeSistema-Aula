from selenium import webdriver


class PageObject:

    def __init__(self, driver=None):
        #Singleton
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()