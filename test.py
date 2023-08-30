import requests

res = requests.get("https://kyzmat24.com/api/users/").json()
print(res)
