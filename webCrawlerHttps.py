import certifi
import requests
from bs4 import BeautifulSoup

url = "https://www.soccersuck.com"  # Example only
headers = {'User-Agent': 'Mozilla/5.0'}  # To avoid blocks

try:
    response = requests.get(url, headers=headers, timeout=5, verify=certifi.where())
    html = response.text
    print("source: " + html)

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    print("Page title:", title)
except Exception as e:
    print("Failed to load page safely:", e)