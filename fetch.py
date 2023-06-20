# import requests


# link = "https://www.youtube.com/watch?v=71obuxwVzhc"

# data = requests.get(link,allow_redirects=True)

# with open("impressive.mp4","wb") as file:
#     file.write(data.content)
import requests

url = "https://api.drugbank.com/v1/adverse_effects?q=nausea"
data = requests.get(url)
print(data)

