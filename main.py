import requests
from bs4 import BeautifulSoup

def check_big_block_price_spar():
    url_spar = "https://www.interspar.at/shop/lebensmittel/search?searchTerm=big%20block"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url_spar, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Beispielhaftes Suchen nach Produktblöcken
    products = soup.find_all("div", class_="product")
    for product in products:
        title_elem = product.find("div", class_="product__info--description")  # Anpassen!
        price_elem = product.find("div", class_="product__info--price")        # Anpassen!
        
        if title_elem and "big block" in title_elem.get_text().lower():
            price_text = price_elem.get_text(strip=True) if price_elem else "N/A"
            # Hier kann man nach Rabatten suchen, z.B. zusätzliches Element mit "Aktion" / "Rabatt" / etc.
            if "Aktion" in product.get_text():
                print(f"SPAR: Big Block gefunden – Preis: {price_text}, derzeit AKTION!")
            else:
                print(f"SPAR: Big Block gefunden – Preis: {price_text}")
            break

def check_big_block_price_mpreis():
    url_mpreis = "https://www.mpreis.at/shop/search?query=big%20block"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url_mpreis, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Beispielhaftes Suchen nach Produktblöcken
    # Hier ggf. andere Selektoren
    products = soup.find_all("div", class_="product-tile")
    for product in products:
        title_elem = product.find("h2", class_="product-name")  # Anpassen!
        price_elem = product.find("div", class_="product-price") # Anpassen!
        
        if title_elem and "big block" in title_elem.get_text().lower():
            price_text = price_elem.get_text(strip=True) if price_elem else "N/A"
            # Rabattcheck
            if "aktion" in product.get_text().lower():
                print(f"MPREIS: Big Block gefunden – Preis: {price_text}, derzeit AKTION!")
            else:
                print(f"MPREIS: Big Block gefunden – Preis: {price_text}")
            break

def check_big_block_price_billa():
    url_billa = "https://shop.billa.at/produkte?searchTerm=big%20block"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url_billa, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Beispielhafte Selektoren
    products = soup.find_all("div", class_="product-grid-item")
    for product in products:
        title_elem = product.find("span", class_="product-title")  # Anpassen!
        price_elem = product.find("span", class_="actual-price")    # Anpassen!
        
        if title_elem and "big block" in title_elem.get_text().lower():
            price_text = price_elem.get_text(strip=True) if price_elem else "N/A"
            # Rabattcheck
            # Manchmal steht "club" oder "aktion" in einer separaten Klasse
            if "aktion" in product.get_text().lower():
                print(f"BILLA: Big Block gefunden – Preis: {price_text}, derzeit AKTION!")
            else:
                print(f"BILLA: Big Block gefunden – Preis: {price_text}")
            break

if __name__ == "__main__":
    check_big_block_price_spar()
    check_big_block_price_mpreis()
    check_big_block_price_billa()
