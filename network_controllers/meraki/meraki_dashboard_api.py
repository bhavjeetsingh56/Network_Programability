import requests
from pprint import pprint


headers = {
    "X-Cisco-Meraki-API-Key": "49f646908b8da1eec8e876e87ac85ad5af5a08ec"
}



def get_organization_id():
    URL = "https://dashboard.meraki.com/api/v1/organizations"
    response = requests.get(URL, headers=headers)
    
    #Targetting a specific organization
    for element in response.json():
        if element["name"] == "DevNet Sandbox":
            return element["id"]

def get_networks_under_specific_organizations(org_id):
    URL = "https://dashboard.meraki.com/api/v1/organizations/{}/networks".format(org_id)
    response = requests.get(URL, headers=headers)
    for network_dict in response.json():
        if network_dict["name"] == "DevNet Sandbox ALWAYS ON":
            return network_dict["id"]

def get_devices_for_network_under_organization(org_id, net_id):
    URL = "https://dashboard.meraki.com/api/v1/organizations/{}/networks/{}/devices".format(org_id, net_id)
    print(URL)
    response = requests.get(URL, headers=headers)
    return response.json()



organization_id = get_organization_id()
network_id = get_networks_under_specific_organizations(org_id=organization_id)
devices = get_devices_for_network_under_organization(org_id=organization_id, net_id=network_id)


pprint(devices)