import subprocess
import time
import pyautogui as pag
import pygetwindow as gw
from pathlib import Path
from datetime import datetime

# Configurações de Segurança
pag.FAILSAFE = True
pag.PAUSE = 0.5

def executar_robo_notepad():
    # 1. Abrir Notepad direto
    subprocess.Popen(['notepad.exe'])
    
    # 4. Espera Inteligente
    print("Aguardando janela...")
    janela_focada = False
    for _ in range(20): # Tenta por 10 segundos
        win = gw.getWindowsWithTitle('Bloco de Notas') or gw.getWindowsWithTitle('Notepad')
        if win:
            win[0].activate()
            janela_focada = True
            break
        time.sleep(0.5)
    
    if not janela_focada:
        print("Erro: Janela não encontrada.")
        return

    # 6. Escrever com Data/Hora
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pag.write(f"Estudo de Caso RPA\nData de execucao: {agora}\n", interval=0.01)

    # 5. Snapshot antes de salvar
    pag.screenshot("evidencia_escrita.png")

    # 2. Salvar com Ctrl+S e Pathlib
    pag.hotkey("ctrl", "s")
    time.sleep(1.0)
    
    desktop = Path.home() / "Documents"
    nome_arquivo = f"rpa_final_{datetime.now().strftime('%H%M%S')}.txt"
    caminho_completo = desktop / nome_arquivo
    
    pag.write(str(caminho_completo))
    pag.press("enter")
    time.sleep(1.0)

    # 3. Fechar Universal (Alt+F4)
    pag.hotkey("alt", "f4")
    print(f"Sucesso! Arquivo salvo em: {caminho_completo}")

if __name__ == "__main__":
    executar_robo_notepad()