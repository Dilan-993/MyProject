import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/" # сохраняем ссылку интернет страницы
response = requests.get(url) # скачиваю страницу по указыной ссылки

soup = BeautifulSoup(response.text, "html.parser") # это раскладывание кода(html) по полочкам
quotes = soup.find_all("div", class_="quote") # находим нужные элементы из разложенной информации
for quote in quotes: # беру отдельную цитату среди всех цитат
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    print(text)
    print("автор: ",author)
