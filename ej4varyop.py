#ingrese tres numeros que se muesten ordenados

numero1= int(input("Introduce el primer numero: "))
numero2= int(input("Introduce el segundo numero: "))
numero3= int(input("Introduce el tercer numero: "))
if numero1<numero2<numero3:
    print("Los numeros ordenados son:" ,numero1,numero2,numero3)
elif numero1<numero3<numero2:
    print("Los numeros ordenados son:" ,numero1,numero3,numero2)
elif numero2 < numero1 < numero3:
    print("Los numeros ordenados son:" ,numero2,numero1,numero3)
elif numero2 < numero3 < numero1:
    print("Los numeros ordenados son:" ,numero2,numero3,numero1)
elif numero3 < numero1 < numero2:
    print("Los numeros ordenados son:" ,numero3,numero1,numero2)
elif numero3 < numero2 < numero1:
    print("los numeros ordenados son:" ,numero3,numero2,numero1)
else:
    print("Los numeros son iguales")
