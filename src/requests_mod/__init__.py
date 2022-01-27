import httpx

from random import choice
from tinydb import TinyDB
from pathlib import Path


def update_db():
    db_path = Path("src/data/db.json").resolve()
    conn = TinyDB(db_path)

    r = httpx.get(
        f"https://jsonplaceholder.typicode.com/users/{choice(range(3, 10))}")

    try:
        person = r.json()
        conn.insert(person)
    except Exception as e:
        print(e)

    conn.close()


if __name__ == "__main__":
    update_db()
