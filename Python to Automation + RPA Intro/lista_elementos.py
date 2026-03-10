# Trabalhar com listas de elementos
# Importa a API síncrona do Playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Faz login no saucedemo
    page.goto('https://www.saucedemo.com')
    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.get_by_role('button', name='Login').click()
    page.wait_for_load_state('networkidle')

    # Contar elementos

    # Localiza todos os nomes de produtos
    locator_nomes = page.locator('[data-test="inventory-item-name"]')

    # count() retorna o número total de elementos encontrados
    total = locator_nomes.count()
    print(f'Total de produtos: {total}')

    # Pegar o primeiro e o último

    # first acessa o primeiro elemento da lista
    primeiro = locator_nomes.first.text_content()
    print(f'Primeiro produto: {primeiro}')

    # last acessa o último elemento da lista
    ultimo = locator_nomes.last.text_content()
    print(f'Último produto: {ultimo}')

    # Pegar por índice

    # nth(índice) acessa o elemento na posição indicada
    # índices começam em 0
    terceiro = locator_nomes.nth(2).text_content()
    print(f'Terceiro produto: {terceiro}')

    # Pegar todos de uma vez

    # all_text_contents() retorna uma lista Python com o texto de cada elemento
    todos = locator_nomes.all_text_contents()
    print('\nTodos os produtos:')
    for i, nome in enumerate(todos, start=1):
        print(f'  {i}. {nome}')

    # Filtrar por texto

    # filter(has_text=) retorna apenas os elementos que contêm o texto
    locator_filtrado = page.locator('[data-test="inventory-item-name"]')
    locator_filtrado = locator_filtrado.filter(has_text='Sauce Labs')
    total_sauce = locator_filtrado.count()
    print(f'\nProdutos com "Sauce Labs" no nome: {total_sauce}')

    browser.close()
