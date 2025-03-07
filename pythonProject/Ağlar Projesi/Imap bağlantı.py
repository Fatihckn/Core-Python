import imaplib

# Alıcı e-posta bilgileri
receiver_email = "cokanfatih03@gmail.com"
receiver_password = "vqidyihpdnxnbgzw"

# IMAP sunucusuna bağlanma
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(receiver_email, receiver_password)

# Gelen kutusunu seçme
mail.select("inbox")

# Tüm gelen e-postaları al
status, messages = mail.search(None, "ALL")
messages = messages[0].split()

for message in messages:
    status, msg = mail.fetch(message, "(RFC822)")
    print(msg[0][1])

# Bağlantıyı sonlandırma
mail.close()
mail.logout()
