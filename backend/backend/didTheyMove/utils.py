from .models import DidTheyMove, HomeData
from dotenv import load_dotenv
import os
import http.client
import json

RAPID_API = os.getenv('FLOOR_TOKEN')

def getAllZipcodes(client):
    print("hello")
    clientCustomers = list(DidTheyMove.objects.filter(client=client.upper()).values('zipCode').distinct())[0]
    getHomesForSale(clientCustomers['zipCode'])
    getHomesForRent(clientCustomers['zipCode'])

def getHomesForSale(zipCode):
    offset = 0
    # conn = http.client.HTTPSConnection("us-real-estate.p.rapidapi.com")

    # headers = {
    #     'X-RapidAPI-Key': RAPID_API,
    #     'X-RapidAPI-Host': "us-real-estate.p.rapidapi.com"
    #     }

    # conn.request("GET", f"/v2/for-sale-by-zipcode?zipcode={zipCode}&offset={offset}&limit=200", headers=headers)

    # res = conn.getresponse()
    # data = res.read().decode("utf-8")
    # data = json.loads(data)
    with open("/Users/reidelkins/Solana/didTheyMove/t1.json", "r") as f:
        data = json.load(f)
    # with open("/Users/reidelkins/Solana/didTheyMove/t1.json", "w") as f:
    #     print("t1")
    #     json.dump(data, f)
    total = data['data']['home_search']['total']
    offset += data['data']['home_search']['count']
    data = data['data']['home_search']['results']
    print(total)
    print(offset)
    # with open("/Users/reidelkins/Solana/didTheyMove/t2.json", "w") as f:
    #     print("t2")
    #     json.dump(data, f)
    
    
    for d in data:
        HomeData.objects.update_or_create(address=d['location']['address']['line'], zipCode=zipCode, status='For Sale', listDate=d['list_date'][:-10], property_id=d['property_id'])
    print("for sale")

def getHomesForRent(zipCodes):
    print("for rent")

