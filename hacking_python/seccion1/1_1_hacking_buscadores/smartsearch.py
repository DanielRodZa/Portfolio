import os
import re
import argparse

from transformers import GPT2Tokenizer
from openai import OpenAI
from dotenv import load_dotenv


class SmartSearch:
    """
    Smart Search Class
    Ayuda a buscar un patrón creado por una expresión regular en una carpeta o fichero
    """

    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.files = self._read_files()

    def _read_files(self):
        """
        Esto lee el contenido de los ficheros que se encuentran en un directorio
        Returns:
            None
        """
        files = {}
        # Listar los ficheros del directorio
        for archivo in os.listdir(self.dir_path):
            file_path = os.path.join(self.dir_path, archivo)
            try:
                with open(file_path, mode='r', encoding='utf-8') as f:
                    files[archivo] = f.read()
            except Exception as e:
                print(f"Error al leer el archivo {file_path}:\nERROR: {e}")
        return files

    def regex_search(self, regex):
        """
        Busca información utilizando expresiones regulares
        Args:
            regex (str)

        Returns:
            coincidencias (dict)
        """
        coincidencias = {}
        # Recorremos el contenido de todos los ficheros del directorio
        for f, text in self.files.items():
            respuesta = ""
            while respuesta not in ("y", "n", "yes", "no"):
                respuesta = input(f"El fichero {f} tiene una longitud de {len(text)} caracteres\n"
                                  f"¿Quieres procesarlo? (yes/no)")
                if respuesta in ("no", "n"):
                    continue
                matches = re.findall(regex, text, re.IGNORECASE)
                if not matches == []:
                    coincidencias[file] = matches
        return coincidencias

    def ia_search(self, prompt, model_name='gpt-3.5-turbo-0125', max_tokens=100):
        """
        Realiza búsquedas en ficheros con inteligencia artificial
        Args:
            prompt (str)
            model_name (str)
            max_tokens (int)

        Returns:

        """
        coincidencias = {}
        for text_file, text in self.files.items():
            respuesta = ""
            tokens, coste = self._calcular_coste(
                text=text,
                prompt=prompt,
                model_name=model_name,
                max_tokens=max_tokens)
            while respuesta not in ("y", "n", "yes", "no"):
                respuesta = input(f"El fichero {text_file} tiene una longitud de {tokens} tokens.\n"
                                  f"El coste aproximado es ${coste} dlls.\n"
                                  f"¿Quieres procesarlo? (yes/no)")
            if respuesta in ("no", "n"):
                continue

            # Dividimos el fichero en segmentos
            file_segments = self._split_file(
                file_text=text,
                model_name=model_name)

            # Inicializamos el cliente de OpenAI
            client = OpenAI()
            resultados_segmentos = []

            for index, segmento in enumerate(file_segments):
                print(f"Procesando el segmento {index + 1}/{len(file_segments)}...")
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"{prompt}\n\nTexto:\n {segmento}"
                        }
                    ],
                    model=model_name,
                    max_tokens=max_tokens,
                    n=1,
                )
                resultados_segmentos.append(chat_completion.choices[0].message.content)
            coincidencias[text_file] = resultados_segmentos
        return coincidencias

    @staticmethod
    def _split_file(file_text, model_name):
        """
        Divide el contenido del fichero en segmentos
        Args:
            file_text:
            model_name:

        Returns:
            list of split text
        """
        context_window_sizes = {
            "gpt-4-0125-preview": 128000,
            "gpt-4-1106-preview": 128000,
            "gpt-4": 16000,
            "gpt-4-32k": 32000,
            "gpt-3.5-turbo-0125": 16000,
            "gpt-3.5-turbo-instruct": 4000
        }
        return [
            file_text[i:i + context_window_sizes[model_name]]
            for i in range(0, len(file_text), context_window_sizes[model_name])
        ]

    @staticmethod
    def _calcular_coste(text, prompt, model_name, max_tokens):
        """
        Calcula el coste para un modelo de OpenAI
        Args:
            text (str)
            prompt (str)
            model_name (str)
            max_tokens (int)

        Returns:
            (tuple): len_tokens_prompt + len_tokens_text, input_cost + output_cost
        """
        precios = {
            "gpt-4-0125-preview": {"input_cost": 0.01, "output_cost": 0.03},
            "gpt-4-1106-preview": {"input_cost": 0.01, "output_cost": 0.03},
            "gpt-4-1106-vision-preview": {"input_cost": 0.01, "output_cost": 0.03},
            "gpt-4": {"input_cost": 0.03, "output_cost": 0.06},
            "gpt-4-32k": {"input_cost": 0.06, "output_cost": 0.12},
            "gpt-3.5-turbo-0125": {"input_cost": 0.0005, "output_cost": 0.0015},
            "gpt-3.5-turbo-instruct": {"input_cost": 0.0015, "output_cost": 0.002}
        }
        # Tokenizamos el texto perteneciente al archivo
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

        len_tokens_prompt = len(tokenizer.tokenize(prompt))
        len_tokens_text = len(tokenizer.tokenize(text))

        # Calculamos el coste de la predicción
        input_cost = ((len_tokens_prompt + len_tokens_text) / 1000) + precios[model_name]["input_cost"]
        output_cost = (max_tokens / 1000) + precios[model_name]["output_cost"]

        return len_tokens_prompt + len_tokens_text, input_cost + output_cost


if __name__ == "__main__":
    # Cargamos las variables de entorno
    load_dotenv()
    # Configuramos los argumentos del programa
    parser = argparse.ArgumentParser(
        description="Smart Search:\n"
                    "Esta herramienta realiza búsquedas en los ficheros de un directorio"
    )
    parser.add_argument("dir_path", type=str,
                        help="La ruta al directorio en el que se encuentran los ficheros")
    parser.add_argument("-r", "--regex", type=str,
                        help="La expresión regular para realizar la búsqueda")
    parser.add_argument("-p", "--prompt", type=str,
                        help="El prompt para realizar la búsqueda con GPT")
    parser.add_argument("-m", "--model_name", type=str, default="gpt-3.5-turbo-0125",
                        help="El nombre del modelo de OpenAi para realizar la búsqueda")
    parser.add_argument("--max_tokens", type=int, default=100,
                        help="El número máximo de tokens en la predicción\\generación.")

    # Parseamos los argumentos
    args = parser.parse_args()
    if args.regex:
        searcher = SmartSearch(args.dir_path)
        resultados = searcher.regex_search(args.regex)
        for file, results in resultados.items():
            print(file)
            for r in results:
                print(f"\t-\t{r}")

    if args.prompt:
        searcher = SmartSearch(args.dir_path)
        resultados = searcher.ia_search(
            prompt=args.prompt,
            max_tokens=args.max_tokens,
            model_name=args.model_name,
        )
        for file, results in resultados.items():
            print(file)
            for r in results:
                print(f"\t-\t{r}")
