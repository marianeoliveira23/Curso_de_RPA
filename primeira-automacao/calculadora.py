import pyautogui
import pandas as pd
import pyperclip
import time
import subprocess
from datetime import datetime

RELATORIO_SAIDA = "relatorio_pedidos_final.xlsx"
PAUSA = 0.5

def gerar_dados_sinteticos():
    data = {
        "ID_Pedido": [101, 102, 103, 104, 105],
        "Produto": ["Notebook", "Mouse", "Monitor", "Teclado", "Servidor"],
        "Quantidade": [2, 15, 6, 4, 1],
        "Preco_Unitario": [4500.00, 50.00, 1200.00, 150.00, 25000.00],
        "Desconto_%": [5, 0, 2, 0, 10]
    }
    return pd.DataFrame(data)

def abrir_calculadora():
    subprocess.Popen("calc")
    time.sleep(1.5)

def fechar_calculadora():
    pyautogui.hotkey("alt", "f4")
    time.sleep(0.5)

def calcular_total_na_calc(quantidade, preco_unit):
    abrir_calculadora()
    pyautogui.write(str(quantidade), interval=0.05)
    pyautogui.press("*")
    pyautogui.write(str(preco_unit), interval=0.05)
    pyautogui.press("=")
    time.sleep(PAUSA)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.3)
    fechar_calculadora()
    
    valor = pyperclip.paste()
    valor_limpo = ''.join(c for c in valor if c.isdigit() or c in ',.')
    return float(valor_limpo.replace(",", "."))

# Calcular Desconto Progressivo
def calcular_desconto_progressivo(quantidade):
    if quantidade < 5:
        return 0
    elif 5 <= quantidade <= 9:
        return 3
    else: # Quantidade >= 10
        return 7

# Processar Pedido com Categorização
def processar_pedido(row):
    id_ped = row["ID_Pedido"]
    qtd = int(row["Quantidade"])
    preco = float(row["Preco_Unitario"])
    desc_original = float(row["Desconto_%"])
    
    # Cálculo do Desconto Final (Soma do original + progressivo)
    desc_extra = calcular_desconto_progressivo(qtd)
    desc_total_pct = desc_original + desc_extra
    
    # Cálculo Financeiro via Calculadora
    total_bruto = calcular_total_na_calc(qtd, preco)
    valor_desconto = round(total_bruto * (desc_total_pct / 100), 2)
    total_liquido = round(total_bruto - valor_desconto, 2)
    
    # Status (Regra original)
    status = "Aprovado" if total_liquido <= 20000 else "Revisao"
    
    # Classificação de Categoria (Nova Regra)
    if total_liquido <= 1000:
        categoria = "Pequeno"
    elif total_liquido <= 20000:
        categoria = "Médio"
    else:
        categoria = "Grande"

    print(f"Processado ID {id_ped}: Total R$ {total_liquido:.2f} ({categoria})")

    return {
        "ID_Pedido": id_ped,
        "Produto": row["Produto"],
        "Total_Liquido": total_liquido,
        "Status": status,
        "Categoria": categoria,
        "Desconto_Final_%": desc_total_pct
    }

# Exportar com Resumo Agrupado
def exportar_relatorio(resultados, caminho):
    df_out = pd.DataFrame(resultados)
    
    # Salvar Excel
    df_out.to_excel(caminho, index=False)
    
    resumo = df_out.groupby("Status")["Total_Liquido"].agg(['count', 'sum']).rename(
        columns={'count': 'Qtd Pedidos', 'sum': 'Total Líquido'}
    )
    
    print("\n" + "="*30)
    print("RESUMO POR STATUS")
    print("="*30)
    print(resumo)
    print("="*30)
    print(f"Relatório salvo em: {caminho}")

# ─── MAIN
def main():
    print("Iniciando processamento sintético...\n")
    df = gerar_dados_sinteticos()
    
    lista_resultados = []
    for _, row in df.iterrows():
        resultado = processar_pedido(row)
        lista_resultados.append(resultado)
    
    exportar_relatorio(lista_resultados, RELATORIO_SAIDA)

if __name__ == "__main__":
    main()