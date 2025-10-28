import numpy as np
from scriptClearData import data_test, dataCar_train
import matplotlib.pyplot as plt

w = np.load("weight.npy")

X_train = np.array(dataCar_train.iloc[:, :-1])
X_train = np.insert(X_train, 0, [1 for _ in range(X_train.shape[0])],axis=1)
Y_train = np.array(dataCar_train["Price"])
mask = ~np.isnan(X_train).any(axis=1)
X_train = X_train[mask]
Y_train = Y_train[mask]

X_test = np.array(data_test.iloc[:, :-1])
X_test = np.insert(X_test, 0, [1 for _ in range(X_test.shape[0])],axis=1)
Y_test = np.array(data_test["Price"])
mask = ~np.isnan(X_test).any(axis=1)
X_test = X_test[mask]
Y_test = Y_test[mask]



print("MSE_train: ", np.mean((Y_train - X_train@w)**2))
print("MSE_test: ", np.mean((Y_test - X_test@w)**2))

plt.scatter(Y_test, X_test@w, color='red')
plt.plot(Y_test,Y_test, label="True line")
plt.show()