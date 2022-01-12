from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication, QMessageBox, QWidget, QLabel, QPushButton, QGridLayout
)

app = QApplication([])
app.setStyle('macos')
window = QWidget()
window.setWindowTitle('Watermarking Images')
window.setGeometry(100, 100, 280, 80)
window.move(600, 200)
window.setStyleSheet("background-color: white;")
layout = QGridLayout()

btn1 = QPushButton('Back')
btn2 = QPushButton('Choose Images')
btn3 = QPushButton('Clear Images')
btn4 = QPushButton('Next Step')

img_label = QLabel()
pixmap = QPixmap('example_picture.jpeg')
img_label.setPixmap(pixmap)

# Optional, resize window to image size
img_label.resize(pixmap.width(),pixmap.height())

layout.addWidget(btn1, 0, 0)
layout.addWidget(btn2, 0, 1)
layout.addWidget(btn3, 0, 2)
layout.addWidget(btn4, 0, 3)
layout.addWidget(img_label, 1, 1, 1, 2)


def on_btn1_clicked():
    alert = QMessageBox()
    alert.setText('this is an alert msg')
    alert.exec()


btn1.clicked.connect(on_btn1_clicked)

window.setLayout(layout)
window.show()
app.exec()
