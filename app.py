import requests
from bs4 import BeautifulSoup

#Used headers/agent because the request was timed out and asking for an agent.
#Using the following code we can fake the agent
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get("https://www.zomato.com/ncr/connaught-place-delhi-restaurants", headers=headers)

content = response.content
soup = BeautifulSoup(content, "html.parser")

top_rest = soup.find_all("div",attrs={"class": "sc-7kepeu-0 sc-TZjqS laOdpC"})
list_tr = soup.find_all("div",attrs={"class": ["sc-aewfc", "jumbo-tracker"]})

list_rest = []
for tr in list_tr:
    dataframe = {}
    dataframe["rest_name"] = (tr.find("div", attrs={"class": ["sc-1hez2tp-0 sc-iupvsZ", "sc-1hez2tp-0 sc-hCaUpS", "sc-1hez2tp-0 sc-bvTASY"]}))
    dataframe["delivery_time"] = (tr.find("div",attrs={"class": ["sc-1hez2tp-0 sc-goBNrf", "sc-1hez2tp-0 sc-bSbAYC"]}))
    list_rest.append(dataframe)
list_rest
print(list_rest)
