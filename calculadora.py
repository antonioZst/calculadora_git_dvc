import math
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise valueError("No se puede dividir entre cero")
    return a / b

def seno(angulo):                # Recibe un ángulo en grados.
    return math.sin(math.radians(angulo))  # Calcula el seno.

def coseno(angulo):              # Recibe un ángulo en grados.
    return math.cos(math.radians(angulo))  # Calcula el coseno.

def tangente(angulo):            # Recibe un ángulo en grados.
    return math.tan(math.radians(angulo))  # Calcula la tangente.