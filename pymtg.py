#!/usr/bin/env python
"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

import json, os
from numpy import genfromtxt
import urllib.request as ur


class Card:
    def __init__(self, block, number):
        self.block = block
        self.number = number
        with open(self.block.upper() + '.json') as json_data:
            data = json.load(json_data)
        for i in range(len(data['cards'])):
            if int(data['cards'][i]['number']) == self.number:
                self.dict = data['cards'][i]

    def __str__(self):
        return self.dict['name']

    def get_mana_cost(self):
        return self.dict['manaCost']

    def get_rarity(self):
        return self.dict['rarity']

    def get_uid(self):
        return int(self.dict['multiverseid'])

    def get_gatherer_url(self):
        return 'http://gatherer.wizards.com/Pages/Card/Details.aspx?printed=false&multiverseid={}'.format(
            self.get_uid())

    def get_mci_url(self):
        return 'http://magiccards.info/{}/en/{}.html'.format(self.block, self.number).lower()

    def get_url_and_image(self, folder, download=False, size='small'):
        if size == 'medium':
            url = 'http://mtgimage.com/multiverseid/{}.jpg'.format(self.get_uid())
        elif size == 'small':
            url = 'http://magiccards.info/scans/en/{}/{}.jpg'.format(self.block, self.number).lower()

        if download:
            g = ur.urlopen(url)
            with open('./{}/{}.jpg'.format(folder, self.get_uid()), 'b+w') as f:
                f.write(g.read())
        return url


class Deck:
    def __init__(self, name):
        self.card_list = []
        self.name = name

    def __str__(self):
        out = ''
        for i in range(len(self.card_list)):
            out += self.card_list[i].__str__()
            if i < len(self.card_list) - 1:
                out += '\n'
        return out

    def get_size(self):
        return '--> Total number of cards in deck: {}'.format(len(self.card_list))

    def make_from_file(self, filename):
        cards_file = genfromtxt(filename, dtype=None)
        for i in range(len(cards_file)):
            for j in range(cards_file[i][2]):
                cc = Card(cards_file[i][0].decode("utf-8"), cards_file[i][1])
                self.add_card(cc)

    def add_card(self, card):
        self.card_list.append(card)

    def store_pictures(self):
        if not os.path.exists(self.name):
            os.makedirs(self.name)
        for i in range(len(self.card_list)):
            print('--> Retrieving image of {} from {}'.format(self.card_list[i],
                                                              self.card_list[i].get_url_and_image(self.name,
                                                                                                  download=True,
                                                                                                  size='medium')))

if __name__ == "__main__":
    all_cards = Deck("all_cards")
    all_cards.make_from_file('cards.txt')
    print(all_cards)
    print(all_cards.get_size())
    # print(all_cards.card_list[0].get_mtg_image_url(all_cards.name))
    all_cards.store_pictures()