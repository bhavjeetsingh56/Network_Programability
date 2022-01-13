from pprint import pprint
from ncclient import manager
import xmltodict

netconf_filter=open("ietf-interfaces-filter.xml").read()
#print(netconf_filter)

device = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": 830,
    "user": "developer",
    "password": "C1sco12345"
}

if __name__ == "__main__":
    with manager.connect(
                    host=device["host"],
                    port=device["port"],
                    username=device["user"],
                    password=device["password"],
                    hostkey_verify=False) as my_manager:
        
        #Get Configuration and state information for interface
        netconf_reply = my_manager.get(netconf_filter)
        #pprint(netconf_reply)

        #Process the XML and store in Dictionary
        intf_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
        intf_config = intf_details["interfaces"]["interface"]
        intf_info = intf_details["interfaces-state"]["interface"]

        print("")
        print("Interface Details")
        print(" Name: {}".format(intf_config["name"]["#text"]))
        print(" Description: {}".format(intf_config["description"]))
        print(" Type: {}".format(intf_config["type"]["#text"]))
        print(" Mac Address: {}".format(intf_info["phys-address"]))
        print(" Packets Input: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
        print(" Packets Output: {}".format(intf_info["statistics"]["out-unicast-pkts"]))

