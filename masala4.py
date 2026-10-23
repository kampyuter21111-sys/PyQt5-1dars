import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

oyna = QWidget()
oyna.setWindowTitle("4-masala")
oyna.resize(300, 150)

label = QLabel("Rangli matn")
label.setStyleSheet("font-size: 24px;")
tugma = QPushButton("Rangni almashtir")

ranglar = ["red", "blue", "green", "yellow"]


def rang_almashtir():
    rang = random.choice(ranglar)
    label.setStyleSheet("font-size: 24px; color: " + rang + ";")


tugma.clicked.connect(rang_almashtir)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(tugma)
oyna.setLayout(layout)

oyna.show()
sys.exit(app.exec_())
