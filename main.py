from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys
import qtawesome as qta


class UI(QWidget):
    def __init__(self):

        super().__init__()
        self.setFixedWidth(600)
        self.setFixedHeight(300)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
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
        self.icon_exit = qta.icon('mdi.close', color='white', scale_factor=2)
        self.btn_exit = QPushButton(self.icon_exit, '', self)
        self.btn_exit.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_exit.clicked.connect(exit)
        self.btn_exit.setStyleSheet("background: #222;" + "border: none;" + "color: white;")
        self.btn_exit.move(560, 20)

        self.title = QLabel('Authentication', self)
        self.title.setStyleSheet("background: #222;" + "color: white;")
        self.title.move(25, 20)

        self.entry_username = QLineEdit(self)
        self.entry_username.setPlaceholderText("Enter username")
        self.entry_username.setStyleSheet(
            """
            background: white; 
            color: #222;
            """)
        self.entry_username.move(160, 97)

        self.entry_password = QLineEdit(self)
        self.entry_password.setPlaceholderText("Enter password")
        self.entry_password.move(160, 150)

        self.btn_login = QPushButton('Login', self)
        self.btn_login.clicked.connect(self.login)
        self.btn_login.setStyleSheet(
            """
            * {
                background: #222;
                color: #ff007f;
                border: 1px solid #ff007f;
                padding: 10px 50px;
                border-radius: 2px;
            }
            
            :hover {
                background: #ff007f;
                color: #222;
            }
            """)
        self.btn_login.move(244, 200)
        self.dict_user_pass = {"Zoe": "wavywave99", "Adam": "bighead64", "dekapaan": "dayon"}

        self.old_pos = self.pos()

        self.show()

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        moved = QtCore.QPoint(event.globalPos() - self.old_pos)
        self.move(self.x() + moved.x(), self.y() + moved.y())
        self.old_pos = event.globalPos()

    def login(self):
        try:
            user = self.entry_username.text()
            password = self.entry_password.text()
            if user in self.dict_user_pass:
                if password == self.dict_user_pass[user]:
                    import exception_handling
                    root.destroy()
                else:
                    raise ValueError
            else:
                raise KeyError

        except ValueError:
            msg_box = QMessageBox()
            msg_box.setText("Incorrect password")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.exec()

        except KeyError:
            msg_box = QMessageBox()
            msg_box.setText("Username doesn't exist")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.exec()


app = QApplication(sys.argv)
root = UI()
app.exec()
