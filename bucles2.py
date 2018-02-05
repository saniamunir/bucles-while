# coding:utf -8

lim = float(input("Escribe el valor: "))
while lim <= 0:
    lim = float(input("El valor debe ser mayor que 0. Inténtelo de nuevo: "))
num = float(input("Escribe un número: "))
suma = 0
suma += num
while suma < lim:
    num = float(input("Escribe otro número: "))
    suma += num
print("Ha superado el lim. La suma de los num positivos es", str(suma) + ".")

