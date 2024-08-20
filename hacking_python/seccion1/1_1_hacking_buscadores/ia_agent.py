from gpt4all import GPT4All
from openai import OpenAI
from dotenv import load_dotenv


class GPT4AllGenerator:
    def __init__(self, model_name="Meta-Llama-3-8B-Instruct.Q4_0.gguf"):
        self.model = GPT4All(model_name)

    def generate(self, prompt):
        return self.model.generate(prompt)


class OpenAIGenerator:
    def __init__(self, model_name="gpt-4"):
        self.model_name = model_name
        self.client = OpenAI()

    def generate(self, prompt):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-4"
        )
        return chat_completion.choices[0].message.content


class IAAgent:
    def __init__(self, generator):
        self.generator = generator

    def generate_gdork(self, description):
        # Construimos el prompt
        prompt = self._build_promt(description)
        try:
            output = self.generator.generate(prompt)
            return output
        except Exception as e:
            print(f"Error al generar {e}")

    def _build_promt(self, description):
        return f"""
        Genera un Google Dork específico basado en la descripción del usuario. Un Google Dork utiliza operadores avanzados en motores de búsqueda para encontrar información específica que es difícil de encontrar mediante una búsqueda normal. Tu tarea es convertir la descripción del usuario en un Google Dork preciso. A continuación, se presentan algunos ejemplos de cómo deberías formular los Google Dorks basándote en diferentes descripciones:

        Descripción: Documentos PDF relacionados con la seguridad informática publicados en el último año.
        Google Dork: filetype:pdf "seguridad informática" after:2023-01-01
        
        Descripción: Presentaciones de Powerpoint sobre cambio climático disponibles en sitios .edu.
        Google Dork: site:.edu filetype:ppt "cambio climático"
        
        Descripción: Listas de correos electrónicos en archivos de texto dentro de dominios gubernamentales.
        Google Dork: site:.gov filetype:txt "email" | "correo electrónico"
        
        Ahora, basado en la siguiente descripción proporcionada por el usuario, genera el Google Dork correspondiente:
        
        Descripción: {description}
        """



if __name__ == "__main__":
    descripcion = "Listado de usuarios y contraseñas en el contenido de ficheros de texto, Utiliza variaciones de la palabra password y user (passwd, pwd...)"
    # ia_agent = IAAgent()
    # print(ia_agent.generate_gdork(descripcion))
    #
    # from openai import OpenAI

    load_dotenv()

    openai_generator = OpenAIGenerator()
    ia_agent = IAAgent(openai_generator)

    resultado = ia_agent.generate_gdork(descripcion)
    print(resultado)



