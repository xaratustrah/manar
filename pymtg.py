#!/usr/bin/env python
"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

from deck import Deck


if __name__ == "__main__":
    allcards = Deck("my_cards")
    allcards.make_from_file('mycards.txt')
    lst = allcards.nonland_card_list
    lst = Deck.get_unique_list(lst)
    Deck.print_list(Deck.get_blacks(lst))
#    allcards.download_images()
    Deck.get_mana_curve(Deck.get_blacks(lst))
