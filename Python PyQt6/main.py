from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap
app = QApplication([])  # step 1 - create application-object
window = QWidget()      # step 2 - create window
window.resize(200, 400)

lb_image = QLabel()
pixmapimage = QPixmap("profile_image.jpg")
pixmapimage = pixmapimage.scaled(200, 200)
lb_image.setPixmap(pixmapimage)

resume_lb = QLabel('Resume')
name_lb = QLabel('Name: Arslonbek')


skills_lb = QLabel('Skills')
lang_lb = QLabel('Python | PHP | SQL | JavaScript')


expr_lb = QLabel('Experience')
time_lb = QLabel('March 2022 - Today')

line1 = QVBoxLayout()
line1.addWidget(skills_lb)
line1.addWidget(lang_lb)
line1.addStretch(1)
line1.setSpacing(1)

line2 = QVBoxLayout()
line2.addWidget(expr_lb)
line2.addWidget(time_lb)
line2.addStretch(1)
line2.setSpacing(1)

main_line = QVBoxLayout()
main_line.addWidget(lb_image)
main_line.addWidget(resume_lb)
main_line.addWidget(name_lb)
main_line.addStretch(1)
main_line.setSpacing(60)
main_line.addLayout(line1)
main_line.addLayout(line2)


window.setLayout(main_line)

window.show()           # step 3 - show the window
app.exec()              # step 4 - run application




# from PyQt6.QtWidgets import *
# from random import *
# app = QApplication([])  # step 1 - create application-object
# window = QWidget()      # step 2 - create window
# window.resize(200, 400)
#
# greeting = QLabel()
# line = QVBoxLayout()
# btn = QPushButton("Click me!")
# line.addWidget(greeting)
# line.addWidget(btn)
# window.setLayout(line)
#
# def greet():
#     greeting.setText(str(randint(1, 100)))
#
# btn.clicked.connect(greet)
# window.show()
# app.exec()