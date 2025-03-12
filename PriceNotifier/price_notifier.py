# importing necessary libraries
import os
import json
import re
import requests
from datetime import datetime
from bs4 import BeautifulSoup

class PriceNotifier:
    def __init__(self, product_file="monitored_products.json"):
        self.product_file = product_file

    # Get the price of a product from a URL
    def get_product_data(self, url, selector_css=None, decimal_separator=','):
        try:
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                "Accept-Language": "en-US,en;q=0.5"
            }

            response = requests.get(url, headers=header, timeout=10)

            if response.status_code != 200:
                return None

            soup = BeautifulSoup(response.text, 'html.parser')

            # Search for the price 
            element_price = None
            if selector_css:
                element_price = soup.select_one(selector_css)
            else:
                selectors_css = [
                    '.price', '.product-price', '.offer-price', '.current-price',
                    '[itemprop="price"]', '.price-value', '.price-current',
                    '.a-price', '#priceblock_ourprice', '#priceblock_dealprice',
                    '#priceblock_saleprice', '#priceblock_pospromoprice',
                    '.andes-money-amount__fraction', '.price-tag-fraction'
                ]

                for selector in selectors_css:
                    element_price = soup.select_one(selector)
                    if element_price:
                        break

            if not element_price:
                return None

            text_price = element_price.text.strip()

            # Handling the thousands separator
            if decimal_separator != '.':
                text_price = text_price.replace('.', '')
                text_price = text_price.replace(',', '.')
            else:
                text_price = text_price.replace(',', '')

            # Getting the price
            clear_price = re.sub(r'[^\d.]', '', text_price)
            match = re.search(r'\d+.\d+|\d+', clear_price)

            return float(match.group()) if match else None

        except Exception as e:
            return None

    # Load the products from the file
    def load_products(self):
        if os.path.exists(self.product_file):
            try:
                with open(self.product_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except Exception as e:
                pass
        return []

    # Save the list of products to the file
    def save_products(self, products):
        try:
            with open(self.product_file, 'w', encoding='utf-8') as file:
                json.dump(products, file, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            return False

    # Add a product to the list
    def add_product(self, name, url, wanted_price, selector_css=None, decimal_separator=','):
        products = self.load_products()

        # Check if the product already exists
        for product in products:
            if product['url'] == url:
                return False

        # Get the price of the product
        current_price = self.get_product_data(url, selector_css, decimal_separator)
        if current_price is None:
            return False

        product = {
            'name': name,
            'url': url,
            'wanted_price': float(wanted_price),
            'current_price': current_price,
            'selector_css': selector_css,
            'decimal_separator': decimal_separator,
            'last_check': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'history': [],
        }

        if current_price is not None:
            product['history'].append({
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'price': current_price
            })

        products.append(product)
        self.save_products(products)

        return True

    # Update the price of a product
    def update_products(self):
        products = self.load_products()
        updated_products = []

        for product in products:
            decimal_separator = product.get('decimal_separator', ',')
            current_price = self.get_product_data(product['url'], product.get('selector_css'), decimal_separator)

            if current_price is not None:
                before_price = product['current_price']
                product['current_price'] = current_price

                # Add the price to the history
                product['history'].append({
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'price': current_price
                })

                # Limit the history to 10 items
                if len(product['history']) > 30:
                    product['history'] = product['history'][-30:]

                # Check if the price has dropped or reached the wanted price
                if (current_price is not None and current_price < before_price) or (current_price <= product['wanted_price']):
                    updated_products.append(product)

        self.save_products(products)
        return updated_products

    # Remove a product from the list
    def remove_product(self, index):
        products = self.load_products()
        if not products or index < 1 or index > len(products):
            return False
        products.pop(index - 1)
        self.save_products(products)
        return True

    # Get the list of products
    def get_products(self):
        return self.load_products()