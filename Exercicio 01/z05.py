from datetime import datetime

agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
texto_com_data = f"Este texto foi gerado via RPA em: {agora}"
pag.write(texto_com_data, interval=0.01)