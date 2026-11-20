# Plantilla de protocolo — Experimento de ubicación de producto

**Estudiante:** Pavel Ganchala · **Fecha:** 19/11/2026

## 1. Pregunta e hipótesis

**Pregunta de investigación:** ¿La ubicación de un producto en el pasillo principal genera un mayor promedio de ventas durante cuatro semanas, en comparación con mantenerlo en su ubicación habitual?

- **Hipótesis nula (H₀):** El promedio de unidades vendidas por tienda durante cuatro semanas es igual entre el grupo que ubica el producto en el pasillo principal y el grupo que lo mantiene en su ubicación habitual.

- **Hipótesis alternativa (H₁):** El promedio de unidades vendidas por tienda durante cuatro semanas es mayor en el grupo que ubica el producto en el pasillo principal que en el grupo que lo mantiene en su ubicación habitual.

## 2. Unidad experimental

- **Unidad:** Cada tienda participante, ya que en cada una se probará una ubicación específica para el producto durante el experimento.

- **Número de unidades y justificación:** Se trabajará con 10 tiendas, divididas en dos grupos de 5: uno experimental y otro de control. Esta cantidad permitirá comparar los resultados de las dos ubicaciones durante cuatro semanas. Sin embargo, como se trata de un número reducido de tiendas, las conclusiones serán limitadas. Para obtener resultados más confiables, sería recomendable realizar el experimento con una mayor cantidad de tiendas.

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada):
- **Niveles** (valores del factor):
- **Tratamiento** (combinación asignada):

## 4. Grupo de control

*¿Cuál es la referencia sin tratamiento y qué rol cumple?*

## 5. Aleatorización

*¿Cómo se asignan las unidades a los grupos? ¿Por qué es necesaria?*

- **Línea de código de la asignación (Python o R):** escribe el comando que asigna al azar tus N unidades a los dos grupos (tratamiento y control) y ejecútalo con semilla. Incluye el resultado de una corrida y explica por qué el sorteo reparte los factores desconocidos entre los grupos.

## 6. Respuesta y medición

- Variable respuesta:
- Período de medición:
- Quién registra y cómo (¿ciego?):

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. | |
| 2. | |
| 3. | |
| 4. | |

## 8. Limitaciones del diseño

*¿Qué podría invalidar el experimento si no se controla? ¿Qué no se podrá concluir?*

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- ¿Qué grupo muestra mayor venta promedio en la plantilla?
- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?
- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?
