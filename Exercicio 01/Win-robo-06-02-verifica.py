import time
import pygetwindow as gw

titulos_possiveis = ['Bloco de Notas', 'Notepad']

print('Aguardando o Notepad abrir... (Ctrl+C para parar)')

while True:
    notepad_aberto = any(gw.getWindowsWithTitle(t) for t in titulos_possiveis)

    if notepad_aberto:
        print('Notepad está aberto. Saindo do bot.')
        break

    time.sleep(0.5)