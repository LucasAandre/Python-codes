import PyPDF2
import os

merger = PyPDF2.PdfMerger() # Mesclador de arquivos

lista_arquivos = os.listdir("Arquivos")
lista_arquivos.sort()

print(lista_arquivos)

for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        merger.append(f'Arquivos/{arquivo}')

merger.write('PDF Final') # Salva em um novo arquivo
