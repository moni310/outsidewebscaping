from bs4 import BeautifulSoup
import requests
import json
url="https://affyo.com/networks/gamblingpro/ "
s=requests.get(url)
# print(s)
soup=BeautifulSoup(s.text,"html.parser")
# print(soup)
div=soup.find("div",id="bo")
div1=div.find("div",class_="wr").text
print(div1)
list1=[div1]
# print(list1)







