"""
This is a Steelhead API 102 script, 1 of 3, following on from Steelhead API 101 script. 
The goal of this script, using a GET API call, is to show all the current routes on the SteelHead.
If you have any questions please reach out to me.
"""

__author__ = "Nick Hurst nhurst@riverbed.com"

import requests
import json
import time

#Your SteelHead mgmt IP address
device_ip = '192.168.111.109'

#You'll need to create an access code from the steelhead, Administration -> Security -> REST API Access
#https://{steelhead_ip_addr}/mgmt/gui?p=setupRESTInterface
#this access code is required to get a Bearer Token
access_code = "eyJhbGciOiJub25lIn0K.eyJhdWQiOiAiaHR0cHM6Ly8xNDItTEFCL2FwaS9jb21tb24vMS4wL3Rva2VuIiwgImlzcyI6ICJodHRwczovLzE0Mi1MQUIiLCAicHJuIjogImFkbWluIiwgImp0aSI6ICI3Y2ZiZjg0MS0wYWNjLTQ5M2MtYWIxOS00NTJlZmM5NDVjOGUiLCAiZXhwIjogIjAiLCAiaWF0IjogIjE1ODg2MTY2MTUifQ=="

#initial post url to get Bearer token
url = "https://"+device_ip+"/api/common/1.0/oauth/token?Content-type=application/x-www-form-urlencoded&Accept=application/json"

#with access code create API request payload
payload = 'grant_type=access_code&assertion=eyJhbGciOiJub25lIn0K.'+access_code+'.&state=state_string'

#Post request... Verify false, is due to not trusting the self signed cert of the SteelHead
response = requests.request("POST", url, data = payload,verify=False)

#get response in json format, we now have the Bearer Token
json_response = response.json()

#print out response in a more readable format
print(json.dumps(json_response, indent = 6, sort_keys=True))

#create the API header using the Bearer Token for authentication and authorization
#Plus insuring the response is a json format.
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+json_response["access_token"],
}

#the url, for the location of objects we wish to access
url_feed="/api/mgmt.til.networking/1.0/routes/ipv4"

#create the full url for query
url = 'https://'+device_ip+url_feed
print (url)

#GET request...
response = requests.get(url, headers=headers, verify=False)

#get response in json format: we now have all the routes
data_info = (response.json())

print(json.dumps(data_info, indent = 6, sort_keys=True))
