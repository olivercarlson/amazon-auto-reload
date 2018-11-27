import json
import os
import sys
import amazon
import time
from card import Card
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

with open('config.json') as properties:
    data = json.load(properties)
    username = data["username"]
    password = data["password"]
    delay = data["reloadDelay"]
    cards = []
    for card in data["cards"]:
        newCard = Card(card['cardNumber'], card['reloadAmount'], card['reloadTimes'])
        cards.append(newCard)

driver = webdriver.Chrome("{}\\chromedriver.exe".format(os.path.dirname(os.path.realpath(sys.argv[0]))))
wait = WebDriverWait(driver, 30)
amazon.login(username, password, driver, wait)
    
for card in cards:
    last_four = card.card_number[-4:]
    while card.reload_times > 0:
        print("Reloading card ending in {} with ${}.".format(last_four, card.reload_amount))
        amazon.reload(card.card_number, last_four, card.reload_amount, driver, wait)
        card.reload_times -= 1
        if card.reload_times > 0:
            print("Pausing for {} seconds.".format(delay))
            time.sleep(delay)
        
driver.quit()
quit()