from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
import sys

class Window(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(Window_for_Sydorenko,self).__init__()
        self.initUI()

    def initUI(self, parent = None):
        self.setWindowTitle('My Window')
        self.resize(750, 650)
        self.move(500, 500)
        self.id = 0
        self.createDesk()
        self.createTable()
        self.button_add.resize(self.button_add.sizeHint())
        self.button_add.setFixedWidth(70)
        self.button_add.clicked.connect(start.on_clicked)
        self.button_del = QtWidgets.QPushButton("Delete All")
        self.button_del.resize(self.button_del.sizeHint())
        self.button_del.move(70, 20)
        self.button_del.clicked.connect(delet.on_deleted)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.button_add)
        self.layout.addWidget(self.t,QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.button_del)
        self.setLayout(self.layout) 
        self.show()

    def createDesk(self, parent = None):
        self.desk = QtWidgets.QFrame()
        self.desk.setFrameShape(QtWidgets.QFrame.StyledPanel)

    def createTable(self, parent = None):
        self.t = QtWidgets.QTableWidget()
        self.t.setColumnCount(4)
        self.t.setRowCount(3)
        self.t.move(150,150)
        self.t.setHorizontalHeaderLabels(["Lastname","Name","Patronumic","Class"])
        self.t.doubleclicked.connect(self.on_click_inf)

    def createGhostTable(self, parent = None):
        self.g = QtWidgets.QTableWidget()
        self.g.setColumnCount(6)
        self.g.setRowCount(8)
        self.g.move(150,150)
        self.g.doubleClicked.connect(self.on_click_inf)

    @pyqtSlot()
    def on_click_inf(self):
        wizardInf = MyWizardInf(ex) 
        wizardInf.setOption(QtWidgets.QWizard.NoDefaultButton, True)
        wizardInf.show()
 
class MyPage1(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setTitle("Main information of student")
        self.label1 = QtWidgets.QLabel("Lustname")
        self.line1 = QtWidgets.QLineEdit()
        self.box1 = QtWidgets.QVBoxLayout()
        self.box1.addWidget(self.label1)
        self.box1.addWidget(self.line1)
        self.setLayout(self.box1)
        self.registerField("line1*", self.line1)
  
class MyPage2(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setTitle("Other information of student")
        self.label4 = QtWidgets.QLabel("Class")
        self.line4 = QtWidgets.QLineEdit()
        self.box2 = QtWidgets.QVBoxLayout()
        self.box2.addWidget(self.label4)
        self.box2.addWidget(self.line4)
        self.setLayout(self.box2)
        self.registerField("line4*", self.line4)


class MyPage3(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.infTable = QtWidgets.QTableWidget()
        self.infTable.setColumnCount(1)
        self.infTable.setRowCount(6)
        self.infTable.move(150,150)
        self.box3 = QtWidgets.QVBoxLayout()
        self.box3.addWidget(self.infTable)
        self.setLayout(self.box3)

class StudentModel():
    def __init__(self):
        self.lustname = None 
        self.name = None
        self.patronumic = None
        self.clas = None
              
    

  
class MyWizardAdd(QtWidgets.QWizard):
    def __init__(self, parent=None):
        QtWidgets.QWizard.__init__(self, parent)
        self.setWindowTitle("Add student")
        self.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        #self.studentModel = StudentModel()
        self.page1 = MyPage1(self)
        self.page2 = MyPage2(self)
        self.idPage1 = self.addPage(self.page1)

    def setTable(self, table):
        self.table = table

    def accept(self):
        self.table.addData(self.studentModel)
        self.close()



class MyWizardInf(QtWidgets.QWizard):
    def __init__(self, parent=None):
        QtWidgets.QWizard.__init__(self, parent)
        self.setWindowTitle("Information about student")
        self.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        self.setOption(self.NoBackButtonOnStartPage)
        self.page3 = MyPage3(self)
        self.idPage3 = self.addPage(self.page3)
  
class Start():
    @staticmethod
    def on_clicked():
        wizard = MyWizardAdd(ex)
        result = wizard.exec_()
        if result == QtWidgets.QDialog.Accepted:          
            ex.t.setItem(ex.id,0, QtWidgets.QTableWidgetItem(wizard.field("line1")))
            ex.g.setItem(ex.id,0, QtWidgets.QTableWidgetItem(wizard.field("line1")))
            ex.g.setItem(ex.id,3, QtWidgets.QTableWidgetItem(wizard.field("line4")))
            ex.id += 1
        else:
            print("Touch Cancel, touch exit or button <Esc>",
                  result)
class Del():
    @staticmethod
    def on_deleted():   
        ex.t.clearContents()
        ex.g.clearContents()
        ex.t.removeRow(ex.id)
        ex.g.removeRow(ex.id)
        while ex.id > 0:
            ex.id -= 1
            ex.t.removeRow(ex.id)
            ex.g.removeRow(ex.id)
            
  

start = Start()
delet = Del()
app = QtWidgets.QApplication(sys.argv)
ex = Window_for_Sydorenko()
sys.exit(app.exec_())
