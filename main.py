from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello visitor!"}


@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}
    
@app.get("/query/{food}")
async def query(food: str):
    """Query calories by food name"""

    url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"

    querystring = {"query":food}

    headers = {
        "X-RapidAPI-Key": "155edcf844msh7d2f8265bf24668p17f256jsn999e77a74d46",
        "X-RapidAPI-Host": "calorieninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring, timeout=10)

    return {"result": response.text}


@app.get("/query/{date}")
async def query2(date: str):
    """Query covid19 statistics by location and date"""

    url = "https://rapidapi.com/axisbits-axisbits-default/api/covid-19-statistics/"

    querystring = {"query": date}

    headers = {
        "X-RapidAPI-Key": "155edcf844msh7d2f8265bf24668p17f256jsn999e77a74d46",
        "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring, timeout=10)

    return {"result": response.text}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
