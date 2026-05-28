import customtkinter as ctk
from PIL import Image  # Substituímos o PhotoImage do tkinter pelo Image do Pillow
from tkinter import messagebox
import sqlite3


class BackEnd():
    def conecta_db(self): 
        self.conexao = sqlite3.connect("Banco_de_dados_sistema_users.db")
        # Ponto de entrada para executar comandos SQL
        self.cursor = self.conexao.cursor()
        print("Banco de dados conectado com sucesso!")
        
    def desconecta_db(self):
        self.conexao.close()
        print("Banco de dados desconectado com sucesso!")

    def criar_tabela(self):
        self.conecta_db()
        self.cursor.execute("""

            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL, 
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirma_Senha TEXT NOT NULL
            );""")
        self.conexao.commit()
        print("Tabela criada com sucesso!")
        self.desconecta_db()

    def cadastrar_usuario(self):
        # .get() é o método utilizado para pegar o valor digitado pelo usuário na entry
        self.user_name_cadastro = self.user_name_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.senha_cadastro = self.cadastro_senha_entry.get()
        self.confirma_senha_cadastro = self.confirma_senha_cadastro_entry.get()

        self.conecta_db()
        # Aqui você pode adicionar validações para os campos, como verificar se as senhas coincidem, se o email é válido, etc.
        self.cursor.execute("""
            INSERT INTO usuarios (Username, Email, Senha, Confirma_Senha) 
            VALUES (?,?,?,?)""", (self.user_name_cadastro, self.email_cadastro, self.senha_cadastro, self.confirma_senha_cadastro))
        
        try: 
            if (self.user_name_cadastro == "" or self.email_cadastro == "" or self.senha_cadastro == "" or self.confirma_senha_cadastro == ""): 
                messagebox.showerror(title = "Sistema de Login", message = "Por favor, preencha todos os campos!")
            elif (len(self.user_name_cadastro) < 4): 
                messagebox.showerror(title = "Sistema de Login", message = "O nome de usuário deve ser de pelo menos 4 caractéres!")
            elif (self.senha_cadastro != self.confirma_senha_cadastro):
                messagebox.showerror(title = "Sistema de Login", message = "ERRO!!! \nAs senhas colocadas não são iguais. Coloque senhas iguais!")
            elif (len(self.senha_cadastro) < 4): 
                messagebox.showerror(title = "Sistema de Login", message = "A senha deve ser de pelo menos 4 caractéres!")
            else:
                self.conexao.commit()
                messagebox.showinfo(title = "Sistema de Login", message = f"Parabéns! {self.user_name_cadastro}, os seus dados foram cadastrados com sucesso!")
                self.desconecta_db()
                self.limpa_entry_cadastro()
        except: 
            messagebox.showerror(title = "Sistema de Login", message = "Erro no Processamento do seu cadastro! Por favor tente novamente!")
            self.desconecta_db()

    def login_verify(self):
        self.user_name_login = self.user_name_login_entry.get()
        self.senha_login = self.user_name_senha_entry.get()
        
        self.conecta_db()
        # Aqui você pode adicionar validações para os campos, como verificar se o nome de usuário e senha estão corretos, etc.
        self.cursor.execute("""
            SELECT * FROM usuarios WHERE (Username = ? AND Senha = ?)""", (self.user_name_login, self.senha_login))
        self.verifica_dados = self.cursor.fetchone() # Percorrendo os dados do banco de dados para verificar se o nome de usuário e senha estão corretos

        try: 
            if (self.user_name_login == "" or self.senha_login == ""):
                messagebox.showerror(title = "Sistema de Login", message = "Por favor, preencha todos os campos!")
            elif (self.user_name_login in self.verifica_dados and self.senha_login in self.verifica_dados): 
                messagebox.showinfo(title = "Sistema de Login", message = f"Parabéns {self.user_name_login}\nLogin feito com sucesso!")
                self.desconecta_db()
                self.limpa_entry_login()
        except: 
            messagebox.showerror(title = "Sistema de Login", message = "ERRO!!! \nDados não encontrados em nosso sistema! \nPor favor verifique seus dados ou cadastre-se no nosso sistema!")
            self.desconecta_db()

        
