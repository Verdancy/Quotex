from scraper import Scraper
from storage import Storage

scraper = Scraper()
storage = Storage("quotes.json")

page_number = 1
data = []

while True:
    print(f"Scraping page {page_number}...")
    page_data = scraper.scrape_page(page_number)
    
    if page_data is None:
        break

    data.extend(page_data)
    page_number += 1

storage.save(data)

print("Scraping completed. Data saved to 'quotes.json'.")

