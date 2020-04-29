# https://realpython.com/python-json/

import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
with open("json1.json", "w") as write_file:
    t= json.dump(data, write_file)
    print(t)

