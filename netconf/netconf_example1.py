from ncclient import manager
from pprint import pprint

ios_xe_device = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": 830,
    "user": "developer",
    "password": "C1sco12345"
}

if __name__ == "__main__":
    with manager.connect(host=ios_xe_device["host"],
                        port=ios_xe_device["port"],
                        username=ios_xe_device["user"],
                        password=ios_xe_device["password"],
                        hostkey_verify=False) as my_manager:

        print("Below are netconf Capabilities: ")
        for capability in my_manager.server_capabilities:
            print(capability)


