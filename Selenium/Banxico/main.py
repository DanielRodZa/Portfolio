import glob
import platform
import shutil
import smtplib
import time
import os
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Define date
today = datetime.datetime.now()


# Path to downloaded file (Default: same than script)
download_path = 'C:/Users/Daniel/Documents/PuebaTecnicaPT/Prueba_1'

# For dates use format: 'DDMMYYYY'
INIT_DATE = '28/08/2023'
FINAL_DATE = '04/09/2023'

with open('../lista_correos.txt', 'r') as file:
    emails = file.readlines()

send_to = [x.replace('\n','') for x in emails]
# send_to = ['lsantiago@yaganaste.com', 'ntovar@pagatodo.com','mts.zavaleta@gmail.com']
# send_to = ['mts.zavaleta@gmail.com']
mensaje = "Hola,\n\nAdjunto el archivo xlsx para la pueba 1 desde un email enviado automaticamente con Python.\n\nSaludos,\nDaniel Rodriguez Zavaleta"

def download_directory():
    if platform.system() == 'Windows':
        directory = os.path.join(os.environ["USERPROFILE"], 'Downloads')
    elif platform.system() == 'Linux':
        directory = os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        print("No se encuetra el sistema operativo")
        directory = None

    return directory

def download_file():
    """
        Descarga un archivo de un sitio web utilizando Selenium WebDriver.

        Esta función configura el directorio de descarga, navega al sitio web,
        completa los campos de entrada requeridos e inicia la descarga.
        Luego cambia el nombre del archivo y lo mueve a la ruta de descarga especificada.

    """

    # Create a Edge WevDriver options
    edge_options = Options()
    edge_options.add_argument(f'--download.default_directory={download_path}')
    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()
    URL = 'https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?sector=6&accion=consultarCuadro&idCuadro=CF102&locale=es'
    driver.get(URL)

    time.sleep(5)


    try:
        button = driver.find_element(By.ID, 'exportaCuadroToggle')
        button.click()

        time.sleep(3)

        initial_date_input = driver.find_element(By.ID, 'expCuadroFechaInicio')
        initial_date_input.clear()
        initial_date_input.send_keys(INIT_DATE)

        final_date_input = driver.find_element(By.ID, 'expCuadroFechaFinal')
        final_date_input.clear()
        final_date_input.send_keys(FINAL_DATE)

        download = driver.find_element(By.ID, 'botonExportarCuadro')
        download.send_keys(Keys.ENTER)
    except:
        raise Exception('Error al descargar archivo.')
    # download.click()

    time.sleep(10)

    file_pattern = f"Consulta_{today.strftime('%Y%m%d')}-*.xlsx"
    original_directory = download_directory()

    selected_file = glob.glob(os.path.join(original_directory, file_pattern))

    new_name = f'TIPO DE CAMBIO AL {today.strftime("%d%m%Y")}.xlsx'

    shutil.move(selected_file[0], os.path.join(download_path, new_name))

    time.sleep(10)
    driver.close()

def send_mail():
    """
    Envía un correo electrónico con un archivo adjunto utilizando el protocolo SMTP.
    """
    xlsx_file = f'TIPO DE CAMBIO AL {today.strftime("%d%m%Y")}.xlsx'

    with open('../credenciales.txt', 'r') as credentials:
        lines = credentials.readlines()
    sender_email = lines[0].strip()
    sender_pass = lines[1].strip()

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(send_to)
    msg['Subject'] = xlsx_file
    msg.attach(MIMEText(mensaje, 'plain'))

    try:
        msg_file = open(xlsx_file, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((msg_file).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={xlsx_file}')
        msg.attach(part)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        server.login(sender_email, sender_pass)

        email_text = msg.as_string()
        server.sendmail(sender_email, send_to, email_text)

        server.quit()

        msg_file.close()

        print("Correo correctamente enviado")
    except Exception as e:
        print(f"No se pudo enviar el correo\nError: {e}")


def main():
    download_file()
    send_mail()


if __name__ == '__main__':
    main()