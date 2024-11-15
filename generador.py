import pandas as pd
import numpy as np
from faker import Faker
import random

# Inicializar Faker
fake = Faker()

# Funciones para generar datos específicos
def generate_phone(index):
    fakeIndex = random.uniform(2,10)
    if index % fakeIndex == 0:
        country_code = f"+{random.randint(1, 99)}" 
        return f"{country_code} {fake.phone_number()}" 
    return fake.phone_number()[:15]

def generate_salary(index):
    fakeIndex = random.uniform(2,10)
    if index % fakeIndex == 0:
        return f"{random.randint(10000, 1000000):,}".replace(',', '.')    
    return f"{random.randint(10000, 1000000):,}"

def generate_weight(index):
    fakeIndex = random.uniform(2,10)
    weight = random.uniform(50, 100)
    if index % fakeIndex == 0:
        return f"{weight * 2.20462:.2f} lbs"  # Peso en libras cada 10 registros
    return f"{weight:.2f} kg"

def generate_height(index):
    fakeIndex = random.uniform(2,10)
    height = random.uniform(150, 200)
    if index % fakeIndex == 0:
        return f"{height * 0.0328084:.2f} ft"  # Altura en pies cada 10 registros
    return f"{height:.2f} cm"

def generate_birthdate(index):
    fakeIndex = random.uniform(2,10)
    birthdate = fake.date_time_between(start_date='-70y', end_date='-18y').strftime("%d/%m/%Y %H:%M:%S")
    if index % fakeIndex == 0:
        birthdate = fake.date_time_between(start_date='-70y', end_date='-18y').strftime("%Y-%m-%d")
    return birthdate

def generate_nationality():
    return fake.country()

def generate_blood_group():
    return random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])

size = 300
# Generar datos
data = {
    'Nombres': [fake.name() for _ in range(size)],
    'Telefonos': [generate_phone(i) for i in range(size)],
    'Salario': [generate_salary(i) for i in range(size)],
    'Pesos': [generate_weight(i) for i in range(size)],
    'Alturas': [generate_height(i) for i in range(size)],
    'Nacionalidades': [generate_nationality() for _ in range(size)],
    'Grupo Sanguineos': [generate_blood_group() for _ in range(size)],
    'Fechas de Nacimiento': [generate_birthdate(i) for i in range(size)]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Introducir valores nulos aleatoriamente
for col in df.columns:
    df.loc[df.sample(frac=0.05).index, col] = np.nan  # 5% de valores nulos

# Guardar en un archivo CSV para su uso posterior
df.to_csv('dataset.csv', index=False)
