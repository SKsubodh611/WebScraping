import requests
from bs4 import BeautifulSoup

# URL of the product page
url = 'https://www.amazon.in/s?k=shoes&crid=1672LSO65KM4N&sprefix=sho%2Caps%2C395&ref=nb_sb_noss_2'

# Add headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}



# Send a request to fetch the content of the page
response = requests.get(url, headers=headers)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.content, 'lxml')
# print(soup.get_text().strip())

# Find the product name (try to find the tag based on id or class name)
product_name = soup.find('span', {'id': 'productTitle'}).get_text().strip()

# Find the product price (try to find the tag based on id or class name)
product_price = soup.find('span', {'class': 'a-price-whole'}).get_text().strip()
# Print the results
    
print(f"Product Name: {product_name}")
print(f"Product Price: {product_price}")
