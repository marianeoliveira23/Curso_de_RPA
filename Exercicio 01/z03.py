import pygetwindow as gw
import time

# Melhoria 4: Espera inteligente (Substitui o time.sleep fixo)
print("Aguardando o Notepad aparecer...")
timeout = 10
start_time = time.time()
while time.time() - start_time < timeout:
    # Busca títulos em PT e EN
    janelas = gw.getWindowsWithTitle('Bloco de Notas') or gw.getWindowsWithTitle('Notepad')
    if janelas:
        janela = janelas[0]
        janela.activate() # Foca na janela encontrada
        break
    time.sleep(0.5)

# Melhoria 3: Fechar sem depender de menus de idioma (Alt+F4)
pag.hotkey("alt", "f4")