# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Mar  4 21:58:13 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(630, 10, 341, 494))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.graphicsView_card = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView_card.setGeometry(QtCore.QRect(10, 30, 320, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_card.sizePolicy().hasHeightForWidth())
        self.graphicsView_card.setSizePolicy(sizePolicy)
        self.graphicsView_card.setObjectName("graphicsView_card")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 500, 961, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.groupBox_base = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_base.setGeometry(QtCore.QRect(10, 10, 291, 491))
        self.groupBox_base.setObjectName("groupBox_base")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_base)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_r_base = QtWidgets.QCheckBox(self.groupBox_base)
        self.checkBox_r_base.setStyleSheet("background-color:rgb(128, 0, 0)")
        self.checkBox_r_base.setText("")
        self.checkBox_r_base.setChecked(True)
        self.checkBox_r_base.setObjectName("checkBox_r_base")
        self.horizontalLayout.addWidget(self.checkBox_r_base)
        self.checkBox_g_base = QtWidgets.QCheckBox(self.groupBox_base)
        self.checkBox_g_base.setStyleSheet("background-color:rgb(0, 128, 0)")
        self.checkBox_g_base.setText("")
        self.checkBox_g_base.setChecked(True)
        self.checkBox_g_base.setObjectName("checkBox_g_base")
        self.horizontalLayout.addWidget(self.checkBox_g_base)
        self.checkBox_w_base = QtWidgets.QCheckBox(self.groupBox_base)
        self.checkBox_w_base.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.checkBox_w_base.setText("")
        self.checkBox_w_base.setChecked(True)
        self.checkBox_w_base.setObjectName("checkBox_w_base")
        self.horizontalLayout.addWidget(self.checkBox_w_base)
        self.checkBox_u_base = QtWidgets.QCheckBox(self.groupBox_base)
        self.checkBox_u_base.setStyleSheet("background-color:rgb(0, 0, 255)")
        self.checkBox_u_base.setText("")
        self.checkBox_u_base.setChecked(True)
        self.checkBox_u_base.setObjectName("checkBox_u_base")
        self.horizontalLayout.addWidget(self.checkBox_u_base)
        self.checkBox_b_base = QtWidgets.QCheckBox(self.groupBox_base)
        self.checkBox_b_base.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.checkBox_b_base.setText("")
        self.checkBox_b_base.setChecked(True)
        self.checkBox_b_base.setObjectName("checkBox_b_base")
        self.horizontalLayout.addWidget(self.checkBox_b_base)
        self.checkBox_cl_base = QtWidgets.QCheckBox(self.groupBox_base)
        self.checkBox_cl_base.setStyleSheet("background-color:rgb(128, 128, 128)")
        self.checkBox_cl_base.setText("")
        self.checkBox_cl_base.setChecked(True)
        self.checkBox_cl_base.setObjectName("checkBox_cl_base")
        self.horizontalLayout.addWidget(self.checkBox_cl_base)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_color = QtWidgets.QLabel(self.groupBox_base)
        self.label_color.setObjectName("label_color")
        self.horizontalLayout_2.addWidget(self.label_color)
        self.radioButton_mono_base = QtWidgets.QRadioButton(self.groupBox_base)
        self.radioButton_mono_base.setObjectName("radioButton_mono_base")
        self.horizontalLayout_2.addWidget(self.radioButton_mono_base)
        self.radioButton_dual_base = QtWidgets.QRadioButton(self.groupBox_base)
        self.radioButton_dual_base.setObjectName("radioButton_dual_base")
        self.horizontalLayout_2.addWidget(self.radioButton_dual_base)
        self.radioButton_multi_base = QtWidgets.QRadioButton(self.groupBox_base)
        self.radioButton_multi_base.setChecked(True)
        self.radioButton_multi_base.setObjectName("radioButton_multi_base")
        self.horizontalLayout_2.addWidget(self.radioButton_multi_base)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_type_base = QtWidgets.QLabel(self.groupBox_base)
        self.label_type_base.setObjectName("label_type_base")
        self.horizontalLayout_4.addWidget(self.label_type_base)
        self.comboBox_type_base = QtWidgets.QComboBox(self.groupBox_base)
        self.comboBox_type_base.setObjectName("comboBox_type_base")
        self.comboBox_type_base.addItem("")
        self.comboBox_type_base.addItem("")
        self.comboBox_type_base.addItem("")
        self.comboBox_type_base.addItem("")
        self.comboBox_type_base.addItem("")
        self.comboBox_type_base.addItem("")
        self.comboBox_type_base.addItem("")
        self.comboBox_type_base.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_type_base)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labe_mana_base = QtWidgets.QLabel(self.groupBox_base)
        self.labe_mana_base.setObjectName("labe_mana_base")
        self.horizontalLayout_3.addWidget(self.labe_mana_base)
        self.comboBox_mana_base = QtWidgets.QComboBox(self.groupBox_base)
        self.comboBox_mana_base.setObjectName("comboBox_mana_base")
        self.comboBox_mana_base.addItem("")
        self.comboBox_mana_base.addItem("")
        self.comboBox_mana_base.addItem("")
        self.comboBox_mana_base.addItem("")
        self.comboBox_mana_base.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_mana_base)
        self.spinBox_mana_base = QtWidgets.QSpinBox(self.groupBox_base)
        self.spinBox_mana_base.setMinimum(1)
        self.spinBox_mana_base.setMaximum(50)
        self.spinBox_mana_base.setProperty("value", 1)
        self.spinBox_mana_base.setObjectName("spinBox_mana_base")
        self.horizontalLayout_3.addWidget(self.spinBox_mana_base)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_ability_base = QtWidgets.QLabel(self.groupBox_base)
        self.label_ability_base.setObjectName("label_ability_base")
        self.horizontalLayout_5.addWidget(self.label_ability_base)
        self.comboBox_ability_base = QtWidgets.QComboBox(self.groupBox_base)
        self.comboBox_ability_base.setObjectName("comboBox_ability_base")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.comboBox_ability_base.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_ability_base)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_subtype_base = QtWidgets.QLabel(self.groupBox_base)
        self.label_subtype_base.setObjectName("label_subtype_base")
        self.horizontalLayout_6.addWidget(self.label_subtype_base)
        self.comboBox_subtype_base = QtWidgets.QComboBox(self.groupBox_base)
        self.comboBox_subtype_base.setObjectName("comboBox_subtype_base")
        self.comboBox_subtype_base.addItem("")
        self.comboBox_subtype_base.addItem("")
        self.comboBox_subtype_base.addItem("")
        self.comboBox_subtype_base.addItem("")
        self.comboBox_subtype_base.addItem("")
        self.comboBox_subtype_base.addItem("")
        self.comboBox_subtype_base.addItem("")
        self.comboBox_subtype_base.addItem("")
        self.comboBox_subtype_base.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_subtype_base)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_rarity_base = QtWidgets.QLabel(self.groupBox_base)
        self.label_rarity_base.setObjectName("label_rarity_base")
        self.horizontalLayout_7.addWidget(self.label_rarity_base)
        self.comboBox_rarity_base = QtWidgets.QComboBox(self.groupBox_base)
        self.comboBox_rarity_base.setObjectName("comboBox_rarity_base")
        self.comboBox_rarity_base.addItem("")
        self.comboBox_rarity_base.addItem("")
        self.comboBox_rarity_base.addItem("")
        self.comboBox_rarity_base.addItem("")
        self.comboBox_rarity_base.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_rarity_base)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(self.groupBox_base)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(self.groupBox_base)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.pushButton_load = QtWidgets.QPushButton(self.groupBox_base)
        self.pushButton_load.setObjectName("pushButton_load")
        self.horizontalLayout_10.addWidget(self.pushButton_load)
        self.pushButton_clear_base = QtWidgets.QPushButton(self.groupBox_base)
        self.pushButton_clear_base.setObjectName("pushButton_clear_base")
        self.horizontalLayout_10.addWidget(self.pushButton_clear_base)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.groupBox_base)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_base)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_8.addWidget(self.pushButton_save)
        self.pushButton_clear_new = QtWidgets.QPushButton(self.groupBox_base)
        self.pushButton_clear_new.setObjectName("pushButton_clear_new")
        self.horizontalLayout_8.addWidget(self.pushButton_clear_new)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.line_2 = QtWidgets.QFrame(self.groupBox_base)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_stat = QtWidgets.QPushButton(self.groupBox_base)
        self.pushButton_stat.setObjectName("pushButton_stat")
        self.horizontalLayout_9.addWidget(self.pushButton_stat)
        self.pushButton_manarlize = QtWidgets.QPushButton(self.groupBox_base)
        self.pushButton_manarlize.setObjectName("pushButton_manarlize")
        self.horizontalLayout_9.addWidget(self.pushButton_manarlize)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.groupBox_base_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_base_2.setGeometry(QtCore.QRect(310, 10, 311, 491))
        self.groupBox_base_2.setObjectName("groupBox_base_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_base_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listView_base = QtWidgets.QListView(self.groupBox_base_2)
        self.listView_base.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_base.setTabKeyNavigation(True)
        self.listView_base.setDragEnabled(False)
        self.listView_base.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.listView_base.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.listView_base.setAlternatingRowColors(True)
        self.listView_base.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listView_base.setMovement(QtWidgets.QListView.Snap)
        self.listView_base.setObjectName("listView_base")
        self.verticalLayout_4.addWidget(self.listView_base)
        self.listView_new = QtWidgets.QListView(self.groupBox_base_2)
        self.listView_new.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_new.setTabKeyNavigation(True)
        self.listView_new.setProperty("showDropIndicator", False)
        self.listView_new.setDragDropOverwriteMode(False)
        self.listView_new.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.listView_new.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.listView_new.setAlternatingRowColors(True)
        self.listView_new.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listView_new.setMovement(QtWidgets.QListView.Snap)
        self.listView_new.setObjectName("listView_new")
        self.verticalLayout_4.addWidget(self.listView_new)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 22))
        self.menubar.setObjectName("menubar")
        self.menuDeck = QtWidgets.QMenu(self.menubar)
        self.menuDeck.setObjectName("menuDeck")
        self.menuCard = QtWidgets.QMenu(self.menubar)
        self.menuCard.setObjectName("menuCard")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad_Base_Deck = QtWidgets.QAction(MainWindow)
        self.actionLoad_Base_Deck.setObjectName("actionLoad_Base_Deck")
        self.actionSave_New_Deck = QtWidgets.QAction(MainWindow)
        self.actionSave_New_Deck.setObjectName("actionSave_New_Deck")
        self.actionPrint_URL = QtWidgets.QAction(MainWindow)
        self.actionPrint_URL.setObjectName("actionPrint_URL")
        self.actionManaRlize = QtWidgets.QAction(MainWindow)
        self.actionManaRlize.setObjectName("actionManaRlize")
        self.actionGet_Statistics = QtWidgets.QAction(MainWindow)
        self.actionGet_Statistics.setObjectName("actionGet_Statistics")
        self.actionPrint_JSON = QtWidgets.QAction(MainWindow)
        self.actionPrint_JSON.setObjectName("actionPrint_JSON")
        self.actionDownload_Images = QtWidgets.QAction(MainWindow)
        self.actionDownload_Images.setObjectName("actionDownload_Images")
        self.actionClear_Base_Deck = QtWidgets.QAction(MainWindow)
        self.actionClear_Base_Deck.setObjectName("actionClear_Base_Deck")
        self.actionClear_New_Deck = QtWidgets.QAction(MainWindow)
        self.actionClear_New_Deck.setObjectName("actionClear_New_Deck")
        self.menuDeck.addAction(self.actionLoad_Base_Deck)
        self.menuDeck.addAction(self.actionClear_Base_Deck)
        self.menuDeck.addSeparator()
        self.menuDeck.addAction(self.actionSave_New_Deck)
        self.menuDeck.addAction(self.actionClear_New_Deck)
        self.menuDeck.addSeparator()
        self.menuDeck.addAction(self.actionDownload_Images)
        self.menuDeck.addSeparator()
        self.menuDeck.addAction(self.actionManaRlize)
        self.menuDeck.addAction(self.actionGet_Statistics)
        self.menuCard.addAction(self.actionPrint_URL)
        self.menuCard.addAction(self.actionPrint_JSON)
        self.menuCard.addSeparator()
        self.menubar.addAction(self.menuDeck.menuAction())
        self.menubar.addAction(self.menuCard.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ManaR"))
        self.groupBox.setTitle(_translate("MainWindow", "Card view"))
        self.groupBox_3.setTitle(_translate("MainWindow", "ManaRlysis results"))
        self.groupBox_base.setTitle(_translate("MainWindow", "Filters"))
        self.label_color.setText(_translate("MainWindow", "Color"))
        self.radioButton_mono_base.setText(_translate("MainWindow", "mono"))
        self.radioButton_dual_base.setText(_translate("MainWindow", "dual"))
        self.radioButton_multi_base.setText(_translate("MainWindow", "multi"))
        self.label_type_base.setText(_translate("MainWindow", "Type"))
        self.comboBox_type_base.setItemText(0, _translate("MainWindow", "All Cards"))
        self.comboBox_type_base.setItemText(1, _translate("MainWindow", "Artifact"))
        self.comboBox_type_base.setItemText(2, _translate("MainWindow", "Creature"))
        self.comboBox_type_base.setItemText(3, _translate("MainWindow", "Enchantment"))
        self.comboBox_type_base.setItemText(4, _translate("MainWindow", "Instant"))
        self.comboBox_type_base.setItemText(5, _translate("MainWindow", "Land"))
        self.comboBox_type_base.setItemText(6, _translate("MainWindow", "Planeswalker"))
        self.comboBox_type_base.setItemText(7, _translate("MainWindow", "Sorcery"))
        self.labe_mana_base.setText(_translate("MainWindow", "Mana Cost"))
        self.comboBox_mana_base.setItemText(0, _translate("MainWindow", ">="))
        self.comboBox_mana_base.setItemText(1, _translate("MainWindow", "="))
        self.comboBox_mana_base.setItemText(2, _translate("MainWindow", "<"))
        self.comboBox_mana_base.setItemText(3, _translate("MainWindow", "<="))
        self.comboBox_mana_base.setItemText(4, _translate("MainWindow", ">"))
        self.label_ability_base.setText(_translate("MainWindow", "Ability/Mechanic"))
        self.comboBox_ability_base.setItemText(0, _translate("MainWindow", "Any"))
        self.comboBox_ability_base.setItemText(1, _translate("MainWindow", "Bolster"))
        self.comboBox_ability_base.setItemText(2, _translate("MainWindow", "Dash"))
        self.comboBox_ability_base.setItemText(3, _translate("MainWindow", "Dearthtouch"))
        self.comboBox_ability_base.setItemText(4, _translate("MainWindow", "Delve"))
        self.comboBox_ability_base.setItemText(5, _translate("MainWindow", "Ferocious"))
        self.comboBox_ability_base.setItemText(6, _translate("MainWindow", "Flash"))
        self.comboBox_ability_base.setItemText(7, _translate("MainWindow", "Flying"))
        self.comboBox_ability_base.setItemText(8, _translate("MainWindow", "Haste"))
        self.comboBox_ability_base.setItemText(9, _translate("MainWindow", "Hexproof"))
        self.comboBox_ability_base.setItemText(10, _translate("MainWindow", "Indestructible"))
        self.comboBox_ability_base.setItemText(11, _translate("MainWindow", "Lifelink"))
        self.comboBox_ability_base.setItemText(12, _translate("MainWindow", "Manifest"))
        self.comboBox_ability_base.setItemText(13, _translate("MainWindow", "Morph"))
        self.comboBox_ability_base.setItemText(14, _translate("MainWindow", "Outlast"))
        self.comboBox_ability_base.setItemText(15, _translate("MainWindow", "Protection"))
        self.comboBox_ability_base.setItemText(16, _translate("MainWindow", "Prowess"))
        self.comboBox_ability_base.setItemText(17, _translate("MainWindow", "Raid"))
        self.comboBox_ability_base.setItemText(18, _translate("MainWindow", "Reach"))
        self.comboBox_ability_base.setItemText(19, _translate("MainWindow", "Vigilance"))
        self.label_subtype_base.setText(_translate("MainWindow", "Sub Type"))
        self.comboBox_subtype_base.setItemText(0, _translate("MainWindow", "Any"))
        self.comboBox_subtype_base.setItemText(1, _translate("MainWindow", "Assassin"))
        self.comboBox_subtype_base.setItemText(2, _translate("MainWindow", "Beast"))
        self.comboBox_subtype_base.setItemText(3, _translate("MainWindow", "Dragon"))
        self.comboBox_subtype_base.setItemText(4, _translate("MainWindow", "Goblin"))
        self.comboBox_subtype_base.setItemText(5, _translate("MainWindow", "Human"))
        self.comboBox_subtype_base.setItemText(6, _translate("MainWindow", "Orc"))
        self.comboBox_subtype_base.setItemText(7, _translate("MainWindow", "Soldier"))
        self.comboBox_subtype_base.setItemText(8, _translate("MainWindow", "Warrior"))
        self.label_rarity_base.setText(_translate("MainWindow", "Rarity"))
        self.comboBox_rarity_base.setItemText(0, _translate("MainWindow", "Any"))
        self.comboBox_rarity_base.setItemText(1, _translate("MainWindow", "Common"))
        self.comboBox_rarity_base.setItemText(2, _translate("MainWindow", "Uncommon"))
        self.comboBox_rarity_base.setItemText(3, _translate("MainWindow", "Rare"))
        self.comboBox_rarity_base.setItemText(4, _translate("MainWindow", "Mythic"))
        self.label.setText(_translate("MainWindow", "Base Deck"))
        self.pushButton_load.setText(_translate("MainWindow", "Load"))
        self.pushButton_clear_base.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "New Deck"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_clear_new.setText(_translate("MainWindow", "Clear"))
        self.pushButton_stat.setText(_translate("MainWindow", "Statistics"))
        self.pushButton_manarlize.setText(_translate("MainWindow", "ManaRlize"))
        self.groupBox_base_2.setTitle(_translate("MainWindow", "Deck List"))
        self.menuDeck.setTitle(_translate("MainWindow", "Deck"))
        self.menuCard.setTitle(_translate("MainWindow", "Card"))
        self.actionLoad_Base_Deck.setText(_translate("MainWindow", "Load Base Deck"))
        self.actionLoad_Base_Deck.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_New_Deck.setText(_translate("MainWindow", "Save New Deck"))
        self.actionSave_New_Deck.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPrint_URL.setText(_translate("MainWindow", "Print URL"))
        self.actionManaRlize.setText(_translate("MainWindow", "ManaRlize"))
        self.actionManaRlize.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionGet_Statistics.setText(_translate("MainWindow", "Get Statistics"))
        self.actionGet_Statistics.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionPrint_JSON.setText(_translate("MainWindow", "Print JSON"))
        self.actionDownload_Images.setText(_translate("MainWindow", "Download Images"))
        self.actionDownload_Images.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionClear_Base_Deck.setText(_translate("MainWindow", "Clear Base Deck"))
        self.actionClear_New_Deck.setText(_translate("MainWindow", "Clear New Deck"))

