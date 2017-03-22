import json
from jsonschema import validate


with open('crack.json') as data_file:
    data = json.load(data_file)

with open('crack.schema.json') as schema_file:
	schema = json.load(schema_file)

validate(data,schema)


with open('corrosion.json') as data_file:
    data = json.load(data_file)

with open('corrosion.schema.json') as schema_file:
	schema = json.load(schema_file)

validate(data,schema)

print("Validation complete")
