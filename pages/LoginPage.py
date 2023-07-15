from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):

    # Funções do Selenium ficam dentro da Page
    # Locators

    url = 'https://www.saucedemo.com/'
    id_login_button = 'login-button'
    login_error_message = '[data-test="error"]'
    txt_login_error_message = 'Epic sadface: Username is required'
    id_username = 'user-name'
    id_password = 'password'


    def __init__(self):
      super(LoginPage, self).__init__()
      self.driver.get(self.url)

    # Services
    def close_browser(self):
        self.driver.quit()

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.id_login_button).click()

    def is_url_login(self):
        return self.driver.current_url == self.url

    def has_login_error_message(self):
        error_message = self.driver.find_element(By.CSS_SELECTOR, self.login_error_message).text
        return error_message == self.txt_login_error_message

    def login(self, user_name='standard_user', password='secret_sauce'):
        self.driver.find_element(By.ID, self.id_username).send_keys(user_name)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.click_login_btn()

