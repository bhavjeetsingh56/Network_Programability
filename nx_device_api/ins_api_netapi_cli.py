import requests
import json
from pprint import pprint



URL= "https://sandbox-nxos-1.cisco.com/ins"

nx_device = {
    "host": "sandbox-nxos-1.cisco.com",
    "port": 443,
    "username": "admin",
    "password": "Admin_1234!"
}


headers = {"Content-type": "application/json"}

payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show ip interface brief vrf management",
    "output_format": "json"
  }
}


response = requests.post(URL, data=json.dumps(payload), headers=headers, auth=(nx_device["username"], nx_device["password"]), verify=False)
prefix = response.json()["ins_api"]["outputs"]["output"]["body"]["TABLE_intf"]["ROW_intf"]["prefix"]

print(prefix)








