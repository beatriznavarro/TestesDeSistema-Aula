#### FINALIZAR A COMPRA DE UM PRODUTO COM SUCESSO
#### Pré-condições: Possuir pelo menos 1 produto no carrinho de compras
#### Procedimento:
# 1 - Clicar em CHECKOUT,
# 2 - Preencher os campos : First Name, Last Name e Zip/Postal Code,
# 3 - Clicar em 'CONTINUE' e
# 4 - Clicar em 'FINISH'
#### Resultado esperado:
# 1 - Página 'CHECKOUT: YOUR INFORMATION" deve ser exibida,
# 2 - A aplicação deve exibir a página 'CHECKOUT:OVERVIEW',
# 3 - Confirmar os dados do pedido,
# 4 - A aplicação deve exibir a página 'CHECKOUT: COMPLETE!',
# 5 - Uma mensagem de agradecimento deve ser exibida
#### Pós-condições: Fechar o browser

from pages.CheckoutCompletePage import CheckoutCompletePage
from pages.CheckoutInformationPage import CheckoutInformationPage
from pages.CheckoutOverviewPage import CheckoutOverviewPage
from pages.YourCartPage import YourCartPage


class Test5:

    def test_buy_prod(self, has_prod_in_cart):
        prod_page, prod_name = has_prod_in_cart
        prod_page.open_cart()
        your_cart_page = YourCartPage(driver=prod_page.driver)
        assert your_cart_page.check_your_cart_page(), 'Não é a page de carrinho!'
        your_cart_page.click_checkout()

        checkout_info_page = CheckoutInformationPage(driver=your_cart_page.driver)
        assert checkout_info_page.check_checkout_info_page(), 'Não está na página de checkout infos!'
        checkout_info_page.fill_first_name('Beatriz')
        checkout_info_page.fill_last_name('Navarro')
        checkout_info_page.fill_zip_code('01313015')
        checkout_info_page.click_continue()

        checkout_overview = CheckoutOverviewPage(driver=checkout_info_page.driver)
        assert checkout_overview.check_checkout_overview_page(), 'Não está na página de checkout overview!'
        assert checkout_overview.check_data(prod_name), "Dados incorretos!"
        checkout_overview.click_finish()
        checkout_complete = CheckoutCompletePage(driver=checkout_overview.driver)
        assert checkout_complete.check_checkout_complete_page(), 'Não está na página de checkout complete!'
        assert checkout_complete.has_msg_success(), 'Compra não realizada com sucesso!'

