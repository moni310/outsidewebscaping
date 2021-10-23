from bs4 import BeautifulSoup
import requests
def fun():
    url="https://www.boohoo.com/womens/skirts"
    url1=requests.get(url)
    soup=BeautifulSoup(url1.text,"html.parser")
    # print(soup)
    d_name=soup.find_all("a",class_="name-link js-canonical-link")
    s=soup.find_all("span",class_="product-sales-price")
    m=""
    for i in s:
        dic={}
        m=i.text
        n=m.split()
        # dic["price"]=m
        for j in d_name:
            name=j.text[1:]
            dic["dress_name"]=name[:-2]
            dic["price"]=n
            print(dic)
fun()



