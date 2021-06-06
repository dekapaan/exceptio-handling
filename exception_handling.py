from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys
import qtawesome as qta


class ExceptionHandling(QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setFixedWidth(400)
        self.setFixedHeight(200)
        self.setStyleSheet(
            """
            * {background: #222;}

            QLineEdit {
                background: white; 
                color: #222;
                border-radius: 2px;
                width: 300px;
                height: 30px;
            }
            """
        )
        self.title = QLabel('Exception handling', self)
        self.title.setStyleSheet("background: #222;" + "color: white;")
        self.title.move(12, 11)

        self.icon_exit = qta.icon('mdi.close', color='white', scale_factor=2)
        self.btn_exit = QPushButton(self.icon_exit, '', self)
        self.btn_exit.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_exit.clicked.connect(exit)
        self.btn_exit.setStyleSheet("background: #222;" + "border: none;" + "color: white;")
        self.btn_exit.move(370, 12)

        self.entry_amount = QLineEdit(self)
        self.entry_amount.setPlaceholderText("Enter amount in your account")
        self.entry_amount.move(50, 70)

        self.btn_login = QPushButton('Check Qualification', self)
        self.btn_login.clicked.connect(self.check)
        self.btn_login.setStyleSheet(
            """
            * {
                background: #222;
                color: #ff007f;
                border: 1px solid #ff007f;
                padding: 10px 30px;
                border-radius: 2px;
            }

            :hover {
                background: #ff007f;
                color: #222;
            }
            """)
        self.btn_login.move(100, 120)

        self.show()

        self.old_pos = self.pos()

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        moved = QtCore.QPoint(event.globalPos() - self.old_pos)
        self.move(self.x() + moved.x(), self.y() + moved.y())
        self.old_pos = event.globalPos()

    def check(self):
        try:
            amount = int(self.entry_amount.text())
            if amount < 0:
                raise ValueError

            if amount < 3000:
                msg_box = QMessageBox()
                msg_box.setText("Insufficient Amount")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setWindowTitle("Warning")
                msg_box.exec()

            elif amount >= 3000:
                msg_box = QMessageBox()
                msg_box.setText("Congratulations. You qualify to go to Malaysia")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Good News")
                msg_box.exec()

        except ValueError:
            msg_box = QMessageBox()
            msg_box.setText("Invalid amount")
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.exec()


app = QApplication(sys.argv)
root = ExceptionHandling()