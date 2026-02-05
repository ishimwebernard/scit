# Import libraries
from sklearn.linear_model import LogisticRegression
# Define input and output data
data = [[1.5, 0], [2.4, 1], [3.4, 1 ], [2.1, 0 ], [2.5, 1 ],
[0.8, 0 ], [2.9, 0 ], [4.0, 1], [2.3, 1], [2.1, 0], [3.6, 1 ], [0.5, 0]]
# Separate features (X) and labels (y)
X = [[row[0]] for row in data] # Feature
y = [row[1] for row in data]
 # Label
# Build the logistic model
Lmodel = LogisticRegression()
Lmodel.fit(X,y)
# Display the coefficients of the logistic regression
(a,b) = (Lmodel.intercept_[0], Lmodel.coef_[0,0])
print("Coefficients: ", (round(a,3),round(b,3)))
# Display the accuracy of the model
s = Lmodel.score(X,y)
print("Accuracy: ", round(s, 3))