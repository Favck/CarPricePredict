from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import random
import time
import json

linkCars = []
with open("linkCars.txt", "r", encoding="UTF-8") as file:
    linkCars = [i[:-1] for i in file.readlines()]


dictCars = {"name":[],"V":[], "P":[], "Distance":[], "countPeople":[], "Price":[]}
# Цена|  Пробег, объём двигателя, мощность, марка, владельцы
k = len(set(linkCars))
err = 0
for i in set(linkCars):
    k-=1
    print("Go: ", k, "err: ", err)
    try:
        url = i
        resp = requests.get(url=url)
        soup = BeautifulSoup(resp.text, "html.parser")
        time.sleep(random.randint(0, 1))

        div = soup.find("div",  {"data-app-root":"bull-page"}).find("div", {"class":"ftldj60 css-1yado2t"}).find("div", {"class":"css-0 epjhnwz1"})
        divPrice = div
        div_temp = div.find("div", {"class":"css-10ib5jr i2nf562"}).find_all("tr")
        Price = divPrice.find("div",{"class":"wb9m8q0"}).get_text()
        sp = []
        try:
            dictCars["Price"].append(Price)
        except:
            dictCars["Price"].append(None)

        for j in div_temp:
            sp.append(j.find("td").get_text())
        sp = [item for item in sp if item]

        try:
            dictCars["V"].append(sp[0])
        except:
            print("V")
            dictCars["V"].append(None)
        try:
            dictCars["P"].append(sp[1])
        except:
            print("P")
            dictCars["P"].append(None)
        temp = 0
        try:
            if "км" in sp[5] or "нов" in sp[5]:
                temp = 5
                dictCars["Distance"].append(sp[5])
            elif "км" in sp[6] or "нов" in sp[6]:
                temp = 6
                dictCars["Distance"].append(sp[6])
            elif "км" in sp[4] or "нов" in sp[4]:
                temp = 4
                dictCars["Distance"].append(sp[4])
            else:
                dictCars["Distance"].append(None)
        except:
            print("Distance")
            dictCars["Distance"].append(None)
        try:
            dictCars["countPeople"].append(sp[temp+1])
        except:
            print("countPeople")
            dictCars["countPeople"].append(None)
        dictCars["name"].append(i)
    except:
        dictCars["V"].append(None)
        dictCars["P"].append(None)
        dictCars["Distance"].append(None)
        dictCars["countPeople"].append(None)
        dictCars["name"].append(i)
        dictCars["Price"].append(None)
        err += 1
        print("Error")
        continue

with open("data.json", 'w', encoding='UTF-8') as file:
    json.dump(dictCars, file, ensure_ascii=False, indent=4)

data = pd.DataFrame(dictCars)
    
data.to_csv("Data.csv")