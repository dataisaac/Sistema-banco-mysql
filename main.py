import tkinter as tk
from database import conectar

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_tel.get()

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO clientes (nome,email,telefone) VALUES (%s,%s,%s)"
    valores = (nome,email,telefone)

    cursor.execute(sql,valores)

    conexao.commit()
    conexao.close()

    print("Cliente cadastrado!")

janela = tk.Tk()
janela.title("Cadastro de Clientes")

tk.Label(janela,text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela,text="Email").pack()
entry_email = tk.Entry(janela)
entry_email.pack()

tk.Label(janela,text="Telefone").pack()
entry_tel = tk.Entry(janela)
entry_tel.pack()

tk.Button(janela,text="Cadastrar",command=cadastrar).pack()

janela.mainloop()