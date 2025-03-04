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

"""**Análise exploratória**

***Histogramas, lineplots e scatterplots***

*Age*
"""

df['Age'].plot(kind='hist', edgecolor='black')
plt.title('Histograma da Feature Age')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

sns.lineplot(data=df['Age'])
plt.title('Lineplot da Feature Age')
plt.xlabel('Índice')
plt.ylabel('Idade')
plt.show()

sns.scatterplot(x=df.index, y='Age', data=df)
plt.title('Scatterplot da Feature Age')
plt.xlabel('Índice')
plt.ylabel('Idade')
plt.show()

"""*Height*"""

df['Height'].plot(kind='hist', edgecolor='black')
plt.title('Histograma da Feature Height')
plt.xlabel('Altura')
plt.ylabel('Frequência')
plt.show()

sns.lineplot(data=df['Height'])
plt.title('Lineplot da Feature Height')
plt.xlabel('Índice')
plt.ylabel('Altura')
plt.show()

sns.scatterplot(x=df.index, y='Height', data=df)
plt.title('Scatterplot da Feature Height')
plt.xlabel('Índice')
plt.ylabel('Altura')
plt.show()

"""*Weight*"""

df['Weight'].plot(kind='hist', edgecolor='black')
plt.title('Histograma da Feature Weight')
plt.xlabel('Peso')
plt.ylabel('Frequência')
plt.show()

sns.lineplot(data=df['Weight'])
plt.title('Lineplot da Feature Weight')
plt.xlabel('Índice')
plt.ylabel('Peso')
plt.show()

sns.scatterplot(x=df.index, y='Weight', data=df)
plt.title('Scatterplot da Feature Weight')
plt.xlabel('Índice')
plt.ylabel('Peso')
plt.show()

"""*FCVC (Do you usually eat vegetables in your meals?)*"""

df['FCVC'].plot(kind='hist', edgecolor='black')
plt.title('Histograma da Feature FCVC')
plt.xlabel('FCVC')
plt.ylabel('Frequência')
plt.show()

sns.lineplot(data=df['FCVC'])
plt.title('Lineplot da Feature FCVC')
plt.xlabel('Índice')
plt.ylabel('FCVC')
plt.show()

sns.scatterplot(x=df.index, y='FCVC', data=df)
plt.title('Scatterplot da Feature FCVC')
plt.xlabel('Índice')
plt.ylabel('FCVC')
plt.show()

"""*NCP (How many main meals do you have daily?)*"""

df['NCP'].plot(kind='hist', edgecolor='black')
plt.title('Histograma da Feature NCP')
plt.xlabel('NCP')
plt.ylabel('Frequência')
plt.show()

sns.lineplot(data=df['NCP'])
plt.title('Lineplot da Feature NCP')
plt.xlabel('Índice')
plt.ylabel('NCP')
plt.show()

sns.scatterplot(x=df.index, y='NCP', data=df)
plt.title('Scatterplot da Feature NCP')
plt.xlabel('Índice')
plt.ylabel('NCP')
plt.show()

"""*CH2O (How much water do you drink daily?)*"""

df['CH2O'].plot(kind='hist', edgecolor='black')
plt.title('Histograma da Feature CH2O')
plt.xlabel('CH2O')
plt.ylabel('Frequência')
plt.show()

sns.lineplot(data=df['CH2O'])
plt.title('Lineplot da Feature CH2O')
plt.xlabel('Índice')
plt.ylabel('CH2O')
plt.show()

sns.scatterplot(x=df.index, y='CH2O', data=df)
plt.title('Scatterplot da Feature CH2O')
plt.xlabel('Índice')
plt.ylabel('CH2O')
plt.show()

"""*FAF (How often do you have physical activity?)*"""

df['FAF'].plot(kind='hist', edgecolor='black')
plt.title('Histograma da Feature FAF')
plt.xlabel('FAF')
plt.ylabel('Frequência')
plt.show()

sns.lineplot(data=df['FAF'])
plt.title('Lineplot da Feature FAF')
plt.xlabel('Índice')
plt.ylabel('FAF')
plt.show()

