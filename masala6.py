import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

oyna = QWidget()
oyna.setWindowTitle("6-masala")
oyna.resize(300, 150)

son = 0

label = QLabel("0")
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("font-size: 30px;")

btn_plus = QPushButton("+1")
btn_minus = QPushButton("-1")


def oshir():
    global son
    son += 1
    label.setText(str(son))


def kamaytir():
    global son
    son -= 1
    label.setText(str(son))


btn_plus.clicked.connect(oshir)
btn_minus.clicked.connect(kamaytir)

tugmalar = QHBoxLayout()
tugmalar.addWidget(btn_plus)
tugmalar.addWidget(btn_minus)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addLayout(tugmalar)
oyna.setLayout(layout)

oyna.show()
sys.exit(app.exec_())
