import pyautogui
import pandas as pd
import time
import os
from datetime import datetime

PASTA_ATUAL = os.getcwd()
PLANILHA_ENTRADA = "clientes.xlsx"
PLANILHA_SAIDA = "clientes_processados.xlsx"

timestamp_nome = datetime.now().strftime("%Y%m%d_%H%M%S")
NOME_ARQUIVO_FINAL = f"PyAutoGUI-Pandas-{timestamp_nome}.txt"

def esperar_notepad():
    print("Aguardando o Bloco de Notas abrir...")
    time.sleep(2) 
    
    tentativas = 0
    while tentativas < 30:
        janelas = pyautogui.getAllTitles()
        
        for j in janelas:
            if "bloco de notas" in j.lower() or "notepad" in j.lower():
                print(f"Janela encontrada: {j}")
                try:
                    import pygetwindow as gw
                    win = gw.getWindowsWithTitle(j)[0]
                    win.activate()
                except:
                    pass 
                return True
        
        time.sleep(0.5)
        tentativas += 1
    return False

# ─── MAIN: Fluxo Principal
def main():
    # 1. Ler a planilha (deve ter as colunas: Nome, Email, Cargo, Telefone)
    try:
        df = pd.read_excel(PLANILHA_ENTRADA)
    except Exception as e:
        print(f"Erro ao ler planilha: {e}")
        return

    resultados = []

    # 2. Abrir o Bloco de Notas
    pyautogui.hotkey("win", "r")
    pyautogui.typewrite("notepad", interval=0.01)
    pyautogui.press("enter")
    
    if not esperar_notepad():
        print("Erro: O Bloco de Notas não abriu a tempo.")
        return

    # 3. Processar todos os clientes dentro do mesmo arquivo
    for index, row in df.iterrows():
        nome     = str(row["Nome"])
        email    = str(row["Email"])
        cargo    = str(row["Cargo"])
        telefone = str(row["Telefone"])
        
        # Captura data/hora exata do processamento da ficha
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Digitar os dados
        texto_ficha = (
            f"--- FICHA {index + 1} ---\n"
            f"Nome:     {nome}\n"
            f"Email:    {email}\n"
            f"Cargo:    {cargo}\n"
            f"Telefone: {telefone}\n"
            f"Gerado em: {agora}\n"
            f"{'-' * 30}\n\n"
        )
        
        pyautogui.write(texto_ficha, interval=0.01)

        resultados.append({
            "ID": index + 1,
            "Nome": nome,
            "Email": email,
            "Cargo": cargo,
            "Telefone": telefone,
            "Data_Processamento": agora, # Data/hora exigida
            "Status": "Processado"
        })
        print(f"[OK] Adicionado: {nome}")

    pyautogui.hotkey("ctrl", "s")
    time.sleep(1)
    
    caminho_salvamento = os.path.join(PASTA_ATUAL, NOME_ARQUIVO_FINAL)
    pyautogui.write(caminho_salvamento, interval=0.01)
    pyautogui.press("enter")
    
    time.sleep(1)
    pyautogui.hotkey("ctrl", "w")

    df_saida = pd.DataFrame(resultados)
    df_saida.to_excel(PLANILHA_SAIDA, index=False)
    print(f"\nAutomação concluída!")
    print(f"Arquivo de texto: {NOME_ARQUIVO_FINAL}")
    print(f"Relatório Excel: {PLANILHA_SAIDA}")

if __name__ == "__main__":
    main()