class App(ctk.CTk, BackEnd):

    
    # O erro era não ter chamado a função self.criar_tabela() dentro do __init__, o que fazia com que a tabela não fosse criada no banco de dados, e consequentemente, quando tentávamos cadastrar um usuário, dava erro de "no such table: usuarios"
    def __init__(self):
        super().__init__()
        self.configuracao_janela_principal()
        self.tela_de_login()
        #self.tela_de_cadastro()
        self.criar_tabela()

    # Configurando a janela principal
    def configuracao_janela_principal(self):
        self.title("Sistema de Login")
        self.geometry("700x400")
        self.resizable(False, False)

    def tela_de_login(self):
        # removendo a tela de cadastro
        
        # 1. Abrimos a imagem usando o Pillow
        imagem_pillow = Image.open("logi-img.png")

        # 2. Envolvemos ela no CTkImage do CustomTkinter e definimos o tamanho (ex: 200x200)
        self.img = ctk.CTkImage(light_image=imagem_pillow, size=(320, 380))

        # 3. Passamos para o CTkLabel (obs: o correto para sem texto é text="")
        self.lb_img = ctk.CTkLabel(self, text="", image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10)
        # Título da tela de login
        self.title = ctk.CTkLabel(self, text="Faça o seu login ou cadastre-se \nna nossa plataforma para acessar\n os nossos serviços", font=("Century Gothic bold", 14))
        self.title.grid(row=0, column=0, pady= 10, padx = 10)

        #formulário tela de login
        self.frame_login = ctk.CTkFrame(self, width= 350, height= 380)
        self.frame_login.place(x=350, y= 10)

        # Colocando widgets dentro do frame de login
        self.lb_title = ctk.CTkLabel(self.frame_login, text="Faça o seu login", font = ("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        self.user_name_login_entry = ctk.CTkEntry(self.frame_login, width = 300, placeholder_text="Seu nome de usuário", font = ("Century Gothic bold", 16), corner_radius=15, border_color = "#008")
        self.user_name_login_entry.grid(row=1, column=0, padx=10, pady=10)

        self.user_name_senha_entry = ctk.CTkEntry(self.frame_login, width = 300, placeholder_text="Sua senha", font = ("Century Gothic bold", 16), corner_radius=15, border_color = "#008", show= "*")
        self.user_name_senha_entry.grid(row=2, column=0, padx=10, pady=10)

        self.user_name_ver_senha_entry = ctk.CTkCheckBox(self.frame_login, text = "Clique para ver a senha", font = ("Century Gothic bold", 12), corner_radius=20)
        self.user_name_ver_senha_entry.grid(row=3, column=0, padx=10, pady=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width = 300, text = "Fazer login".upper(), font = ("Century Gothic bold", 16), corner_radius=15, fg_color = "#008", command = self.login_verify)
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)

        self.sap = ctk.CTkLabel(self.frame_login, text = "Se não tem uma conta, clique no botão abaixo para se cadastrar", font = ("Century Gothic", 10))
        self.sap.grid(row=5, column=0, padx=10, pady=10)

        self.btn_cadastrar = ctk.CTkButton(self.frame_login, width = 300, text = "Fazer cadastro".upper(), font = ("Century Gothic bold", 16), corner_radius=15, fg_color = "green", hover_color = "#050", command = self.tela_de_cadastro)
        self.btn_cadastrar.grid(row=6, column=0, padx=10, pady=10)

    def tela_de_cadastro(self):
        # Remover o formulário de login
        self.frame_login.place_forget()

        # Frame de formulário de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width= 350, height= 380)
        self.frame_cadastro.place(x=350, y= 10)

        #Criando o título da tela de cadastro
        self.lb_title = ctk.CTkLabel(self.frame_cadastro, text="Faça o seu cadastro", font = ("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=5)

        # Criar os widgets para a tela de cadastro
        self.user_name_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width = 300, placeholder_text="Nome de usuário", font = ("Century Gothic bold", 16), corner_radius=15, border_color = "#008")
        self.user_name_cadastro_entry.grid(row=1, column=0, padx=10, pady=5)


        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width = 300, placeholder_text="Email de usuário", font = ("Century Gothic bold", 16), corner_radius=15, border_color = "#008")
        self.email_cadastro_entry.grid(row=2, column=0, padx=10, pady=5)

        self.cadastro_senha_entry = ctk.CTkEntry(self.frame_cadastro, width = 300, placeholder_text="Senha do usuário", font = ("Century Gothic bold", 16), corner_radius=15, border_color = "#008", show= "*")
        self.cadastro_senha_entry.grid(row=3, column=0, padx=10, pady=5)

        self.confirma_senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width = 300, placeholder_text="Confirme sua senha", font = ("Century Gothic bold", 16), corner_radius=15, border_color = "#008", show= "*")
        self.confirma_senha_cadastro_entry.grid(row=4, column=0, padx=10, pady=5)

        self.user_name_ver_senha_entry = ctk.CTkCheckBox(self.frame_cadastro, text = "Clique para ver a senha", font = ("Century Gothic bold", 12), corner_radius=20)
        self.user_name_ver_senha_entry.grid(row=5, column=0, padx=10, pady=5)

        self.btn_cadastrar = ctk.CTkButton(self.frame_cadastro, width = 300, text = "Fazer cadastro".upper(), font = ("Century Gothic bold", 16), corner_radius=15, fg_color = "green", hover_color = "#050", command = self.cadastrar_usuario)
        self.btn_cadastrar.grid(row=6, column=0, padx=10, pady=5)

        self.btn_voltar_login = ctk.CTkButton(self.frame_cadastro, width= 300, text = "Voltar para a tela de login".upper(), font = ("Century Gothic bold", 14), corner_radius = 15, fg_color = "#444", hover_color = "#333", command = self.tela_de_login)
        self.btn_voltar_login.grid(row=7, column=0, padx=10, pady=5)
    
    def limpa_entry_cadastro(self): 
        self.user_name_cadastro_entry.delete(0, ctk.END)
        self.cadastro_senha_entry.delete(0, ctk.END)
        self.email_cadastro_entry.delete(0, ctk.END)
        self.confirma_senha_cadastro_entry.delete(0, ctk.END)

    def limpa_entry_login(self):
        self.user_name_login_entry.delete(0, ctk.END)
        self.user_name_senha_entry.delete(0, ctk.END)

        

if __name__ == "__main__":
    app = App()
    app.mainloop()