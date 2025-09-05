import requests

url = "https://api.github.com/users?per_page=5"
response = requests.get(url).json()
print(response)

print(f"{list(response[0].keys())}") 
print(f"Login:{response[0]['login']}") 
print(f"Avatar url:{response[0]['avatar_url']}") 
