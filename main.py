import requests
import time
from bs4 import BeautifulSoup
from telegram import Bot

BOT_TOKEN = "8886585352:AAFp7Y_5XVEa1-Kx6nNhqBECaHxc3vIYWkE"
CHAT_ID = "7169536769"

SELLER_URL = "https://www.vinted.fr/member/209349416-onemi5"

bot = Bot(token=BOT_TOKEN)

seen = set()

def check_vinted():
    global seen

    response = requests.get(SELLER_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    for link in links:
        href = link.get("href")

        if href and "/items/" in href:
            full_link = "https://www.vinted.fr" + href

            if full_link not in seen:
                seen.add(full_link)

                bot.send_message(
                    chat_id=CHAT_ID,
                    text=f"Nouvelle annonce Vinted 🚨\n{full_link}"
                )

while True:
    try:
        check_vinted()
    except Exception as e:
        print(e)

    time.sleep(60)
