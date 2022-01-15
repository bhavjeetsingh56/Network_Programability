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


headers = {"Content-type": "application/json-rpc"}

payload = [
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "show vlan brief",
            "version": 1
        },
        "id": 1
    }
]

response = requests.post(URL, data=json.dumps(payload), headers=headers, auth=(nx_device["username"], nx_device["password"]), verify=False)
vlan_list = response.json()["result"]["body"]["TABLE_vlanbriefxbrief"]["ROW_vlanbriefxbrief"]

human_readable_vlan_dict = dict()
human_readable_vlan_list = list()

for vlan_dict in vlan_list:
    human_readable_vlan_list.append({
        vlan_dict["vlanshowbr-vlanid"] : vlan_dict["vlanshowplist-ifidx"]
    })


for vlan_dict in human_readable_vlan_list:
    for key, value in vlan_dict.items():
        print("{}  ----->   {}".format(key, value))






