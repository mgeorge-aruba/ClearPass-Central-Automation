import pyclearpass
from pycentral.base import ArubaCentralBase
from pyclearpass import *
from pprint import pprint
import json
import credsConfig


def get_gateway_info(central):
    # Sample API call using 'ArubaCentralBase.command()'
    # GET gateways from Aruba Central
    apiPath = "/monitoring/v1/gateways"
    apiMethod = "GET"
    apiParams = {
        "limit": 20,
        "offset": 0
    }
    print("\n\nFetching list of gateways from Aruba Central:\n")
    gateway_resp = central.command(apiMethod=apiMethod,
                                   apiPath=apiPath,
                                   apiParams=apiParams)
    gateway_resp_items = gateway_resp.get('msg').get('gateways')
    pprint(gateway_resp_items)
    return gateway_resp_items



def create_gw_nad(central,gateway_info):
    # Adding gateways to ClearPass as NAD with RadSec disabled
    print("\n\n##########################################################")
    print("\n\nAdding gateways to ClearPass as NAD")
    for gateway in gateway_info:
        if gateway.get('site') is not None and gateway.get('group_name') is not None:
            nad_attributes = {
                'name': gateway.get('name'),
                'ip_address': gateway.get('ip_address'),
                'radius_secret': 'aruba123',
                'tacacs_secret': 'aruba123',
                'vendor_name': 'Aruba',
                'vendor_id': 14823,
                'coa_capable': 'true',
                'coa_port': 3799,
                'radsec_enabled': 'false',
                'attributes': {
                    'Central_Site': gateway.get('site'),
                    'Central_Group': gateway.get('group_name'),
                    'Model': gateway.get('model'),
                    'Serial': gateway.get('serial'),
                    'firmware_version': gateway.get('firmware_version')
                }
            }
            nad_create = pyclearpass.ApiPolicyElements.new_network_device(login, body=nad_attributes)
            print(
                "\nNAD create executed for gateway: " + gateway.get('name') + " with IP: " + gateway.get('ip_address'))
            pprint(nad_create)

        else:
            print("\n Site / Group information missing for Gateway: " + gateway.get('name') + " with IP: " + gateway.get('ip_address'))


def create_gw_nad_radsec(central,gateway_info):
    # Adding gateways to ClearPass as NAD with RadSec enabled
    print("\n\n##########################################################")
    print("\n\nAdding gateways to ClearPass as NAD")
    for gateway in gateway_info:
        if gateway.get('site') is not None and gateway.get('group_name') is not None:
            nad_attributes = {
                'name': gateway.get('name'),
                'ip_address': gateway.get('ip_address'),
                'radius_secret': 'aruba123',
                'tacacs_secret': 'aruba123',
                'vendor_name': 'Aruba',
                'vendor_id': 14823,
                'coa_capable': 'true',
                'coa_port': 3799,
                'radsec_enabled': 'false',
                "radsec_config": {
                    "validate_cert": "NONE",
                    "src_override_ip": gateway.get('ip_address')
                },
                'attributes': {
                    'Central_Site': gateway.get('site'),
                    'Central_Group': gateway.get('group_name'),
                    'Model': gateway.get('model'),
                    'Serial': gateway.get('serial'),
                    'firmware_version': gateway.get('firmware_version')
                }
            }
            nad_create = pyclearpass.ApiPolicyElements.new_network_device(login, body=nad_attributes)
            print(
                "\nNAD create executed for gateway: " + gateway.get('name') + " with IP: " + gateway.get('ip_address'))
            pprint(nad_create)

        else:
            print("\n Site / Group information missing for Gateway: " + gateway.get('name') + " with IP: " + gateway.get('ip_address'))

def get_switch_info(central):
    # Sample API call using 'ArubaCentralBase.command()'
    # GET switches from Aruba Central
    apiPath = "/monitoring/v1/switches"
    apiMethod = "GET"
    apiParams = {
        "limit": 20,
        "offset": 0
    }

    print("\n\n\n\n##########################################################")
    print("\n\nFetching list of switches from Aruba Central:")
    switch_resp = central.command(apiMethod=apiMethod,
                                  apiPath=apiPath,
                                  apiParams=apiParams)
    switch_resp_items = switch_resp.get('msg').get('switches')
    pprint(switch_resp_items)
    return switch_resp_items




