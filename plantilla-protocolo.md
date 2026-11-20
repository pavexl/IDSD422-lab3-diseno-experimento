# Plantilla de protocolo — Experimento de ubicación de producto

**Estudiante:** Pavel Ganchala

**Fecha:** 19/11/2026

## 1. Pregunta e hipótesis

**Pregunta de investigación:** ¿La ubicación de un producto en el pasillo principal genera un mayor promedio de ventas durante cuatro semanas, en comparación con mantenerlo en su ubicación habitual?

- **Hipótesis nula (H₀):** El promedio de unidades vendidas por tienda durante cuatro semanas es igual entre el grupo que ubica el producto en el pasillo principal y el grupo que lo mantiene en su ubicación habitual.

- **Hipótesis alternativa (H₁):** El promedio de unidades vendidas por tienda durante cuatro semanas es mayor en el grupo que ubica el producto en el pasillo principal que en el grupo que lo mantiene en su ubicación habitual.

## 2. Unidad experimental

- **Unidad:** Cada tienda participante, ya que en cada una se probará una ubicación específica para el producto durante el experimento.

- **Número de unidades y justificación:** Se trabajará con 10 tiendas, divididas en dos grupos de 5: uno experimental y otro de control. Esta cantidad permitirá comparar los resultados de las dos ubicaciones durante cuatro semanas. Sin embargo, como se trata de un número reducido de tiendas, las conclusiones serán limitadas. Para obtener resultados más confiables, sería recomendable realizar el experimento con una mayor cantidad de tiendas.

## 3. Factor, niveles y tratamiento

- **Factor (variable manipulada):** La ubicación del producto dentro de la tienda.

- **Niveles (valores del factor):**

  **I.** Pasillo principal.

  **II.** Ubicación habitual.

- **Tratamiento (combinación asignada):** Las 5 tiendas del grupo experimental colocarán el producto en el pasillo principal durante cuatro semanas. Por otro lado, las 5 tiendas del grupo de control mantendrán el producto en su ubicación habitual durante ese mismo período.

## 4. Grupo de control

El grupo de control estará formado por 5 tiendas que mantendrán el producto en su ubicación habitual durante las cuatro semanas del experimento. Este grupo permitirá comparar sus ventas con las del grupo experimental, donde el producto se colocará en el pasillo principal. Esto permitirá analizar si el cambio de ubicación influye en el promedio de unidades vendidas.

## 5. Aleatorización

- **Método:** Se utilizará una asignación aleatoria simple. Primero se mezclarán las 10 tiendas y luego se asignarán las primeras 5 al grupo experimental y las 5 restantes al grupo de control.

- **Justificación:** La aleatorización permite que todas las tiendas tengan la misma oportunidad de formar parte de cualquiera de los dos grupos, evitando que la selección dependa de las preferencias del investigador. Además, permite mantener una distribución equilibrada de 5 tiendas por grupo.

- **Código Python:**

```python
import pandas as pd

tiendas = pd.DataFrame({
    "tienda": [
        "Tienda 1", "Tienda 2", "Tienda 3",
        "Tienda 4", "Tienda 5", "Tienda 6",
        "Tienda 7", "Tienda 8", "Tienda 9",
        "Tienda 10"
    ]
})

tiendas_aleatorias = tiendas.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

tiendas_aleatorias["grupo"] = [
    "Experimental" if i < 5 else "Control"
    for i in range(10)
]

print(tiendas_aleatorias)
```

- **Resultado de una corrida:** Al utilizar la semilla `42`, las tiendas 9, 2, 6, 1 y 8 quedaron asignadas al grupo experimental, mientras que las tiendas 3, 10, 5, 4 y 7 formaron parte del grupo de control.

- **Reproducibilidad:** El parámetro `random_state=42` permite repetir la asignación y obtener los mismos resultados, siempre que se utilice la misma lista de tiendas.

## 6. Respuesta y medición

- **Variable respuesta:** Cantidad total de unidades del producto vendidas en cada tienda durante las cuatro semanas que durará el experimento.

- **Unidad de medida:** Número de unidades vendidas por cada tienda durante ese período.

- **Período de medición:** Se tomarán en cuenta cuatro semanas consecutivas, utilizando las mismas fechas para las 10 tiendas participantes

- **Método de registro:** Las ventas se obtendrán de los registros del sistema de punto de venta (POS) de cada tienda. Las ventas se recopilarán semanalmente y al finalizar el experimento se sumarán las unidades vendidas de cada tienda.

- **Responsable del registro:** El personal encargado de ventas o inventario de cada tienda revisará los registros. Después, la información será recopilada y organizada por la persona encargada del análisis.

