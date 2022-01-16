import requests
import json
import urllib3
from pprint import pprint

headers = {
    "content-type": "application/json",
    "Accept": "application/json",
    "x-auth-token": ""
}
dna_centre = {
    "host": "sandboxdnac.cisco.com",
    "port": 443,
    "username": "devnetuser",
    "password": "Cisco123!"
}

def dna_centre_login(ip, port, username, password):
    #Using the RESTAPI to login into the DNA Centre and retrieve the token.
    url = "https://{}:{}/dna/system/api/v1/auth/token/".format(ip, port)

    #Make Login Request and make the response body.
    response = requests.request("POST", url, auth=(dna_centre["username"], dna_centre["password"]), headers=headers, verify=False)
    return response.json()["Token"]


def network_device_list(host, token):
    #USE THE RESTAPI TO GET THE LIST OF NETWORK DEVICES MANAGED BY CISCO DNA.

    url = "https://{}/dna/intent/api/v1/network-device".format(dna_centre["host"])
    headers["x-auth-token"] = token


    #Make API request and return the response body.
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.json()["response"]



if __name__ == "__main__":
    #Login to the DNA Centre Controller to get the token
    token = dna_centre_login(ip=dna_centre["host"], port=dna_centre["port"], username=dna_centre["username"], password=dna_centre["password"])
    #print(token)

    #Get the list of devices
    devices = network_device_list(dna_centre["host"], token)
    


    for device in devices:
        print("{} in family {}".format(device["hostname"],
        device["family"]))
        print(" Management IP: {}".format(
        device["managementIpAddress"]))
        print(" Platform Type: {}".format(device["platformId"]))
        print(" Software Version: {}".format(device["softwareVersion"]))
        print("")

