import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from collections import Counter

# Nacti dataset a vyhod z dat u koureni hodnoty Unkown | target atribute je stroke, ktery je binarni, tudiz netreba upravovat
df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df = df[df['smoking_status'] != 'Unknown']
df = df.dropna(subset=['bmi'])  # Vyhod radky s chybejicimi hodnotami BMI
df = df.drop('id', axis=1)
df['gender']=pd.factorize(df['gender'])[0].astype(float)
df['ever_married']=pd.factorize(df['ever_married'])[0].astype(float)
df['work_type']=pd.factorize(df['work_type'])[0].astype(float)
df['Residence_type']=pd.factorize(df['Residence_type'])[0].astype(float)
df['smoking_status']=pd.factorize(df['smoking_status'])[0].astype(float)
# Rozdel dataset do trenovaciho a testovaciho
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

X=df.drop('stroke', axis=1)
feature_cols = ['gender', 'age', 'hypertension', 'heart_disease','ever_married','work_type','Residence_type','avg_glucose_level', 'bmi', 'smoking_status']
y=df['stroke']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)