sns.scatterplot(x=df.index, y='FAF', data=df)
plt.title('Scatterplot da Feature FAF')
plt.xlabel('Índice')
plt.ylabel('FAF')
plt.show()

"""*TUE (How much time do you use technological devices such as cell phone, videogames, television, computer and others?)*"""

df['TUE'].plot(kind='hist', edgecolor='black')
plt.title('Histograma da Feature TUE')
plt.xlabel('TUE')
plt.ylabel('Frequência')
plt.show()

sns.lineplot(data=df['TUE'])
plt.title('Lineplot da Feature TUE')
plt.xlabel('Índice')
plt.ylabel('TUE')
plt.show()

sns.scatterplot(x=df.index, y='TUE', data=df)
plt.title('Scatterplot da Feature TUE')
plt.xlabel('Índice')
plt.ylabel('TUE')
plt.show()

"""***Correlação de Pearson***"""

aux=df
numerica = aux.select_dtypes(include=np.number).columns
correlation_matrix = aux[numerica].corr(method='pearson')
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlação de Pearson')
plt.show()

"""**Numerizando features categoricas**

*Modificando features binárias para 0 e 1*
"""

pd.set_option('future.no_silent_downcasting', True)

df['Gender'].replace({'Male': 0, 'Female': 1}, inplace=True)
df['FAVC'].replace({'no': 0, 'yes': 1}, inplace=True) # Do you eat high caloric food frequently?
df['SCC'].replace({'no': 0, 'yes': 1}, inplace=True) # Do you monitor the calories you eat daily?
df['SMOKE'].replace({'no': 0, 'yes': 1}, inplace=True) # Do you smoke?
df['family_history_with_overweight'].replace({'no': 0, 'yes': 1}, inplace=True) # Has a family member suffered or suffers from overweight?

"""*Features não-binárias*"""

