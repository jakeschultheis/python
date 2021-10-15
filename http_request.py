import requests

url = '$URL' #URL Value

headers = {   'User-Agent': '$USER_AGENT' } #User Agent
 
r = requests.get (url, headers=headers)
print (f"Status code: {r.status_code}")
print (f"Headers: {r.headers}")
