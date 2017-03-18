from PySide import QtWebKit
from PySide import QtCore
from PySide import QtGui
from design import main
import sys

class MIM(QtGui.QDialog, main.Ui_Dialog):
	def __init__(self):
		super(MIM, self).__init__()

		self._webKit = QtWebKit.QWebView()
		self.setupUi(self)
		self.config()


	def config(self):
		self._webKit.load(QtCore.QUrl('http://mimfoundation.or.id/santri/account/login'))
		self.verticalLayout_2.addWidget(self._webKit)
		self.connect(QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F1), self), QtCore.SIGNAL('activated()'), self._about)	
		self.connect(QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F5), self), QtCore.SIGNAL('activated()'), self._reload)


	def _reload(self):
		self._webKit.reload()

	def _about(self):
		QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://SufferProgrammer.github.io/'))

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	MIMFoundation = MIM()
	MIMFoundation.show()
	sys.exit(app.exec_())

