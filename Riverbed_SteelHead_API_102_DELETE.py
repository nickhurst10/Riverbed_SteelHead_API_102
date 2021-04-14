"""
This is a Steelhead API 102 script, 3 of 3.
The goal of this script, using an API DELETE call, is to remove the static route we added in the POST script.
If you have any questions please reach out to me
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

#POST request to get Bearer Token... Verify false, is due to not trusting the self signed cert of the SteelHead
response = requests.request("POST", url, data = payload,verify=False)

#get response in json format, we now have the Bearer Token
json_response = response.json()

#print out response in a more readable format
print(json.dumps(json_response, indent = 6, sort_keys=True))

#create the API header using the Bearer Token for authentication and authorization
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer '+json_response["access_token"],
}

#the url, for the location of object we wish to access
url_feed="/api/mgmt.til.networking/1.0/routes/ipv4"

# the ID of the odject we wish to DELETE
id_delete='/0.0.0.0-0-192.168.111.240-primary'


#create the full url for query
url = 'https://'+device_ip+url_feed+id_delete
#DELETE request...
response = requests.delete(url, headers=headers, verify=False)

#printer response, which should be a 204
print (response)
