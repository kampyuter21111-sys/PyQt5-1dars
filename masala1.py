import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

oyna = QWidget()
oyna.setWindowTitle("1-masala")
oyna.resize(300, 150)

label = QLabel("Son: ?")
tugma = QPushButton("Random son")


def random_son():
    label.setText("Son: " + str(random.randint(1, 100)))


tugma.clicked.connect(random_son)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(tugma)
oyna.setLayout(layout)

oyna.show()
sys.exit(app.exec_())
