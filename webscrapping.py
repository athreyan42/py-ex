import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
soup.findAll('a')
line_count = 1  # variable to track what line you are on...
for one_a_tag in soup.findAll('a'):
    if line_count >= 38:
        link = one_a_tag['href']
        download_url = 'http://web.mta.info/developers/' + link
        urllib.request.urlretrieve(
            download_url, './'+link[link.find('/turnstile_')+1:])
        time.sleep(1)
    line_count += 1
