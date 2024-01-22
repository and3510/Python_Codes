import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações de e-mail
remetente_email = "alisonleao.01@gmail.com"
remetente_senha = 'oO0192g#'
destinatario_email = 'and.dovale@gmail.com'
assunto = 'Assunto do e-mail'
mensagem_corpo = 'Corpo do e-mail.'

# Configuração do servidor SMTP do Gmail
smtp_servidor = 'smtp.gmail.com'
smtp_porta = 587

# Criando o objeto MIMEText para o corpo do e-mail
mensagem = MIMEMultipart()
mensagem.attach(MIMEText(mensagem_corpo, 'plain'))

# Configuração do cabeçalho do e-mail
mensagem['From'] = remetente_email
mensagem['To'] = destinatario_email
mensagem['Subject'] = assunto

# Iniciando a conexão com o servidor SMTP
with smtplib.SMTP(smtp_servidor, smtp_porta) as servidor_smtp:
    # Iniciando a comunicação com o servidor
    servidor_smtp.starttls()
    
    # Logando no servidor SMTP
    servidor_smtp.login(remetente_email, remetente_senha)
    
    # Convertendo a mensagem para string
    corpo_mensagem = mensagem.as_string()
    
    # Enviando o e-mail
    servidor_smtp.sendmail(remetente_email, destinatario_email, corpo_mensagem)

print('E-mail enviado com sucesso!')
