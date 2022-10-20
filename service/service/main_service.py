import json
import time

import pandas as pd
import requests
from loguru import logger

from service.constants import mensagens

class ListaDeRepositorios():

    def __init__(self):
         logger.debug(mensagens.INICIO_LOAD_SERVICO)
-        self.load_servico()
 
    def requisicao_api(self, usuario):
         resposta = requests.get(
+            f'https://api.github.com/users/{usuario}/repos')
         if resposta.status_code == 200:
            return resposta.json()
+           print(resposta.json())
+           for repo in resposta.json():
+           return [repo['url'] for repo in resposta.json()]
         else:
+           return None
 
    def imprime_repositorios(self):
        dados_api = self.requisicao_api()
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                print(dados_api[i]['name'])
        else:
            print(dados_api)

        response = {
                     "listaRepositorios": json.loads(dados_api.to_json(
                                                                            orient='records', force_ascii=False))}

        return response
