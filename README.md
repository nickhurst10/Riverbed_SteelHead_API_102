# Riverbed_SteelHead_API_102
The following three scripts (GET, POST and DELETE) follows on from Riverbed_Steelhead_API_101 script, where we gave examples of performing API GET requests.

The three scripts are as follows;
  1) A GET, to show all the current routes on the device (Riverbed_SteelHead_API_102_GET.py)
  2) A POST, to add a static route to the Primary interface (Riverbed_SteelHead_API_102_POST.py)
  3) A DELETE, to remove the static route we added (Riverbed_SteelHead_API_102_DELETE.py)
  
Order of operations:
1) Run the GET script to see the current routes,
2) Run the POST script to add the static route, followed by GET to verify. 
3) Run the DELETE script to remove the static route, followed by GET to verify.

The script is writen for Python3.

To work in your environment, update the device_ip and access_code variables in the script with the relevant information.

Before the script can work, you’ll need to enable Rest API Access and create an access code.

https://{steelhead_ip_addr}/mgmt/gui?p=setupRESTInterface

The access code is used to request a Bearer token

This script should only be used in a test environment.

If you have any questions please reach out to me.
