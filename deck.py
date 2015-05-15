"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

import os
import numpy as np
import matplotlib.pyplot as plt
import urllib.request as ur
import xml.etree.ElementTree as et
from card import Card


class Deck(object):
    def __init__(self, view):
        self.card_list = []
        self.view = view
        self.name = ''
        self.folder_json = ''
        self.folder_imgdb = ''

    def __str__(self):
        out = ''
        for i in range(len(self.card_list)):
            out += self.card_list[i].__str__()
            if i < len(self.card_list) - 1:
                out += '\n'
        return out

    def __cmp__(self, other):
        # todo: here compare method for sort

        return

    def make_from_cod(self, file_name):
        with open(file_name, 'rb') as f:
            ba = f.read()
        xml_tree_root = et.fromstring(ba)
        for elem in xml_tree_root.iter(tag='card'):
            for i in range(int(elem.attrib['number'])):
                print(elem.attrib['name'])
                # todo: cod import finish

    def make_from_csv(self, file_name):
        cards_file = np.genfromtxt(file_name, dtype=None)
        self.name = os.path.splitext(file_name)[0]
        for i in range(len(cards_file)):
            for j in range(cards_file[i][2]):
                block = cards_file[i][0].decode("utf-8")
                number = cards_file[i][1]
                cc = Card(block, number)
                json_file_name = self.folder_json + block + '.json'
                if os.path.exists(json_file_name):
                    cc.load_dict_from_json(json_file_name)
                    self.add_card(cc)
                else:
                    self.view.update_text_field(
                        'File {} does not exist. Downloading ...'.format(json_file_name))
                    self.download_json(block)
                    self.make_from_csv(file_name)  # recursive call!
                    return

        # now sort by name
        self.card_list.sort(key=lambda x: x.name)
        return

    def download_json(self, block):
        g = ur.urlopen('http://mtgjson.com/json/{}.json'.format(block))
        with open(self.folder_json + '{}.json'.format(block), 'b+w') as f:
            f.write(g.read())

    def add_card(self, card):
        self.card_list.append(card)

    def get_deck_stat(self):
        text = 'Total No. of cards in Deck: {}\nMore statistics to come...'.format(len(self.card_list))
        self.view.update_text_field(text)

    def download_images(self):
        for i in range(len(self.card_list)):
            img_file_name = self.folder_imgdb + '{}.jpg'.format(self.card_list[i].get_uid())
            if not os.path.exists(img_file_name):
                url = self.card_list[i].get_image_url(size='small')
                message = '--> Retrieving image of {} from {}'.format(self.card_list[i], url)
                self.view.update_text_field(message)
                g = ur.urlopen(url)
                with open(img_file_name, 'b+w') as f:
                    f.write(g.read())

    def save_to_cod(self, file_name):
        root = et.Element('cockatrice_deck')
        root.set('version', '1')
        tree = et.ElementTree(root)
        et.SubElement(root, 'deckname')
        et.SubElement(root, 'comments')
        zone = et.SubElement(root, 'zone')
        for i in range(len(self.card_list)):
            card = et.SubElement(zone, 'card')
            card.set('number', '1')
            card.set('price', '0')
            card.set('name', self.card_list[i].name)
        tree.write(file_name, encoding='utf-8', xml_declaration=True)

    def save_to_csv(self, file_name):
        with open(file_name, 'w') as f:
            for i in range(len(self.card_list)):
                f.write('{}\t{}\t1\n'.format(self.card_list[i].block, self.card_list[i].number))

    def get_image_file_name_from_name(self, name):
        for c in self.card_list:
            if name == c.__str__():
                return self.folder_imgdb + '{}.jpg'.format(c.get_uid())

    def get_card_from_name(self, name):
        for c in self.card_list:
            if name == c.__str__():
                return c

    @staticmethod
    def get_cards_of_type(lst_in, typ):
        lst_out = []
        for c in lst_in:
            if typ in c.get_types():
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_cards_of_subtype(lst_in, subtyp):
        lst_out = []
        for c in lst_in:
            if subtyp in c.get_subtypes():
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_cards_of_rarity(lst_in, rarity):
        lst_out = []
        for c in lst_in:
            if rarity in c.get_rarity():
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
        for c in lst_in:
            if c.__str__() not in lst_out:
                lst_out.append(c.__str__())
                lst_out.append(c)
        return lst_out

    @staticmethod
    def get_whites(lst_in, mono=False):
        lst_out = []
        for c in lst_in:
            mc = c.get_mana_cost()
            if '{W}' in mc:
                if mono:
                    if not ('{U}' in mc or '{B}' in mc or '{R}' in mc or '{G}' in mc):
                        lst_out.append(c)
                else:
                    lst_out.append(c)

        return lst_out

    @staticmethod
    def get_blues(lst_in, mono=False):
        lst_out = []
        for c in lst_in:
            mc = c.get_mana_cost()
            if '{U}' in mc:
                if mono:
                    if not ('{W}' in mc or '{B}' in mc or '{R}' in mc or '{G}' in mc):
                        lst_out.append(c)
                else:
                    lst_out.append(c)

        return lst_out

    @staticmethod
    def get_blacks(lst_in, mono=False):
        lst_out = []
        for c in lst_in:
            mc = c.get_mana_cost()
            if '{B}' in mc:
                if mono:
                    if not ('{U}' in mc or '{W}' in mc or '{R}' in mc or '{G}' in mc):
                        lst_out.append(c)
                else:
                    lst_out.append(c)

        return lst_out

    @staticmethod
    def get_reds(lst_in, mono=False):
        lst_out = []
        for c in lst_in:
            mc = c.get_mana_cost()
            if '{R}' in mc:
                if mono:
                    if not ('{U}' in mc or '{B}' in mc or '{W}' in mc or '{G}' in mc):
                        lst_out.append(c)
                else:
                    lst_out.append(c)

        return lst_out

    @staticmethod
    def get_greens(lst_in, mono=False):
        lst_out = []
        for c in lst_in:
            mc = c.get_mana_cost()
            if '{G}' in mc:
                if mono:
                    if not ('{U}' in mc or '{B}' in mc or '{R}' in mc or '{W}' in mc):
                        lst_out.append(c)
                else:
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

    @staticmethod
    def get_mana_curve(lst):
        cost = []
        for c in lst:
            cost.append(c.get_converted_mana_cost())
            # todo: here complete CLI mana curve