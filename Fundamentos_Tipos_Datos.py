"""Sección 1: Fundamentos, Variables, Tipos de Datos y Manipulación de Cadenas"""

import math

# ❄️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ❄️
# 1. CONSTANTES Y VARIABLES BÁSICAS
# ❄️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ❄️
# Las constantes se escriben en MAYÚSCULAS por convención
PI = 3.14159
DATABASE_NAME = "clientes_db"

# Tipos de datos primitivos
nombre: str = "Sebastián"
edad: int = 24
nivel_energia: float = 87.5
tiene_capa: bool = False
compania_actual = None  # NoneType

print("=== 1. FICHA DE DATOS ===")
print(f"Nombre: {nombre} | Edad: {edad} | Energía: {nivel_energia}")


# ❄️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ❄️
# 2. MANIPULACIÓN DE CADENAS (STRINGS)
# ❄️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ❄️
# Uso de F-Strings (forma moderna y limpia de concatenar)
presentacion = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(f"\n=== 2. F-STRINGS ===\n{presentacion}")

# Métodos comunes para limpiar y transformar textos
texto_sucio = "   Aprender Python es genial   "
texto_limpio = texto_sucio.strip().lower().replace("genial", "poderoso")
print(f"\n=== 3. MÉTODOS DE STRINGS ===")
print(f"Original: '{texto_sucio}'")
print(f"Limpio y modificado: '{texto_limpio}'")

# Búsqueda de subcadenas
frase = "Desarrollo de software en Python"
indice = frase.find("Python")
print(f"La palabra 'Python' empieza en el índice: {indice}")


# ❄️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ❄️
# 3. TÉCNICA DE SLICING (REBANADO)
# ❄️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ❄️
tecnologia = "PROGRAMACION"

print(f"\n=== 4. SLICING EN CADENAS ===")
print(f"Texto original: {tecnologia}")
print(f"Primeras 4 letras [:4]: {tecnologia[:4]}")
print(f"Últimas 4 letras [-4:]: {tecnologia[-4:]}")
print(f"Texto invertido [::-1]: {tecnologia[::-1]} (Muy útil en algoritmos)")


# ❄️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ❄️
# 4. MULTIPLICACIÓN Y FORMATOS ESPECIALES
# ❄️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ❄️
print(f"\n=== 5. FORMATOS Y MULTIPLICACIÓN ===")
# Multiplicación de strings para separadores visuales
print("❄️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ❄️")
print("Línea divisoria generada con multiplicación de strings")
print("❄️ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ❄️")

# Cadenas multilínea (útiles para menús o correos)
menu = """
--------------------
   MENÚ PRINCIPAL
--------------------
1. Iniciar sesión
2. Registrarse
3. Salir
"""
print(menu)