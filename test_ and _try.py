import requests
from bs4 import BeautifulSoup
import sqlite3


# Функция для создания соединения с базой данных SQLite и создания таблицы, если она не существует
def create_table():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (title TEXT, price TEXT)''')
    conn.commit()
    conn.close()


# Функция для парсинга данных с веб-страницы и сохранения их в базу данных SQLite
def parse_and_save(url):
    r = requests.get("https://magnum.kz/catalog?discountType=all&city=almaty")
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        products = soup.select('.page-catalog_items > .product-block')

        conn = sqlite3.connect('products.db')
        c = conn.cursor()

        for product in products:
            title = product.select_one('.product-block_right > .product-block_descr').text.strip()
            price = product.select_one('.product-block_price-wrapper > .product-block_price').text.strip()

            c.execute("INSERT INTO products (title, price) VALUES (?, ?)", (title, price))

        conn.commit()
        conn.close()
        print("Data has been successfully parsed and saved to the database.")
    else:
        print("Failed to retrieve data from the URL.")


# URL для парсинга данных
url = "https://magnum.kz/catalog?discountType=all&city=almaty"

# Создание таблицы в базе данных SQLite (если не существует)
create_table()

# Парсинг данных с веб-страницы и их сохранение в базу данных SQLite
parse_and_save(url)
