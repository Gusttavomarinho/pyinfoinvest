import postgresql
from AppController import *
import time
class BD():
    _db = None
    def __init__(self):
        self._db = postgresql.open("pq://postgres:gustavo10@localhost/infoinvest")
        #acesso ao bd local

    def manipular(self,sql):
        try:
            self._db.execute(sql)
        except:
            return  False

    def consultar(self,sql):
        rs=None
        try:
            rs=self._db.prepare(sql)
        except:
            return None
        return rs
    def fechar(self):
        self._db.close()





def cadastrar_cambio(tipo_moeda,valor,data):
    con = BD()
    sql = "INSERT INTO cambio (id,tipo_moeda,valor,data,data_cadastro) VALUES (default,'{}',{},'{}',current_timestamp)".format(tipo_moeda,valor,data)
    con.manipular(sql)

def cadastrar_cambio_automatico():
    con = BD()
    getdolar = "{:.3f}".format(get_dolar(self=None))
    geteuro = "{:.3f}".format(get_euro(self=None))
    getbtc = "{:.3f}".format(get_btc(self=None))
    sqldolar = "INSERT INTO cambio (id,tipo_moeda,valor,data,data_cadastro) VALUES (default,'USD',{},current_date,current_timestamp)".format(getdolar)
    sqleuro = "INSERT INTO cambio (id,tipo_moeda,valor,data,data_cadastro) VALUES (default,'EUR',{},current_date,current_timestamp)".format(geteuro)
    sqlbtc = "INSERT INTO cambio (id,tipo_moeda,valor,data,data_cadastro) VALUES (default,'BTC',{},current_date,current_timestamp)".format(getbtc)
    con.manipular(sqldolar)
    con.manipular(sqleuro)
    con.manipular(sqlbtc)




#fica repetindo e inserindo na tabela
while True:
    cadastrar_cambio_automatico()
    time.sleep(660)





