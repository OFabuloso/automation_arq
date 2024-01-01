"""
Projeto de automação, desenvolvido em video aula Prof. Lira.
Envia documentos de uma pasta para outra, alem de organizar
conforme necessidade.
"""
__author__ = "Fabuloso"
__version__ = "0.0.1"
import os
from tkinter.filedialog import askdirectory

pasta_origem = askdirectory(title="Pasta Origem")
pasta_destino = askdirectory(title="Pasta Destino")

regras_arquivos = {
    "jan":"janeiro",
    "fev" : "fevereiro",
    "mar" : "março"
   
}

lista_arquivos = os.listdir(pasta_origem)

for nome_arquivo in lista_arquivos:
    for chave in regras_arquivos.keys():
        if chave in nome_arquivo:
            nova_pasta = regras_arquivos[chave]
            nome_completo_original = os.path.join(pasta_origem, nome_arquivo)
            nome_completo_final = os.path.join(pasta_destino, nova_pasta, nome_arquivo)
            # verificar se existe a pasta nova_pasta no destino (pasta_destino)
            caminho_nova_pasta = os.path.join(pasta_destino, nova_pasta)
            if not os.path.exists(caminho_nova_pasta):
                os.mkdir(caminho_nova_pasta)
            os.rename(nome_completo_original, nome_completo_final)