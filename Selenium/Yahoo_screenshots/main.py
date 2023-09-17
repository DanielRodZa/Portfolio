import datetime
import time
import smtplib


from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from selenium import webdriver

with open('../lista_correos.txt', 'r') as file:
    emails = file.readlines()

send_to = [x.replace('\n','') for x in emails]
# send_to = ['lsantiago@yaganaste.com', 'ntovar@pagatodo.com','mts.zavaleta@gmail.com']
# send_to = ['mts.zavaleta@gmail.com']

mensaje = "Hola,\n\nAdjunto las 3 capturas de pantall para la prueba 2 desde un email enviado automaticamente con Python.\n\nSaludos,\nDaniel Rodriguez Zavaleta"

def main():
    url = 'https://finance.yahoo.com/quote/MXN=X?p=MXN=X&.tsrc=fin-srch'
    img_path_list = []

    driver = webdriver.Edge()
    driver.get(url)
    driver.maximize_window()

    for i in range(3):
        print("Tomando screenshot")
        current_time = datetime.datetime.now().time()
        screenshot_path = f'C:/Users/Daniel/Documents/PuebaTecnicaPT/Prueba_2/Image_{current_time.hour}_{current_time.minute}_{current_time.second}.png'
        driver.refresh()
        driver.save_screenshot(screenshot_path)
        img_path_list.append(screenshot_path)
        if i == 2:
            break
        time.sleep(60)

    print(img_path_list)
    driver.close()

    send_mail(img_path_list)


def send_mail(img_path_list):
    """
        Envía un correo electrónico con 3 capturas de pantalla utilizando el protocolo SMTP.
    """
    with open('../credenciales.txt','r') as credentials:
        lines = credentials.readlines()
    sender_email = lines[0].strip()
    sender_pass = lines[1].strip()

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    today = datetime.datetime.now()
    format_today = today.strftime('%d%m%Y')

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(send_to)
    msg['Subject'] = f'Tipo de cambio online {format_today}'
    msg.attach(MIMEText(mensaje, 'plain'))

    try:
        for image in img_path_list:
            try:
                with open(image, 'rb') as ss:
                    img = MIMEImage(ss.read())
                msg.attach(img)
            except:
                print(f"Unable to attach image: {image}")

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        server.login(sender_email, sender_pass)

        email_text = msg.as_string()
        server.sendmail(sender_email, send_to, email_text)

        server.quit()

        print("Correo correctamente enviado")
    except Exception as e:
        print(f"No se pudo enviar el correo\nError: {e}")


if __name__ == '__main__':
    main()