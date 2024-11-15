import pandas as pd

# Leer datos desde un archivo CSV
df = pd.read_csv('dataset.csv')
print (df.head())


# Encontrar valores nulos
print (df.isnull().sum())

# Intentar convertir a datetime y encontrar errores
df['fecha'] = pd.to_datetime(df['Fechas de Nacimiento'], errors='coerce')
print(df[df['fecha'].isnull()])


# Valores atipicos
# Resumen estadístico para detectar valores atípicos
print(df.describe())

# Usar z-score para detectar valores atípicos
from scipy import stats
z_scores = stats.zscore(df.select_dtypes(include=['float64', 'int64']))
abs_z_scores = abs(z_scores)
outliers = (abs_z_scores > 3).all(axis=1)
print(df[outliers])

# Encontrar filas duplicadas
print(df.duplicated().sum())

# Eliminar filas duplicadas
df = df.drop_duplicates()

# Llenar valores nulos
df['columna'] = df['Nombres'].fillna('valor_por_defecto')
df['Nombres'] = df['Nombres'].fillna('valor_por_defecto')
df['columna_innecesaria'] = df['columna']
# Remover columnas 
df = df.drop(columns=['columna_innecesaria'])
# Reemplazar
df['columna'] = df['columna'].replace('valor_viejo', 'valor_nuevo')

# Filtrar
# Filtrar filas basadas en una condición
df_filtrado = df[df['Salario'] == "75000"]

# # Encontrar filas que contienen 'abc'
df_contains_abc = df[df['Nombres'].str.contains('abc')]
print(df_contains_abc)

# Reemplazar todos los números por 'NUM'
df['Nombres'] = df['Nombres'].str.replace(r'\d+', 'NUM', regex=True)
print(df)

# Extraer los números de la columna 'texto'
df['numeros'] = df['Nombres'].str.extract(r'(\d+)', expand=False)
print(df)


# Personalizar funciones
import re

def agregar_fila_si_regex_cumple(row, pattern):
    if re.search(pattern, row['Nombres']):
        return row['Nombres']
    return None

# Definir el patrón regex
pattern = r'abc\d+'

# Aplicar la función y agregar una nueva columna
df['cumple_regex'] = df.apply(agregar_fila_si_regex_cumple, axis=1, pattern=pattern)


import pandas as pd
df['Salario'] = df['Salario'].astype(str).fillna('0')

# Reemplazar comas por nada 
df['Salario'] = df['Salario'].str.replace(',', '') 
df['Salario'] = df['Salario'].str.replace('.', '') 

# Verificar el reemplazo 
df['tofloat'] = df['Salario'].str.replace('nan','0')
print (df['tofloat'])

df['columna_numerica'] = pd.to_numeric(df['tofloat'])

#df['columna_timedelta'] = pd.to_timedelta(df['Fechas de Nacimiento'])

df['columna_fecha'] = pd.to_datetime(df['Fechas de Nacimiento'], format='%d/%m/%Y', errors="coerce")

df['columna_nueva'] = df['columna_numerica'].astype('int')
print(df.head())
df.to_csv('procesed.csv')
 # Filtrar filas donde las fechas no cumplen el formato 
fechas_invalidas = df[df['columna_fecha'].isna()] 
# Mostrar las filas con fechas inválidas 
print(fechas_invalidas.head())