"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

import os
import numpy as np
import matplotlib.pyplot as plt
from card import Card


class Deck:
    def __init__(self, name, view):
        self.card_list = []
        self.nonland_card_list = []
        self.name = name
        self.view = view

    def __str__(self):
        out = ''
        for i in range(len(self.card_list)):
            out += self.card_list[i].__str__()
            if i < len(self.card_list) - 1:
                out += '\n'
        return out

    def make_from_file(self, filename):
        cards_file = np.genfromtxt(filename, dtype=None)
        for i in range(len(cards_file)):
            for j in range(cards_file[i][2]):
                cc = Card(cards_file[i][0].decode("utf-8"), cards_file[i][1])
                self.add_card(cc)
                # self.unique_card_list = self.get_unique_list(self.card_list)
                #self.nonland_card_list = self.get_nonland()

    def add_card(self, card):
        self.card_list.append(card)

    def get_deck_stat(self):
        text = 'Total No. of cards in Deck: {}\nMore statistics to come...'.format(len(self.card_list))
        self.view.update_text_field(text)

    def download_images(self):
        if not os.path.exists(self.name):
            os.makedirs(self.name)
        for i in range(len(self.card_list)):
            url = self.card_list[i].get_image_url(size='small')
            text = '--> Retrieving image of {} from {}'.format(self.card_list[i], url)
            self.view.update_text_field(text)
            self.card_list[i].download_image(url, self.name)

    def save_to_disk(self):
        if not os.path.exists(self.name):
            os.makedirs(self.name)
        with open('./{}/{}.txt'.format(self.name, self.name), 'w') as f:
            for i in range(len(self.card_list)):
                f.write('{}\t{}\t1\n'.format(self.card_list[i].block, self.card_list[i].number))

    def get_filename_from_name(self, name):
        for c in self.card_list:
            if name == c.__str__():
                return self.name + '/' + '{}.jpg'.format(c.get_uid())

    @staticmethod
    def get_cards_of_type(lst_in, typ):
        lst_out = []
        for c in lst_in:
            if typ in c.get_types():
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_cards_of_ability(lst_in, abil):
        lst_out = []
        for c in lst_in:
            if abil in c.get_text():
                lst_out.append(c)
        return lst_out

    @staticmethod
    def print_list(lst_in):
        for c in lst_in:
            print(c)

    @staticmethod
    def get_unique_list(lst_in):
        lst_out = []
        lst_out = []
        for c in lst_in:
            if c.__str__() not in lst_out:
                lst_out.append(c.__str__())
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_whites(lst_in):
        lst_out = []
        for c in lst_in:
            if '{W}' in c.get_mana_cost():
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_blues(lst_in):
        lst_out = []
        for c in lst_in:
            if '{U}' in c.get_mana_cost():
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_blacks(lst):
        lst_out = []
        for c in lst:
            if '{B}' in c.get_mana_cost():
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_reds(lst):
        lst_out = []
        for c in lst:
            if '{R}' in c.get_mana_cost():
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_greens(lst):
        lst_out = []
        for c in lst:
            if '{G}' in c.get_mana_cost():
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_colorless(lst):
        lst_out = []
        for c in lst:
            if '{W}' not in c.get_mana_cost():
                if '{U}' not in c.get_mana_cost():
                    if '{B}' not in c.get_mana_cost():
                        if '{G}' not in c.get_mana_cost():
                            if '{R}' not in c.get_mana_cost():
                                lst_out.append(c)
        return lst_out

    @staticmethod
    def plot_mana_curve(lst):
        cost = []
        for c in lst:
            cost.append(c.get_converted_mana_cost())
        acost = np.asarray(cost)
        fig = plt.figure()
        # axes = plt.gca()
        # axes.set_xlim([-4, 4])
        # axes.set_ylim([-4, 4])
        plt.hist(acost, bins=len(cost), color='r', alpha=0.5)
        plt.grid(False)
        # plt.axis('off')
        fig.set_size_inches(2.5, 0.8)
        fig.savefig('manacurve.png', dpi=100)
        print(cost)
