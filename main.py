import csv
import requests
import datetime as dt
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/52255828;0280-0.htm"

# Product:
# Joystick Thrustmaster T.16000M FCS Flight Pack
# ===============================================
# Price trend, no logging to Ceneo.pl needed!
# py file should be running once a day
# It gets the first (lowest) price from list
# Then saves data into CSV file
# and so on every day.

headers = {
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")
    first_offer = soup.find(name="div", class_="product-offer__container")
    shop_url = first_offer.get('data-shopurl')
    data_price = float(first_offer.get('data-price'))
    today = str(dt.datetime.today())[0:10]
    with open("gathered_data.csv", mode="a", newline='') as data_file:
        data = csv.writer(data_file)
        data.writerow([today, data_price, shop_url])
    print('Today data saved!')
except ConnectionError:
    print('Server cannot be reached. No data saved')
except FileNotFoundError:
    print('No file, no data saved')