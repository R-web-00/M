# -*- coding: utf-8 -*-
"""LogisticRegression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IlrtpPAcEhS4lCYR9tbo5L8gv-2_88a2
"""

import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix ,classification_report

df=pd.read_csv('titanic-data.csv')
df.info()

df.head()

df = df[['Survived', 'Age', 'Sex', 'Pclass']]
df=pd.get_dummies(df,columns=['Sex','Pclass'])
df.dropna(inplace=True)
df.head()

x=df.drop('Survived',axis=1)
y=df['Survived']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LogisticRegression(random_state=0)
model.fit(x_train,y_train)

model.score(x_test,y_test)

y_pred=model.predict(x_test)

confusion_matrix(y_test,y_pred)
print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test, y_pred))

female = [[30, 1, 0, 1, 0, 0]]
model.predict(female)[0]

male = [[60, 0, 1, 0, 0, 1]]
model.predict(male)[0]