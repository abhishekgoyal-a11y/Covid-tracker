import requests
import json
from pprint import pprint
url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "933662c0c9msh015e7b88e232d19p1c9fe5jsn22d671dc690d"
    }

response = requests.request("GET", url, headers=headers)

a=json.loads(response.text)
state_wise = a['state_wise']
district='agra'
def get_cases(state,city):
    confirmed=(state_wise[state]['district'][city]['confirmed'])
    death=(state_wise[state]['district'][city]['deceased'])
    recovered=(state_wise[state]['district'][city]['recovered'])
    active=(state_wise[state]['district'][city]['active'])
    return confirmed,death,recovered,active

for i in state_wise:
    print(i)
    for j in state_wise[i]['district']:
        c,d,r,a=get_cases(i,j)
        print('                  ',j)
        print('                           confirmed',c)
        print('                           death',d)
        print('                           recovered',r)
        print('                           active',a)
    print("\n")

