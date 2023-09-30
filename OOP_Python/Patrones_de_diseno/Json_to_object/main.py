from abc import ABC, abstractmethod

class Adapter(ABC):
    @abstractmethod
    def converter(self, object): pass

class ToJson(Adapter):
    def converter(self, object):
        return convert_to_json(object)

class FromJson(Adapter):
    def converter(self, object):
        return convert_to_object(object)

class Object: pass

def convert_to_object(json:dict):
    object_python = Object()

    for key, value in json.items():
        object_python.__setattr__(key, value)
    return object_python

def convert_to_json(object):
    json = {}
    for attr, value in object.__dict__.items():
        json[attr] = value
    return json

perfil_objeto = Object()
perfil_objeto.nombre = 'Gaston'
perfil_objeto.edad = 21
perfil_objeto.ocupacion = 'NiNi'

perfil_json = {
    'nombre':'Daniel',
    'edad':31,
    'ocupacion':'Programador'
}

to_json = ToJson()
data = to_json.converter(perfil_objeto)
print(data)

from_json = FromJson()
data = from_json.converter(perfil_json)
for attr, value in data.__dict__.items():
    print(f'{attr}: {value}')
print(data)

