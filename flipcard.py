from bs4 import BeautifulSoup
import requests
import json
url=" https://www.flipkart.com/apple-iphone-12-purple-128-gb/p/itmebc78f1cb26d3?pid=MOBG2EPZK5ZD9KYS&lid=LSTMOBG2EPZK5ZD9KYSDUOOA2&marketplace=FLIPKART&store=tyyF4io&srno=b_1_24&otracker=browse&fm=organic&iid=e70815d3-42c7-4c16-9a3d-e68cf2aa482e.MOBG2EPZK5ZD9KYS.SEARCH&ppt=None&ppn=None&ssid=awdpsancqo0000001635009470539"
s=requests.get(url)
# print(s)
dic={ }
soup=BeautifulSoup(s.text,"html.parser")
# print(soup)
price=soup.find("div",class_="_30jeq3 _16Jk6d").text
name=soup.find("span",class_="B_NuCI").text[:-19]
colour=soup.find("span",class_="B_NuCI").text[17:23]
rating=soup.find("div",class_="_3LWZlK").text
image = "https://rukminim1.flixcart.com/image/416/416/ko0d6kw0/mobile/6/h/y/iphone-12-mjnm3hn-a-apple-original-imag2k2v6ehvnzfd.jpeg?q=70"
dic["model_name"]=name
dic["Rating"]=rating
dic["price"]=price
dic["colour"]=colour
dic["image_url"]=image
# print(dic)
with open("apple.json","w") as f:
    json.dump(dic,f,indent=4)