# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo
print("Su nombre completo es:",nombre,apellido)
# Almacenar su nombre completo en una variable
# nombre_completo = .....
nombre_completo = nombre+apellido
print("Su nombre completo es:",nombre_completo)
# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
cantidad_letras = len(nombre)+len(apellido)
print("La cantidad de letras de su mombre completo es",cantidad_letras)
