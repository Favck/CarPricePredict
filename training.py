import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataCar_train = pd.read_csv("dataTrain.csv")
target = np.array(dataCar_train["Price"])
X = np.array(dataCar_train.iloc[:, :-1])
X = np.insert(X, 0, [1 for _ in range(X.shape[0])], axis=1)
mask = ~np.isnan(X).any(axis=1)
X = X[mask]
target = target[mask]

w = np.random.rand(X.shape[1]) 
w_old = np.zeros(X.shape[1])

alpha = 1e-2
tolerance = 1e-6
N = X.shape[0]

while np.linalg.norm(w-w_old) > tolerance:
    f = X@w
    err = f-target
    w_old = w.copy()
    w-= alpha*2*X.T.dot(err)/N

# np.save("weight", w)



