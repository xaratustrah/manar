"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

import os
from numpy import genfromtxt
from card import Card


class Deck:
    def __init__(self, name):
        self.card_list = []
        self.nonland_card_list = []
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
        # self.unique_card_list = self.get_unique_list(self.card_list)
        self.nonland_card_list = self.get_nonland()

    def add_card(self, card):
        self.card_list.append(card)

    def download_images(self):
        if not os.path.exists(self.name):
            os.makedirs(self.name)
        for i in range(len(self.card_list)):
            url = self.card_list[i].get_image_url(size='small')
            print('--> Retrieving image of {} from {}'.format(self.card_list[i], url))
            self.card_list[i].download_image(url, self.name)

    def save_to_disk(self):
        if not os.path.exists(self.name):
            os.makedirs(self.name)
        with open('./{}/{}.txt'.format(self.name, self.name), 'w') as f:
            for i in range(len(self.card_list)):
                f.write('{}\t{}\t1\n'.format(self.card_list[i].block, self.card_list[i].number))

                # TODO: change with generator function

    def get_lands(self):
        lst = []
        for c in self.card_list:
            if 'Land' in c.get_types():
                lst.append(c)
        return lst

    def get_sorceries(self):
        lst = []
        for c in self.card_list:
            if 'Sorcery' in c.get_types():
                lst.append(c)
        return lst

    def get_instants(self):
        lst = []
        for c in self.card_list:
            if 'Instant' in c.get_types():
                lst.append(c)
        return lst

    def get_enchantments(self):
        lst = []
        for c in self.card_list:
            if 'Enchantment' in c.get_types():
                lst.append(c)
        return lst

    def get_planeswalkers(self):
        lst = []
        for c in self.card_list:
            if 'Planeswalker' in c.get_types():
                lst.append(c)
        return lst

    def get_artifacts(self):
        lst = []
        for c in self.card_list:
            if 'Artifact' in c.get_types():
                lst.append(c)
        return lst

    def get_creatures(self):
        lst = []
        for c in self.card_list:
            if 'Creature' in c.get_types():
                lst.append(c)
        return lst

    # @staticmethod
    def get_nonland(self):
        lst = []
        lst.extend(self.get_creatures())
        lst.extend(self.get_artifacts())
        lst.extend(self.get_enchantments())
        lst.extend(self.get_planeswalkers())
        lst.extend(self.get_sorceries())
        lst.extend(self.get_instants())

        return lst

    @staticmethod
    def print_list(lst):
        for c in lst:
            print(c)

    @staticmethod
    def get_unique_list(lst):
        checked = []
        lst_out = []
        for c in lst:
            if c.__str__() not in checked:
                checked.append(c.__str__())
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_whites(lst):
        checked = []
        for c in lst:
            if '{W}' in c.get_mana_cost():
                checked.append(c)
        return checked

    @staticmethod
    def get_blues(lst):
        checked = []
        for c in lst:
            if '{U}' in c.get_mana_cost():
                checked.append(c)
        return checked

    @staticmethod
    def get_blacks(lst):
        checked = []
        for c in lst:
            if '{B}' in c.get_mana_cost():
                checked.append(c)
        return checked

    @staticmethod
    def get_reds(lst):
        checked = []
        for c in lst:
            if '{R}' in c.get_mana_cost():
                checked.append(c)
        return checked

    @staticmethod
    def get_greens(lst):
        checked = []
        for c in lst:
            if '{G}' in c.get_mana_cost():
                checked.append(c)
        return checked

    @staticmethod
    def get_colorless(lst):
        checked = []
        for c in lst:
            if '{W}' not in c.get_mana_cost():
                if '{U}' not in c.get_mana_cost():
                    if '{B}' not in c.get_mana_cost():
                        if '{G}' not in c.get_mana_cost():
                            if '{R}' not in c.get_mana_cost():
                                checked.append(c)
        return checked
