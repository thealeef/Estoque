from tkinter import *
from time import *
from functools import partial
from tkinter.messagebox import *
import sqlite3 
from tkinter import ttk
from datetime import *

def Login():

    def Chama_Validando():
        Validando(usuario, senha)

    def Validando(usuario, senha):

        usuario = usuario.get()
        senha = senha.get()

        banco = sqlite3.connect('BD.db')
        cursor = banco.cursor() 

        #AQUI CONSULTAMOS USUÁRIO NO BANCO DE DADOS E VALIDAMOS COM O QUE ELE DIGITOU

        cursor.execute('SELECT Usuario FROM Usuarios')

        coluna_usuario = cursor.fetchall()

        for n in coluna_usuario:

            lista_usuarios = str(n)[2:-3]

            if usuario == lista_usuarios:
                
                banco = sqlite3.connect('BD.db')
                cursor = banco.cursor() 

                cursor.execute('SELECT Senha FROM Usuarios')

                coluna_senhas = cursor.fetchall()

                for x in coluna_senhas:

                    lista_senha = str(x)[2:-3]

                    if senha == lista_senha:                 

                        showinfo(title=" ", message="Autenticado")

                        app.destroy()
                        
                        Painel_Controle() 

                        break

                    else:
                        showinfo(title=" ", message="Erro")
                        break

                break

            else:
                showinfo(title=" ", message="Erro")
                break

    def Esqueceu():
       
        app.destroy()
        Esqueceu_Senha()

    def Enter(event):

         Chama_Validando()

    app = Tk()
    altura = 175
    largura = 325
    app.resizable(0, 0)

    largura_tela = app.winfo_screenwidth()
    altura_tela =  app.winfo_screenmmheight()

    posix = largura_tela/3 
    posiy = altura_tela/3 + 200

    app.geometry("%dx%d+%d+%d" % (largura, altura, posix,posiy))
    app.title('ESTOQUE')

    app.bind("<Return>", Enter)

    titulo_label = Label(
        app,
        bg='gray18',
        fg='white',
        width=46, height=1,
        text='Bem Vindo!')
    titulo_label.place(x=0, y=5)
 
    usuario_label = Label(
        width=16, height=1,
        text='Usuário')
    usuario_label.place(x=35, y=42)

    usuario = StringVar()
    usuario_box = Entry(textvariable=usuario)
    usuario_box.place(x=145, y=43)

    senha_label = Label(
        text="Senha",
        width=16, height=1)
    senha_label.place(x=27, y=65)

    senha = StringVar()
    senha_box = Entry(
        show='*', 
        textvariable=senha,)
    senha_box.place(x=145, y=66)

    entrar_botao = Button(
        app,
        text="Entrar",
        width=10,
        height=1,
        command= Chama_Validando)

    entrar_botao.place(x=120, y=100)

    esqueci_botao = Button(
        text="Esqueci a Senha",
        width=12,
        height=0,
        command= Esqueceu)
    esqueci_botao.place(x=10, y=140)

    sair_botao = Button(
        app,
        text="Sair",
        width=10,
        height=0,
        command= app.destroy)
    sair_botao.place(x=235, y=140)

    app.mainloop()

def Esqueceu_Senha():

    app = Tk()
    altura = 175
    largura = 325
    app.resizable(0, 0)

    largura_tela = app.winfo_screenwidth()
    altura_tela =  app.winfo_screenmmheight()

    posix = largura_tela/3 
    posiy = altura_tela/3 + 200

    app.geometry("%dx%d+%d+%d" % (largura, altura, posix,posiy))
    app.title('ESTOQUE')

    email_label = Label(
        width=16, height=1,
        text='E-mail')
    email_label.place(x=37, y=60)

    email = StringVar()
    email_box = Entry(textvariable=email)
    email_box.place(x=145, y=60, relheight=0.1, relwidth=0.5)

    enviar_botao = Button(
        app,
        text="Enviar",
        width=10,
        height=1)
    enviar_botao.place(x=120, y=100)
   
    app.mainloop()

def Painel_Controle():

    def Chama_Cadastro():
        app.destroy()
        Cadastro()

    def Chama_Itens():
        app.destroy()
        Cadastro_Itens()

    app = Tk()
    altura = 700
    largura = 1000
    app.resizable(0, 0)

    largura_tela = app.winfo_screenwidth()
    altura_tela =  app.winfo_screenmmheight()

    posix = largura_tela/3
    posiy = altura_tela/3

    app.geometry("%dx%d+%d+%d" % (largura, altura, posix,posiy))
    app.title('ESTOQUE 0.1')
    
    cadastrar_botao = Button(
        app,
        text="Cadastrar Usuários",
        width=17,
        height=1,
        command= Chama_Cadastro)
    cadastrar_botao.place(x=120, y=100)

    itens_botao = Button(
        app,
        text="Cadastrar Itens",
        width=17,
        height=1,
        command= Chama_Itens)
    itens_botao.place(x=260, y=100)

    app.mainloop()

