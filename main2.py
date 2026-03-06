import tkinter as tk
from database import conectar

def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_tel.get()

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "Insert into clientes (nome,email,telefone)" \
    "values (%s,%s,%s)"
    valores = (nome,email,telefone)

    cursor.execute(sql,valores)

    conexao.commit()
    conexao.close()

    print("Cliente cadastrado!")

janela = tk.Tk()
janela.title("Cadastro de Clientes")

tk.Label(janela,
         text="Nome",
         font=("Arial", 16, "bold"),
         fg="navy",
         bg="#eef",
         padx=8, pady=4).pack(padx=10, pady=5, anchor="w")
entry_nome = tk.Entry(janela, font=("Arial", 16, "bold"), width=30)
entry_nome.pack(padx=10, pady=5)

tk.Label(janela,
         text="Email",
         font=("Arial", 16, "bold"),
         fg="navy",
         bg="#eef",
         padx=8, pady=4).pack(padx=10, pady=5, anchor="w")
entry_email = tk.Entry(janela, font=("Arial", 16, "bold"), width=30)
entry_email.pack(padx=10, pady=5)

tk.Label(janela,
         text="Telefone",
         font=("Arial", 16, "bold"),
         fg="navy",
         bg="#eef",
         padx=8, pady=4).pack(padx=10, pady=5, anchor="w")
entry_tel = tk.Entry(janela, font=("Arial", 16, "bold"), width=30)
entry_tel.pack(padx=10, pady=5)

tk.Button(janela,
          text="Cadastrar",
          font=("Arial", 16, "bold"),
          bg="green",
          fg="white",
          padx=10, pady=5,
          command=cadastrar).pack(padx=10, pady=20)

janela.configure(bg="#eef")  # Cor de fundo da janela


janela.mainloop()


# …resto dos widgets…