df['CAEC'].replace({'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}, inplace=True) # Do you eat any food between meals?
df['CALC'].replace({'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}, inplace=True) # How often do you drink alcohol?
df['MTRANS'].replace({'Walking': 0, 'Bike': 1, 'Public_Transportation': 2, 'Motorbike': 3, 'Automobile': 4}, inplace=True) # Which transportation do you usually use?

# Obesity level - Classe
df['NObeyesdad'].replace({'Insufficient_Weight': 0, 'Normal_Weight': 1, 'Overweight_Level_I': 2, 'Overweight_Level_II': 3, 'Obesity_Type_I': 4, 'Obesity_Type_II': 5, 'Obesity_Type_III': 6}, inplace=True)

"""**Abordagem KFold (10) + normalização min-max + gridsearch com 4 algoritmos + Acurácia + DICE (Precisão) + MSE (Sensibilidade/Recall) + F1 + Wilcoxon**"""

# Separando a classe das features (em X e Y)
X = df. drop(['NObeyesdad'],axis=1)
y = df['NObeyesdad']

# Identificando colunas numéricas
numerical_cols = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']

# Instanciando kfold
kfold = KFold(n_splits=10, shuffle=True, random_state=42)

# Definindo os classificadores e seus hiperparâmetros
classifiers = {
    'KNN': {
        'model': KNeighborsClassifier(),
        'param_grid': {'n_neighbors': [3, 5, 7, 9, 11, 15], 'metric': ['euclidean', 'manhattan', 'minkowski', 'cosine']}
    },
    'DecisionTree': {
        'model': DecisionTreeClassifier(),
        'param_grid': {'max_depth': [None, 5, 10, 15], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 2, 4]}
    },
    'SVM': {
        'model': SVC(),
        'param_grid': {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf', 'poly'], 'gamma': ['scale', 'auto']}
    },
    'NaiveBayes': {
        'model': GaussianNB(),
        'param_grid': {}  # Naive Bayes Gaussiano não tem hiperparâmetros para ajustar
    }
}

# Armazenar resultados (um dicionário de dicionários)
results = {}
for clf_name in classifiers:
    results[clf_name] = {'accuracy': [], 'precision': [], 'recall': [], 'f1': [], 'mse': []}

# Iterar ao longo dos folds a partir do método kfold.split(X)
# Praticamente todo o código deve estar identado nesse for
for train_index, test_index in kfold.split(X):
  X_train, X_test = X.iloc[train_index], X.iloc[test_index]
  y_train, y_test = y.iloc[train_index], y.iloc[test_index]

  X_trainDivided, X_val, y_trainDivided, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

  # Normalização (Validação)
  scaler_val = MinMaxScaler()
  X_trainDivided_scaled = X_trainDivided.copy()
  X_val_scaled = X_val.copy()

  X_trainDivided_scaled[numerical_cols] = scaler_val.fit_transform(X_trainDivided[numerical_cols])
  X_val_scaled[numerical_cols] = scaler_val.transform(X_val[numerical_cols])

  # Loop através dos classificadores
  for clf_name, clf_data in classifiers.items():
      model = clf_data['model']
      param_grid = clf_data['param_grid']

      accs_val = []
      par = []

      y_trainDivided = y_trainDivided.astype(int) # Ensure y_trainDivided is of the correct type
      y_val = y_val.astype(int)  # Ensure y_val is of integer type

      # GridSearch
      for params in ParameterGrid(param_grid):
        model.set_params(**params)  # Define os hiperparâmetros
        model.fit(X_trainDivided_scaled, y_trainDivided) # treinado no conjunto de treino dividido com dados normalizados
        y_pred = model.predict(X_val_scaled) # predições no conjunto de validação com dados normalizados
        acc = accuracy_score(y_val, y_pred)
        # A combinação entre as listas de acurácias e parâmetros é salva
        accs_val.append(acc)
        par.append(params)

      best_params = par[accs_val.index(max(accs_val))]
      
      print(f"Melhores hiperparâmetros para {clf_name}: {best_params}") # Informa-nos os melhores hiperparâmetros para esse classificador.

      # Normalização (Treino Completo)
      scaler_train = MinMaxScaler()
      X_train_scaled = X_train.copy()
      X_test_scaled = X_test.copy()

      X_train_scaled[numerica] = scaler_train.fit_transform(X_train[numerica])
      X_test_scaled[numerica] = scaler_train.transform(X_test[numerica])

      y_train = y_train.astype(int)  # Ensure y_train is of integer type

      # Instanciado com os melhores hiperparâmetros
      model.set_params(**best_params)
      model.fit(X_train_scaled, y_train) # treina o modelo com o conjunto de treinamento COMPLETO com dados normalizados
      y_pred = model.predict(X_test_scaled) # predições no conjunto de testes

      y_test = y_test.astype(int)  # Ensure y_train is of integer type


      # --- CÁLCULO DAS MÉTRICAS (IMPRESSÃO PARA DEBUG) ---
      accuracy = accuracy_score(y_test, y_pred)
      precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
      recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
      f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
      mse = mean_squared_error(y_test, y_pred)

      """ # DEBUG
      print(f"--- Fold {len(results[clf_name]['accuracy']) + 1}, Modelo: {clf_name} ---")
      print(f"  Acurácia: {accuracy:.4f}")
      print(f"  Precisão: {precision:.4f}")
      print(f"  Recall: {recall:.4f}")
      print(f"  F1: {f1:.4f}")
      print(f"  MSE: {mse:.4f}")
      print(f"  y_pred: {y_pred}")  # IMPRIMA AS PREDIÇÕES!
      print(f"  y_test: {y_test.values}")  # IMPRIMA OS VALORES REAIS!
      """

      results[clf_name]['accuracy'].append(accuracy)
      results[clf_name]['precision'].append(precision)
      results[clf_name]['recall'].append(recall)
      results[clf_name]['f1'].append(f1)
      results[clf_name]['mse'].append(mse)

""" # Para debug
print("\nConteúdo completo de 'results' após o KFold:")
import pprint  # Para impressão bonita de dicionários
pprint.pprint(results)
"""

# --- Resultados e Teste de Wilcoxon ---
print("\nMétricas Médias (por classificador):\n")
for clf_name, metrics in results.items():
    print(f"--- {clf_name} ---")
    for metric_name, values in metrics.items():
        print(f"  {metric_name.capitalize()}: {np.mean(values):.4f}")

print("\n--- Teste de Wilcoxon (Comparação entre pares de classificadores) ---\n")

model_combinations = list(combinations(classifiers.keys(), 2))  # Todas as combinações de 2 modelos

for model1, model2 in model_combinations:
    print(f"Comparando {model1} vs {model2}:")
    for metric in ['accuracy', 'precision', 'recall', 'f1', 'mse']:
        # O teste de Wilcoxon precisa que os arrays tenham o mesmo tamanho (número de folds)
        # e que não existam empates perfeitos (todas as diferenças = 0).
        # Se houver empates, o teste pode gerar um erro ou um aviso.
        # A correção 'zsplit' divide os valores de z entre as observações empatadas.
        try:
            stat, p = wilcoxon(results[model1][metric], results[model2][metric], zero_method='zsplit')
            print(f"  {metric.capitalize()}:")
            print(f"    Estatística de Wilcoxon = {stat:.4f}, Valor-p = {p:.4f}")
            if p < 0.05:
                print(f"    Diferença estatisticamente significativa (p < 0.05) entre {model1} e {model2} para {metric}.")
            else:
                print(f"    Não há diferença estatisticamente significativa (p >= 0.05) entre {model1} e {model2} para {metric}.")

        except ValueError as e:
            print(f"    Erro ao calcular Wilcoxon para {metric}: {e}")
            print("    Provavelmente há empates ou os arrays têm tamanhos diferentes.")

"""**EXTRA**"""

# Versão balanceada
from imblearn.over_sampling import SMOTE  # Importe a técnica de balanceamento
from collections import Counter

# Separando a classe das features (em X e Y)
X = df.drop(['NObeyesdad'], axis=1)
y = df['NObeyesdad']

# Identificando colunas numéricas
numerical_cols = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']

# --- Divisão Treino/Teste ANTES do Balanceamento ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# --- Balanceamento (SMOTE) APENAS nos Dados de Treinamento ---
smote = SMOTE(random_state=42)
y_train = y_train.astype(int)  # Ensure y_train is of integer type
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

print('Contagens de classes (treino original):', Counter(y_train))
print('Contagens de classes (treino balanceado):', Counter(y_train_resampled))


# --- Daqui para frente, use X_train_resampled e y_train_resampled para treinar ---
# --- X_test e y_test NÃO são modificados! ---

# Instanciando o KFold
kfold = KFold(n_splits=10, shuffle=True, random_state=42)

# Classificadores e hiperparâmetros (sem alterações)
classifiers = {
    'KNN': {
        'model': KNeighborsClassifier(),
        'param_grid': {'n_neighbors': [3, 5, 7, 9, 11, 15], 'metric': ['euclidean', 'manhattan', 'minkowski', 'cosine']}
    },
    'DecisionTree': {
        'model': DecisionTreeClassifier(),
        'param_grid': {'max_depth': [None, 5, 10, 15], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 2, 4]}
    },
    'SVM': {
        'model': SVC(),
        'param_grid': {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf', 'poly'], 'gamma': ['scale', 'auto']}
    },
    'NaiveBayes': {
        'model': GaussianNB(),
        'param_grid': {}
    }
}

# Armazenar resultados
results = {}
for clf_name in classifiers:
    results[clf_name] = {'accuracy': [], 'precision': [], 'recall': [], 'f1': [], 'mse': []}

# Iterar sobre os folds
for train_index, val_index in kfold.split(X_train_resampled):  # Use X_train_resampled
    # Agora 'train_index' e 'val_index' se referem às linhas de X_train_resampled
    X_train_fold, X_val_fold = X_train_resampled.iloc[train_index], X_train_resampled.iloc[val_index]
    y_train_fold, y_val_fold = y_train_resampled.iloc[train_index], y_train_resampled.iloc[val_index]


    # --- Normalização (Validação) ---
    scaler_val = MinMaxScaler()
    X_train_fold_scaled = X_train_fold.copy()
    X_val_fold_scaled = X_val_fold.copy()
    X_train_fold_scaled.loc[:, numerical_cols] = scaler_val.fit_transform(X_train_fold.loc[:, numerical_cols])
    X_val_fold_scaled.loc[:, numerical_cols] = scaler_val.transform(X_val_fold.loc[:, numerical_cols])


    # Loop sobre os classificadores
    for clf_name, clf_data in classifiers.items():
        model = clf_data['model']
        param_grid = clf_data['param_grid']

        accs_val = []
        par = []

        # GridSearch
        for params in ParameterGrid(param_grid):
            model.set_params(**params)
            model.fit(X_train_fold_scaled, y_train_fold)  # Treina com dados balanceados e normalizados
            y_pred = model.predict(X_val_fold_scaled)   # Predição com dados balanceados e normalizados
            acc = accuracy_score(y_val_fold, y_pred)
            accs_val.append(acc)
            par.append(params)

        best_params = par[accs_val.index(max(accs_val))]


        # --- Normalização (Treino Completo, APÓS Validação) ---
        # Normalizamos o X_train_resampled COMPLETO.
        scaler_train = MinMaxScaler()
        X_train_resampled_scaled = X_train_resampled.copy()
        X_test_scaled = X_test.copy() # X_test não foi balanceado

        X_train_resampled_scaled.loc[:, numerical_cols] = scaler_train.fit_transform(X_train_resampled.loc[:, numerical_cols])
        X_test_scaled.loc[:, numerical_cols] = scaler_train.transform(X_test.loc[:, numerical_cols]) #Transform no X_test original

        y_train_resampled = y_train_resampled.astype(int)  # Ensure y_train is of integer type

        # Treinando com os melhores hiperparâmetros e calculando métricas
        model.set_params(**best_params)
        model.fit(X_train_resampled_scaled, y_train_resampled) #Treina com o X_train_resampled
        y_pred = model.predict(X_test_scaled)  # Predição no conjunto de teste (NÃO balanceado)

        y_test = y_test.astype(int)  # Ensure y_train is of integer type

        # Calculando as métricas (com average='weighted' para multiclasse)
        results[clf_name]['accuracy'].append(accuracy_score(y_test, y_pred)) #y_test original
        results[clf_name]['precision'].append(precision_score(y_test, y_pred, average='weighted', zero_division=0))
        results[clf_name]['recall'].append(recall_score(y_test, y_pred, average='weighted', zero_division=0))
        results[clf_name]['f1'].append(f1_score(y_test, y_pred, average='weighted', zero_division=0))
        results[clf_name]['mse'].append(mean_squared_error(y_test, y_pred))



# Resultados e Teste de Wilcoxon
print("\nMétricas Médias (por classificador):\n")
for clf_name, metrics in results.items():
    print(f"--- {clf_name} ---")
    for metric_name, values in metrics.items():
        print(f"  {metric_name.capitalize()}: {np.mean(values):.4f}")

print("\n--- Teste de Wilcoxon (Comparação entre pares de classificadores) ---\n")
model_combinations = list(combinations(classifiers.keys(), 2))
for model1, model2 in model_combinations:
    print(f"Comparando {model1} vs {model2}:")
    for metric in ['accuracy', 'precision', 'recall', 'f1', 'mse']:
        try:
            stat, p = wilcoxon(results[model1][metric], results[model2][metric], zero_method='zsplit')
            print(f"  {metric.capitalize()}:")
            print(f"    Estatística de Wilcoxon = {stat:.4f}, Valor-p = {p:.4f}")
            if p < 0.05:
                print(f"    Diferença estatisticamente significativa (p < 0.05) entre {model1} e {model2} para {metric}.")
            else:
                print(f"    Não há diferença estatisticamente significativa (p >= 0.05) entre {model1} e {model2} para {metric}.")
        except ValueError as e:
            print(f"    Erro ao calcular Wilcoxon para {metric}: {e}")
            print("    Provavelmente há empates ou os arrays têm tamanhos diferentes.")
