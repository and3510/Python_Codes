import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='cadastro',
)

cursor = conexao.cursor()

# -------------------------
name = str(input("Digite o nome: "))
nascimento = str(input("Digite o data de nascimento <YYYY-mm-dd>: "))
profissao = str(input("Digite a Profissão: "))
sexo = str(input("Digite (M ou F): "))
peso = float(input("Digite o peso: "))
altura = float(input("Digite o altura: "))
nacionalidade = str(input("Digite a Nacionalidade: "))
# -------------------------

comando = f'insert into cadastro.pessoas (name, profissao, nascimento, sexo, peso, altura, nacionalidade) values ("{name}", "{profissao}", "{nascimento}", "{sexo}", {peso}, {altura}, "{nacionalidade}")'
cursor.execute(comando)
conexao.commit()
print("Commit bem Sucedido!")

cursor.close()
conexao.close()