from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

dataset=data.values
X=dataset[:,0:-1]
y=dataset[:,-1]
X=X.astype(str)
y=y.reshape((len(y),1))
ohe=OneHotEncoder()
ohe.fit(X)
X_oenc = ohe.transform(X)
le=LabelEncoder()
le.fit(y)
y_enc=le.transform(y)
X_oenc_train, X_oenc_test, y_enc_train, y_enc_test = train_test_split(X_oenc, y_enc, test_size=0.4, random_state=1)
clfs=RandomForestClassifier()
scores = cross_val_score(clfs, X_oenc_train, y_enc_train.ravel(), cv=5, scoring = 'f1')
clf = clfs.fit(X_oenc_train, y_enc_train.ravel())
Y_pred = clf.predict(X_oenc_test)
f1 = f1_score(y_enc_test, Y_pred)
print ("%0.2f", f1)