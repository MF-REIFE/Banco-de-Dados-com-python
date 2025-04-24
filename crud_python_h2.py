import jaydebeapi

class Database:
    def __init__(self, db_name="testdb"):
        self.h2_jar = "h2/bin/h2-1.4.200.jar"
        self.conn = jaydebeapi.connect("org.h2.Driver", f"jdbc:h2:mem: {db_name}", ["sa", ""], self.h2_jar)
        self.cursor = self.conn.cursor()
        print(f"Banco de Dados {db_name} conectado!")

    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Conexão fechada. ")

class Cliente:
    def __init__(self, database):
        self.db = database
        self.db.execute("CREATE TABLE IF NOT EXISTS clientes (id INT PRIMARY KEY, nome VARCHAR(100)); ")

    def inserir(self, id, nome):
        self.db.execute("INSERT INTO clientes VALUES (?,?);", (id, nome))

    def buscar_todos(self):
        self.db.execute("SELECT * FROM clientes;")
        return self.db.fetchall()

    def atualizar(self, id, novo_nome):
        self.db.execute("UPDATE clientes SET nome=? WHERE id=?;", (novo_nome, id))

    def deletar(self, id):
        self.db.execute("DELETE FROM clientes WHERE id=?", (id,))

# Função de interação com o usuário (fora da classe Cliente)