def create_switch_nad(central,switch_info):
    # Adding switches to ClearPass as NAD with RadSec disabled
    print("\n\n##########################################################")
    print("\n\nAdding switches to ClearPass as NAD")
    for switch in switch_info:
        if switch.get('site') is not None and switch.get('group_name') is not None:
            nad_attributes = {
                'name': switch.get('name'),
                'ip_address': switch.get('ip_address'),
                'radius_secret': 'aruba123',
                'tacacs_secret': 'aruba123',
                'vendor_name': 'Aruba',
                'vendor_id': 14823,
                'coa_capable': 'true',
                'coa_port': 3799,
                'radsec_enabled': 'false',
                'attributes': {
                    'Central_Site': switch.get('site'),
                    'Central_Group': switch.get('group_name'),
                    'Model': switch.get('model'),
                    'Serial': switch.get('serial'),
                    'firmware_version': switch.get('firmware_version')
                }
            }
            nad_create = pyclearpass.ApiPolicyElements.new_network_device(login, body=nad_attributes)
            print("\nNAD create executed for switch: " + switch.get('name') + " with IP: " + switch.get('ip_address'))
            pprint(nad_create)

        else:
            print("\n Site / Group information missing for Switch: " + switch.get('name') + " with IP: " + switch.get('ip_address'))



def create_switch_nad_radsec(central,switch_info):
    # Adding switches to ClearPass as NAD with RadSec enabled
    print("\n\n##########################################################")
    print("\n\nAdding switches to ClearPass as NAD")
    for switch in switch_info:
        if switch.get('site') is not None and switch.get('group_name') is not None:
            nad_attributes = {
                'name': switch.get('name'),
                'ip_address': switch.get('ip_address'),
                'radius_secret': 'aruba123',
                'tacacs_secret': 'aruba123',
                'vendor_name': 'Aruba',
                'vendor_id': 14823,
                'coa_capable': 'true',
                'coa_port': 3799,
                'radsec_enabled': 'true',
                "radsec_config": {
                    "validate_cert": "NONE",
                    "src_override_ip": switch.get('ip_address')
                },
                'attributes': {
                    'Central_Site': switch.get('site'),
                    'Central_Group': switch.get('group_name'),
                    'Model': switch.get('model'),
                    'Serial': switch.get('serial'),
                    'firmware_version': switch.get('firmware_version')
                }
            }
            nad_create = pyclearpass.ApiPolicyElements.new_network_device(login, body=nad_attributes)
            print("\nNAD create executed for switch: " + switch.get('name') + " with IP: " + switch.get('ip_address'))
            pprint(nad_create)

        else:
            print("\n Site / Group information missing for Switch: " + switch.get('name') + " with IP: " + switch.get('ip_address'))


def get_ap_info(central):
    # Sample API call using 'ArubaCentralBase.command()'
    # GET access points from Aruba Central
    apiPath = "/monitoring/v2/aps"
    apiMethod = "GET"
    apiParams = {
        "limit": 20,
        "offset": 0
    }

    print("\n\n\n\n##########################################################")
    print("\n\nFetching list of APs from Aruba Central:")
    ap_resp = central.command(apiMethod=apiMethod,
                              apiPath=apiPath,
                              apiParams=apiParams)
    ap_resp_items = ap_resp.get('msg').get('aps')
    pprint(ap_resp_items)
    return ap_resp_items


def create_ap_nad(central,ap_info):
    # Adding APs to ClearPass as NAD with RadSec disabled
    print("\n\n##########################################################")
    print("\n\nAdding APs to ClearPass as NAD")
    for ap in ap_info:
        if ap.get('site') is not None and ap.get('group_name') is not None:
            nad_attributes = {
                'name': ap.get('name'),
                'ip_address': ap.get('ip_address'),
                'radius_secret': 'aruba123',
                'tacacs_secret': 'aruba123',
                'vendor_name': 'Aruba',
                'vendor_id': 14823,
                'coa_capable': 'true',
                'coa_port': 3799,
                'radsec_enabled': 'false',
                'attributes': {
                    'Central_Site': ap.get('site'),
                    'Central_Group': ap.get('group_name'),
                    'Model': ap.get('model'),
                    'Serial': ap.get('serial'),
                    'firmware_version': ap.get('firmware_version')
                }
            }
            nad_create = pyclearpass.ApiPolicyElements.new_network_device(login, body=nad_attributes)
            print("\nNAD create executed for AP: " + ap.get('name') + " with IP: " + ap.get('ip_address'))
            pprint(nad_create)
            pprint(nad_attributes)

        else:
            print("\n Site / Group information missing for AP: "+ ap.get('name') + " with IP: " + ap.get('ip_address'))

