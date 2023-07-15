import pytest
from pages.LoginPage import LoginPage


@pytest.fixture()
def setup():
    login_page = LoginPage()
    yield login_page
    login_page.close_browser()