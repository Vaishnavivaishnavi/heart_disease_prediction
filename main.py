import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

heart_data = pd.read_csv('/content/data.csv')

heart_data.head()

heart_data.tail()

heart_data.shape

heart_data.info()

heart_data.isnull().sum()

heart_data.describe()

heart_data['target'].value_counts()

"""1 --> Defective Heart

0 --> Healthy Heart

Splitting the Features and Target
"""

X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

print(X)

print(Y)

"""Splitting the Data into Training data & Test Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training

Logistic Regression
"""

model = LogisticRegression()

model.fit(X_train, Y_train)

"""Model Evaluation

Accuracy Score
"""

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training data : ', training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on Test data : ', test_data_accuracy)

"""Building a Predictive System"""

input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

input_data_as_numpy_array= np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')