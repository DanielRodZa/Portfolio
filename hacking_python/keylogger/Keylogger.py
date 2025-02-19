import keyboard

class Keylogger:
    def __init__(self):
        pass

    def grabar(self):
        print("Presiona Esc para detener la grabación...")
        recorded = keyboard.record(until="esc")
        print("Grabación finalizada...\n")
        return recorded

    def reproducir(self, grabacion):
        print("Presiona 'enter' para reproducir...")
        keyboard.wait("enter")
        print("Reproduciendo\n")
        keyboard.play(grabacion)
        print("Fin de la repoducción")

    def obtener_lista(self, grabacion):
        lista_letras = []
        for evento in grabacion:
            if evento.even_type == 'down':
                lista_letras.append(evento.name)

        return lista_letras

    def obtener_cadena(self, lista_letras):
        cadena_de_texto = ''.join(lista_letras)
        return cadena_de_texto


