def nome_da_funcion(parametro1, parametro2):
    """
    Función de ejemplo para mostrar como se escriben las funciones

    La función hace una suma, si es número, del parámetro 1 y 2
    :param parametro1: Primer número a sumar
    :param parametro2: Segundo número a sumar
    :return: Suma de parametro1 y parametro2
    """
    print(parametro1, parametro2)
    return parametro1 + parametro2

print(nome_da_funcion(1, 2))

print(nome_da_funcion("hola", "que tal"))  # Al hacer print, hace print del return, al ser una suma las pone juntas

print(nome_da_funcion(parametro2="que tal", parametro1="Ola"))  # Puedes mandar los parámetros de forma desordenada

def repetir(cadea, veces=1):
    """
    Función que imprime una cadena repetida cierto número de veces.

    :param cadea: Cadena a repetir
    :param veces: Número de veces que se repetirá la cadena (por defecto es 1)
    """
    print(cadea * veces)

repetir("Hola ", 5)
repetir("Adeus")

def volumeParalelogramo(lado1=1, lado2=1, altura=1):
    """
    Función que calcula el volumen de un paralelogramo.

    :param lado1: Longitud del primer lado (por defecto es 1)
    :param lado2: Longitud del segundo lado (por defecto es 1)
    :param altura: Altura del paralelogramo (por defecto es 1)
    :return: Volumen del paralelogramo
    """
    return lado1 * lado2 * altura

print(volumeParalelogramo())
print(volumeParalelogramo(6))
print(volumeParalelogramo(6, 4))
print(volumeParalelogramo(6, 4, 5))
print(volumeParalelogramo(altura=5))

def funcionSumaMoitosParametros(valor1, valor2, *outros):
    """
    Función que suma varios números, incluyendo dos valores iniciales.

    :param valor1: Primer valor a sumar
    :param valor2: Segundo valor a sumar
    :param outros: Otros valores a sumar (argumentos variables)
    :return: Suma de todos los valores proporcionados
    """
    suma = valor1 + valor2
    for x in outros:
        suma += x
    return suma

print(funcionSumaMoitosParametros(1, 2, 4, 5, 6, 7, 8, 9, 10, 11))

def usuarioConDatosExtendidos(nome, dni, edade, **outros):
    """
    Función que imprime información extendida sobre un usuario.

    :param nome: Nombre del usuario
    :param dni: DNI del usuario
    :param edade: Edad del usuario
    :param outros: Otros datos adicionales del usuario (argumentos con nombre)
    """
    print("Nome: " + nome)
    print("Dni: " + dni)
    print("Edad:", edade)
    for clave in outros.keys():
        print(clave, ":", outros[clave])

usuarioConDatosExtendidos("Nico", "98798754Y", 20, Sexo="Varón", Direccion="Balaidos", Estado="Casado", Vivo=True)

var = 5
def funcion(valor):
    """
    Función que muestra un valor y lo asigna a una variable local.

    :param valor: Valor a mostrar y asignar
    """
    var = valor
    print(var)

funcion(9)
print(var)
