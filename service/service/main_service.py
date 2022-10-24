import json
import time

import pandas as pd
import requests
from loguru import logger

from service.constants import mensagens

class ListaDeRepositorios():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
 
    def requisicao_api(self, usuario):
        resposta = requests.get(
           f'https://api.github.com/users/{usuario}/repos')

        if resposta.status_code == 200:
            url_vector = []

            for repo in resposta.json():
                url_vector.append(repo['html_url'])
            return [repo['url'] for repo in resposta.json()]

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
