import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://example.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.text
print("Title:", title)

# Log save
with open("log.txt", "a") as f:
    f.write(f"{datetime.now()} - {title}\n")
