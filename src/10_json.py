import json

json_data = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
            '{"ID":20,"Name":"David Lee","Role":"Editor"}]'

json_object = json.loads(json_data)

json_formatted_str = json.dumps(json_object, indent=2)

# print(json_formatted_str)

# Working with files
with open('Cars.json', 'r') as json_file:
    json_object = json.load(json_file)

print(type(json_object))
print(f'\nJson objet:\n\n{json_object}')

print(type(json.dumps(json_object)))
print(f'\nJson dumps:\n\n {json.dumps(json_object)}')

print(f'\nJson dunmps with indent 1:\n\n {json.dumps(json_object, indent=6)}')
