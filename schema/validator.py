import json
from jsonschema import validate

# Validate Cracks
with open('crack.json') as data_file:
    data = json.load(data_file)

with open('crack.schema.json') as schema_file:
	schema = json.load(schema_file)

validate(data,schema)

# Validate Corrosion
with open('corrosion.json') as data_file:
    data = json.load(data_file)

with open('corrosion.schema.json') as schema_file:
	schema = json.load(schema_file)

validate(data,schema)

# Validate Spalls
with open('spall.json') as data_file:
    data = json.load(data_file)

with open('spall.schema.json') as schema_file:
	schema = json.load(schema_file)

validate(data,schema)

# Validate label
with open('label.json') as data_file:
    data = json.load(data_file)

with open('label.schema.json') as schema_file:
	schema = json.load(schema_file)

validate(data,schema)

print("Validation complete")
