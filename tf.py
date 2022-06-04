import json
import argparse

parser = argparse.ArgumentParser(description='Process Terraform state file to extract resource types.')
parser.add_argument('state', help='The path to the Terraform state file')
args = parser.parse_args()

# Opening JSON file
f = open(args.state)
data = json.load(f)

resource_types = {}

# Looping through the resources and storing the number in resource_types dictionnary
for i in data.get('resources'):
    resource_type = i.get('type')
    if resource_type in resource_types:
        resource_types[resource_type] += 1
    else:
        resource_types[resource_type] = 1

print(json.dumps(resource_types, indent=2, sort_keys=True))

# Closing file
f.close()
