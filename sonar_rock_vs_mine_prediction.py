# -*- coding: utf-8 -*-
"""Sonar Rock vs Mine prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dmRyMr2hxhfztwXupD0hLia-fMRWsoI8

Importing Libraries
"""

import numpy as np #for array
import matplotlib as mtl # for graph
import pandas as pd # for data pre processing
from sklearn.model_selection import train_test_split #to split data in train or test data
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score

"""Data collection and data processing"""

#loading the data set to the pandas data frame
sonar_data = pd.read_csv('sonar.csv', header = None)

sonar_data.head() #it will display the first five row of our data

#to find number of rows and column in sonar.csv
sonar_data.shape

sonar_data.describe() #describe--> statistical measures of the data

sonar_data[60].value_counts() #[60] --> column index

"""more the data more accurate the model is"""

sonar_data.groupby(60).mean() #this will give us mean value of 60 columns for Rock or Mine through which we can predict either object is rock or mine

#separting data(integers) and label(rock/mine)
X = sonar_data.drop(columns = 60, axis = 1) #for column axis =1 and for row axis =0
Y = sonar_data[60]

print(X)
print(Y)

"""Splitting traing and test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size= 0.1, stratify = Y, random_state= 1)

print(X.shape,X_test.shape, X_train.shape)

"""Now we train our model --> Logistic regression"""

model = LogisticRegression()

#training the logistic regression model with training data
model.fit(X_train, Y_train)

"""Model Evaluation"""

#accuracy on the training data (>70 is good)
X_train_prediction = model.predict(X_train)
traning_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on traing data: ',traning_data_accuracy)

#accuracy on the test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on tes data: ', test_data_accuracy)

#making a predictive system
input_data = (0.0249,0.0119,0.0277,0.0760,0.1218,0.1538,0.1192,0.1229,0.2119,0.2531,0.2855,0.2961,0.3341,0.4287,0.5205,0.7087,0.7236,0.7577,0.7726,0.8098,0.8995,0.9247,0.9365,0.9853,0.9776,1.0000,0.9896,0.9076,0.7306,0.5758,0.4469,0.3719,0.2079,0.0955,0.0488,0.1406,0.2554,0.2054,0.1614,0.2232,0.1773,0.2293,0.2521,0.1464,0.0673,0.0965,0.1492,0.1128,0.0463,0.0193,0.0140,0.0027,0.0068,0.0150,0.0012,0.0133,0.0048,0.0244,0.0077,0.0074)
#changing the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting the one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)

print(prediction)

if prediction[0] == 'R':
  print("it is rock")
else:
  print('alert it is a mine')

