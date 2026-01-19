# AI_Project – EDA de ventas sintéticas

Este repositorio contiene un flujo de Análisis Exploratorio de Datos (EDA) con datos sintéticos de ventas mensuales. Se genera un dataset ficticio, se limpia, se calculan métricas descriptivas, se agregan ingresos por categoría y se visualiza la tendencia temporal de ventas.

## Requisitos
- Python 3.10+
- Entorno virtual (recomendado): `.venv`
- Dependencias: definidas en [requirements.txt](requirements.txt)

## Instalación y entorno
1) Crear entorno virtual (si no existe):
```bash
python -m venv .venv
```
2) Activar (macOS/Linux):
```bash
source .venv/bin/activate
```
3) Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso
Ejecuta el EDA completo (genera datos, limpia, describe, agrega y grafica):
```bash
python recomendation_system.py
```

## Descripción del flujo
- Generación de datos sintéticos mensuales por producto y categoría con variación estocástica en precio y cantidad.
- Limpieza y coerción de tipos (`Fecha`, `Ventas_USD`, `Cantidad`), descarte de filas con nulos críticos.
- Estadística descriptiva básica sobre ventas y cantidades.
- Agregación de ingresos totales por categoría.
- Visualización de la tendencia mensual de ventas con Seaborn/Matplotlib.

El código principal vive en [recomendation_system.py](recomendation_system.py); las versiones fijadas están en [requirements.txt](requirements.txt).

## Instrucciones solicitadas (criterios de evaluación)
Se implementaron exactamente los pasos requeridos en el enunciado para evidenciar el uso de IA generativa:
1) Crear un script de Python para análisis exploratorio (EDA).
2) Generar un DataFrame sintético con pandas que simule ventas mensuales (Fecha, Producto, Categoria, Ventas_USD, Cantidad).
3) Limpiar datos (verificación de nulos y coerción de tipos numéricos/fecha).
4) Realizar análisis estadístico descriptivo básico (`describe`).
5) Agrupar por Categoría para calcular el ingreso total.
6) Visualizar la tendencia de ventas a lo largo del tiempo (Seaborn/Matplotlib, línea temporal).
7) Documentar el código y el proceso paso a paso (este README).

## Proceso y uso de IA generativa
- Se solicitó a la IA la creación del script de EDA con datos sintéticos, limpieza, descriptivos, agregaciones y gráfica temporal; la IA generó y organizó las funciones en [recomendation_system.py](recomendation_system.py).
- Se creó un entorno virtual `.venv` y se instalaron las dependencias listadas en [requirements.txt](requirements.txt), fijando versiones para reproducibilidad.
- La documentación se redactó con apoyo de la IA, incorporando las instrucciones originales y la justificación del flujo.
- Ajustes sugeridos: modificar `num_meses` o `semilla` para variar el dataset; agregar más visualizaciones (p. ej., distribución de ventas por producto) si se requiere.

## Resultados esperados
- Salida en consola con:
	- Vista inicial del dataset sintético (primeras filas).
	- Tipos de datos y conteo de nulos antes y después de la limpieza.
	- Estadística descriptiva (`describe`).
	- Tabla de ingresos totales por categoría.
- Gráfico de línea que muestra la tendencia de ventas mensuales (se abre en una ventana Matplotlib).

## Capturas de pantalla
Coloca tus capturas en `docs/img/` y actualiza los nombres si difieren. Ejemplos de referencias en Markdown (los archivos no se incluyen por defecto):
- ![Salida en consola](docs/img/console_output.png)
- ![Gráfico de tendencia](docs/img/ventas_tendencia.png)

## Estructura breve
- [recomendation_system.py](recomendation_system.py): script EDA completo (datos sintéticos, limpieza, agregados, gráfica).
- [requirements.txt](requirements.txt): dependencias con versiones fijadas.
- README.md: esta documentación.

## Notas
- El dataset es completamente sintético; no requiere datos externos.
- Ajusta los parámetros `num_meses` o `semilla` en la función `generar_datos_sinteticos` si deseas modificar el tamaño o reproducibilidad.