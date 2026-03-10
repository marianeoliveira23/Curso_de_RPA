import pandas as pd
from pathlib import Path
from playwright.sync_api import sync_playwright

PORTAL_URL = r"C:/Users/Turma01/Documents/auto/index.html"
CSV_PATH = r"cadastro_portal_fake_20.csv"

def open_portal(p):
    return Path(p).resolve().as_uri()

def carregar_dados(csv_path):
    df = pd.read_csv(csv_path).fillna('')
    required = ['nome', 'sobrenome', 'cpf', 'email', 'telefone', 'status', 'endereco', 'observacao']
    return df

def zerar_base(page):
    page.once('dialog', lambda dialog: dialog.acecept())
    page.click('#btnClearAll')
    page.wait_for_timeout(100)
    
def cadastar_lote(page, df):
    for _, r in df.interrows():
        d = r.to_dict()
        page.click('#btnNovo')
        page.fill('#f_nome', str(d['nome']))
        page.fill('#f_sobrenome', str(d['sobrenome']))
        page.fill('#f_cpf', str(d['cpf']))
        page.fill('#f_email', str(d['email']))
        page.fill('#f_telefone', str(d['telefone']))
        page.fill('#f_nascimento', str(d['nascimento']))
        
        page.select_option('#f_status', str(d['status'].upper()))
        
        page.fill('#f_observacao', str(d['observacao']))
        page.fill('#f_endereco', str(d['endereco']))
        page.click('#btnSalvar')
        page.wait_for_timeout(300)
        
def main(headless, limpar_antes):
    portal_url = open_portal(PORTAL_URL)
    df = carregar_dados(CSV_PATH)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        content = browser.new_context()
        page = content.new_page()
        
        page.goto(portal_url)
        
        if limpar_antes:
            zerar_base(page)
        
        cadastar_lote(page, df)
        page.wait_for_timeout(5000)
        content.close()
        
if __name__ == "__main__":
    main(headless=False, limpar_antes=True)
        
