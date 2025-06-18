import requests
from bs4 import BeautifulSoup

url = "	https://app.ibsystem.com.br/pdf/mypage.plala.or.jp/plala.or.jp/"  # Example only
headers = {'User-Agent': 'Mozilla/5.0'}  # To avoid blocks

try:
    response = requests.get(url, timeout=5, verify=False)
    html = response.text
    print("source: " + html)
    print('-------------------')
    soup = BeautifulSoup(html, 'html.parser')
    #soup.find_all('link')
    #for meta in soup.find_all('script'):
    #    print(meta.text)

    for meta in soup.find_all('link'):
        print(meta['href'])

    #title = soup.title.string
    #print("Page title:", title)
    #print(soup.find('div',{'class': 'header_label'}))
    #print(soup.find('div',{'class': 'header_label'}).text)

except Exception as e:
    print("Failed to load page safely:", e)