def Cadastro():

    def Banco_Dados(nome, usuario, senha, con_senha, email):

        nome = nome.get()
        usuario = usuario.get()
        senha = senha.get()
        con_senha = con_senha.get()
        email = email.get()

        if senha == con_senha:

            banco = sqlite3.connect('BD.db')

            cursor = banco.cursor()    

            cursor.execute("CREATE TABLE IF NOT EXISTS Usuarios (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Nome VARCHAR, Usuario VARCHAR, Senha VARCHAR, Email VARCHAR)")  

            lista = [(nome, usuario, senha, email)]    
            
            cursor.executemany("INSERT INTO Usuarios (Nome, Usuario, Senha, Email) VALUES (?, ?, ?, ?)", lista)

            banco.commit()

            showinfo(title=" ", message="Gravado" )

            banco.close()

            app.destroy()

        else:

            erro_label = Label(
                text="**",
                foreground='red',
                width=2, height=1)
            erro_label.place(x=297, y=120)

            erro2_label = Label(
                text="**",
                foreground='red',
                width=2, height=1)
            erro2_label.place(x=297, y=145)

    def Chama_Banco():

        Banco_Dados(nome, usuario, senha, con_senha, email)

    def Chama_Painel():

        app.destroy()
        Painel_Controle()
        
    app = Tk()

    altura = 500
    largura = 325
    app.resizable(0, 0)

    largura_tela = app.winfo_screenwidth()
    altura_tela =  app.winfo_screenmmheight()

    posix = largura_tela/3 + 100
    posiy = altura_tela/3 + 100

    app.geometry("%dx%d+%d+%d" % (largura, altura, posix,posiy))
    app.title('ESTOQUE')

    titulo_label = Label(
        app,
        bg='gray18',
        fg='white',
        width=46, height=1,
        text='Cadastro')
    titulo_label.place(x=0, y=5)

    nome_label = Label(
        width=16, height=1,
        text='Nome Completo')
    nome_label.place(x=18, y=67)

    nome = StringVar()
    nome_box = Entry(textvariable = nome)
    nome_box.place(x=135, y=68, relheight=0.04, relwidth=0.5)

    usuario_label = Label(
        width=16, height=1,
        text='Usuário')
    usuario_label.place(x=18, y=94)

    usuario = StringVar()
    usuario_box = Entry(textvariable = usuario)
    usuario_box.place(x=135, y=95, relheight=0.04, relwidth=0.5)

    senha_label = Label(
        text="Senha",
        width=16, height=1)
    senha_label.place(x=17, y=120)

    senha = StringVar()
    senha_box = Entry(
        show='*', 
        textvariable = senha)
    senha_box.place(x=135, y=121, relheight=0.04, relwidth=0.5)

    con_senha_label = Label(
        text="Confirmar Senha",
        width=16, height=1)
    con_senha_label.place(x=17, y=145)

    con_senha = StringVar()
    con_senha_box = Entry(
        show='*', 
        textvariable = con_senha)
    con_senha_box.place(x=135, y=146, relheight=0.04, relwidth=0.5)

    email_label = Label(
        width=16, height=1,
        text='E-Mail')
    email_label.place(x=18, y=170)

    email = StringVar()
    email_box = Entry(textvariable = email)
    email_box.place(x=135, y=171, relheight=0.04, relwidth=0.5)

    nascimento_label = Label(
        width=16, height=1,
        text='Data de Nascimento')
    nascimento_label.place(x=18, y=195)

    nascimento = StringVar()
    nascimento_box = Entry(textvariable = nascimento)
    nascimento_box.place(x=135, y=196, relheight=0.04, relwidth=0.5)

    sexo_label = Label(
        width=16, height=1,
        text='Sexo')
    sexo_label.place(x=18, y=220)

    sexo_combobox = ttk.Combobox( values=[
        'MASCULINO',
        'FEMININO'])
    sexo_combobox.place(x=135, y=221, relheight=0.04, relwidth=0.5)

    gravar_botao = Button(
        app,
        text="Gravar",
        width=17,
        height=1,
        command= Chama_Banco)
    gravar_botao.place(x=185, y=465)

    voltar_botao = Button(
        app,
        text="Voltar",
        width=17,
        height=1,
        command= Chama_Painel)
    voltar_botao.place(x=10, y=465)

    app.mainloop()

