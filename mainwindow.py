"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

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
        self.base_deck = Deck("base_deck", self)
        self.setupUi(self)

        # signals
        self.actionLoad_Deck.triggered.connect(self.open_file_dialog)
        self.actionDownload_Images.triggered.connect(self.base_deck.download_images)
        self.comboBox_type_base.activated.connect(self.process_filter_base)
        self.pushButton_manarlize.clicked.connect(self.base_deck.get_deck_stat)

        self.listView_base.clicked.connect(self.update_card_view)

    def update_text_field(self, text):
        self.textEdit.append(text)

    def update_card_view(self, index):
        card_name = self.listView_base.model().itemData(index)[0]
        pic_filename = self.base_deck.get_filename_from_name(card_name)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(pic_filename))
        self.graphicsView_card.setScene(scene)

    def update_base_deck_list_view(self, lst):
        model_base = QStandardItemModel(self.listView_base)
        for c in lst:
            item = QStandardItem(c.__str__())
            model_base.appendRow(item)
        self.listView_base.setModel(model_base)
        self.listView_base.show()

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Deck", '', "All Files (*)")

        if not file_name:
            return

        self.base_deck.make_from_file(file_name)
        lst = self.base_deck.card_list
        # lst = Deck.get_unique_list(lst)
        self.update_base_deck_list_view(lst)

    def process_filter_base(self):
        typ = self.comboBox_type_base.currentText()
        ability = self.comboBox_ability_base.currentText()

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
            lst_out.extend(Deck.get_reds(lst))

        if g:
            lst_out.extend(Deck.get_greens(lst))

        if w:
            lst_out.extend(Deck.get_whites(lst))

        if u:
            lst_out.extend(Deck.get_blues(lst))

        if b:
            lst_out.extend(Deck.get_blacks(lst))

        if cl:
            lst_out.extend(Deck.get_colorless(lst))

        if not ability == 'Any':
            lst_out = Deck.get_cards_of_ability(lst_out, ability)

        self.update_base_deck_list_view(lst_out)

        # fileName, _ = QFileDialog.getSaveFileName(self, "Export Contact", '',
        # "vCard Files (*.vcf);;All Files (*)")
        #
        # if not fileName:
        # return
        #
        # out_file = QFile(fileName)
        #
        # if not out_file.open(QIODevice.WriteOnly):
        # QMessageBox.information(self, "Unable to open file",
        # out_file.errorString())
        # return