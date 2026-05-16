#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
    QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout)

#buatjendela
APP = QApplication([])
JENDELA = QWidget()
JENDELA.setWindowTitle("APLIKASI QUIZ")
JENDELA.setFixedSize(400, 400)

#menambahkanwidget
pertanyaan = QLabel('ini untuk pertanyaan')
tombol = QPushButton('Jawab')
radio1 = QRadioButton('pilihan 1')
radio2 = QRadioButton('pilihan 2')
radio3 = QRadioButton('pilihan 3')
radio4 = QRadioButton('pilihan 4')
radioGrup = QGroupBox('pilihan jawaban')

#tambahkan widget unutk grup jawaban
hasil = QLabel('BENAR/SALAH')
jawaban = QLabel('INi jawabannya')
jawabanGrup = QGroupBox('Hasilnya adalah')

#menambahkan layout
v1Grup = QVBoxLayout()
v1Grup.addWidget(radio1)
v1Grup.addWidget(radio2)
v2Grup = QVBoxLayout()
v2Grup.addWidget(radio3)
v2Grup.addWidget(radio4)
hGrup = QHBoxLayout()
hGrup.addLayout(v1Grup)
hGrup.addLayout(v2Grup)
radioGrup.setLayout(hGrup)
#menambahkan layout unutk grup jawaban
VGrupJawaban = QVBoxLayout()
VGrupJawaban.addWidget(hasil)
VGrupJawaban.addWidget(jawaban)
jawabanGrup.setLayout(VGrupJawaban)

#menambahkan layout untuk tampilan utama
V_utama = QVBoxLayout()
V_utama.addWidget(pertanyaan)
V_utama.addWidget(radioGrup)
V_utama.addWidget(jawabanGrup)
V_utama.addWidget(tombol)
JENDELA.setLayout(V_utama)

#munculkan jendela dan jalankan
JENDELA.show()
APP.exec_()

