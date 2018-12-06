# importações
import json , requests , urllib.request



# link da api informações gerais : https://economia.awesomeapi.com.br/all , link github: https://github.com/raniellyferreira/economy-api

def get_dolar(self):
    response = requests.get("http://economia.awesomeapi.com.br/USD-BRL/1?format=JSONP")
    dados = json.loads(response.content)
    # recebe o valor puro do dolar e arredonda e transformando de string em numero decimal
    valor_dolar = float(dados[0]['ask'])
    get_keys = dados[0].keys()
    # transforma em 2 casas decimais
    #print("Dolar: {:.2f}".format(valor_dolar))
    return  valor_dolar
    #print(get_keys)

def get_euro(self):
    response = requests.get("http://economia.awesomeapi.com.br/EUR-BRL/1?format=JSONP")
    dados = json.loads(response.content)
    # recebe o valor puro do eur e arredonda e transformando de string em numero decimal
    valor_euro = float(dados[0]['ask'])
    get_keys = dados[0].keys()
    # transforma em 2 casas decimais
    #print("EUR: {:.2f}".format(valor_dolar))
    return  valor_euro
    #print(get_keys)

def get_btc(self):
    response = requests.get("http://economia.awesomeapi.com.br/BTC-BRL/1?format=JSONP")
    dados = json.loads(response.content)
    # recebe o valor puro do eur e arredonda e transformando de string em numero decimal
    valor_btc = float(dados[0]['ask'])
    get_keys = dados[0].keys()
    # transforma em 2 casas decimais
    #print("EUR: {:.2f}".format(valor_dolar))
    return  valor_btc
    #print(get_keys)