import keyboard

def main():
    grabacion = recording()
    keyboard.wait("enter")
    keyboard.play(grabacion)

    cadena = []

    for evento in grabacion:
        if evento.event_type == 'down':
            print(type(evento))
            print(evento.event_type)
            print(evento.scan_code)
            print(evento.name)
            cadena.append(evento.name)
            print(evento.time)
            print(evento.device)
            print(evento.is_keypad)
            print(evento.modifiers)

    print(cadena)

def recording():
    print("Presiona Esc para detener la grabación...")
    recorded = keyboard.record(until="esc")
    print("Grabación finalizada... Presiona enter para reproducirla...")
    return recorded

def get_string(grabacion):
    lista_letras = []
    for evento in grabacion:
        if evento.event_type == 'down':
            lista_letras.append(evento.name)
    return lista_letras


if __name__ == "__main__":
    main()