import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
from tkinter import messagebox, Toplevel, font
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext

# Global e-posta listesi
emails = []

# Seçilen e-posta sağlayıcısı ve kullanıcı bilgileri
email_provider = ''
user_email = ''
user_password = ''

# IMAP ve SMTP ayarları
IMAP_SERVERS = {
    'hotmail': 'outlook.office365.com',
    'gmail': 'imap.gmail.com'
}

SMTP_SERVERS = {
    'hotmail': 'smtp-mail.outlook.com',
    'gmail': 'smtp.gmail.com'
}

# E-posta listbox'ını günceller
def update_emails_listbox():
    tree.delete(*tree.get_children())  # Mevcut listeyi temizler
    for email in emails:
        tree.insert("", "end", values=(email["from"], email["subject"], email["preview"]))  # E-postaları listeye ekler

# E-postaları alır
def fetch_emails():
    global emails
    try:
        imap_server = IMAP_SERVERS[email_provider]  # Seçilen e-posta sağlayıcısına göre IMAP sunucusunu alır

        mail = imaplib.IMAP4_SSL(imap_server)  # IMAP sunucusuna bağlanır
        mail.login(user_email, user_password)  # Kullanıcı ile giriş yapar
        mail.select('inbox')  # Gelen kutusunu seçer
        typ, data = mail.search(None, 'ALL')  # Tüm e-postaları arar
        mail_ids = data[0].split()[-50:]  # Son 50 e-postayı alır

        emails = []
        for num in mail_ids:
            typ, data = mail.fetch(num, '(RFC822)')  # E-postayı getirir
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            content = extract_content(email_message)  # E-posta içeriğini çıkarır

            emails.append({
                "from": email_message["from"],
                "subject": email_message["subject"],
                "content": content,
                "preview": content[:30] + '...'  # İçeriğin ilk 30 karakterini önizleme olarak kullanır
            })
        emails.reverse()  # E-postaları ters çevirir, en son gelenler en başta olsun
        mail.logout()  # IMAP oturumunu kapatır
    except Exception as e:
        emails = [{"from": "Error", "subject": "", "content": str(e), "preview": ""}]  # Hata durumunda mesaj gösterir
    update_emails_listbox()  # Listbox'ı günceller

# E-posta içeriğini çıkarır
def extract_content(email_message):
    content = ''
    for part in email_message.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))

        if ctype == 'text/plain' and 'attachment' not in cdispo:
            content += part.get_payload(decode=True).decode('utf-8', errors='ignore')  # Düz metin içeriğini alır
    return content

# E-posta içeriğini yeni bir pencerede gösterir
def show_email_details(email_content):
    detail_window = Toplevel(root)  # Yeni bir pencere açar
    detail_window.title("E-posta Detayları")
    detail_window.geometry("800x600")
    detail_window.configure(bg='#282c34')

    text_area = scrolledtext.ScrolledText(detail_window, wrap=WORD, bg='#282c34', fg='#abb2bf')
    text_area.insert(INSERT, email_content)  # E-posta içeriğini metin alanına ekler
    text_area.pack(expand=True, fill='both')

# Listbox'tan seçilen e-posta detaylarını gösterir
def on_email_select(event):
    selected_item = tree.selection()  # Seçili öğeyi alır
    if selected_item:
        index = tree.index(selected_item)
        email_content = emails[index]["content"]
        show_email_details(email_content)  # Seçilen e-postanın içeriğini gösterir

# E-posta gönderir
def send_email(to, subject, body):
    msg = MIMEMultipart()
    msg['From'] = user_email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        smtp_server = SMTP_SERVERS[email_provider]  # Seçilen e-posta sağlayıcısına göre SMTP sunucusunu alır
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        server.login(user_email, user_password)
        text = msg.as_string()
        server.sendmail(user_email, to, text)  # E-postayı gönderir
        server.quit()
        return "E-posta başarıyla gönderildi."
    except Exception as e:
        return "E-posta gönderilirken hata oluştu: " + str(e)

# Gönder butonuna tıklanıldığında çağrılır
def send():
    response = send_email(to_entry.get(), subject_entry.get(), body_text.get("1.0", END))
    messagebox.showinfo("Gönderim Durumu", response)  # Gönderim durumunu gösterir
    to_entry.delete(0, END)
    subject_entry.delete(0, END)
    body_text.delete("1.0", END)

# E-postaları günceller
def update_emails():
    fetch_emails()

# Giriş yapar
def login():
    global email_provider, user_email, user_password
    email_provider = provider_var.get()  # Seçilen e-posta sağlayıcısını alır
    user_email = email_entry.get()
    user_password = password_entry.get()

    if not user_email or not user_password:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun!")
        return

    try:
        imap_server = IMAP_SERVERS[email_provider]  # Seçilen e-posta sağlayıcısına göre IMAP sunucusunu alır
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(user_email, user_password)
        mail.logout()
        show_main_window()  # Giriş başarılı olursa ana pencereyi gösterir
    except imaplib.IMAP4.error:
        messagebox.showerror("Hata", "E-posta veya şifre hatalı, tekrar deneyin.")
    except Exception as e:
        messagebox.showerror("Hata", f"Giriş başarısız: {str(e)}")

