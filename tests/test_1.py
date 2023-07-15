class Test1:

    def test_click_login_btn(self, setup):
        login_page = setup
        login_page.click_login_btn()
        assert login_page.is_url_login(), "Página mudou!"
        assert login_page.has_login_error_message(), 'Mensagem de erro não encontrada!'

