def sumar(a, b):
    suma = a +b
    return suma
    # aqui se realiza la suma de dos numeros

def restar(a, b):
    resta= a -b 
    return resta
    # aqui se realiza la resta de dos numeros

def multiplicar(a, b):
    multiplicacion = a * b
    return multiplicacion
    # aqui se realiza la multiplicacion de dos numeros

def dividir(a, b):
    if b== 0:
        return "Error: No se puede dividir por cero"
    divicion = a/b
    return divicion
    # aqui se realiza la division de dos numeros

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Suma:", sumar(num1, num2))
    print("Resta:", restar(num1, num2))
    print("Multiplicación:", multiplicar(num1, num2))
    print("División:", dividir(num1, num2))

if __name__ == "__main__":
    main()
