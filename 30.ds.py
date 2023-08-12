from sklearn.tree import DecisionTreeRegressor
import numpy as np
data = np.array([
    [50000, 3, 20000],
    [80000, 5, 15000],
    [30000, 2, 25000],
    [60000, 4, 18000],
    # ... add more data
])

X = data[:, :-1]
y = data[:, -1]
new_car_features = [int(input("Enter mileage: ")), int(input("Enter age (in years): "))]

regressor = DecisionTreeRegressor(random_state=42)
regressor.fit(X, y)
predicted_price = regressor.predict([new_car_features])

print(f"Predicted price: ${predicted_price[0]:,.2f}")
