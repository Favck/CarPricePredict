from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def target_encoding(data):


    stats = data.groupby('name').Price.agg(["count", "mean"])
    global_mean = data["Price"].mean()
    alpha = 1
    # print((stats["count"]*stats["mean"] + global_mean*alpha)/(stats["count"]+alpha))
    return (stats["count"]*stats["mean"] + global_mean*alpha)/(stats["count"]+alpha)

    

with open("data.json", "r") as file:
    data = json.load(file)
sp = ["Price", "Distance", "P", "V", "countPeople"]

dataCar = pd.DataFrame(data)
index = []
for i in range(len(dataCar["Price"])):
    if dataCar["Price"][i] is None:
        index.append(i)
    
    if dataCar["Distance"][i] is None:
        index.append(i)

dataCar = dataCar.drop(index)
# dataCar.to_csv("Data.csv")

dataCar = dataCar[(dataCar["V"].str.contains("л"))]

dataCar["V"] = dataCar["V"].str.replace("бензин, ", "")\
    .str.replace(",", " ").str.replace("л", "")\
    .str.replace("дизеь", "").str.replace("ГБО", "")\
    .str.replace("гибрид", "").str.replace("эектро", "0.0")

dataCar["P"] = dataCar["P"].str.replace("налог", "").str.replace("л.с.,", "")


mask = ~dataCar["V"].str.contains("н")
dataCar = dataCar[mask]

mask = ~dataCar["P"].str.contains("м")
dataCar = dataCar[mask]
dataCar["P"] = dataCar["P"].astype(float)

dataCar["V"] = dataCar["V"].astype(float)

dataCar["Distance"] = dataCar["Distance"].str.replace("новый автомобиль", "0").str.replace("км", "").str.replace(",", "")\
    .str.replace("без", "").str.replace("пробега", "").str.replace("по","").str.replace("РФ","").str.replace("\xa0", "")
dataCar["Distance"] = dataCar["Distance"].astype(float)

dataCar["countPeople"] = dataCar["countPeople"].str.replace("левый", "0").str.replace("и", "").str.replace("более", "")\
    .str.replace("правый", "0")
dataCar["countPeople"] = dataCar["countPeople"].astype(float)
dataCar["Price"] = dataCar["Price"].str.replace("₽", "").str.replace("\xa0", "")
dataCar["Price"] = dataCar["Price"].astype(float)

dataCar["name"] = dataCar["name"].str.replace("/"," ").str.split()
dataCar["name"] = dataCar["name"].apply(lambda x: x[3])


dataCar["V"] = dataCar["V"].astype(float)
# dataCar.to_csv("Data.csv")

id = dataCar["Price"].idxmax()
dataCar = dataCar.drop(id)
id = dataCar["Price"].idxmax()
dataCar = dataCar.drop(id)
id = dataCar["P"].idxmax()
dataCar = dataCar.drop(id)
id = dataCar["Distance"].idxmax()
dataCar = dataCar.drop(id)
id = dataCar["Distance"].idxmax()
dataCar = dataCar.drop(id)


name_encoding = target_encoding(dataCar)
name_enc = name_encoding.reset_index()
name_enc.columns = ['name', 'enc']
# print(name_enc)
dataCar = dataCar.merge(name_enc, on='name', how='left')

# dataCar_train.to_csv("dataTrain.csv")
dataCar["name"] = dataCar["enc"]
del dataCar['enc']

dataCar.to_csv("data.csv")


data_test = dataCar.truncate(before=300)
dataCar_train = dataCar.truncate(after=300)




# print(dataCar_train)


#SCALE
name_max, name_min = dataCar_train["name"].max(), dataCar_train["name"].min()
V_max, V_min =  dataCar_train["V"].max(), dataCar_train["V"].min()
P_max, P_min = dataCar_train["P"].max(), dataCar_train["P"].min()
S_max, S_min = dataCar_train["Distance"].max(), dataCar_train["Distance"].min()
peop_max, peop_min = dataCar_train["countPeople"].max(), dataCar_train["countPeople"].min()
price_max, price_min = dataCar_train["Price"].max(), dataCar_train["Price"].min()

dataCar_train["name"] = (dataCar_train["name"] - name_min)/(name_max-name_min)
dataCar_train["V"] = (dataCar_train["V"] - V_min)/(V_max-V_min)
dataCar_train["P"] = (dataCar_train["P"] - P_min)/(P_max-P_min)
dataCar_train["Distance"] = (dataCar_train["Distance"] - S_min)/(S_max-S_min)
dataCar_train["countPeople"] = (dataCar_train["countPeople"] - peop_min)/(peop_max-peop_min)
dataCar_train["Price"] = (dataCar_train["Price"] - price_min)/(price_max-price_min)

data_test["name"] = (data_test["name"] - name_min)/(name_max-name_min)
data_test["V"] = (data_test["V"] - V_min)/(V_max-V_min)
data_test["P"] = (data_test["P"] - P_min)/(P_max-P_min)
data_test["Distance"] = (data_test["Distance"] - S_min)/(S_max-S_min)
data_test["countPeople"] = (data_test["countPeople"] - peop_min)/(peop_max-peop_min)
data_test["Price"] = (data_test["Price"] - price_min)/(price_max-price_min)

# dataCar_train.to_csv("dataTrain.csv")
# data_test.to_csv("dataTest.csv")