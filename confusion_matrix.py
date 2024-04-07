from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from new_preprocessing import y_test, X_train, y_train, X_test

clf_rf =RandomForestClassifier()
clf_rf.fit(X_train, y_train)

y_pred_rf = clf_rf.predict(X_test)
cm=confusion_matrix(y_test, y_pred_rf)
cm
tn, fp, fn, tp = cm.ravel()
print("tn:"+str(tn), "fp:"+ str(fp),"fn:" + str(fn), "tp:" + str(tp))