import json
import os

taboo_cards = []
cards_file = os.path.join(os.path.dirname(__file__), 'taboo-cards.json')

with open(cards_file, 'r') as f:
    data = json.load(f)
    taboo_cards = data['cards']
