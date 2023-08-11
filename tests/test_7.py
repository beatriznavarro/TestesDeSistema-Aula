#### Filtrar produtos do menor preço para o maior preço
#### Pré-condições: Estar logado na aplicação
#### Procedimento:
# 1 - Na página de produtos, escolher o filtro "Price (low to high)"
#### Resultado esperado:
# 1 - A lidat de produtos deve ser exibida pela ordem de preço, do mais barato para o mais caro
#### Pós-condições: Fechar o browser

from pages.ProductsPage import ProductsPage


class Teste7:


    def test_filtra_menor_para_maior(self, login_saucedemo):
        products_page = ProductsPage(driver=login_saucedemo.driver)
        products_page.filter()
        assert products_page.filter_validate_low_to_high(), 'Ordenação incorreta!'
