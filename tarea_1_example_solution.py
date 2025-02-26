def separa_letras(cadena):
    """Separa letras mayúsculas y minúsculas de una cadena.

    Entradas:
        cadena: El string de entrada.

    Salidas:
        tupla: Estado, lista de mayúsculas, lista de minúsculas.
            - Cadena vacía, devuelve -300.
            - Cadena contiene algo más que letras, devuelve -200.
            - Cadena no es un string, devuelve -100.
    """
    if isinstance(cadena, str):
        # Si la cadena está vacía
        if cadena == "":
            return -300, None, None

        # Separa las letras en mayúsculas y minúsculas
        list_may = ''.join(letra for letra in cadena if letra.isupper())
        list_min = ''.join(letra for letra in cadena if letra.islower())

        # Si la cadena contiene solo letras
        if cadena.isalpha():
            return 0, list_may, list_min

        # Si la cadena contiene algo más que letras
        return -200, None, None

    # Error si la entrada no es texto
    return -100, None, None


def potencia_manual(base, potencia):
    """Calcula la potencia de un número.

    Entradas:
        base : Base de la potencia.
        potencia: Exponente.

    Salidas:
        tupla: Estado, resultado de la potencia.
            - Si las entradas no son enteros, devuelve -400.
            - Si la potencia es 0, devuelve 0, 1
            - Si la potencia es diferente de 0, devuelve la potencia.
    """
    # Verifica que los parámetros sean enteros
    if isinstance(base, int) and isinstance(potencia, int):
        # Inicializa en 1
        resultado = 1
        # Si la potencia no es 0 realiza el cálculo de la potencia
        if potencia != 0:
            for _ in range(potencia):
                contador = 0
                # Calcula la potencia
                for _ in range(resultado):
                    contador += base
                resultado = contador
            return 0, resultado

        # Si la potencia es 0 entrega 1
        return 0, 1

    # Si las entradas no son enteras da un error
    return -400, None
