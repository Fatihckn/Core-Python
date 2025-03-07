import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    try:
        # E-posta bilgilerini al
        sender_email = entry_email.get()
        sender_password = entry_password.get()
        recipient_email = entry_recipient.get()
        subject = entry_subject.get()
        message = text_message.get("1.0", "end-1c")  # Metin alanındaki mesajı al

        # E-posta oluştur
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # SMTP sunucusuna bağlan
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # E-posta gönder
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        messagebox.showinfo("Başarılı", "E-posta başarıyla gönderildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"E-posta gönderilirken bir hata oluştu: {str(e)}")

# Ana uygulama penceresini oluştur
root = tk.Tk()
root.title("Gelişmiş E-posta Arayüzü")
root.geometry("600x500")
root.resizable(False,False)
# Giriş kutuları ve etiketler
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)


root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)

label_email = tk.Label(root, text="E-posta Adresi:")
label_email.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_email = tk.Entry(root,width=50)
entry_email.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Şifre:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_password = tk.Entry(root, width=30, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

label_recipient = tk.Label(root, text="Alıcı E-posta:")
label_recipient.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_recipient = tk.Entry(root, width=30)
entry_recipient.grid(row=2, column=1, padx=10, pady=5)

label_subject = tk.Label(root, text="Konu:")
label_subject.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_subject = tk.Entry(root, width=30)
entry_subject.grid(row=3, column=1, padx=10, pady=5)

label_message = tk.Label(root, text="Mesaj:")
label_message.grid(row=4, column=0, padx=10, pady=5, sticky="nw")
text_message = scrolledtext.ScrolledText(root, width=30, height=6)
text_message.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Gönderme düğmesi
button_send = tk.Button(root, text="Gönder", width=10, command=send_email)
button_send.grid(row=5, column=1, pady=10)

# Ana döngüyü başlat
root.mainloop()
