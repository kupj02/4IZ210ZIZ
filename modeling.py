import pandas as pd
import numpy as np
from IPython.core.display_functions import display
from graphviz import Source

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz
df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df = df[df['smoking_status'] != 'Unknown']
df = df.dropna(subset=['bmi'])  # Vyhod radky s chybejicimi hodnotami BMI
df['gender']=pd.factorize(df['gender'])[0].astype(float)
df['ever_married']=pd.factorize(df['ever_married'])[0].astype(float)
df['work_type']=pd.factorize(df['work_type'])[0].astype(float)
df['Residence_type']=pd.factorize(df['Residence_type'])[0].astype(float)
df['smoking_status']=pd.factorize(df['smoking_status'])[0].astype(float)
# Rozdel dataset do trenovaciho a testovaciho
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

X=df.drop('stroke', axis=1)
y=df['stroke']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
rf = RandomForestClassifier()
rf.fit(X_train,y_train)
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


for i in range(10):
    tree = rf.estimators_[i]
    dot_data = export_graphviz(tree,
                               feature_names=X_train.columns,
                               filled=True,
                               max_depth=2,
                               impurity=False,
                               proportion=True)
    graph: Source = graphviz.Source(dot_data)
    display(graph)
param_dist = {'n_estimators': randint(50,500),
              'max_depth': randint(1,20)}

# Create a random forest classifier
rf = RandomForestClassifier()

# Use random search to find the best hyperparameters
rand_search = RandomizedSearchCV(rf,
                                 param_distributions = param_dist,
                                 n_iter=5,
                                 cv=5)

# Fit the random search object to the data
rand_search.fit(X_train, y_train)
# Create a variable for the best model
best_rf = rand_search.best_estimator_

# Print the best hyperparameters
print('Best hyperparameters:',  rand_search.best_params_)