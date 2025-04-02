"""
Este script demuestra el uso de clases para realizar
operaciones básicas matemáticas y calcular promedios.

Clases:
    - OperacionesBasicas: Realiza suma y resta de dos números.
    - CalculadoraPromedio: Calcula el promedio de una lista de valores.

Uso:
    Ejecutar el script para ver los resultados de las operaciones
    matemáticas y el cálculo de promedio.
"""

from typing import List, Union


class OperacionesBasicas:
    """Clase para realizar operaciones matemáticas básicas como suma y resta."""

    def __init__(self):
        """Inicializa la clase con un atributo resultado."""
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado.

        Args:
            a (float | int): Primer número.
            b (float | int): Segundo número.
        """
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado.

        Args:
            a (float | int): Primer número.
            b (float | int): Segundo número.
        """
        self.resultado = a - b

    def obtener_resultado(self):
        """Obtiene el resultado de la última operación realizada.

        Returns:
            float | int: Resultado de la última operación.
        """
        return self.resultado


class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores: List[Union[float, int]]):
        """Inicializa la clase con una lista de valores.

        Args:
            valores (list[float | int]): Lista de números para calcular el promedio.
        """
        self._valores = valores

    @property
    def valores(self) -> List[Union[float, int]]:
        """Obtiene la lista de valores.

        Returns:
            List[Union[float, int]]: Lista de valores almacenados.
        """
        return self._valores

    @valores.setter
    def valores(self, nuevos_valores: List[Union[float, int]]):
        """Establece una nueva lista de valores, validando que sean numéricos.

        Args:
            nuevos_valores (List[Union[float, int]]): Nueva lista de valores.

        Raises:
            ValueError: Si la lista contiene elementos no numéricos.
        """
        if not all(isinstance(valor, (int, float)) for valor in nuevos_valores):
            raise ValueError("Todos los elementos de 'valores' deben ser números.")
        self._valores = nuevos_valores

    def calcular_promedio(self) -> float:
        """Calcula el promedio de los valores almacenados en la lista.

        Returns:
            float: Promedio de los valores. Retorna 0 si la lista está vacía.
        """
        if not self._valores:
            return 0.0
        return sum(self._valores) / len(self._valores)


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio}")