- **Cegamiento:** No será posible mantener al personal de las tiendas sin conocimiento de la ubicación asignada al producto. Sin embargo, la persona encargada del análisis recibirá los datos identificados con códigos para los grupos A y B, sin conocer inicialmente cuál corresponde al pasillo principal y cuál a la ubicación habitual. De esta manera, se reducen los posibles sesgos durante el análisis de los resultados.

## 7. Factores a controlar

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. Precio del producto | Se mantendrá el mismo precio en las 10 tiendas durante las cuatro semanas del experimento. |
| 2. Promociones y descuentos | Se evitarán promociones o descuentos adicionales para el producto. Si se presenta alguno que no se pueda evitar, se dejará registrado para tenerlo en cuenta al analizar las ventas. |
| 3. Disponibilidad del inventario | Se intentará mantener suficiente stock en todas las tiendas. También se registrarán los días en los que el producto no esté disponible. |
| 4. Temporada y fechas de medición | Las 10 tiendas realizarán el experimento durante las mismas cuatro semanas, para evitar que las diferencias entre períodos comerciales afecten los resultados. |
| 5. Afluencia de clientes | Se registrará la cantidad de clientes que visitan cada tienda, ya que una mayor afluencia puede generar más oportunidades de venta. |
| 6. Características del producto | Se utilizará el mismo producto, con igual presentación y tamaño en todas las tiendas, para mantener las mismas condiciones durante el experimento. |

## 8. Limitaciones del diseño

El experimento presenta algunas limitaciones que deben considerarse al interpretar los resultados:

1. **Número reducido de tiendas:** Se utilizarán únicamente 10 tiendas, por lo que la muestra podría no representar adecuadamente a todas las sucursales de RetailAndina.

2. **Diferencias entre tiendas:** Las tiendas pueden tener distintos niveles de afluencia de clientes, ubicación geográfica y características del público, lo que podría influir en las ventas.

3. **Duración del experimento:** Las cuatro semanas de medición podrían no ser suficientes para identificar cambios en las ventas a largo plazo o variaciones relacionadas con temporadas comerciales.

4. **Factores externos:** Situaciones imprevistas, como promociones inesperadas, falta de inventario o cambios en el comportamiento de los clientes, podrían afectar los resultados.

5. **Limitación del cegamiento:** El personal de las tiendas conocerá la ubicación asignada al producto, por lo que no será posible eliminar completamente los posibles sesgos durante el experimento.

Por estas razones, los resultados permitirán evaluar el efecto de la ubicación del producto en las tiendas participantes durante el período estudiado, pero no se podrá asegurar que el mismo efecto ocurra en todas las tiendas, productos o períodos comerciales.

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- **¿Qué grupo muestra mayor venta promedio en la plantilla?**

  El grupo que ubicó el producto en el pasillo principal obtuvo un promedio de 1335 unidades vendidas, mientras que el grupo que mantuvo el producto en su ubicación habitual alcanzó un promedio de 1040 unidades. Por lo tanto, el grupo experimental presentó un promedio de ventas más alto.
  
- **¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?**

   Porque solo se cuenta con cuatro registros, dos por cada grupo, correspondientes a una semana de ventas. Además, una de las tiendas del grupo experimental tuvo una promoción al mismo tiempo, lo que pudo influir en sus resultados. Por esta razón, no hay suficientes datos para afirmar que el aumento de ventas se deba al cambio de ubicación.

- **Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?**
  
  Harían falta los registros de las 10 tiendas durante las cuatro semanas del experimento. También habría que tomar en cuenta otros factores que pueden influir en las ventas, como el precio del producto, las promociones, la disponibilidad de inventario y la cantidad de clientes que visitan cada tienda. Así se podría realizar una comparación más completa y justa entre los dos grupos.

### Resultados obtenidos al ejecutar el código

```text
Promedio de ventas por ubicación:
ubicacion
habitual             1040.0
pasillo_principal    1335.0

Número de registros por ubicación:
ubicacion
pasillo_principal    2
habitual             2
```
### Interpretación de los resultados

Los resultados muestran que las tiendas que colocaron el producto en el pasillo principal tuvieron un promedio de ventas más alto que aquellas que lo mantuvieron en su ubicación habitual. Sin embargo, solo se cuenta con cuatro registros, dos por cada grupo, correspondientes a una semana de ventas, por lo que todavía no es posible determinar si esta diferencia se debe realmente al cambio de ubicación.

Para obtener resultados más confiables, sería necesario incluir más tiendas y ampliar el tiempo de medición. También se deberían controlar factores como las promociones y la disponibilidad del inventario, ya que pueden influir en las ventas.
