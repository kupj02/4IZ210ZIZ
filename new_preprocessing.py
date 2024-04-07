import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df = df[df['smoking_status'] != 'Unknown'] # Vyhod radky s neznamou hodnotou koureni
df = df.dropna(subset=['bmi'])  # Vyhod radky s chybejicimi hodnotami BMI
df = df.drop('id', axis=1) # Vyhod nahodne zvolene ID osob
# Nahrazeni stringu floaty
df.replace({'gender': {'Male': 0, 'Other': 1, 'Female': 2}}, inplace=True)
df.replace({'ever_married': {'No': 0, 'Yes': 1}}, inplace=True)
df.replace({'work_type': {'children': 0, 'Govt_job': 1, 'Never_worked': 2, 'Private': 3, 'Self-employed': 4}}, inplace=True)
df.replace({'Residence_type': {'Urban': 0, 'Rural': 1}}, inplace=True)
df.replace({'smoking_status': {'never smoked': 0, 'formerly smoked': 1, 'smokes': 2}}, inplace=True)

#rozdeleni promenych dle typu
numerical_variables=['age','avg_glucose_level','bmi']
nominal_variables=['gender','hypertension','heart_disease','ever_married','work_type','Residence_type',]
ordinal_variables=['smoking_status']
target_variable = "stroke"

X, y = df.loc[:, df.columns != target_variable], df[target_variable]
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

X_train.head()
X_test.head()
#Preprocessing numerickych promenych
imputer_numerical = SimpleImputer(strategy='mean')
X_train[numerical_variables] = imputer_numerical.fit_transform(X_train[numerical_variables])
scaler = StandardScaler()
X_train[numerical_variables] = scaler.fit_transform(X_train[numerical_variables])
scaler.mean_
#Preprocessing nominalnich promenych
imputer_nominal = SimpleImputer(strategy='most_frequent')
X_train[nominal_variables] = imputer_nominal.fit_transform(X_train[nominal_variables])
#Preprocessing ordinalnich promenych
ordinal_enc = OrdinalEncoder(categories=[[0,1,2]])
X_train[ordinal_variables]=ordinal_enc.fit_transform(X_train[ordinal_variables])
ordinal_enc.categories_