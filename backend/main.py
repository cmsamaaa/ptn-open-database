import json

from fastapi import FastAPI

# Load crimebrands JSON into dict
crimebrands = {}
with open('./data/crimebrands.json') as crimebrands_json:
    crimebrands = json.load(crimebrands_json)

app = FastAPI()


@app.get("/crimebrand/all")
def get_crimebrand():
    return crimebrands

@app.get("/crimebrand/{name}")
def get_crimebrand(name:str):
    return crimebrands[name]