def create_ap_nad_radsec(central,ap_info):
    # Adding APs to ClearPass as NAD with RadSec enabled
    print("\n\n##########################################################")
    print("\n\nAdding APs to ClearPass as NAD")
    for ap in ap_info:
        if ap.get('site') is not None and ap.get('group_name') is not None:
            nad_attributes = {
                'name': ap.get('name'),
                'ip_address': ap.get('ip_address'),
                'radius_secret': 'aruba123',
                'tacacs_secret': 'aruba123',
                'vendor_name': 'Aruba',
                'vendor_id': 14823,
                'coa_capable': 'true',
                'coa_port': 3799,
                'radsec_enabled': 'false',
                "radsec_config": {
                    "validate_cert": "NONE",
                    "src_override_ip": ap.get('ip_address')
                },
                'attributes': {
                    'Central_Site': ap.get('site'),
                    'Central_Group': ap.get('group_name'),
                    'Model': ap.get('model'),
                    'Serial': ap.get('serial'),
                    'firmware_version': ap.get('firmware_version')
                }
            }
            nad_create = pyclearpass.ApiPolicyElements.new_network_device(login, body=nad_attributes)
            print("\nNAD create executed for AP: " + ap.get('name') + " with IP: " + ap.get('ip_address'))
            pprint(nad_create)

        else:
            print("\n Site / Group information missing for AP: "+ ap.get('name') + " with IP: " + ap.get('ip_address'))


def create_ap_endpoint(central,ap_info):
    # Adding APs to ClearPass Endpoint Repository
    print("\n\n##########################################################")
    print("\n\nAdding APs to ClearPass Endpoint Repository")
    for ap in ap_info:
        if ap.get('site') is not None and ap.get('group_name') is not None:
            endpoint_attributes = {
                'ip_address': ap.get('ip_address'),
                'vendor_name': 'Aruba',
                'status': 'Known',
                'mac_address': ap.get('macaddr'),
                'attributes': {
                    'Central_Site': ap.get('site'),
                    'Central_Group': ap.get('group_name'),
                    'Model': ap.get('model'),
                    'Serial': ap.get('serial'),
                    'firmware_version': ap.get('firmware_version'),
                    'Device Name': ap.get('name')
                }
            }
            endpoint_create = pyclearpass.ApiIdentities.new_endpoint(login, body=endpoint_attributes)
            print("\nEndpoint create executed for AP: " + ap.get('name') + " with IP: " + ap.get('ip_address'))
            pprint(endpoint_create)

        else:
            print("\n Site / Group information missing for AP: "+ ap.get('name') + " with IP: " + ap.get('ip_address'))


#Configuring ClearPass OAuth client credentials
#SAMPLE clientid = "CPPM-TMELab-Cloud"
#SAMPLE clientsecret = "D4fg32jBIhdfh454932/1MKOwNEly3wZTok6Lq2ET"

clientid = credsConfig.clientid
clientsecret = credsConfig.clientsecret
login = ClearPassAPILogin(server="https://cxcii.arubasecurity.net:443/api", granttype="client_credentials",clientsecret=clientsecret, clientid=clientid)

#Configring central OAuth details
# SAMPLE central_info = {
#            "username": "dummy@aruba.com",
#            "password": "xxxxxxx",
#            "client_id": "BEw9Th7dummyJHDbhwe9dDO65",
#            "client_secret": "ap4KPshdummy1i1a5ynf6LZ",
#            "customer_id": "326a992fdummy25a662fd41b37222",
#            "base_url": "https://internal-apigw.central.arubanetworks.com/swagger/apps/nms/"
#        }
ssl_verify = False
central = ArubaCentralBase(central_info=credsConfig.central_info,
                           ssl_verify=ssl_verify)

# Fetch gateway information from Aruba Central
gateway_info = get_gateway_info(central)

# Create RADIUS NAD entries for gateways
create_gw_nad(central,gateway_info)
# Create RadSec NAD entries for gateways
create_gw_nad_radsec(central,gateway_info)

# Fetch switch information from Aruba Central
switch_info = get_switch_info(central)

# Create RADIUS NAD entries for switches
create_switch_nad(central,switch_info)
# Create RadSec NAD entries for switches
create_switch_nad_radsec(central,switch_info)

# Fetch access point information from Aruba Central
ap_info = get_ap_info(central)

# Create RADIUS NAD entries for access points
create_ap_nad(central,ap_info)
# Create RADIUS NAD entries for access points
create_ap_nad_radsec(central,ap_info)
# Create Endpoint Repository entries for access points
create_ap_endpoint(central,ap_info)