def Cadastro_Itens():

    def Chama_Painel():
        app.destroy()
        Painel_Controle()

    def Chama_Itens():
        Banco_Dados_itens(nome_item, valor_item, quantidade_item)    

    def Banco_Dados_itens(nome_item, valor_item, quantidade_item):

        nome_item = nome_item.get()
        valor_item = valor_item.get()
        quantidade_item = quantidade_item.get()

        data = date.today()
        data_string = data.strftime("%d/%m/%Y")

        
        banco = sqlite3.connect('BD.db')

        cursor = banco.cursor()    

        cursor.execute("CREATE TABLE IF NOT EXISTS Itens (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Nome VARCHAR, Valor VARCHAR, Quantidade INTEGER, Data_Inserido VARCHAR)")  

        lista = [(nome_item, valor_item , quantidade_item, data_string)]    
            
        cursor.executemany("INSERT INTO Itens (Nome, Valor, Quantidade, Data_Inserido) VALUES (?, ?, ?, ?)", lista)

        banco.commit()

        showinfo(title=" ", message="Gravado" )

        Atualiza_BD()

        banco.close()

    def Atualiza_BD():

        banco = sqlite3.connect('BD.db')
        cursor = banco.cursor() 

        cursor.execute('SELECT * FROM Itens')

        bd_itens = cursor.fetchall()

        for x in bd_itens:
            lista_produtos.delete(*lista_produtos.get_children())

        for n in bd_itens:        
    
            lista_produtos.insert('', 'end', values=n)

        lista_produtos.place(x=10, y=200, height = 230, width= 305)

    app = Tk()

    altura = 500
    largura = 325
    app.resizable(0, 0)

    largura_tela = app.winfo_screenwidth()
    altura_tela =  app.winfo_screenmmheight()

    posix = largura_tela/3 + 100
    posiy = altura_tela/3 + 100

    app.geometry("%dx%d+%d+%d" % (largura, altura, posix,posiy))
    app.title('ESTOQUE')

    titulo_label = Label(
        app,
        bg='gray18',
        fg='white',
        width=46, height=1,
        text='Itens')
    titulo_label.place(x=0, y=5)

    nome_label = Label(
        width=16, height=1,
        text='Nome Do Item')
    nome_label.place(x=18, y=67)

    nome_item = StringVar()
    nome_box = Entry(textvariable = nome_item)
    nome_box.place(x=135, y=68, relheight=0.04, relwidth=0.5)

    valor_label = Label(
        width=16, height=1,
        text='Valor')
    valor_label.place(x=18, y=94)

    valor_item = StringVar()
    valor_box = Entry(textvariable = valor_item)
    valor_box.place(x=135, y=95, relheight=0.04, relwidth=0.5)

    quantidade_label = Label(
        text="Quantidade",
        width=16, height=1)
    quantidade_label.place(x=17, y=120)

    quantidade_item = StringVar()
    senha_box = Entry(textvariable = quantidade_item)
    senha_box.place(x=135, y=121, relheight=0.04, relwidth=0.5)

    gravar_botao = Button(
        app,
        text="Gravar",
        width=17,
        height=1,
        command= Chama_Itens)
    gravar_botao.place(x=185, y=465)

    voltar_botao = Button(
        app,
        text="Voltar",
        width=17,
        height=1,
        command= Chama_Painel)
    voltar_botao.place(x=10, y=465)

    lista_produtos = ttk.Treeview(app, columns=('ID', 'Nome', 'Valor', 'Quantidade', 'Data Inserida'), show='headings')

    lista_produtos.heading('ID', text='Id')
    lista_produtos.heading('Nome', text='Nome')
    lista_produtos.heading('Valor', text='Valor')
    lista_produtos.heading('Quantidade', text='Quantidade')
    lista_produtos.heading('Data Inserida', text='Data Inserida')

    # TAMANHO DAS COLUNAS

    lista_produtos.column('ID', minwidth=0, width=10)
    lista_produtos.column('Nome', minwidth=0, width=40)
    lista_produtos.column('Valor', minwidth=0, width=20)
    lista_produtos.column('Quantidade', minwidth=0, width=50)
    lista_produtos.column('Data Inserida', minwidth=0, width=50)

    banco = sqlite3.connect('BD.db')
    cursor = banco.cursor() 

    cursor.execute('SELECT * FROM Itens')

    bd_itens = cursor.fetchall()

    for n in bd_itens:        
    
        lista_produtos.insert('', 'end', values=n)

    lista_produtos.place(x=10, y=200, height = 230, width= 305)

    
    app.mainloop()

    


Cadastro_Itens()