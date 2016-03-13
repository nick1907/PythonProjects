import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from file_editor_adv import Ui_MainWindow

__author__ = 'brzydki'


class Main(QMainWindow):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Main()
	window.show()
	sys.exit(app.exec_())