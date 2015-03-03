"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

import os
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QFileDialog
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtCore import QModelIndex
from mainwindow_ui import Ui_MainWindow

from deck import Deck
from interface import Interface


class mainWindow(QMainWindow, Ui_MainWindow, Interface):
    def __init__(self):
        super(mainWindow, self).__init__()

        # Set up the user interface from Designer.

        self.folder_home = os.path.expanduser('~')+'/.manar/'
        self.folder_json = os.path.expanduser('~')+'/.manar/json/'
        self.folder_imgdb = os.path.expanduser('~')+'/.manar/imgdb/'

        self.base_deck = Deck(self)
        self.base_deck.folder_json = self.folder_json
        self.base_deck.folder_imgdb = self.folder_imgdb

        self.new_deck = Deck(self)
        self.new_deck.folder_json = self.folder_json
        self.new_deck.folder_imgdb = self.folder_imgdb

        self.setupUi(self)
        self.make_folders()

        # Signals
        self.connect_signals()

    def connect_signals(self):
        self.actionDownload_Images.triggered.connect(self.base_deck.download_images)

        self.actionLoad_Deck.triggered.connect(self.open_file_dialog)
        self.pushButton_load.clicked.connect(self.open_file_dialog)

        self.actionSave_Deck.triggered.connect(self.save_file_dialog)
        self.pushButton_save.clicked.connect(self.save_file_dialog)

        self.actionClear_Deck.triggered.connect(self.clear_base_deck_list)
        self.pushButton_clear.clicked.connect(self.clear_base_deck_list)

        self.pushButton_manarlize.clicked.connect(self.base_deck.get_deck_stat)

        self.listView_base.clicked.connect(self.update_card_view_base)
        self.listView_new.clicked.connect(self.update_card_view_new)
        self.listView_base.doubleClicked.connect(self.update_new_deck_list_view)

        self.comboBox_type_base.activated.connect(self.process_filter_base)
        self.comboBox_mana_base.activated.connect(self.process_filter_base)
        self.comboBox_ability_base.activated.connect(self.process_filter_base)
        self.comboBox_subtype_base.activated.connect(self.process_filter_base)
        self.comboBox_rarity_base.activated.connect(self.process_filter_base)
        self.checkBox_r_base.clicked.connect(self.process_filter_base)
        self.checkBox_u_base.clicked.connect(self.process_filter_base)
        self.checkBox_b_base.clicked.connect(self.process_filter_base)
        self.checkBox_w_base.clicked.connect(self.process_filter_base)
        self.checkBox_g_base.clicked.connect(self.process_filter_base)
        self.checkBox_cl_base.clicked.connect(self.process_filter_base)
        self.radioButton_mono_base.clicked.connect(self.process_filter_base)
        self.radioButton_dual_base.clicked.connect(self.process_filter_base)
        self.radioButton_multi_base.clicked.connect(self.process_filter_base)
        self.spinBox_mana_base.valueChanged.connect(self.process_filter_base)

    def make_folders(self):
        if not os.path.exists(self.folder_home):
            os.mkdir(self.folder_home)
        if not os.path.exists(self.folder_json):
            os.mkdir(self.folder_json)
        if not os.path.exists(self.folder_imgdb):
            os.mkdir(self.folder_imgdb)
        return

    def update_text_field(self, message):
        self.textEdit.append(message)

    def update_new_deck_list_view(self, index):
        card_name = self.listView_base.model().itemData(index)[0]
        card_object = self.base_deck.get_card_from_name(card_name)
        self.new_deck.add_card(card_object)
        model_new = QStandardItemModel(self.listView_base)
        for c in self.new_deck.card_list:
            item = QStandardItem(c.__str__())
            model_new.appendRow(item)
        self.listView_new.setModel(model_new)
        self.listView_new.show()

    def update_base_deck_list_view(self, lst):
        model_base = QStandardItemModel(self.listView_base)
        for c in lst:
            item = QStandardItem(c.__str__())
            model_base.appendRow(item)
        self.listView_base.setModel(model_base)
        self.listView_base.show()

    def clear_base_deck_list(self):
        self.base_deck.card_list = []
        self.update_base_deck_list_view(self.base_deck.card_list)

    def update_card_view_base(self, index):
        card_name = self.listView_base.model().itemData(index)[0]
        pic_filename = self.base_deck.get_image_filename_from_name(card_name)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(pic_filename))
        self.graphicsView_card.setScene(scene)

    def update_card_view_new(self, index):
        card_name = self.listView_new.model().itemData(index)[0]
        pic_filename = self.new_deck.get_image_filename_from_name(card_name)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(pic_filename))
        self.graphicsView_card.setScene(scene)

    def save_file_dialog(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save deck", '',
                                                  "Tab separated values (*.csv)")  # ;;All Files (*)"
        if not fileName:
            return

        self.new_deck.save_to_disk(fileName)

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Deck", '', "Tab separated values (*.csv)")

        if not file_name:
            return

        self.base_deck.make_from_file(file_name)
        lst = self.base_deck.card_list
        # lst = Deck.get_unique_list(lst)
        self.update_base_deck_list_view(lst)

    def process_filter_base(self):
        typ = self.comboBox_type_base.currentText()
        ability = self.comboBox_ability_base.currentText()
        subtype = self.comboBox_subtype_base.currentText()
        rarity = self.comboBox_rarity_base.currentText()

        if typ == 'All Cards':
            lst = self.base_deck.card_list
            self.update_base_deck_list_view(lst)
            return

        if typ == 'Land':
            lst = Deck.get_cards_of_type(self.base_deck.card_list, typ)
            self.update_base_deck_list_view(lst)
            return

        lst = Deck.get_cards_of_type(self.base_deck.card_list, typ)

        lst_out = []

        r = self.checkBox_r_base.isChecked()
        g = self.checkBox_g_base.isChecked()
        w = self.checkBox_w_base.isChecked()
        u = self.checkBox_u_base.isChecked()
        b = self.checkBox_b_base.isChecked()
        cl = self.checkBox_cl_base.isChecked()

        if r:
            lst_out.extend(Deck.get_reds(lst, self.radioButton_mono_base.isChecked()))

        if g:
            lst_out.extend(Deck.get_greens(lst, self.radioButton_mono_base.isChecked()))

        if w:
            lst_out.extend(Deck.get_whites(lst, self.radioButton_mono_base.isChecked()))

        if u:
            lst_out.extend(Deck.get_blues(lst, self.radioButton_mono_base.isChecked()))

        if b:
            lst_out.extend(Deck.get_blacks(lst, self.radioButton_mono_base.isChecked()))

        if cl:
            lst_out.extend(Deck.get_colorless(lst))

        if not ability == 'Any':
            lst_out = Deck.get_cards_of_ability(lst_out, ability)

        if not subtype == 'Any':
            lst_out = Deck.get_cards_of_ability(lst_out, subtype)

        if not rarity == 'Any':
            lst_out = Deck.get_cards_of_ability(lst_out, rarity)

        self.update_base_deck_list_view(lst_out)

