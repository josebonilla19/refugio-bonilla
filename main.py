'''
Simulación de un día en el refugio
'''


from animal import Animal


# Instancias animales
luna = Animal('Luna', 'gato', 3)
rocky = Animal('Rocky', 'perro', 5)
kiwi = Animal('Kiwi', 'loro', 2)

# Presentaciopnes
luna.presentarse()
rocky.presentarse()
kiwi.presentarse()

# Actividad Luna
luna.jugar()
luna.comer(150)
luna.dormir()

# Actividad Rocky
rocky.jugar()
rocky.comer(500)
rocky.dormir()

# Actividad Kiwi
kiwi.comer(100)
kiwi.dormir()

print(f'\nLa energia de Luna es: {luna.energia}')
print(f'\nLa energia de Rocky es: {rocky.energia}')
print(f'\nLa energia de Kiwi es: {kiwi.energia}')
