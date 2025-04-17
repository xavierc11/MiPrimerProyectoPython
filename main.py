
import utilidades
import ope_math

def do_operations(ope, dig1, dig2):
    match ope:
        case 1:
            resultado_suma = ope_math.suma(dig1, dig2)
            print(f'El resultado de la suma es: {resultado_suma}')
        case 2: 
            resultado_resta = ope_math.resta(dig1, dig2)
            print(f'El resultado de la resta es: {resultado_resta}')
        case 3:
            resultado_multi = ope_math.multi(dig1, dig2)
            print(f'El resultado de la multiplicación es: {resultado_multi}')
        case 4:
            resultado_divi = ope_math.divi(dig1, dig2)
            print(f'El resultado de la división es: {resultado_divi}')

print(f"Bienvenido a mi calculadora para bots!")
print("\n")
operacion = int(input(f"Ingrese la operación a realizar\n(1=suma, 2=resta, 3=multiplicacion, 4=division): "))
digito1 = float(input("Ingrese el dígito 1: "))
digito2 = float(input("Ingrese el dígito 2: "))

do_operations(operacion, digito1, digito2)
print(f'La fecha y hora actual es: {utilidades.get_current_date()}')
print(f"Gracias por utilizar este servicio!.")









