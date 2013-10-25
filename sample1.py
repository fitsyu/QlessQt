from QlessQtGui import *

class myWidget(Widget):
	
	def __init__(self):
		super(myWidget, self).__init__()
		self.button1 = PushButton('Click me!')
		self.btExit = PushButton('exit')
		self.btExit.clicked.connect(self.close)
		self.label1 = Label('hello to QT without Q program!\n enjoy!')
		self.te = TextEdit('example ')
		self.le = LineEdit('example' )
		
		self.layout1 = HBoxLayout()
		self.layout1.addWidget(self.label1)
		self.layout1.addWidget(self.te)
		self.layout1.addWidget(self.btExit)
		
		self.layout2 = VBoxLayout()
		self.layout2.addWidget(self.button1)
		self.layout2.addWidget(self.le)
		
		self.gl = GridLayout()
		self.gl.addLayout(self.layout1,1,1)
		self.gl.addLayout(self.layout2,2,1)
		
		
		self.setLayout(self.gl)
		self.show()
		
if __name__ == '__main__':
	a1 = Application([])
	w = myWidget()
	a1.exec_()