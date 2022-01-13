import requests
import json

url = "https://sandbox-iosxe-recomm-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet2",
    "description": "Configured by RESTCONF Demo 2",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "10.255.255.1",
          "netmask": "255.255.255.0"
        }
      ]
    },
    "ietf-ip:ipv6": {}
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("PUT", url, headers=headers, data=payload, verify=False)





payload={}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

