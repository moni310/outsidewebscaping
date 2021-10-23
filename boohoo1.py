from bs4 import BeautifulSoup
import requests
import json
url="https://www.boohoo.com/cut-out-detail-mini-skirt/FZZ34266.html?color=123"
s=requests.get(url)
# print(s)
soup=BeautifulSoup(s.text,"html.parser")
print(soup)
price=soup.find("span",class_="price-sales").text
p=price.split()
# colour=soup.find("ul",class_="swatches color clearfix")
c=soup.find("span",class_="selected-value").text
colour=c.split()
size=soup.find("div",class_="attribute size-attribute").text
s=size.split()
m=s[4:-3]
# m1=m[:-3]
dic={ }
dic["price"]=p
dic["colour"]=colour

dic["size"]=m
# print(dic)
with open("boohoo.json","w") as f:
    json.dump(dic,f,indent=4)