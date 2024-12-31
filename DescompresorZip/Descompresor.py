import zipfile
import py7zr
import os

class Descompresor:
    def __init__(self, archivo_zip, directorio_destino=None):
        """
        Constructor

        Args:
            archivo_zip (str): Ruta del archivo .zip
            directorio_destino (str, opcional): Ruta del directorio destino
        """

        self.archivo_zip = archivo_zip
        self.directorio_destino = directorio_destino

    def validar_archivo(self):
        """
        Valida si archivo zip existe
        Returns:
            bool: True si archivo zip existe
        """

        return os.path.isfile(self.archivo_zip)

    def descomprimir(self):
        """
        Descomprime el archivo .zip
        Raises:
            FileNotFoundError: No se encontraron archivo .zip
            zipfile.BadZipFile: Si el archivo no es válido
        """
        if not self.validar_archivo():
            raise FileNotFoundError(f"El archivo {self.archivo_zip} no existe")
        try:
            with zipfile.ZipFile(self.archivo_zip, 'r') as zip_ref:
                zip_ref.extractall(self.directorio_destino)
                print(f"Archivo de {self.directorio_destino} descomprimido exitosamente en {self.directorio_destino}")

        except zipfile.BadZipFile:
            print(f"El archivo {self.archivo_zip} no es un archivo válido para zipfile")

        try:
            with py7zr.SevenZipFile(self.archivo_zip, 'r') as z:
                z.extractall(path=self.directorio_destino)
                print(f"Archivo '{self.archivo_zip}' descomprimido exitosamente en {self.directorio_destino}")
        except Exception as e:
            print(f"El archivo {self.archivo_zip} no es un archivo válido para 7z")


