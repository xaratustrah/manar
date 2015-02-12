"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

Feb 2015 Xaratustrah

"""

from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QFileDialog
from PyQt5.QtGui import QPixmap, QKeyEvent, QStandardItemModel, QStandardItem
from mainwindow_ui import Ui_MainWindow

from deck import Deck
from card import Card


class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        self.model = QStandardItemModel(self.listView_db)

        # signals
        self.actionLoad_Deck.triggered.connect(self.open_file_dialog)
        self.listView_db.clicked.connect(self.update_card_view)

    def update_card_view(self):
        filename = 'my_cards/386554.jpg'
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(filename))
        self.graphicsView_card.setScene(scene)


    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Deck", '', "All Files (*)")

        if not file_name:
            return

        base_deck = Deck("base_deck")
        base_deck.make_from_file(file_name)
        lst = base_deck.nonland_card_list
        # lst = Deck.get_unique_list(lst)
        self.update_base_deck_list_view(lst)

    def update_base_deck_list_view(self, lst):
        for c in lst:
            item = QStandardItem(c.__str__())
            self.model.appendRow(item)
        self.listView_db.setModel(self.model)
        self.listView_db.show()



        # fileName, _ = QFileDialog.getSaveFileName(self, "Export Contact", '',
        # "vCard Files (*.vcf);;All Files (*)")
        #
        # if not fileName:
        # return
        #
        # out_file = QFile(fileName)
        #
        # if not out_file.open(QIODevice.WriteOnly):
        #     QMessageBox.information(self, "Unable to open file",
        #             out_file.errorString())
        #     return