#!/usr/bin/python3
# http_get_py - js

import urllib3

headers = {
   'User-Agent': '(UserAgentTest)'
}

http = urllib3.PoolManager()

url = 'http://127.0.0.1'

resp = http.request('GET', url, headers=headers)

http_data = (resp.status, resp.reason, resp.headers, resp.data)
print (http_data)
