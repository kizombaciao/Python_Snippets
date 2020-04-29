import json

# a Python object (dict):
x = {
  "name": True,
  "age": False,
  "city": None
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

