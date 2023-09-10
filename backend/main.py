import json

from fastapi import FastAPI

# Load crimebrands JSON into dict
crimebrands = {}
with open('./data/crimebrands.json') as crimebrands_json:
    crimebrands = json.load(crimebrands_json)

# Load sinners JSON into dict
sinners = {}
with open('./data/sinners.json') as sinners_json:
    sinners = json.load(sinners_json)

app = FastAPI()


@app.get("/crimebrand/all")
def get_crimebrand():
    return crimebrands

@app.get("/crimebrand/{name}")
def get_crimebrand(name:str):
    return crimebrands[name]

@app.get("/sinners/all")
def get_all_sinners():
    return sinners

@app.get("/sinners/{rank}")
def get_sinners_by_rank(rank: str):
    rank_list = []
    for name, dic in sinners.items():
        if dic["rank"] == rank:
            rank_list.append(name)
    return rank_list

@app.get("/sinner/{name}")
def get_sinner(name:str):
    return sinners[name]