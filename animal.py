"""
Calse de Animal
"""


class Animal:
    def __init__(self, param_nombre, param_especie, param_edad):
        self.nombre = param_nombre
        self.especie = param_especie
        self.edad = param_edad
        self.energia = 50 

    def presentarse(self):
        text = f'Hola, soy {self.nombre} ({self.especie} | {self.edad} ā)'
        print(text)

    def jugar(self):
        self.energia -= 20
        if self.energia < 0:
            self.energia = 0
        print(f'\n{self.nombre} Jugando... energías nueva: {self.energia}')

    def comer(self, gramos: int):
        self.energia += (gramos//10)
        if self.energia > 100:
            self.energia = 100
        print(f'\n{self.nombre} Comiendo... energia nueva: {self.energia}')

    def dormir(self):
        self.energia += 30
        if self.energia > 100:
            self.energia = 100
        print(f'\n{self.nombre} Durmienrdo... energía nueva: {self.energia}')


