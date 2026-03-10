# Seletores CSS variados
# Importa a API síncrona do Playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://www.saucedemo.com')
    page.wait_for_load_state('networkidle')

    # Seletor por tag
    # Seleciona TODOS os inputs da página
    # Retorna uma coleção — usamos .count() para ver quantos são
    total_inputs = page.locator('input').count()
    print(f'Total de inputs na página: {total_inputs}')

    # Seletor por classe
    # O ponto (.) indica seleção por classe CSS
    # form_input é a classe dos campos de login
    total_form_inputs = page.locator('.form_input').count()
    print(f'Inputs com classe form_input: {total_form_inputs}')

    # Seletor por id
    # O # indica seleção por id
    # Seleciona especificamente o campo user-name
    campo_usuario = page.locator('#user-name')
    campo_usuario.fill('standard_user')
    print('Campo usuário preenchido via id: OK')

    # Seletor por atributo
    # Colchetes [] indicam seleção por atributo
    # Seleciona input cujo type é password
    campo_senha = page.locator('input[type="password"]')
    campo_senha.fill('secret_sauce')
    print('Campo senha preenchido via atributo type: OK')

    # Seletor combinado: tag + atributo
    # Seleciona input que tem type submit E name login-button
    botao = page.locator('input[type="submit"][name="login-button"]')
    botao.click()
    page.wait_for_load_state('networkidle')
    print('Login realizado via seletor combinado: OK')

    # Seletor por classe após login
    # Conta quantos itens de inventário existem na página de produtos
    total_itens = page.locator('.inventory_item').count()
    print(f'Total de itens no inventário: {total_itens}')

    browser.close()
