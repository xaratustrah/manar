"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

from abc import ABCMeta, abstractmethod


class Interface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update_text_field(self, text):
        pass
