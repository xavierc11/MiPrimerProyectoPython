
import utilidades

def suma(num1, num2):
    #print(f"Función suma, params => num1: {num1} y num2: {num2}")
    result = num1 + num2
    return result

def resta(num1, num2):
    #print(f"Función resta, params => num1: {num1} y num2: {num2}")
    result = num1 - num2
    return result

def multi(num1, num2):
    #print(f"Función multiplicacion, params => num1: {num1} y num2: {num2}")
    result = num1 * num2
    return result

def divi(num1, num2):
    #print(f"Función divi, params => num1: {num1} y num2: {num2}")
    result = num1 / num2
    return result

def do_operations(ope, dig1, dig2):
    match ope:
        case 1:
            resultado_suma = suma(dig1, dig2)
            print(f'El resultado de la suma es: {resultado_suma}')
        case 2: 
            resultado_resta = resta(dig1, dig2)
            print(f'El resultado de la resta es: {resultado_resta}')
        case 3:
            resultado_multi = multi(dig1, dig2)
            print(f'El resultado de la multiplicación es: {resultado_multi}')
        case 4:
            resultado_divi = divi(dig1, dig2)
            print(f'El resultado de la división es: {resultado_divi}')

print(f"Bienvenido a mi calculadora para bots!")
print("\n")
operacion = int(input(f"Ingrese la operación a realizar\n(1=suma, 2=resta, 3=multiplicacion, 4=division): "))
digito1 = float(input("Ingrese el dígito 1: "))
digito2 = float(input("Ingrese el dígito 2: "))

do_operations(operacion, digito1, digito2)
print(f'La fecha y hora actual es: {utilidades.get_current_date()}')
print(f'{utilidades.save_file('ruta')}')
print(f"Gracias por utilizar este servicio!.")









