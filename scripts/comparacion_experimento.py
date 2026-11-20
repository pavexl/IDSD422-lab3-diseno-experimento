# comparacion_experimento.py — Comparación de grupos (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py

# TODO 1: carga plantillas/registro_experimento.csv con pandas
import pandas as pd
datos = pd.read_csv("plantillas/registro_experimento.csv")

# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
promedios = datos.groupby("ubicacion")["ventas_producto"].mean()

print("Promedio de ventas por ubicación:")
print(promedios)

# TODO 3: imprime el número de registros por grupo (value_counts)
conteo = datos["ubicacion"].value_counts()

print("\nNúmero de registros por ubicación:")
print(conteo)

# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis
print("\nInterpretación:")
print("El pasillo principal presenta un promedio de ventas mayor que la ubicación habitual.")
print("Sin embargo, solo existen cuatro registros, dos por ubicación, correspondientes a una semana.")
print("Se necesitarían más tiendas y semanas de medición, controlando factores como promociones e inventario, para evaluar el efecto de la ubicación.")
