#### Verificar mensagem de erro ao não preencher os dados em "Checkout: Your Information"
#### Pré-condições: Possuir pelo menos 1 produto no carrinho de compras
#### Procedimento:
# 1 - Clicar em 'CHECKOUT',
# 2 - Não preencher os campos: First name, Last name e Zip/Postal Code,
# 3 - Clicar em 'CONTINUE'
#### Resultado esperado:
# 1 - Página 'CHECKOUT: YOUR INFORMATION deve ser exibida
# 2 - A aplicação deve permanecer na mesma página
# 3 - A mensagem de erro deve ser exibida:"Error: First Name is required"
#### Pós-condições: Fechar o browser

from pages.CheckoutInformationPage import CheckoutInformationPage
from pages.YourCartPage import YourCartPage


class Test4:

    def test_verify_error_message__in_checkout(self, has_prod_in_cart):
        prod_page, prod_name = has_prod_in_cart
        prod_page.open_cart()
        your_cart_page = YourCartPage(driver=prod_page.driver)
        assert your_cart_page.check_your_cart_page(), 'Não é a página de carrinho!'
        your_cart_page.click_checkout()
        checkout_info_page = CheckoutInformationPage(driver=your_cart_page.driver)
        assert checkout_info_page.check_checkout_info_page(), 'Não está na página de checkout!'
        checkout_info_page.click_continue()
        assert checkout_info_page.has_first_name_required_error_message(), 'Erro!'
