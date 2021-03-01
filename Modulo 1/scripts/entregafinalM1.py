#MODULO 1
#Problema 1-Módulo 1
nombre = input('Introduzca su nombre')
print('Hola '+ nombre)


#Problema 2-Módulo 1
import string
texto = input('Introduzca una palabra o frase')
cifrado = ''
while True:
    try:
        k = int(input('Introduzca el número de posiciones a avanzar en el abecedario'))
        alfabeto = string.ascii_lowercase
        for l in texto:
            if l.lower() in alfabeto:
                p = alfabeto.find(l.lower())
                c = (p + k) % 26
                if l.isupper():
                    cifrado += cifrado.join(alfabeto[c].upper())
                else:
                    cifrado += cifrado.join(alfabeto[c])
            else:
                cifrado += cifrado.join(l)
                print('El text es: '+ texto)
                print('El cifrado es: ' + cifrado)
        break
    except:
        print('Error, introduzca bien los datos')


#Problemas diversos-Módulo 1
#1
inicio = int(input('Ingrese el monto a depositar'))
cap1 = round(inicio * (1 + 0.04),2)
cap2 = round(cap1 * (1 + 0.04),2)
cap3 = round(cap2 * (1 + 0.04),2)
print('El año 1 el capital es de {}'.format(cap1))
print('El año 2 el capital es de {}'.format(cap2))
print('El año 3 el capital es de {}'.format(cap3))


#2
a = int(input('Introduzca el primer número'))
b = int(input('Introduzca el segundo número'))
c = int(input('Introduzca el tercer número'))
discriminante = b ** 2 - 4 * a *c
if discriminante <= 0:
    print('No tiene solución real')
else:    
    solucion1 = (- b + discriminante**(1/2))/(2*a)
    solucion2 = (- b - discriminante**(1/2))/(2*a)
    print('La primera solución es: {}'.format(solucion1))
    print('La segunda solución es: {}'.format(solucion2))