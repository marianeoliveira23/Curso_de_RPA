import pyautogui as pag
from pathlib import Path
import time

# O Path.home() / "Documents" funciona no Windows independente do idioma da interface
diretorio = Path.home() / "Documentos"
# Garante que a pasta existe (cria se não existir)
diretorio.mkdir(parents=True, exist_ok=True) 

caminho_arquivo = diretorio / "meu_arquivo_rpa.txt"

pag.hotkey("ctrl", "s")
time.sleep(1.0) # Tempo para a janela "Salvar Como" aparecer
pag.write(str(caminho_arquivo))
pag.press("enter")C:\Users\Turma01\Documentos\meu_arquivo_rpa.txt
