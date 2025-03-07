import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gönderen e-posta bilgileri
sender_email = "cokanfatih03@gmail.com"
sender_password = "vqidyihpdnxnbgzw"

# Alıcı e-posta adresi
receiver_email = "eymenonar74@gmail.com"

# E-posta sunucusuna bağlanma
server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
server.login(sender_email, sender_password)

# E-posta oluşturma
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test mail"
msg['From'] = sender_email
msg['To'] = receiver_email
html = """
    <h1>Hello world</h1>
"""
msg.attach(MIMEText(html, 'html'))

# E-posta gönderme
server.sendmail(sender_email, receiver_email, msg.as_string())

# Sunucu bağlantısını sonlandırma
server.quit()
