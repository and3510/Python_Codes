import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='cadastro',
)
cursor = conexao.cursor()
name = "Luiz"
nascimento = "2005-07-20"
sexo = "M"
peso = 75.6
altura = 2.0
nacionalidade = "Brazil"

comando = f'insert into cadastro.pessoas (name, nascimento, sexo, peso, altura, nacionalidade) values ("{name}", "{nascimento}", "{sexo}", {peso}, {altura}, "{nacionalidade}")'
cursor.execute(comando)
conexao.commit()
# CRUD

cursor.close()
conexao.close()