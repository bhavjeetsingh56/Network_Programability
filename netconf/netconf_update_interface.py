from ncclient import manager
from pprint import pprint

netconf_template = open("config-temp-ietf-interfaces.xml").read()

device = {
    "host":"sandbox-iosxe-recomm-1.cisco.com",
    "port": 830,
    "user": "developer",
    "password": "C1sco12345"
}

if __name__ == "__main__":
    #Configuration Payload to Send
    netconf_payload = netconf_template.format(
        int_name="GigabitEthernet1",
        int_desc="Configured with Netconf",
        ip_address="10.11.11.11",
        subnet_mask="255.255.255.0"
    )

    print("Configuration Payload:")
    print("===============================")
    print(netconf_payload)


    with manager.connect(host=device["host"],
                        username=device["user"],
                        password=device["password"],
                        hostkey_verify=False) as my_manager:
        
        #Send Netconf Payload
        netconf_reply = my_manager.edit_config(netconf_payload, target="running")


        pprint(netconf_reply)
