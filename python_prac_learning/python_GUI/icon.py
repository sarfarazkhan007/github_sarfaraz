import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300,300,300,250)
		self.setWindowTitle('Khan007')
		self.setWindowIcon(QIcon('web.png'))
		button=QPushButton('sarfaraz press here',self)
		button.move(100,70)
		button.clicked.connect(self.on_click)

		self.show()

	def on_click(self):
		print('click once more')

if __name__ == '__main__':
	app =QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())