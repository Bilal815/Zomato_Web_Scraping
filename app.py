import requests
from bs4 import BeautifulSoup

#Used headers/agent because the request was timed out and asking for an agent.
#Using the following code we can fake the agent
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.zomato.com/ncr", headers=headers)

content = response.content
soup = BeautifulSoup(content, "html.parser")

top_rest = soup.find_all("div",attrs={"class": "sc-7kepeu-0 sc-kxixoS wvMYK"})
list_tr = soup.find_all("div",attrs={"class": "sc-iLVFha"}) 
list_tr = list_tr + soup.find_all("div",attrs={"class": "sc-aewfc"}) 

print(response)