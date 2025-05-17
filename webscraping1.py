
import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com"

resposta = requests.get(url)

if resposta.status_code ==200:
    soup = BeautifulSoup(resposta.text, "html.parser")
    manchetes = soup.find_all("a", class_="feed-post-link")

print("Manchetes principais: ")
for noticia in manchetes:
    print(noticia.text)
    