import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='cadastro',
)

cursor = conexao.cursor()

# -------------------------
name = "Luiz"
nascimento = "2005-07-20"
profissao = "TI"
sexo = "M"
peso = 75.6
altura = 2.0
nacionalidade = "Brazil"
# -------------------------

comando = f'insert into cadastro.pessoas (name, profissao, nascimento, sexo, peso, altura, nacionalidade) values ("{name}", "{profissao}", "{nascimento}", "{sexo}", {peso}, {altura}, "{nacionalidade}")'
cursor.execute(comando)
conexao.commit()
print("Commit bem Sucedido!")

cursor.close()
conexao.close()