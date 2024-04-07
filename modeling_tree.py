import graphviz
from IPython.core.display_functions import display
from graphviz import Source
from six import StringIO
from sklearn import metrics
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier

from preprocessing import X_train, y_train, X_test, y_test, X, feature_cols
from sklearn.tree import export_graphviz
from IPython.display import Image
import pydotplus

clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


dot_data = export_graphviz(clf,
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph: Source = graphviz.Source(dot_data)
display(graph)

