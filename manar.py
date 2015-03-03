#!/usr/bin/env python
"""
Organize your MTG cards, deck and strategy. This is an object oriented interface to mtg cards.

-- GUI Application --

Feb 2015 Xaratustrah

"""

import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import mainWindow


def main():
    app = QApplication(sys.argv)
    form = mainWindow()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