# Çıkış yapar ve giriş ekranına döner
def logout():
    root.destroy()
    show_login_window()

# Giriş ekranını gösterir
def show_login_window():
    global login_window, email_entry, password_entry, provider_var

    login_window = Tk()
    login_window.title("Giriş Ekranı")
    login_window.geometry("600x500")
    login_window.configure(bg='#353b48')

    app_font = font.Font(family="Helvetica", size=12)

    Label(login_window, text="E-posta Sağlayıcısı Seçin:", font=app_font, bg='#353b48', fg='#ffffff').pack(pady=10)
    provider_var = StringVar(value='hotmail')
    Radiobutton(login_window, text="Hotmail", variable=provider_var, value='hotmail', font=app_font, bg='#353b48', fg='#ffffff', selectcolor='#282c34').pack()
    Radiobutton(login_window, text="Gmail", variable=provider_var, value='gmail', font=app_font, bg='#353b48', fg='#ffffff', selectcolor='#282c34').pack()

    Label(login_window, text="E-posta:", font=app_font, bg='#353b48', fg='#ffffff').pack(pady=10)
    email_entry = Entry(login_window, font=app_font, bg='#282c34', fg='#ffffff')
    email_entry.pack(pady=5)

    Label(login_window, text="Şifre:", font=app_font, bg='#353b48', fg='#ffffff').pack(pady=10)
    password_entry = Entry(login_window, font=app_font, bg='#282c34', fg='#ffffff', show='*')
    password_entry.pack(pady=5)

    login_button = Button(login_window, text="Giriş Yap", command=login, font=app_font, bg='#0984e3', fg='#ffffff')
    login_button.pack(pady=20)

    login_window.mainloop()

# Ana pencereyi gösterir
def show_main_window():
    login_window.destroy()

    global root, tree, to_entry, subject_entry, body_text

    root = Tk()
    root.title("E-posta Uygulaması")
    root.geometry("1280x720")  # Pencere boyutunu ayarla
    root.configure(bg='#353b48')  # Nötr bir arka plan rengi ayarla

    app_font = font.Font(family="Helvetica", size=12)

    # Label ve Entry düzenlemeleri
    Label(root, text="Alıcı:", font=app_font, bg='#353b48', fg='#ffffff').grid(row=0, column=0, sticky=W, padx=10, pady=10)
    Label(root, text="Konu:", font=app_font, bg='#353b48', fg='#ffffff').grid(row=1, column=0, sticky=W, padx=10, pady=10)
    Label(root, text="Mesaj:", font=app_font, bg='#353b48', fg='#ffffff').grid(row=2, column=0, sticky=NW, padx=10, pady=10)

    to_entry = Entry(root, font=app_font, bg='#282c34', fg='#ffffff')
    to_entry.grid(row=0, column=1, sticky=EW, padx=10, pady=10)

    subject_entry = Entry(root, font=app_font, bg='#282c34', fg='#ffffff')
    subject_entry.grid(row=1, column=1, sticky=EW, padx=10, pady=10)

    body_text = scrolledtext.ScrolledText(root, height=10, font=app_font, bg='#282c34', fg='#ffffff')
    body_text.grid(row=2, column=1, sticky=EW, padx=10, pady=10)

    # Gönder butonu
    send_button = Button(root, text="Gönder", command=send, font=app_font, bg='#0984e3', fg='#ffffff')
    send_button.grid(row=3, column=1, sticky=EW, padx=10, pady=10)

    columns = ("from", "subject", "preview")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
    tree.heading("from", text="Gönderen")
    tree.heading("subject", text="Konu")
    tree.heading("preview", text="Özet")
    tree.column("from", width=250)
    tree.column("subject", width=300)
    tree.column("preview", width=700)
    tree.grid(row=4, column=0, columnspan=2, sticky=EW, padx=10, pady=10)
    tree.bind("<<TreeviewSelect>>", on_email_select)  #Bu kod satırı, bir kullanıcı Treeview'de bir satır seçtiğinde on_email_select fonksiyonunun çalıştırılmasını sağlayacaktır

    # E-postaları güncelle butonu
    update_button = Button(root, text="E-postaları Güncelle", command=update_emails, font=app_font, bg='#00b894', fg='#ffffff')
    update_button.grid(row=5, column=1, sticky=EW, padx=10, pady=10)

    # Çıkış yap butonu
    logout_button = Button(root, text="Çıkış Yap", command=logout, font=app_font, bg='#e74c3c', fg='#ffffff')
    logout_button.grid(row=6, column=1, sticky=EW, padx=10, pady=10)

    root.mainloop()

# Giriş ekranını göster
show_login_window()