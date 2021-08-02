import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response=requests.post(api_url, json=todo)
print(response.content)
