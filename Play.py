import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import Board


class MainWindow(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet("background-color: #4A6274;")

        self.all_buttons = list()
        self.text_all_buttons = list()
        layout = QtWidgets.QGridLayout(self)
        layout.setSpacing(5)

        for x, rows in enumerate(Board.board):
            for y, cell in enumerate(rows):

                if cell == 0: cell = ' '
                button = QtWidgets.QPushButton(str(cell), self)
                button.setFixedHeight(100)
                button.setFixedWidth(100)
                button.setFont(QtGui.QFont('Times', 25))
                layout.addWidget(button, x, y)

                if cell == ' ':
                    button.setCursor(QtCore.Qt.PointingHandCursor)
                    button.mousePressEvent = lambda event: self.mousePressEvent(event)
                    button.setStyleSheet(
                        'QPushButton {background-color: #94ACBF; color: white; border: 1px solid white}')
                else:
                    button.setEnabled(False)
                    button.setStyleSheet(
                        'QPushButton {background-color: #94ACBF; color: white; border: 1px solid white}')
                self.text_all_buttons.append(cell)
                self.all_buttons.append(button)
        self.last_clicked = ''
        self.setLayout(layout)
        self.show()

    def keyPressEvent(self, event):
        k = (chr(event.key()))
        self.last_clicked.setText(k)
        self.last_clicked.setStyleSheet("background-color: #94ACBF; color: white;  border: 1px solid white")

    def mousePressEvent(self, event):
        widget = self.childAt(event.pos())
        self.last_clicked = widget
        for cell, button in enumerate(self.all_buttons):
            if widget == button:
                button.setStyleSheet("background-color: #c9dff0; color: white; border: 5px solid pink")
            else:
                button.setStyleSheet("background-color: #94ACBF; color: white; border: 1px solid white")

        return QtWidgets.QWidget.mousePressEvent(self, event)

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(QtCore.Qt.white, 7, cap=QtCore.Qt.FlatCap))
        painter.setBrush(QtCore.Qt.white)

        painter.drawLine(957, 8, 5, 8)
        painter.drawLine(957, 324, 5, 324)
        painter.drawLine(957, 638, 5, 638)
        painter.drawLine(957, 954, 5, 954)

        painter.drawLine(8, 5, 8, 957)
        painter.drawLine(324, 5, 324, 957)
        painter.drawLine(638, 5, 638, 957)
        painter.drawLine(954, 5, 954, 957)

        self.setFixedSize(self.size())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
