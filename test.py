import httpx


r = httpx.get(
    f"https://jsonplaceholder.typicode.com/users/1")

print(r.json())
