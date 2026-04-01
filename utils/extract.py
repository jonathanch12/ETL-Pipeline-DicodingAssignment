import requests
from bs4 import BeautifulSoup

BASE_URL = "https://fashion-studio.dicoding.dev"

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None
    
def parse_product(card):
    try:
        title = card.find("h3", class_="product-title").text.strip()
        price = card.find("span", class_="price").text.strip()
        paragraphs = card.find_all("p")
        rating = paragraphs[0].text.strip()
        colors = paragraphs[1].text.strip()
        size = paragraphs[2].text.strip()
        gender = paragraphs[3].text.strip()
        return {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender
        }
    except (AttributeError, IndexError):
        return None

def scrape_page(page_number):
    if page_number == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}/page{page_number}"
    html = get_html(url)
    
    if not html:
        return []

    soup = BeautifulSoup(html, "lxml")
    cards = soup.find_all("div", class_="product-details")

    data = []
    for card in cards:
        product = parse_product(card)
        if product:
            data.append(product)

    return data

def extract_all():
    all_data = []

    for page in range(1, 51):
        print(f"Scraping page {page}...")
        page_data = scrape_page(page)
        all_data.extend(page_data)

    return all_data