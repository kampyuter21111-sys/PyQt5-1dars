import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QLineEdit, QVBoxLayout, QHBoxLayout)

app = QApplication(sys.argv)

oyna = QWidget()
oyna.setWindowTitle("3-masala")
oyna.resize(350, 250)

son1 = QLineEdit()
son1.setPlaceholderText("1-son")
son2 = QLineEdit()
son2.setPlaceholderText("2-son")

btn_qosh = QPushButton("Qo'shish")
btn_ayir = QPushButton("Ayirish")
btn_kopay = QPushButton("Ko'paytirish")
btn_bol = QPushButton("Bo'lish")

label = QLabel("Javob: ")


def sonlarni_ol():
    try:
        return float(son1.text()), float(son2.text())
    except ValueError:
        return None


def qosh():
    s = sonlarni_ol()
    if s is None:
        label.setText("Iltimos, son kiriting!")
    else:
        label.setText("Javob: " + str(s[0] + s[1]))


def ayir():
    s = sonlarni_ol()
    if s is None:
        label.setText("Iltimos, son kiriting!")
    else:
        label.setText("Javob: " + str(s[0] - s[1]))


def kopay():
    s = sonlarni_ol()
    if s is None:
        label.setText("Iltimos, son kiriting!")
    else:
        label.setText("Javob: " + str(s[0] * s[1]))


def bol():
    s = sonlarni_ol()
    if s is None:
        label.setText("Iltimos, son kiriting!")
    elif s[1] == 0:
        label.setText("0 ga bo'lib bo'lmaydi!")
    else:
        label.setText("Javob: " + str(s[0] / s[1]))


btn_qosh.clicked.connect(qosh)
btn_ayir.clicked.connect(ayir)
btn_kopay.clicked.connect(kopay)
btn_bol.clicked.connect(bol)

tugmalar = QHBoxLayout()
tugmalar.addWidget(btn_qosh)
tugmalar.addWidget(btn_ayir)
tugmalar.addWidget(btn_kopay)
tugmalar.addWidget(btn_bol)

layout = QVBoxLayout()
layout.addWidget(son1)
layout.addWidget(son2)
layout.addLayout(tugmalar)
layout.addWidget(label)
oyna.setLayout(layout)

oyna.show()
sys.exit(app.exec_())
