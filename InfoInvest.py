from tkinter import *
from AppController import *
from BD import *
from GraficoVariacaoDia import *
from GraficoTotal import *

class Sistema:
    #####################
    # Telas do Sistema
    #####################
    def __init__(self, janela):
        self.janela = None
        self.caixa = Frame(janela)
        self.caixa.grid()

        janela.title('Tela de Login')
        # Criando os Label
        self.titulo = Label(janela, text='Tela de Login do Sistema')
        self.titulo["font"] = ("Arial", "10", "bold")
        self.usuario = Label(janela, text='Login: ')
        self.senha = Label(janela, text='Senha: ')
        #Criando as entradas
        self.entradaUsuario = Entry(janela)
        self.entradaSenha = Entry(janela, show='*')
        #Criando os botoes
        self.entrar = Button(janela, text='Entrar', command=self.ChecarLogin)
       #self.cadastrar = Button(janela, text='Cadastrar', command=self.JanelaCadastro)
        self.status = Label(janela, text='')
        #Posicionamento na janela
        self.titulo.grid(row=0, column=1, pady=10 ,)
        self.usuario.grid(row=1, column=0, pady=10)
        self.senha.grid(row=2, column=0,  pady=10)
        self.entradaUsuario.grid(row=1, column=1)
        self.entradaSenha.grid(row=2, column=1)
        self.entrar.grid(row=3, column=1,pady=10)
        #self.cadastrar.grid(row=3, column=1, pady=2 , sticky=E)
        self.status.grid(row=4, column=1 , pady=10)

    #Checando
    def ChecarLogin(self):
        buscar_login = buscar_login_usuario(self.entradaUsuario.get())
        login = buscar_login['CPF']
        senha = buscar_login['Senha']
        if self.entradaUsuario.get() == login and self.entradaSenha.get() == senha:
            self.JanelaPrincipal()
            self.status['text'] = 'Logado'
            self.status['bg'] = 'green'

        else:
            self.status['text'] = 'Dados Inválidos'
            self.status['bg'] = 'red'


    def JanelaPrincipal(self):

        self.janela = Tk()
        self.janela.title('Sistema InfoInvest')
        self.janela.geometry('400x350+525+225')
        self.janela.resizable(False,False)
        self.menu = Menu(self.janela)
        self.janela.config(menu=self.menu)

        #Criando as opções de menu
        self.MenuCadastro = Menu(self.menu)
        self.MenuEstatistica = Menu(self.menu)
        self.MenuAdministrador = Menu(self.menu)

        #Criando as opções de cada menu
        self.menu.add_cascade(label="Cadastro", menu=self.MenuCadastro)
        self.MenuCadastro.add_command(label="Investimentos", command = self.JanelaCadastroInvestimento )
        self.MenuCadastro.add_command(label="Perfil de Investimento", )
        self.menu.add_cascade(label="Estatistica", menu=self.MenuEstatistica)
        self.MenuEstatistica.add_command(label="Total Investido" , command = self.JanelaTotalInvestido)
        self.MenuEstatistica.add_command(label="Grafico Barra Total Investido", command=GraficoBarraTotalInvestido)
        self.MenuEstatistica.add_command(label="Grafico Plot Total Investido", command=GraficoPlotTotalInvestido)
        self.MenuEstatistica.add_separator()
        self.MenuEstatistica.add_command(label="Dolar Variação Dia", command=GraficoVdiaDolar)
        self.MenuEstatistica.add_command(label="Euro Variação Dia", command=GraficoVdiaEURO)
        self.MenuEstatistica.add_command(label="Bitcoin Variação Dia", command=GraficoVdiaBTC)
        self.MenuEstatistica.add_separator()
        self.MenuEstatistica.add_command(label="Dolar Variação de Ontem", command=GraficoVdiaDolarontem)
        self.MenuEstatistica.add_command(label="Euro Variação de Ontem", command=GraficoVdiaEUROontem)
        self.MenuEstatistica.add_command(label="Bitcoin Variação de Ontem", command=GraficoVdiaBTContem)
        self.MenuEstatistica.add_separator()
        self.MenuEstatistica.add_command(label='Teste')
        self.menu.add_cascade(label="Administrador", menu=self.MenuAdministrador)
        self.MenuAdministrador.add_command(label="Tipo Investimento", command = self.JanelaTipoinvestimentoCadastro)
        self.MenuAdministrador.add_command(label="Cadastro Usuario",command = self.JanelaCadastro)
        self.menu.add_cascade(label="Sair", command=root.quit)


        #Texto de Bem vindo
        self.titulo = Label(self.janela, text='Seja Bem Vindo ao InfoInvest')
        self.titulo["font"] = ("Arial", "12", "bold")
        self.cambio = Label (self.janela, text = 'Cambio')
        self.cambio['font'] = ("Arial", "15", "bold")
        self.criptomoedas = Label (self.janela, text = 'Criptomoedas')
        self.criptomoedas['font'] = ("Arial", "15", "bold")

        #Informações da moeda com valor
        #Dolar
        self.dolaragora = get_dolar(self)
        self.Dolarhoje = Label(self.janela, text="DÓLAR : R${:.2f}".format(self.dolaragora))
        self.Dolarhoje["font"] = ("Arial", "15")
        #Euro
        self.euroagora = get_euro(self)
        self.Eurohoje = Label(self.janela, text="EURO : R${:.2f}".format(self.euroagora))
        self.Eurohoje["font"] = ("Arial", "15" )
        #Bitcoin
        self.btcagora = get_btc(self)
        self.BTChoje = Label(self.janela, text="BTC : R${:.2f}".format(self.btcagora))
        self.BTChoje["font"] = ("Arial", "15")

        self.titulo.grid(row=0, column=0, columnspan=2, padx=80, pady=10, sticky=N)
        self.cambio.grid(row=1, column=0, padx=10, pady=30)
        self.criptomoedas.grid(row=1, column=1)
        self.Dolarhoje.grid(row=2, column=0, pady=10)
        self.Eurohoje.grid(row=3, column=0, pady=10)
        self.BTChoje.grid(row=2, column=1, pady=10)

    def JanelaCadastro(self):

        self.janela = Tk()
        self.janela.wm_title("Cadastro de Cliente")
        self.janela.geometry('290x300+525+225')
        self.janela.resizable(False,False)

        # Dados texto
        self.txt_nome_usuario = StringVar()
        self.txt_email_usuario = StringVar()
        self.txt_cpf_usuario = StringVar()
        self.txt_renda_usuario = StringVar()
        self.txt_senha_usuario = StringVar()

        # Labels
        self.lbl_nome_usuario = Label(self.janela, text="Nome")
        self.lbl_email_usuario = Label(self.janela, text="Email")
        self.lbl_cpf_usuario = Label(self.janela, text="CPF")
        self.lbl_renda_usuario = Label(self.janela, text="Renda")
        self.lbl_senha_usuario = Label(self.janela, text="Senha")

        # Entries
        self.ent_nome_usuario = Entry(self.janela, textvariable=self.txt_nome_usuario)
        self.ent_email_usuario = Entry(self.janela, textvariable=self.txt_email_usuario)
        self.ent_cpf_usuario = Entry(self.janela, textvariable=self.txt_cpf_usuario)
        self.ent_renda_usuario = Entry(self.janela, textvariable=self.txt_renda_usuario)
        self.ent_senha_usuario = Entry(self.janela, textvariable=self.txt_senha_usuario)

        # Botões
        self.btn_inserir_usuario = Button(self.janela, text="Inserir",command=self.fcadastrar_usuario)
        self.btn_atualizar_usuario = Button(self.janela, text="Atualizar",command=self.fatualizar_usuario)
        self.btn_buscar_usuario = Button(self.janela, text="Buscar",command=self.fbuscar_usuario)
        self.btn_deletar_usuario = Button(self.janela, text="Deletar",command=self.fdeletar_usuario)
        self.btn_fechar_usuario = Button(self.janela, text="Fechar",command=self.janela.destroy)

        # Posicionando os Label na janela
        self.lbl_nome_usuario.grid(row=0, column=0)
        self.lbl_email_usuario.grid(row=1, column=0)
        self.lbl_cpf_usuario.grid(row=2, column=0)
        self.lbl_renda_usuario.grid(row=3, column=0)
        self.lbl_senha_usuario.grid(row=5, column=0)

        # Posicionando as entradas
        self.ent_nome_usuario.grid(row=0, column=1, padx=100, pady=50)
        self.ent_email_usuario.grid(row=1, column=1)
        self.ent_cpf_usuario.grid(row=2, column=1)
        self.ent_renda_usuario.grid(row=3, column=1)
        self.ent_senha_usuario.grid(row=5, column=1)

        # Posicionando os botoes
        self.btn_inserir_usuario.grid(row=6, column=0, columnspan=2)
        self.btn_atualizar_usuario.grid(row=7, column=0, columnspan=2)
        self.btn_buscar_usuario.grid(row=8, column=0, columnspan=2)
        self.btn_deletar_usuario.grid(row=9, column=0, columnspan=2)
        self.btn_fechar_usuario.grid(row=10, column=0, columnspan=2)

        # Ajustando o posicionamento
        x_pad = 5
        y_pad = 3
        width_entry = 30

        for child in self.janela.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky="WE", padx=x_pad, pady=y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)
            elif widget_class == "Scrollbar":
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)
            else:
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)

    def JanelaTipoinvestimentoCadastro(self):

        self.janela = Tk()
        self.janela.wm_title('Cadastro Tipo de Investimento')
        self.janela.geometry('420x250+535+300')
        self.janela.resizable(False, False)

        # Criando os Label
        self.titulo = Label(self.janela, text='Digite o tipo de investimento')
        self.titulo["font"] = ("Arial", "10", "bold")
        self.nome_investimento = Label(self.janela, text=' Nome do Tipo de Investimento ')
        self.lbl_codigo_tipoinvestimento = Label(self.janela,text='Codigo do Tipo de Investimento')

        # Dados texto
        self.txt_tipo_investimento = StringVar()
        self.txt_codigo_tipo_investimento = StringVar()

        # Entries
        self.ent_tipo_investimento = Entry(self.janela, textvariable=self.txt_tipo_investimento)
        self.ent_codigo_tipo_investimento = Entry(self.janela, textvariable=self.txt_codigo_tipo_investimento)

        # Lista de clientes
        self.list_tipo_investimento = Listbox(self.janela,width=30)
        self.scroll_tipo_investimento = Scrollbar(self.janela)

        # Criando os botoes
        self.btn_inserir_tipo_investimento = Button(self.janela, text='Inserir',command=self.fcadastrar_tinvestimento)
        self.btn_deletar_tipo_investimento = Button(self.janela, text='Deletar',command=self.fdeletar_tinvestimento)
        self.btn_buscar_tipo_investimento = Button(self.janela, text='Buscar',command=self.fselecionar_tinvestimento)
        self.btn_fechar_tipo_investimento = Button(self.janela, text="Fechar" , command=self.janela.destroy)


        # Posicionamento na janela
        self.titulo.grid(row=0, column=0, columnspan=2, padx=80, pady=10, sticky=N)
        self.nome_investimento.grid(row=1, column=0, pady=10)
        self.ent_tipo_investimento.grid(row=1,column=1 , pady=10)
        self.lbl_codigo_tipoinvestimento.grid(row=2, column=0, pady=10)
        self.ent_codigo_tipo_investimento.grid(row=2, column=1, pady=10)
        self.btn_inserir_tipo_investimento.grid(row=3, column=0)
        self.btn_buscar_tipo_investimento.grid(row=4, column=0)
        self.btn_deletar_tipo_investimento.grid(row=5, column=0)
        self.btn_fechar_tipo_investimento.grid(row=6, column=0)
        self.list_tipo_investimento.grid(row=3, column=1, rowspan=10)
        self.scroll_tipo_investimento.grid(row=3, column=2, rowspan=10)



        # Ajustando o posicionamento
        x_pad = 5
        y_pad = 3
        width_entry = 30

        for child in self.janela.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky="WE", padx=x_pad, pady=y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)
            elif widget_class == "Scrollbar":
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)
            else:
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)

    def JanelaCadastroInvestimento (self):

        self.janela = Tk()
        self.janela.wm_title("Cadastro de Investimento")
        self.janela.geometry('420x180+525+225')
        self.janela.resizable(False, False)

        # Dados texto
        self.txt_TipoInvestimento = StringVar()
        self.txt_DataAplicacao = StringVar()
        self.txt_DataVencimento = StringVar()
        self.txt_Saldo = StringVar()

        # Labels
        self.lbl_TipoInvestimento = Label(self.janela, text="Tipo de Investimento")
        self.lbl_DataAplicacao = Label(self.janela, text="Data da Aplicação")
        self.lbl_DataVencimento = Label(self.janela, text="Data de Vencimento")
        self.lbl_Saldo = Label(self.janela, text="Saldo")

        # Entries
        self.ent_TipoInvestimento = Entry(self.janela, textvariable=self.txt_TipoInvestimento)
        self.ent_DataAplicacao = Entry(self.janela, textvariable=self.txt_DataAplicacao)
        self.ent_DataVencimento = Entry(self.janela, textvariable=self.txt_DataVencimento)
        self.ent_Saldo = Entry(self.janela, textvariable=self.txt_Saldo)

        # Lista de clientes
        #self.list_clientes = Listbox(self.janela)
        #self.scroll_clientes = Scrollbar(self.janela)

        # Botões
        self.btn_inserir = Button(self.janela, text="Inserir")
        self.btn_fechar = Button(self.janela, text="Fechar", command=self.janela.destroy)

        # Posicionando os Label na janela
        self.lbl_TipoInvestimento.grid(row=0, column=0)
        self.lbl_DataAplicacao.grid(row=1, column=0)
        self.lbl_DataVencimento.grid(row=2, column=0)
        self.lbl_Saldo.grid(row=3, column=0)

        # Posicionando as entradas
        self.ent_TipoInvestimento.grid(row=0, column=1, padx=100, pady=50)
        self.ent_DataAplicacao.grid(row=1, column=1)
        self.ent_DataVencimento.grid(row=2, column=1)
        self.ent_Saldo.grid(row=3, column=1)

        # Posicionando os botoes
        self.btn_inserir.grid(row=6, column=0)
        self.btn_fechar.grid(row=6, column=1)
        #self.list_clientes.grid(row=0, column=2, rowspan=10)
        #self.scroll_clientes.grid(row=0, column=3, rowspan=10)

        # Ajustando o posicionamento
        x_pad = 5
        y_pad = 3
        width_entry = 30

        for child in self.janela.winfo_children():
            widget_class = child.__class__.__name__
            if widget_class == "Button":
                child.grid_configure(sticky="WE", padx=x_pad, pady=y_pad)
            elif widget_class == "Listbox":
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)
            elif widget_class == "Scrollbar":
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)
            else:
                child.grid_configure(sticky="NS", padx=x_pad, pady=y_pad)

        self.janela.mainloop()

    def JanelaTotalInvestido(self):
        self.janela = Tk()
        self.janela.wm_title("Investimentos Totais")
        self.janela.geometry('300x300+525+225')
        self.janela.resizable(False, False)

        # Labels texto
        self.lbl_total_investido = Label(self.janela, text="Total investido em produtos renda fixa:")
        self.lbl_tesouro = Label(self.janela, text="Tesouro Direto:")
        self.lbl_cdb = Label(self.janela, text="CDB:")
        self.lbl_rdb = Label(self.janela, text="RDB:")
        self.lbl_lci = Label(self.janela, text="LCI:")
        self.lbl_lca = Label(self.janela, text="LCA:")
        self.lbl_lc = Label(self.janela, text="LC:")
        self.lbl_poupanca = Label(self.janela, text="Poupança:")

        # Labels valores
        total01 = float(bd_total_investido(1))
        total02 = float(bd_total_investido(2))
        total03 = float(bd_total_investido(3))
        total04 = float(bd_total_investido(4))
        total05 = float(bd_total_investido(5))
        total06 = float(bd_total_investido(6))
        total07 = float(bd_total_investido(7))
        self.lbl_tesouro_valor = Label(self.janela, text="R${:.2f}".format(total01))
        self.lbl_cdb_valor = Label(self.janela, text="R${:.2f}".format(total02))
        self.lbl_rdb_valor = Label(self.janela, text="R${:.2f}".format(total03))
        self.lbl_lci_valor = Label(self.janela, text="R${:.2f}".format(total04))
        self.lbl_lca_valor = Label(self.janela, text="R${:.2f}".format(total05))
        self.lbl_lc_valor = Label(self.janela, text="R${:.2f}".format(total06))
        self.lbl_poupanca_valor = Label(self.janela, text="R${:.2f}".format(total07))

        # Botões
        self.btn_fechar = Button(self.janela, text="Fechar", command=self.janela.destroy)

        # Posicionando os Label na janela
        # renda fixa posição
        self.lbl_total_investido.grid(row=0, column=0)
        self.lbl_tesouro.grid(row=1, column=0)
        self.lbl_tesouro_valor.grid(row=1, column=1)
        self.lbl_cdb.grid(row=2, column=0)
        self.lbl_cdb_valor.grid(row=2, column=1)
        self.lbl_rdb.grid(row=3, column=0)
        self.lbl_rdb_valor.grid(row=3, column=1)
        self.lbl_lci.grid(row=4, column=0)
        self.lbl_lci_valor.grid(row=4, column=1)
        self.lbl_lca.grid(row=5, column=0)
        self.lbl_lca_valor.grid(row=5, column=1)
        self.lbl_lc.grid(row=6, column=0)
        self.lbl_lc_valor.grid(row=6, column=1)
        self.lbl_poupanca.grid(row=7, column=0)
        self.lbl_poupanca_valor.grid(row=7, column=1)

        # Posicionando os botoes
        self.btn_fechar.grid(row=13, column=0, columnspan=2, pady=20)

    #PARTE LOGICA DO SISTEMA PARA FAZER O BOTOES FUNCIONAR E OUTRAS REGRAS DE NEGOCIO
    def fcadastrar_tinvestimento(self):
        #recebendo oque o ususario digitou e cadastrando com a função do BD
        getnome_tinvestimento = self.ent_tipo_investimento.get()
        cadastrar_tipo_investimento(getnome_tinvestimento)
        # zerando o listbox e depois listando ele atualizado
        self.list_tipo_investimento.delete(0,END)
        self.fselecionar_tinvestimento()

    def fdeletar_tinvestimento(self):
        #recebendo o codigo digitado pelo usuario
        getcodigo_tinvestimento = self.ent_codigo_tipo_investimento.get()
        #deletar usando a função do bd
        deletar_tipo_investimento(getcodigo_tinvestimento)
        #zerar a listbox
        self.list_tipo_investimento.delete(0,END)
        #usar a função que busca todos os tipos de investimento e add no listbox
        self.fselecionar_tinvestimento()

    def fselecionar_tinvestimento(self):
        #recebendo uma lista pela função do BD e incrementando a lista
        tipoperfil = selecionar_todos_tipo_investimento()
        for t in tipoperfil:
            self.list_tipo_investimento.insert(END,t)

    def fcadastrar_usuario(self):
        #coletar as informações digitadas pelo usuario
        getnome = self.ent_nome_usuario.get()
        getemail = self.ent_email_usuario.get()
        getcpf = self.ent_cpf_usuario.get()
        getrenda = self.ent_renda_usuario.get()
        getsenha = self.ent_senha_usuario.get()
        #cadastrar usando a função do BD
        cadastrar_usuario(getcpf,getsenha,getnome,getemail,getrenda)

    def fatualizar_usuario(self):
        #coletar informações digitadas pelo usuario
        getnome = self.ent_nome_usuario.get()
        getemail = self.ent_email_usuario.get()
        getcpf = self.ent_cpf_usuario.get()
        getrenda = self.ent_renda_usuario.get()
        getsenha = self.ent_senha_usuario.get()
        #alterar usando a função do BD
        alterar_usuario(getcpf,getsenha,getnome,getemail,getrenda)

    def fdeletar_usuario(self):
        getcpf = self.ent_cpf_usuario.get()
        deletar_usuario(getcpf)

    def fbuscar_usuario(self):
        #coletadndo o cpf digitado pelo usuario para realizar a busca
        getcpf = self.ent_cpf_usuario.get()
        getusuario = selecionar_usuario(getcpf)
        #coletando valores padrao e alterando os valores do entry
        nome = getusuario['Nome']
        email = getusuario['Email']
        cpf = getusuario['CPF']
        renda = getusuario['Renda']
        senha = getusuario['Senha']
        #limpar valores digitado no entry
        self.ent_nome_usuario.delete(0,END)
        self.ent_email_usuario.delete(0,END)
        self.ent_renda_usuario.delete(0,END)
        self.ent_senha_usuario.delete(0,END)
        #inserir novos valores do entry
        self.ent_nome_usuario.insert(0,nome)
        self.ent_email_usuario.insert(0,email)
        self.ent_renda_usuario.insert(0,renda)
        self.ent_senha_usuario.insert(0,senha)








root = Tk()
Sistema(root)
root.geometry('250x220+525+225')
root.resizable(False,False)
root.mainloop()



