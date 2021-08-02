import requests
BASE = "http://127.0.0.1:5000/"

data=[{"likes":  11,"name": "tina", "views": 1000 },{"likes":  10,"name": "tm", "views": 10000 },
      {"likes":  12,"name": "paku", "views": 100000 }, {"likes":  14,"name": "bana", "views": 1600 }
      ]

for i in range(len(data)):
  response=requests.put(BASE+ "video/" + str(i), data[i])
  print(response.json())
input()
response=requests.delete(BASE+"video/1")
print(response.json())
input()
response= requests.get(BASE+"video/2")
print(response.json())