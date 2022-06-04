# tf-state-resource-stats
A python script to extract number of resources per type of resources in a Terraform state file.

## Usage

```sh
$ python3 tf.py -h
usage: tf.py [-h] state

Process Terraform state file to extract resource types.

positional arguments:
  state       The path to the Terraform state file

optional arguments:
  -h, --help  show this help message and exit
```

## Example
```sh
$ python3 tf.py ~/terraform/plan1/terraform.tfstate
{
  "aci_application_epg": 2,
  "aci_application_profile": 1,
  "aci_bridge_domain": 2,
  "aci_epg_to_domain": 2,
  "aci_epg_to_static_path": 2,
  "aci_external_network_instance_profile": 1,
  "aci_l3_domain_profile": 1,
  "aci_l3_ext_subnet": 1,
  "aci_l3_outside": 1,
  "aci_l3out_path_attachment": 1,
  "aci_l3out_path_attachment_secondary_ip": 2,
  "aci_l3out_static_route": 2,
  "aci_l3out_static_route_next_hop": 2,
  "aci_l3out_vpc_member": 2,
  "aci_logical_interface_profile": 1,
  "aci_logical_node_profile": 1,
  "aci_logical_node_to_fabric_node": 2,
  "aci_ranges": 1,
  "aci_subnet": 2,
  "aci_tenant": 1,
  "aci_vlan_pool": 1,
  "aci_vrf": 1
}
```
