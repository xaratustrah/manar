"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

import os
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QFileDialog
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem, QKeyEvent
from PyQt5.QtCore import Qt
from mainwindow_ui import Ui_MainWindow

from deck import Deck
from interface import Interface


class mainWindow(QMainWindow, Ui_MainWindow, Interface):
    def __init__(self):
        super(mainWindow, self).__init__()

        self.current_base_card_index = None
        self.current_new_card_index = None

        # Set up the user interface from Designer.

        self.folder_home = os.path.expanduser('~') + '/.manar/'
        self.folder_json = os.path.expanduser('~') + '/.manar/json/'
        self.folder_imgdb = os.path.expanduser('~') + '/.manar/imgdb/'

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

        # need to keep track of list view, its model and its selection model
        self.listView_base_model = QStandardItemModel()
        self.listView_base.setModel(self.listView_base_model)
        self.listView_base_selection_model = self.listView_base.selectionModel()  # workaround
        self.listView_base_selection_model.selectionChanged.connect(self.on_base_deck_list_view_selection_changed)

        self.listView_new_model = QStandardItemModel()
        self.listView_new.setModel(self.listView_new_model)
        self.listView_new_selection_model = self.listView_new.selectionModel()  # workaround
        self.listView_new_selection_model.selectionChanged.connect(self.on_new_deck_list_view_selection_changed)

    def connect_signals(self):
        self.actionDownload_Images.triggered.connect(self.base_deck.download_images)

        self.actionLoad_Base_Deck.triggered.connect(self.open_file_dialog)
        self.pushButton_load.clicked.connect(self.open_file_dialog)

        self.actionSave_New_Deck.triggered.connect(self.save_file_dialog)
        self.pushButton_save.clicked.connect(self.save_file_dialog)

        self.actionClear_Base_Deck.triggered.connect(self.clear_base_deck_list)
        self.pushButton_clear_base.clicked.connect(self.clear_base_deck_list)

        self.actionClear_New_Deck.triggered.connect(self.clear_new_deck_list)
        self.pushButton_clear_new.clicked.connect(self.clear_new_deck_list)

        self.pushButton_manarlize.clicked.connect(self.base_deck.get_deck_stat)

        self.listView_base.clicked.connect(self.update_card_view_base)
        self.listView_new.clicked.connect(self.update_card_view_new)
        self.listView_base.doubleClicked.connect(self.on_base_deck_list_view_double_clicked)

        self.comboBox_type_base.activated.connect(self.on_process_filter_base)
        self.comboBox_mana_base.activated.connect(self.on_process_filter_base)
        self.comboBox_ability_base.activated.connect(self.on_process_filter_base)
        self.comboBox_subtype_base.activated.connect(self.on_process_filter_base)
        self.comboBox_rarity_base.activated.connect(self.on_process_filter_base)
        self.checkBox_r_base.clicked.connect(self.on_process_filter_base)
        self.checkBox_u_base.clicked.connect(self.on_process_filter_base)
        self.checkBox_b_base.clicked.connect(self.on_process_filter_base)
        self.checkBox_w_base.clicked.connect(self.on_process_filter_base)
        self.checkBox_g_base.clicked.connect(self.on_process_filter_base)
        self.checkBox_cl_base.clicked.connect(self.on_process_filter_base)
        self.radioButton_mono_base.clicked.connect(self.on_process_filter_base)
        self.radioButton_dual_base.clicked.connect(self.on_process_filter_base)
        self.radioButton_multi_base.clicked.connect(self.on_process_filter_base)
        self.spinBox_mana_base.valueChanged.connect(self.on_process_filter_base)


    ## --- base deck -- ##

    def on_base_deck_list_view_selection_changed(self, current, previous):
        items = current.indexes()
        for index in items:
            # print(index.row(), index.column())
            self.current_base_card_index = index
            self.update_card_view_base(index)  # wheewwww!

    def on_base_deck_list_view_double_clicked(self, index):
        self.scan_for_dropped_items()
        card_name = self.listView_base.model().itemData(index)[0]
        card_object = self.base_deck.get_card_from_name(card_name)
        self.new_deck.add_card(card_object)
        self.update_new_deck_list_view(self.new_deck.card_list)

    def update_card_view_base(self, index):
        card_name = self.listView_base.model().itemData(index)[0]
        pic_filename = self.base_deck.get_image_filename_from_name(card_name)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(pic_filename))
        self.graphicsView_card.setScene(scene)

    def update_base_deck_list_view(self, lst):
        self.listView_base_model.clear()
        for c in lst:
            item = QStandardItem(c.__str__())
            self.listView_base_model.appendRow(item)
        self.listView_base.show()

    def clear_base_deck_list(self):
        self.base_deck.card_list = []
        self.listView_base_model.clear()

    ## --- new deck -- ##

    def on_new_deck_list_view_selection_changed(self, current, previous):
        items = current.indexes()
        for index in items:
            # print(index.row(), index.column())
            self.current_new_card_index = index
            self.update_card_view_new(self.current_new_card_index)  # wheewwww!

    def update_card_view_new(self, index):
        card_name = self.listView_new.model().itemData(index)[0]
        pic_filename = self.new_deck.get_image_filename_from_name(card_name)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(pic_filename))
        self.graphicsView_card.setScene(scene)

    def update_new_deck_list_view(self, lst):
        self.listView_new_model.clear()
        for c in lst:
            item = QStandardItem(c.__str__())
            self.listView_new_model.appendRow(item)
        self.listView_new.show()

    def remove_card_from_new_deck_list(self, index):
        card_name = self.listView_new.model().itemData(index)[0]
        card_object = self.base_deck.get_card_from_name(card_name)
        self.new_deck.card_list.remove(card_object)
        self.update_new_deck_list_view(self.new_deck.card_list)

    def clear_new_deck_list(self):
        self.new_deck.card_list = []
        self.listView_new_model.clear()

    ## --------

    def update_text_field(self, message):
        self.textEdit.append(message)

    def save_file_dialog(self):
        self.scan_for_dropped_items()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save deck", '',
                                                  "Tab separated values (*.csv)")  # ;;All Files (*)"
        if not fileName:
            return
        if len(self.new_deck.card_list) < 2:
            self.update_text_field('Deck must contain at least 2 cards. Not saving.')
            return
        self.new_deck.save_to_disk(fileName)

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Deck", '', "Tab separated values (*.csv)")

        if not file_name:
            return

        self.base_deck.make_from_file(file_name)
        lst = self.base_deck.card_list
        self.update_base_deck_list_view(lst)

    def on_process_filter_base(self):
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

    def make_folders(self):
        if not os.path.exists(self.folder_home):
            os.mkdir(self.folder_home)
        if not os.path.exists(self.folder_json):
            os.mkdir(self.folder_json)
        if not os.path.exists(self.folder_imgdb):
            os.mkdir(self.folder_imgdb)
        return

    def keyPressEvent(self, event):
        if type(event) == QKeyEvent:
            # here accept the event and do something
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                self.scan_for_dropped_items()
                if self.focusWidget() is self.listView_base:
                    self.on_base_deck_list_view_double_clicked(self.current_base_card_index)
            event.accept()
            if event.key() == Qt.Key_Delete or event.key() == Qt.Key_Backspace:
                if self.focusWidget() is self.listView_new:
                    self.remove_card_from_new_deck_list(self.current_new_card_index)
            event.accept()
        else:
            event.ignore()

    def scan_for_dropped_items(self):
        self.new_deck.card_list = []
        i = 0
        while self.listView_new_model.item(i):
            card_name = self.listView_new_model.item(i).text()
            card_object = self.base_deck.get_card_from_name(card_name)
            self.new_deck.card_list.append(card_object)
            i += 1
        self.update_new_deck_list_view(self.new_deck.card_list)
