"""
Módulo mychar - Procesamiento de cadenas de texto
==================================================

Este módulo contiene funciones para trabajar con listas de cadenas de texto.
Específicamente, proporciona funcionalidad para encontrar la cadena más larga
de una lista, con criterios de desempate alfabéticos.

Autor: José María García Moreno
Fecha: 5/10/2025
Curso: Puesta en producción segura
Tarea: UD01 - Prueba de aplicaciones web y para dispositivos móviles
"""
from typing import List


def cadena_mas_larga(lista: List[str]) -> str:
    """
    Encuentra la cadena más larga de una lista de cadenas.

    Esta función recibe una lista de cadenas de texto y devuelve aquella
    que tiene la mayor longitud. En caso de empate (varias cadenas con la
    misma longitud máxima), devuelve la primera en orden alfabético.

    Args:
        lista (List[str]): Lista de cadenas de texto a analizar.
                          Puede estar vacía o contener cadenas vacías.

    Returns:
        str: La cadena más larga de la lista. Si hay empate, devuelve la
             primera alfabéticamente. Si la lista está vacía, devuelve"".

    Raises:
        ValueError: Si el argumento no es una lista.
        ValueError: Si algún elemento de la lista no es una cadena (str).

    Examples:
        >>> cadena_mas_larga(["hola", "mundo", "python"])
        'python'

        >>> cadena_mas_larga(["abc", "xyz", "def"])
        'abc'

        >>> cadena_mas_larga([])
        ''

    Notes:
        - La función distingue entre mayúsculas y minúsculas en el ordenamiento
        - Las cadenas vacías son válidas y se procesan normalmente
        - La comparación alfabética usa el orden lexicográfico de Python
    """

    # Validación 1: Verificar que el argumento sea una lista
    if not isinstance(lista, list):
        raise ValueError("El parámetro debe ser una lista de cadenas.")

    # Validación 2: Verificar que todos los elementos sean cadenas
    if any(not isinstance(item, str) for item in lista):
        raise ValueError("Todos los elemento de la lista deben de ser cadenas.")

    # Caso base: lista vacía retorna cadena vacía
    if not lista:
        return ""
    if len(lista) == 0:
        return ""

    # Definición de la "clave" para max():
    def clave(item: str):
        if item == "":
            return 0, float('-inf')
        return len(item), -ord(item[0])

    # Selecciona el elemento con la clave máxima según la función 'clave'.
    return max(lista, key=clave)


def solicitar_palabra(n: int = 5) -> List[str]:
    """
    Solicita al usuario 'n' palabras por teclado.

    Parámetros:
        n (int): Número de palabras a pedir. Por defecto, 5.

    Retorna:
        List[str]: Lista con las palabras introducidas (sin espacios extremos).
    """
    palabras = []
    for i in range(n):
        palabra = input(f"Palabra {i + 1}: ").strip()
        palabras.append(palabra)
    return palabras


def main():
    """
        Punto de entrada interactivo del módulo.

        - Solicita 5 palabras al usuario.
        - Calcula y muestra la palabra "más larga" según el criterio de 'cadena_mas_larga'.
        - Captura ValueError para informar al usuario de entradas inválidas.
    """
    print("Introduce 5 palabras para determinar la más larga:")
    try:
        palabras = solicitar_palabra()
        resultado = cadena_mas_larga(palabras)
        print(f"La palabra más larga es: {resultado}")
    except ValueError as e:
        # Cubre errores de validación (tipo de lista o elementos no str).
        print(f"Error: {e}")


if __name__ == "__main__":
    # Permite ejecutar el módulo directamente desde la terminal.
    # Ejemplo: python mychar.py
    main()
