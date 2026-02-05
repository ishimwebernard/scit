from sklearn.linear_model import LogisticRegression

data = [[1.5, 0], [2.4, 1], [3.4, 1 ], [2.1, 0 ], [2.5, 1 ],[0.8, 0 ], [2.9, 0 ], [4.0, 1], [2.3, 1], [2.1, 0], [3.6, 1 ], [0.5, 0]]
X = [[row[0]] for row in data]
y = [[row[1]] for row in data]
Lmodel = LogisticRegression()
Lmodel.fit(X,y)
(a,b) = (Lmodel.intercept_[0], Lmodel.coef_[0,0])
print("Coefficients: ", round(a,3), round(b,3))
s = Lmodel.score(X,y)
print("Accuracy: ", round(s,3))