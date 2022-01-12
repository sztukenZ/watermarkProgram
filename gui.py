from PySide6.QtWidgets import (
    QApplication, QMessageBox, QWidget, QLabel, QPushButton, QVBoxLayout
)

app = QApplication([])
app.setStyle('macos')
window = QWidget()
window.setWindowTitle('Watermarking Images')
window.setGeometry(100, 100, 280, 80)
window.move(600, 200)
window.setStyleSheet("background-color: white;")
v_layout = QVBoxLayout()

btn1 = QPushButton('button 1')
btn2 = QPushButton('button 2')

v_layout.addWidget(QLabel('hello world'))
v_layout.addWidget(btn1)
v_layout.addWidget(btn2)


def on_btn1_clicked():
    alert = QMessageBox()
    alert.setText('this is an alert msg')
    alert.exec()


btn1.clicked.connect(on_btn1_clicked)

window.setLayout(v_layout)
window.show()
app.exec()
