import numpy as np
import pandas as pd
import pickle
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Read the data from CSV
df = pd.read_csv('USA_Housing.csv')

# Set up the features and predicting values
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 
        'Avg. Area Number of Bedrooms','Area Population']]
y = df['Price']

#Split the data in training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, 
                                                    random_state = 101)

#Extansiate Linear Regression model
lm = LinearRegression()

#Train the model on training data
lm.fit(X_train, y_train)

pred = lm.predict(X_test)

#Serialize the model on the disk
pickle.dump(lm, open('model.pkl', 'wb'))

print(type(X_test))

# model = pickle.load(open('model.pkl', 'rb'))

# print(model.predict(X_test))
