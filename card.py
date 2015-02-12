"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

import json, re
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

    def get_types(self):
        return self.dict['types']

    def get_subtypes(self):
        return self.dict['subtypes']

    def get_watermark(self):
        return self.dict['watermark']

    def get_mana_cost(self):
        return self.dict['manaCost']

    def get_converted_mana_cost(self):
        mc = self.get_mana_cost()
        cmc = mc.count('W') + mc.count('G') + mc.count('B') + mc.count('U') + mc.count('R')
        num = re.findall('\d', mc)
        if len(num) > 0:
            cmc += int(num[0])
        return cmc

    def get_rarity(self):
        return self.dict['rarity']

    def get_uid(self):
        return int(self.dict['multiverseid'])

    def get_gatherer_url(self):
        return 'http://gatherer.wizards.com/Pages/Card/Details.aspx?printed=false&multiverseid={}'.format(
            self.get_uid())

    def get_mci_url(self):
        return 'http://magiccards.info/{}/en/{}.html'.format(self.block, self.number).lower()

    def get_image_url(self, size='small'):
        if size == 'medium':
            url = 'http://mtgimage.com/multiverseid/{}.jpg'.format(self.get_uid())
        elif size == 'small':
            url = 'http://magiccards.info/scans/en/{}/{}.jpg'.format(self.block, self.number).lower()
        return url

    def download_image(self, url, folder):
        # if not os.path.exists(self.name):
        g = ur.urlopen(url)
        with open('./{}/{}.jpg'.format(folder, self.get_uid()), 'b+w') as f:
            f.write(g.read())
        return
