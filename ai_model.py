import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
[1,0,0],
[1,1,0],
[1,1,1],
[0,1,0],
[0,0,1],
[0,0,0]
])

y = np.array([
0.2,
0.6,
1.4,
0.4,
1.1,
0.05
])

model = LinearRegression()
model.fit(X,y)


def predict_energy(light,fan,ac):

    features = np.array([[light,fan,ac]])

    prediction = model.predict(features)

    return round(float(prediction[0]),2)


def energy_advice(energy):

    if energy > 1.2:
        return "⚠ High energy usage detected."

    elif energy > 0.6:
        return "Moderate energy usage."

    else:
        return "Energy usage optimal."