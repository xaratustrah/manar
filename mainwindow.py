"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QFileDialog
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from mainwindow_ui import Ui_MainWindow

from deck import Deck
from card import Card


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.base_deck = Deck("base_deck")
        self.setupUi(self)

        # signals
        self.actionLoad_Deck.triggered.connect(self.open_file_dialog)
        self.listView_base.clicked.connect(self.update_card_view)
        self.comboBox_type_base.activated.connect(self.process_filter_base)

    def update_card_view(self):
        print(self.base_deck.get_filename_from_name('Abzan Guide'))
        print(self.listView_base.clicked)
        print(self.listView_base.data().toString())
        filename = 'my_cards/386554.jpg'
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(filename))
        self.graphicsView_card.setScene(scene)


    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Deck", '', "All Files (*)")

        if not file_name:
            return

        self.base_deck.make_from_file(file_name)
        lst = self.base_deck.card_list
        # lst = Deck.get_unique_list(lst)
        self.update_base_deck_list_view(lst)

    def update_base_deck_list_view(self, lst):
        model_base = QStandardItemModel(self.listView_base)
        for c in lst:
            item = QStandardItem(c.__str__())
            model_base.appendRow(item)
        self.listView_base.setModel(model_base)
        self.listView_base.show()

    def process_filter_base(self):
        typ = self.comboBox_type_base.currentText()
        if typ == 'Land':
            lst = self.base_deck.get_cards_of_type(typ)
            self.update_base_deck_list_view(lst)
            return
        if typ == 'All Cards':
            lst = self.base_deck.card_list
            self.update_base_deck_list_view(lst)
            return
        else:
            lst = self.base_deck.get_cards_of_type(typ)

        lst_out = []
        if self.checkBox_r_base.isChecked():
            lst_out.extend(Deck.get_reds(lst))

        if self.checkBox_g_base.isChecked():
            lst_out.extend(Deck.get_greens(lst))

        if self.checkBox_w_base.isChecked():
            lst_out.extend(Deck.get_whites(lst))

        if self.checkBox_u_base.isChecked():
            lst_out.extend(Deck.get_blues(lst))

        if self.checkBox_b_base.isChecked():
            lst_out.extend(Deck.get_blacks(lst))

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
        #     return