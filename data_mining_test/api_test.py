"""from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True, port=4000)"""


import requests 
import json
import pandas as pd
from pandas import json_normalize

def demo1():
    URL = "https://api.mercadolibre.com/sites"
    try:
        req1 = requests.get(URL)
        dicc = json.loads(req1.text)
        for reg in dicc:
            print("ID: {} - NAME: {}".format(reg1["id"], reg1["name"]))
    except:
        print("Error peticion")
            