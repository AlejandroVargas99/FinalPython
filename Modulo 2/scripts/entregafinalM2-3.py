#MODULO 2
#Problema 1-Módulo 2
while True:
    try:
        n = int(input("¿Cuántos filas desea, colocar de 1 a 8"))
        if n >=1 and n <= 8:
            for i in range(1+n):
                espacio = n - i
                print(' ' * espacio + '#' * i)
            break
        else:
            print('Error, introduzca un valor de 1 a 8')
    except:
        print('Error, introduzca un valor de 1 a 8')


#MODULO 2
#Problema 1-Módulo 2
while True:
    try:
        n = int(input("¿Cuántos filas desea, colocar de 1 a 8"))
        if n >=1 and n <= 8:
            for i in range(1+n):
                espacio = n - i
                print(' ' * espacio + '#' * i)
            break
        else:
            print('Error, introduzca un valor de 1 a 8')
    except:
        print('Error, introduzca un valor de 1 a 8')


#Problemas diversos-Módulo 2 y 3
#1,2,3,4 y 5
aprobados = 0
desaprobados = 0
promtot = 0
lista = []
numero = int(input('Introduzca el núnmro de alumnos'))
for i in range (0,numero):
    nombre = input('Introduzca el nombre del alumno')
    nota1 = int(input('Introduzca la primera nota'))
    nota2 = int(input('Introduzca la segunda nota'))
    nota3 = int(input('Introduzca la tercera nota'))
    promedio = (nota1 + nota2 + nota3)/3
    lista.append(nombre)
    if promedio >= 4:
        aprobados = aprobados + 1
    else:
        desaprobados = desaprobados + 1
    promtot += promedio
promfinal = round(promtot/numero,2)
print('La lista de alumnos es:')
print(lista)
print('El número de aprobados es {}'.format(aprobados))
print('El número de desaprobados es {}'.format(desaprobados))
print('El promedio del salón es {}'.format(promfinal))
