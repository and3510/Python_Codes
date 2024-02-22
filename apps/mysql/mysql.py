import mysql.connector

mydb = mysql.connector.connect(host="dbmyql01",database="cadastro",user="root",password="12345") 

if mydb.is_connected():
  db_info = mydb.get_server_info()
  print("Conectando ao servidor MYSQL versao",db_info)
  cursor = mydb.cursor()
  cursor.execute("Sslect database();")
  linha = cursor.fetchone()
  print("COnectando ao banco de dados",linha)

if mydb.is_connected():
  cursor.close()
  mydb.close()
  print("Conexao ao MYSQL foi")