import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QLineEdit, QVBoxLayout)

app = QApplication(sys.argv)

oyna = QWidget()
oyna.setWindowTitle("5-masala")
oyna.resize(300, 180)

parol = QLineEdit()
parol.setPlaceholderText("Parolni kiriting")
parol.setEchoMode(QLineEdit.Password)
tugma = QPushButton("Tekshirish")
label = QLabel("")


def tekshir():
    if parol.text() == "12345":
        label.setText("Parol to'g'ri")
    else:
        label.setText("Noto'g'ri parol")


tugma.clicked.connect(tekshir)

layout = QVBoxLayout()
layout.addWidget(parol)
layout.addWidget(tugma)
layout.addWidget(label)
oyna.setLayout(layout)

oyna.show()
sys.exit(app.exec_())
