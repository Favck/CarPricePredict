from bs4 import BeautifulSoup
import requests

def massiveCarLinks(links):
    linkCars = []
    for i in links:
        if ".html" in str(i)[-1:-7]:
            linkCars.append(i)
        else:
            try:
                url = i
                response = requests.get(url=url)
                soup = BeautifulSoup(response.text, "html.parser")

                div1 = soup.find('div', {"data-app-root":"bulls-list-auto"}).find("div", {"class":"ftldj64 css-flpniz"}).find("div", {"class":"ftldj61"})\
                    .find("div", {"class":"sptubg0 css-flpniz"})
                k=0
                for link in div1.find_all('a'):
                    if k != 3:
                        linkCars.append(link["href"])
                        k+=1
                    else:
                        break
            except:
                continue
    return linkCars
    

# load web site
url = "https://auto.drom.ru/"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
print(response.status_code)


div1 = soup.find('div', {"data-app-root":"bulls-list-auto-home"})
div2 = div1.find('div', {"class":"ftldj64 css-flpniz"})
div3 = div2.find('div', {"class":"ftldj61"})
a = div3.find_all('a')
links = []
for link in a:
    if link["href"]!="https://auto.drom.ru/all/page2/":
        links.append(link["href"])
    else:
        break

links = links[10:]

linkCars = massiveCarLinks(links)
print(linkCars)
# with open("linkCars.txt", "w", encoding="UTF-8") as file:
#     for i in linkCars:
#         file.write(i + "\n")

