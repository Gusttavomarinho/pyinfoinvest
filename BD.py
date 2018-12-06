import postgresql
import time
import random
class BD():
    _db = None
    def __init__(self):
        self._db = postgresql.open("pq://seu_usuario:sua_senha@localhost/infoinvest")

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


'''def cadastrar_cidade(nome,uf):
    con = BD()
    sql ="INSERT INTO cidade (id,nome,uf) VALUES (default,'{}','{}')".format(nome,uf)
    if con.manipular(sql):
        print("Cidade Cadastrada com Sucesso")
    con.fechar()
def alterar_cidade(id,nome,uf):
    con = BD()
    sql = "UPDATE cidade SET nome = '{}' , uf = '{}' WHERE id={}".format(nome,uf,id)
    con.manipular(sql)
    con.fechar()
def deletar_cidade(id_cidade):
    con = BD()
    sql = "DELETE FROM cidade WHERE id={}".format(id_cidade)
    con.manipular(sql)
    con.fechar()'''

def cadastrar_tipo_investimento(nome):
    con = BD()
    sql = "INSERT INTO tipo_investimento (id,nome) VALUES (default,'{}')".format(nome)
    con.manipular(sql)
    con.fechar()


def alterar_tipo_investimento(id,nome):
    con = BD()
    sql = "UPDATE tipo_investimento SET nome='{}' WHERE id={}".format(nome,id)
    con.manipular(sql)
    con.fechar()


def deletar_tipo_investimento(id):
    con = BD()
    sql = "DELETE FROM tipo_investimento WHERE id={}".format(id)
    con.manipular(sql)
    con.fechar()


def selecionar_tipo_investimento(id):
    con = BD()
    sql = "SELECT * FROM tipo_investimento WHERE id={}".format(id)
    resultado = con.consultar(sql)
    for r in resultado:
        dic = {'Id':r[0],'Nome':r[1]}
        print(dic)
    con.fechar()

def selecionar_todos_tipo_investimento():
    con = BD()
    sql = "SELECT * FROM tipo_investimento"
    resultado = con.consultar(sql)
    lista = []
    for r in resultado:
        dic = {'Id':r[0],'Nome':r[1]}
        resultado_dic = "Codigo: {} = {}".format(dic['Id'],dic['Nome'])
        lista.append(resultado_dic)
    return  lista
    con.fechar()


def cadastrar_perfil(tipo_perfil):
    con = BD()
    sql = "INSERT INTO perfil (id,tipo_perfil) VALUES (default,'{}')".format(tipo_perfil)
    con.manipular(sql)
    con.fechar()


def alterar_perfil(id,tipo_perfil):
    con = BD()
    sql = "UPDATE perfil SET tipo_perfil='{}' WHERE id={}".format(tipo_perfil, id)
    con.manipular(sql)
    con.fechar()


def deletar_perfil(id):
    con = BD()
    sql = "DELETE FROM perfil WHERE id={}".format(id)
    con.manipular(sql)
    con.fechar()


def selecionar_perfil(id):
    con = BD()
    sql = "SELECT * FROM perfil WHERE id={}".format(id)
    resultado = con.consultar(sql)
    for r in resultado:
        dic = {'Id': r[0], 'Tipo Perfil:': r[1]}
        print(dic)
    con.fechar()


def cadastrar_indice(nome,taxa):
    con = BD()
    sql = "INSERT INTO indice (id,nome,taxa) VALUES (default,'{}',{})".format(nome,taxa)
    con.manipular(sql)
    con.fechar()


def alterar_indice(id,nome,taxa):
    con = BD()
    sql = "UPDATE indice SET nome='{}',taxa={} WHERE id={}".format(nome,taxa,id)
    con.manipular(sql)
    con.fechar()


def deletar_indice(id):
    con = BD()
    sql = "DELETE FROM indice WHERE id={}".format(id)
    con.manipular(sql)
    con.fechar()


def selecionar_indice(id):
    con = BD()
    sql = "SELECT * FROM indice WHERE id={}".format(id)
    resultado = con.consultar(sql)
    for r in resultado:
        dic = {'Id': r[0], 'Nome:': r[1], 'Taxa:': r[2]}
        print(dic)
    con.fechar()



def cadastrar_usuario(cpf,senha,nome,email,renda):
    con = BD()
    sql = "INSERT INTO usuario (cpf,senha,nome,email,renda,id_perfil) VALUES ('{}','{}','{}','{}',{},{})".format(cpf,senha,nome,email,renda,0)
    con.manipular(sql)
    con.fechar()


def alterar_usuario(cpf,senha,nome,email,renda):
    con = BD()
    sql = "UPDATE usuario SET senha='{}',nome='{}',email='{}',renda='{}' WHERE cpf='{}'".format(senha,nome,email,renda,cpf)
    con.manipular(sql)
    con.fechar()


def deletar_usuario(cpf):
    con = BD()
    #limpar cadastro investimento antes de deletar o usuario
    sqlinvestimento_cadastro = "DELETE FROM cadastro_investimento WHERE cpf_usuario='{}'".format(cpf)
    con.manipular(sqlinvestimento_cadastro)
    #deletar o usuario
    sql = "DELETE  FROM usuario WHERE cpf='{}'".format(cpf)
    con.manipular(sql)
    con.fechar()


