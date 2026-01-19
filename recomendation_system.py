"""
Análisis exploratorio sintético de ventas mensuales.

Pasos:
1) Generar datos sintéticos de ventas mensuales.
2) Limpiar y validar tipos de datos.
3) Estadística descriptiva básica.
4) Agregar ingresos por categoría.
5) Visualizar la tendencia temporal de ventas.
"""

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.ticker import StrMethodFormatter


def generar_datos_sinteticos(num_meses: int = 24, semilla: int = 42) -> pd.DataFrame:
	"""Crea un DataFrame con ventas mensuales sintéticas por producto."""
	np.random.seed(semilla)

	productos = ["Widget A", "Widget B", "Widget C", "Widget D"]
	categorias = {
		"Widget A": "Gadgets",
		"Widget B": "Gadgets",
		"Widget C": "Accessories",
		"Widget D": "Accessories",
	}

	fechas = pd.date_range(start="2023-01-01", periods=num_meses, freq="MS")
	registros = []

	for fecha in fechas:
		for producto in productos:
			cantidad = np.random.poisson(lam=40) + 5
			precio = np.random.normal(loc=35, scale=8)
			precio = max(precio, 5)  # evita precios negativos o demasiado bajos
			ventas_usd = round(cantidad * precio, 2)

			registros.append(
				{
					"Fecha": fecha,
					"Producto": producto,
					"Categoria": categorias[producto],
					"Ventas_USD": ventas_usd,
					"Cantidad": cantidad,
				}
			)

	return pd.DataFrame(registros)


def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
	"""Normaliza tipos numéricos/fechas y elimina filas con nulos críticos."""
	df = df.copy()
	df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
	df["Ventas_USD"] = pd.to_numeric(df["Ventas_USD"], errors="coerce")
	df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors="coerce")

	df_limpio = df.dropna(subset=["Fecha", "Producto", "Categoria", "Ventas_USD", "Cantidad"])
	return df_limpio


def estadistica_descriptiva(df: pd.DataFrame) -> pd.DataFrame:
	"""Devuelve resumen estadístico de métricas monetarias y de volumen."""
	return df[["Ventas_USD", "Cantidad"]].describe()


def ingresos_por_categoria(df: pd.DataFrame) -> pd.DataFrame:
	"""Agrupa por categoría y suma ingresos."""
	return (
		df.groupby("Categoria", as_index=False)["Ventas_USD"].sum().rename(columns={"Ventas_USD": "Ingresos_Total"})
	)


def visualizar_tendencia(df: pd.DataFrame) -> None:
	"""Grafica la tendencia mensual de ventas totales."""
	mensual = df.groupby("Fecha", as_index=False)["Ventas_USD"].sum()

	sns.set_style("whitegrid")
	plt.figure(figsize=(10, 5))
	sns.lineplot(data=mensual, x="Fecha", y="Ventas_USD", marker="o", color="#1f77b4")
	plt.title("Tendencia de ventas mensuales")
	plt.xlabel("Fecha")
	plt.ylabel("Ventas (USD)")
	plt.gca().yaxis.set_major_formatter(StrMethodFormatter("${x:,.0f}"))
	plt.xticks(rotation=45)
	plt.tight_layout()
	plt.show()


def ejecutar_eda() -> None:
	"""Ejecuta el flujo completo de EDA con registros en consola."""
	# 1) Generación de datos
	df = generar_datos_sinteticos()
	print("===== Vista inicial =====")
	print(df.head())

	# 2) Revisión de tipos y nulos antes de limpieza
	print("\nTipos de datos iniciales:")
	print(df.dtypes)
	print("\nValores nulos por columna (antes):")
	print(df.isnull().sum())

	# 3) Limpieza y coerción de tipos
	df_limpio = limpiar_datos(df)
	print("\n===== Después de limpieza =====")
	print(df_limpio.dtypes)
	print("Nulos por columna (después):")
	print(df_limpio.isnull().sum())
	print(f"Filas descartadas: {len(df) - len(df_limpio)}")

	# 4) Estadística descriptiva
	print("\n===== Estadística descriptiva =====")
	print(estadistica_descriptiva(df_limpio))

	# 5) Ingresos por categoría
	print("\n===== Ingreso total por categoría =====")
	print(ingresos_por_categoria(df_limpio))

	# 6) Visualización de tendencia
	visualizar_tendencia(df_limpio)


if __name__ == "__main__":
	ejecutar_eda()
