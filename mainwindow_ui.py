# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Feb 22 00:15:29 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(310, 10, 342, 494))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView_card = QtWidgets.QGraphicsView(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_card.sizePolicy().hasHeightForWidth())
        self.graphicsView_card.setSizePolicy(sizePolicy)
        self.graphicsView_card.setObjectName("graphicsView_card")
        self.verticalLayout_2.addWidget(self.graphicsView_card)
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_base)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listView_base = QtWidgets.QListView(self.groupBox_base)
        self.listView_base.setMovement(QtWidgets.QListView.Snap)
        self.listView_base.setObjectName("listView_base")
        self.verticalLayout_3.addWidget(self.listView_base)
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
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
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
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_unique_base = QtWidgets.QCheckBox(self.groupBox_base)
        self.checkBox_unique_base.setObjectName("checkBox_unique_base")
        self.horizontalLayout_2.addWidget(self.checkBox_unique_base)
        self.checkBox_mono_base = QtWidgets.QCheckBox(self.groupBox_base)
        self.checkBox_mono_base.setObjectName("checkBox_mono_base")
        self.horizontalLayout_2.addWidget(self.checkBox_mono_base)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
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
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.groupBox_base)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
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
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.pushButton_manarlize = QtWidgets.QPushButton(self.groupBox_base)
        self.pushButton_manarlize.setObjectName("pushButton_manarlize")
        self.verticalLayout_3.addWidget(self.pushButton_manarlize)
        self.groupBox_base_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_base_2.setGeometry(QtCore.QRect(660, 10, 311, 491))
        self.groupBox_base_2.setObjectName("groupBox_base_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_base_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listView_base_2 = QtWidgets.QListView(self.groupBox_base_2)
        self.listView_base_2.setMovement(QtWidgets.QListView.Snap)
        self.listView_base_2.setObjectName("listView_base_2")
        self.verticalLayout_4.addWidget(self.listView_base_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_type_base_2 = QtWidgets.QLabel(self.groupBox_base_2)
        self.label_type_base_2.setObjectName("label_type_base_2")
        self.horizontalLayout_6.addWidget(self.label_type_base_2)
        self.comboBox_type_base_2 = QtWidgets.QComboBox(self.groupBox_base_2)
        self.comboBox_type_base_2.setObjectName("comboBox_type_base_2")
        self.comboBox_type_base_2.addItem("")
        self.comboBox_type_base_2.addItem("")
        self.comboBox_type_base_2.addItem("")
        self.comboBox_type_base_2.addItem("")
        self.comboBox_type_base_2.addItem("")
        self.comboBox_type_base_2.addItem("")
        self.comboBox_type_base_2.addItem("")
        self.comboBox_type_base_2.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_type_base_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_r_base_2 = QtWidgets.QCheckBox(self.groupBox_base_2)
        self.checkBox_r_base_2.setStyleSheet("background-color:rgb(128, 0, 0)")
        self.checkBox_r_base_2.setText("")
        self.checkBox_r_base_2.setChecked(True)
        self.checkBox_r_base_2.setObjectName("checkBox_r_base_2")
        self.horizontalLayout_7.addWidget(self.checkBox_r_base_2)
        self.checkBox_g_base_2 = QtWidgets.QCheckBox(self.groupBox_base_2)
        self.checkBox_g_base_2.setStyleSheet("background-color:rgb(0, 128, 0)")
        self.checkBox_g_base_2.setText("")
        self.checkBox_g_base_2.setChecked(True)
        self.checkBox_g_base_2.setObjectName("checkBox_g_base_2")
        self.horizontalLayout_7.addWidget(self.checkBox_g_base_2)
        self.checkBox_w_base_2 = QtWidgets.QCheckBox(self.groupBox_base_2)
        self.checkBox_w_base_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.checkBox_w_base_2.setText("")
        self.checkBox_w_base_2.setChecked(True)
        self.checkBox_w_base_2.setObjectName("checkBox_w_base_2")
        self.horizontalLayout_7.addWidget(self.checkBox_w_base_2)
        self.checkBox_u_base_2 = QtWidgets.QCheckBox(self.groupBox_base_2)
        self.checkBox_u_base_2.setStyleSheet("background-color:rgb(0, 0, 255)")
        self.checkBox_u_base_2.setText("")
        self.checkBox_u_base_2.setChecked(True)
        self.checkBox_u_base_2.setObjectName("checkBox_u_base_2")
        self.horizontalLayout_7.addWidget(self.checkBox_u_base_2)
        self.checkBox_b_base_2 = QtWidgets.QCheckBox(self.groupBox_base_2)
        self.checkBox_b_base_2.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.checkBox_b_base_2.setText("")
        self.checkBox_b_base_2.setChecked(True)
        self.checkBox_b_base_2.setObjectName("checkBox_b_base_2")
        self.horizontalLayout_7.addWidget(self.checkBox_b_base_2)
        self.checkBox_cl_base_2 = QtWidgets.QCheckBox(self.groupBox_base_2)
        self.checkBox_cl_base_2.setStyleSheet("background-color:rgb(128, 128, 128)")
        self.checkBox_cl_base_2.setText("")
        self.checkBox_cl_base_2.setChecked(True)
        self.checkBox_cl_base_2.setObjectName("checkBox_cl_base_2")
        self.horizontalLayout_7.addWidget(self.checkBox_cl_base_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_unique_base_2 = QtWidgets.QCheckBox(self.groupBox_base_2)
        self.checkBox_unique_base_2.setObjectName("checkBox_unique_base_2")
        self.horizontalLayout_8.addWidget(self.checkBox_unique_base_2)
        self.checkBox_mono_base_2 = QtWidgets.QCheckBox(self.groupBox_base_2)
        self.checkBox_mono_base_2.setObjectName("checkBox_mono_base_2")
        self.horizontalLayout_8.addWidget(self.checkBox_mono_base_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labe_mana_base_2 = QtWidgets.QLabel(self.groupBox_base_2)
        self.labe_mana_base_2.setObjectName("labe_mana_base_2")
        self.horizontalLayout_9.addWidget(self.labe_mana_base_2)
        self.comboBox_mana_base_2 = QtWidgets.QComboBox(self.groupBox_base_2)
        self.comboBox_mana_base_2.setObjectName("comboBox_mana_base_2")
        self.comboBox_mana_base_2.addItem("")
        self.comboBox_mana_base_2.addItem("")
        self.comboBox_mana_base_2.addItem("")
        self.comboBox_mana_base_2.addItem("")
        self.comboBox_mana_base_2.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_mana_base_2)
        self.spinBox_mana_base_2 = QtWidgets.QSpinBox(self.groupBox_base_2)
        self.spinBox_mana_base_2.setMinimum(1)
        self.spinBox_mana_base_2.setMaximum(50)
        self.spinBox_mana_base_2.setProperty("value", 1)
        self.spinBox_mana_base_2.setObjectName("spinBox_mana_base_2")
        self.horizontalLayout_9.addWidget(self.spinBox_mana_base_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.groupBox_base_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.comboBox_ability_base_2 = QtWidgets.QComboBox(self.groupBox_base_2)
        self.comboBox_ability_base_2.setObjectName("comboBox_ability_base_2")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.comboBox_ability_base_2.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_ability_base_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.pushButton_manarlize_2 = QtWidgets.QPushButton(self.groupBox_base_2)
        self.pushButton_manarlize_2.setObjectName("pushButton_manarlize_2")
        self.verticalLayout_4.addWidget(self.pushButton_manarlize_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 22))
        self.menubar.setObjectName("menubar")
        self.menuDeck = QtWidgets.QMenu(self.menubar)
        self.menuDeck.setObjectName("menuDeck")
        self.menuCard = QtWidgets.QMenu(self.menubar)
        self.menuCard.setObjectName("menuCard")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad_Deck = QtWidgets.QAction(MainWindow)
        self.actionLoad_Deck.setObjectName("actionLoad_Deck")
        self.actionSave_Deck = QtWidgets.QAction(MainWindow)
        self.actionSave_Deck.setObjectName("actionSave_Deck")
        self.actionPrint_URL = QtWidgets.QAction(MainWindow)
        self.actionPrint_URL.setObjectName("actionPrint_URL")
        self.actionManaRlize = QtWidgets.QAction(MainWindow)
        self.actionManaRlize.setObjectName("actionManaRlize")
        self.actionGet_Statistics = QtWidgets.QAction(MainWindow)
        self.actionGet_Statistics.setObjectName("actionGet_Statistics")
        self.actionUpdate_Mana_Curve = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Mana_Curve.setObjectName("actionUpdate_Mana_Curve")
        self.actionPrint_JSON = QtWidgets.QAction(MainWindow)
        self.actionPrint_JSON.setObjectName("actionPrint_JSON")
        self.actionNext_Card_in_Deck = QtWidgets.QAction(MainWindow)
        self.actionNext_Card_in_Deck.setObjectName("actionNext_Card_in_Deck")
        self.actionPrev_Card_in_Deck = QtWidgets.QAction(MainWindow)
        self.actionPrev_Card_in_Deck.setObjectName("actionPrev_Card_in_Deck")
        self.actionDownload_Images = QtWidgets.QAction(MainWindow)
        self.actionDownload_Images.setObjectName("actionDownload_Images")
        self.menuDeck.addAction(self.actionLoad_Deck)
        self.menuDeck.addAction(self.actionSave_Deck)
        self.menuDeck.addSeparator()
        self.menuDeck.addAction(self.actionDownload_Images)
        self.menuDeck.addSeparator()
        self.menuDeck.addAction(self.actionManaRlize)
        self.menuDeck.addAction(self.actionUpdate_Mana_Curve)
        self.menuDeck.addAction(self.actionGet_Statistics)
        self.menuCard.addAction(self.actionPrint_URL)
        self.menuCard.addAction(self.actionPrint_JSON)
        self.menuCard.addSeparator()
        self.menuCard.addAction(self.actionNext_Card_in_Deck)
        self.menuCard.addAction(self.actionPrev_Card_in_Deck)
        self.menubar.addAction(self.menuDeck.menuAction())
        self.menubar.addAction(self.menuCard.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ManaR"))
        self.groupBox.setTitle(_translate("MainWindow", "Card view"))
        self.groupBox_3.setTitle(_translate("MainWindow", "ManaRlysis results"))
        self.groupBox_base.setTitle(_translate("MainWindow", "Base Deck"))
        self.label_type_base.setText(_translate("MainWindow", "Type"))
        self.comboBox_type_base.setItemText(0, _translate("MainWindow", "All Cards"))
        self.comboBox_type_base.setItemText(1, _translate("MainWindow", "Artifact"))
        self.comboBox_type_base.setItemText(2, _translate("MainWindow", "Creature"))
        self.comboBox_type_base.setItemText(3, _translate("MainWindow", "Enchantment"))
        self.comboBox_type_base.setItemText(4, _translate("MainWindow", "Instant"))
        self.comboBox_type_base.setItemText(5, _translate("MainWindow", "Land"))
        self.comboBox_type_base.setItemText(6, _translate("MainWindow", "Planeswalker"))
        self.comboBox_type_base.setItemText(7, _translate("MainWindow", "Sorcery"))
        self.checkBox_unique_base.setText(_translate("MainWindow", "Unique"))
        self.checkBox_mono_base.setText(_translate("MainWindow", "Mono Color"))
        self.labe_mana_base.setText(_translate("MainWindow", "Mana Cost"))
        self.comboBox_mana_base.setItemText(0, _translate("MainWindow", ">="))
        self.comboBox_mana_base.setItemText(1, _translate("MainWindow", "="))
        self.comboBox_mana_base.setItemText(2, _translate("MainWindow", "<"))
        self.comboBox_mana_base.setItemText(3, _translate("MainWindow", "<="))
        self.comboBox_mana_base.setItemText(4, _translate("MainWindow", ">"))
        self.label.setText(_translate("MainWindow", "Ability/Mechanic"))
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
        self.pushButton_manarlize.setText(_translate("MainWindow", "ManaRlize"))
        self.groupBox_base_2.setTitle(_translate("MainWindow", "New Deck"))
        self.label_type_base_2.setText(_translate("MainWindow", "Type"))
        self.comboBox_type_base_2.setItemText(0, _translate("MainWindow", "All Cards"))
        self.comboBox_type_base_2.setItemText(1, _translate("MainWindow", "Artifact"))
        self.comboBox_type_base_2.setItemText(2, _translate("MainWindow", "Creature"))
        self.comboBox_type_base_2.setItemText(3, _translate("MainWindow", "Enchantment"))
        self.comboBox_type_base_2.setItemText(4, _translate("MainWindow", "Instant"))
        self.comboBox_type_base_2.setItemText(5, _translate("MainWindow", "Land"))
        self.comboBox_type_base_2.setItemText(6, _translate("MainWindow", "Planeswalker"))
        self.comboBox_type_base_2.setItemText(7, _translate("MainWindow", "Sorcery"))
        self.checkBox_unique_base_2.setText(_translate("MainWindow", "Unique"))
        self.checkBox_mono_base_2.setText(_translate("MainWindow", "Mono Color"))
        self.labe_mana_base_2.setText(_translate("MainWindow", "Mana Cost"))
        self.comboBox_mana_base_2.setItemText(0, _translate("MainWindow", ">="))
        self.comboBox_mana_base_2.setItemText(1, _translate("MainWindow", "="))
        self.comboBox_mana_base_2.setItemText(2, _translate("MainWindow", "<"))
        self.comboBox_mana_base_2.setItemText(3, _translate("MainWindow", "<="))
        self.comboBox_mana_base_2.setItemText(4, _translate("MainWindow", ">"))
        self.label_2.setText(_translate("MainWindow", "Ability/Mechanic"))
        self.comboBox_ability_base_2.setItemText(0, _translate("MainWindow", "Any"))
        self.comboBox_ability_base_2.setItemText(1, _translate("MainWindow", "Bolster"))
        self.comboBox_ability_base_2.setItemText(2, _translate("MainWindow", "Dash"))
        self.comboBox_ability_base_2.setItemText(3, _translate("MainWindow", "Dearthtouch"))
        self.comboBox_ability_base_2.setItemText(4, _translate("MainWindow", "Delve"))
        self.comboBox_ability_base_2.setItemText(5, _translate("MainWindow", "Ferocious"))
        self.comboBox_ability_base_2.setItemText(6, _translate("MainWindow", "Flash"))
        self.comboBox_ability_base_2.setItemText(7, _translate("MainWindow", "Flying"))
        self.comboBox_ability_base_2.setItemText(8, _translate("MainWindow", "Haste"))
        self.comboBox_ability_base_2.setItemText(9, _translate("MainWindow", "Hexproof"))
        self.comboBox_ability_base_2.setItemText(10, _translate("MainWindow", "Indestructible"))
        self.comboBox_ability_base_2.setItemText(11, _translate("MainWindow", "Lifelink"))
        self.comboBox_ability_base_2.setItemText(12, _translate("MainWindow", "Manifest"))
        self.comboBox_ability_base_2.setItemText(13, _translate("MainWindow", "Morph"))
        self.comboBox_ability_base_2.setItemText(14, _translate("MainWindow", "Outlast"))
        self.comboBox_ability_base_2.setItemText(15, _translate("MainWindow", "Protection"))
        self.comboBox_ability_base_2.setItemText(16, _translate("MainWindow", "Prowess"))
        self.comboBox_ability_base_2.setItemText(17, _translate("MainWindow", "Raid"))
        self.comboBox_ability_base_2.setItemText(18, _translate("MainWindow", "Reach"))
        self.comboBox_ability_base_2.setItemText(19, _translate("MainWindow", "Vigilance"))
        self.pushButton_manarlize_2.setText(_translate("MainWindow", "ManaRlize"))
        self.menuDeck.setTitle(_translate("MainWindow", "Deck"))
        self.menuCard.setTitle(_translate("MainWindow", "Card"))
        self.actionLoad_Deck.setText(_translate("MainWindow", "Load Deck"))
        self.actionLoad_Deck.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Deck.setText(_translate("MainWindow", "Save Deck"))
        self.actionSave_Deck.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPrint_URL.setText(_translate("MainWindow", "Print URL"))
        self.actionManaRlize.setText(_translate("MainWindow", "ManaRlize"))
        self.actionManaRlize.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionGet_Statistics.setText(_translate("MainWindow", "Get Statistics"))
        self.actionUpdate_Mana_Curve.setText(_translate("MainWindow", "Update Mana Curve"))
        self.actionPrint_JSON.setText(_translate("MainWindow", "Print JSON"))
        self.actionNext_Card_in_Deck.setText(_translate("MainWindow", "Next Card in Deck"))
        self.actionPrev_Card_in_Deck.setText(_translate("MainWindow", "Prev Card in Deck"))
        self.actionDownload_Images.setText(_translate("MainWindow", "Download Images"))
        self.actionDownload_Images.setShortcut(_translate("MainWindow", "Ctrl+D"))