def selecionar_usuario(cpf):
    con = BD()
    sql = "SELECT * FROM usuario WHERE cpf='{}'".format(cpf)
    resultado = con.consultar(sql)
    for r in resultado:
        dic = {'CPF': r[0], 'Senha': r[1], 'Nome': r[2], 'Email': r[3], 'Renda': r[4], 'Id Perfil': r[5]}
    return dic
    con.fechar()

def buscar_login_usuario(cpf):
    con = BD()
    sql = "SELECT cpf,senha FROM usuario WHERE cpf='{}'".format(cpf)
    resultado = con.consultar(sql)
    for r in resultado:
        dic_login = {'CPF': r[0], 'Senha': r[1]}
    return dic_login
    con.fechar()


def cadastrar_investimento(saldo,data_aplicacao,data_retirada,cpf_usuario,tipo_id):
    con = BD()
    sql = "INSERT INTO cadastro_investimento (codigo,saldo,data_aplicacao,data_retirada,cpf_usuario,tipo_id) VALUES (default,'{}','{}','{}','{}',{})".format(saldo,data_aplicacao,data_retirada,cpf_usuario,tipo_id)
    con.manipular(sql)
    con.fechar()


def alterar_investimento(codigo,cpf_usuario,saldo,data_aplicacao,data_retirada):
    #Pegar cpf do usuario
    con = BD()
    #pegar o tipo de investimento
    tipo_sql = "SELECT tipo_id  FROM cadastro_investimento WHERE codigo='{}'".format(codigo)
    resultado_tipo = con.consultar(tipo_sql)
    for t in resultado_tipo:
        dic_tipo = {'tipo':t[0]}
    #aletar o investimento
    sql = "UPDATE cadastro_investimento SET saldo='{}',data_aplicacao='{}',data_retirada='{}',cpf_usuario='{}',tipo_id='{}' WHERE codigo='{}'".format(saldo,data_aplicacao,data_retirada,cpf_usuario,dic_tipo['tipo'],codigo)
    con.manipular(sql)
def deletar_investimento(codigo):
    con = BD()
    sql = "DELETE FROM cadastro_investimento WHERE codigo={}".format(codigo)
    con.manipular(sql)
    con.fechar()


def selecionar_investimento(codigo):
    con = BD()
    sql = "SELECT * FROM cadastro_investimento WHERE codigo='{}'".format(codigo)
    resultado = con.consultar(sql)
    for r in resultado:
        dic = {'Codigo': r[0], 'Saldo:': r[1], 'Data Aplicação:': r[2], 'Data Retirada:': r[3], 'CPF Usuario:': r[4], 'Tipo Investimento:': r[5]}
        print(dic)
    con.fechar()


def cadastrar_cambio(tipo_moeda,valor,data):
    con = BD()
    sql = "INSERT INTO cambio (id,tipo_moeda,valor,data,data_cadastro) VALUES (default,'{}',{},'{}',current_timestamp)".format(tipo_moeda,valor,data)
    con.manipular(sql)


#nao lembro para que serve esta função
def consultar_todos_dolar():
    con = BD()
    sql = "SELECT data , valor FROM cambio WHERE tipo_moeda ='USD'"
    lista = []
    resultado = con.consultar(sql)
    for r in resultado:
        lista.append(r)
    return lista


#funções para consultar a variação das moedas
def consultar_dolar_variacao_dia():
    con = BD()
    sql = "SELECT data , valor FROM cambio WHERE tipo_moeda ='USD' AND data=current_date"
    lista = []
    resultado = con.consultar(sql)
    for r in resultado:
        lista.append(r)
    return lista

def consultar_dolar_variacao_dia_anterior():
    con = BD()
    sql = "SELECT data , valor FROM cambio WHERE tipo_moeda ='USD' AND data=current_date - 1"
    lista = []
    resultado = con.consultar(sql)
    for r in resultado:
        lista.append(r)
    return lista


def consultar_euro_variacao_dia():
    con = BD()
    sql = "SELECT data , valor FROM cambio WHERE tipo_moeda ='EUR' AND data=current_date"
    lista = []
    resultado = con.consultar(sql)
    for r in resultado:
        lista.append(r)
    return lista

def consultar_euro_variacao_dia_anterior():
    con = BD()
    sql = "SELECT data , valor FROM cambio WHERE tipo_moeda ='EUR' AND data=current_date - 1"
    lista = []
    resultado = con.consultar(sql)
    for r in resultado:
        lista.append(r)
    return lista


def consultar_btc_variacao_dia():
    con = BD()
    sql = "SELECT data , valor FROM cambio WHERE tipo_moeda ='BTC' AND data=current_date"
    lista = []
    resultado = con.consultar(sql)
    for r in resultado:
        lista.append(r)
    return lista

def consultar_btc_variacao_dia_anterior():
    con = BD()
    sql = "SELECT data , valor FROM cambio WHERE tipo_moeda ='BTC' AND data=current_date - 1"
    lista = []
    resultado = con.consultar(sql)
    for r in resultado:
        lista.append(r)
    return lista


#coletar informações do total investido
def bd_total_investido(codigo):
    con = BD()
    sql = "SELECT SUM (saldo)FROM cadastro_investimento WHERE tipo_id ={}".format(codigo)
    resultado = con.consultar(sql)
    for t in resultado:
        dic = {'total':float(t[0])}
        return dic['total']


#fica repetindo e inserindo na tabela
'''while True:
    numero = random.randrange(1,999999)
    cidade = "Cidade Teste{}".format(numero)
    cadastrar_cidade(cidade,"TE")
    time.sleep(1)'''


consultar_todos_dolar()




