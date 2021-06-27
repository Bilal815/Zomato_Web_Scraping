import requests
from bs4 import BeautifulSoup
import pandas

#Used headers/agent because the request was timed out and asking for an agent.
#Using the following code we can fake the agent
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get("https://www.zomato.com/ncr", headers=headers)

content = response.content
soup = BeautifulSoup(content, "html.parser")

list_tr = soup.find_all("div",attrs={"class": "sc-fFTYTi eCHMNV"}) 
list_tr += soup.find_all("div",attrs={"class": "sc-DNdyV jNXpDU"})
list_tr += soup.find_all("div",attrs={"class": "sc-DNdyV ktTzui"})

list_rest = []
for tr in list_tr:
    dataframe = {}
    dataframe["rest_name"] = (tr.find("div", attrs={"class": "sc-1hez2tp-0 sc-izvnbC"}))
    dataframe["rest_name"] += (tr.find("div", attrs={"class": "sc-1hez2tp-0 sc-hvvHee ifyMgS"}))
    
    dataframe["Delivery_time"] = (tr.find("div", attrs={"class": "sc-1hez2tp-0 sc-bYTsla bVNAPi"}))
    dataframe["Delivery_time"] += (tr.find("div", attrs={"class": "sc-1hez2tp-0 sc-dKEPtC iavONs"}))
    
    dataframe["No_of_reviews"] += (tr.find("div", attrs={"class": "sc-1hez2tp-0 lhdg1m-8 hztxkg"}))
    dataframe["No_of_reviews"] += (tr.find("div", attrs={"class": "sc-1hez2tp-0 lhdg1m-8 hztxkg"}))
    
    dataframe["Cuisines"] += (tr.find("div", attrs={"class": "sc-1hez2tp-0 sc-cbMPqi dMrcTM"}))
    list_rest.append(dataframe)
list_rest

df = pandas.DataFrame(list_rest)
df.to_csv("zomato_res.csv", index=False)
