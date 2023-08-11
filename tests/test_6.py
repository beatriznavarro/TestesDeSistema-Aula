#### Adicionar um produto no carrinho de compras
#### Pré-condições: Estar logado na aplicação
#### Procedimento:
# 1 - Na página de produtos, escolher um prod e clicar em 'ADD TO CART'
# 2 - Abrir o carrinho de comprar
#### Resultado esperado:
# 1 - O botão ADD TO CART deve mudar para REMOVE
# 2 - O icone do carrinho deve aparecer coma  numeração 1
# 3 - Página de carrinho de compras deve ser exibida
# 4 - O prod selecionado deve ser exibido com item de compra
#### Pós-condições: Fechar o browser

from pages.ProductsPage import ProductsPage
from pages.YourCartPage import YourCartPage


class Test6:

    def test_add_product_to_cart(self, has_prod_in_cart):
        product_p, product_name = has_prod_in_cart
        product_p.open_cart()
        your_cart_p = YourCartPage(driver=product_p.driver)
        assert your_cart_p.check_your_cart_page(), 'Página do carrinho não encontrada!'
        assert your_cart_p.check_product_name_in_cart(product_name), 'Nome do produto não encontrado!'




