# Pré-condições:
# Procedimento:
# Resultado esperado:
# Pós-condições:

from pages.MenuPage import MenuPage

class Test3:

   # def test_logout(self, setup):
      #  login_page = setup
      #  login_page.login()
       # menu_page = MenuPage(driver=login_page.driver)
      #  menu_page.click_menu_btn()
       # menu_page.click_logout()
       # assert login_page.is_url_login(), "Não está na página de login!"

    # versão professor
    def test_logout_app(self, login_saucedemo):
        menu_p = MenuPage(driver=login_saucedemo.driver)
        menu_p.click_menu_btn()
        assert menu_p.is_menu_open(), 'Menu não está aberto!'
        menu_p.logout()
        assert login_saucedemo.is_url_login(), "Não está na página de login!"
