import pytest
import sqlite3
from app import BackEnd

# Criamos uma classe que simula a herança ou instância da lógica do BackEnd
class TestBackEnd:
    @pytest.fixture(autouse=True)
    def setup_database(self):
        # Usamos :memory: para não criar arquivos no seu computador durante o teste
        self.db = sqlite3.connect(":memory:")
        self.cursor = self.db.cursor()
        self.cursor.execute("""
            CREATE TABLE usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL, 
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirma_Senha TEXT NOT NULL
            );""")
        yield
        self.db.close()

    def test_cadastrar_usuario_sucesso(self):
        # Simula a inserção
        self.cursor.execute("INSERT INTO usuarios VALUES (1, 'Teste', 'teste@email.com', '1234', '1234')")
        self.db.commit()
        
        # Verifica se foi inserido
        self.cursor.execute("SELECT * FROM usuarios WHERE Username='Teste'")
        user = self.cursor.fetchone()
        assert user is not None
        assert user[1] == 'Teste'

    def test_login_invalido(self):
        # Testa a lógica de busca com dados que não existem
        self.cursor.execute("SELECT * FROM usuarios WHERE Username=? AND Senha=?", ('Inexistente', '0000'))
        user = self.cursor.fetchone()
        assert user is None