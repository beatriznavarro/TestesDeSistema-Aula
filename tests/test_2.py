
from pages.ProductsPage import ProductsPage


class Test2:

    def test_login(self, setup):
        login_page = setup
        login_page.login()
        products_page = ProductsPage(driver=login_page.driver)
        assert products_page.is_url_products()
        assert products_page.has_products_title()
        assert products_page.get_products_list_size() == 6, 'Lista de produtos incorreta'
        assert products_page.has_menu_button(),'Menu não encontrado!'

