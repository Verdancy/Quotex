import requests
from bs4 import BeautifulSoup

class Scraper:
    BASE_URL = "http://quotes.toscrape.com"
    PAGE_URL = "/page/{}/"

    def scrape_page(self, page_number):
        response = requests.get(self.BASE_URL + self.PAGE_URL.format(page_number))
        
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        data = []

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

            data.append({
                "text": text,
                "author": author,
                "tags": tags,
            })

        return data
