import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

oyna = QWidget()
oyna.setWindowTitle("2-masala")
oyna.resize(300, 200)

label = QLabel("Natija shu yerda chiqadi")
btn1 = QPushButton("Ism")
btn2 = QPushButton("Familiya")
btn3 = QPushButton("Tug'ilgan sana")


def ism():
    label.setText("Ism: Ali")  

def familiya():
    label.setText("Familiya: Valiyev") 


def sana():
    label.setText("Tug'ilgan sana: 01.01.2005") 


btn1.clicked.connect(ism)
btn2.clicked.connect(familiya)
btn3.clicked.connect(sana)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(btn1)
layout.addWidget(btn2)
layout.addWidget(btn3)
oyna.setLayout(layout)

oyna.show()
sys.exit(app.exec_())
