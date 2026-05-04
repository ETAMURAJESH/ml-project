from numpy._core.fromnumeric import reshape
X = np.array ([1,2,3,4,5]).reshape(-1,1)

y = np.array([20,30,80,110,160])

model = LinearRegression()

model. fit(X,y)


# preduction 

predicted = model.predict([[10]])

print("predicted marks:", predicted)