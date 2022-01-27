import uvicorn

# conclusion the data on heroku doesn't affect github
from fastapi import FastAPI
from pydantic import BaseModel
from tinydb import TinyDB, where
from pathlib import Path

app = FastAPI()


class Person(BaseModel):
    name: str
    id: int


@app.get("/")
def index():
    database = TinyDB("src/data/db.json")
    result = [dict(doc) for doc in database.all()]
    database.close()

    return result


@app.get("/{id}")
def get_one(id: int):
    database = TinyDB("src/data/db.json")

    return [dict(doc) for doc in database.search(where("id") == id)]


@app.post("/persons")
def create_person(person: Person):
    database = TinyDB("src/data/db.json")
    database.insert(person.dict())
    return person


def insert():
    path = Path("src/data/db.json").resolve()
    db = TinyDB(path)
    data = [{
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
        {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {
                "lat": "-43.9509",
                "lng": "-34.4618"
            }
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains"
        }
    },
        {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "Nathan@yesenia.net",
        "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157",
            "geo": {
                "lat": "-68.6102",
                "lng": "-47.0653"
            }
        },
        "phone": "1-463-123-4447",
        "website": "ramiro.info",
        "company": {
            "name": "Romaguera-Jacobson",
            "catchPhrase": "Face to face bifurcated interface",
            "bs": "e-enable strategic applications"
        }
    }]

    db.insert_multiple(data)
    db.close()


if __name__ == "__main__":
    # uvicorn.run(app, debug=True, host="0.0.0.0", port=3240)
    insert()
