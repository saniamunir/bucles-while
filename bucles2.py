# coding:utf -8

l = float(input("Escribe el valor: "))
while l <= 0:
    l = float(input("El valor debe ser mayor que 0. Inténtelo de nuevo: "))
num = float(input("Escribe un número: "))
suma = 0
suma += num
while suma < l:
    num = float(input("Escribe otro número: "))
    suma += num
print("Ha superado el l. La suma de los num positivos es", str(suma) + ".")

