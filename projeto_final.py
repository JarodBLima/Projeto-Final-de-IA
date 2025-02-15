# -*- coding: utf-8 -*-
"""Projeto Final

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gPD_XqCgdR8QHdn5unGP9RLsvV8QgO9V

**Importando Bibliotecas**
"""

import pandas as pd # leitura e manipulação de DataFrames
import numpy as np # manipulação matemática de arrays
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import drive # Integração entre drive e colab, a qual permite a leitura de dados no drive
from sklearn.model_selection import KFold # biblioteca que possui a implementação do método de K-Fold
from sklearn.neighbors import KNeighborsClassifier # KNN para classificação
from sklearn.tree import DecisionTreeClassifier # Árvore de Decisão para classificação
from sklearn.svm import SVC # SVM para classificação
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score # métrica de acurácia
from sklearn.metrics import precision_score, recall_score, f1_score, mean_squared_error
from sklearn.model_selection import train_test_split # biblioteca que possui a implementação do método Holdout
from sklearn.model_selection import ParameterGrid # Biblioteca para auxiliar no Gridsearch
from sklearn.preprocessing import MinMaxScaler # Biblioteca para auxiliar na normalização
from scipy.stats import wilcoxon  # Para o teste de Wilcoxon
from itertools import combinations  # Para gerar combinações de modelos

"""***Montando Drive***"""

# Commented out IPython magic to ensure Python compatibility.
drive.mount('/content/drive')
# %cd '/content/drive/MyDrive/Colab Notebooks/'

"""**Checagem de valores faltantes**"""

# Carregar o arquivo CSV
df = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')
# Verificar valores nulos
valores_faltantes = df.isnull().sum()
# Calcular porcentagem de valores faltantes
porcentagem_faltantes = (valores_faltantes / len(df)) * 100

# Criar DataFrame de resumo
resumo = pd.DataFrame({
        'Coluna': valores_faltantes.index,
        'Valores Faltantes': valores_faltantes.values,
        'Porcentagem (%)': porcentagem_faltantes.round(2).values
})

# Total de valores faltantes
total_faltantes = valores_faltantes.sum()
print(f"Total de valores faltantes no dataset: {total_faltantes}")

print("\nResumo de valores faltantes:")
resumo