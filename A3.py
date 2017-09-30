import sys
import mysql.connector
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


my_user = ""
my_password = ""
my_host = ""
my_database = "stu_UPI_COMPSCI_280_C_S2_2017"

def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.showMaximized()
    w.resize(800, 500)
    sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        enterLabel = QLabel("Enter title:")
        
        self.titleEdit = QLineEdit()
        #complete this
        
        
        
        topLayout = QHBoxLayout()
        topLayout.addWidget(enterLabel)
        topLayout.addWidget(self.titleEdit)
        #complete this

	
        layout = QGridLayout()
        layout.addLayout(topLayout, 0, 0)
        #complete this
        
        
        
        self.setLayout(layout)
        
    def populateTable(self):
        print("populate table")
         #complete this
         
         
         
        
    def selectRow(self, index):        
        print("current row is %d", index.row())
         #complete this
         
         
         
         

class MyTableModel(QAbstractTableModel):
    header_labels = ["ID", "Title", "Author"]	

    def __init__(self, my_host, my_database, my_user, my_password, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        try:
            #complete this
            print("constructor")
            
            
            
            
        except Exception as inst:
            print(inst)
            print("Error: unable to fecth data from init")

    #popluate the table
    def populateTable(self, search_title):
        try:
            #complete this
            
            
            
            
            
            self.layoutChanged.emit() 
        except Exception as inst:
            print(inst)
            print("Error: unable to fecth data")

    #Returns bookd details
    def populateDetails(self, row_index):
        try:
            print("details")
             #complete this
            
            
            
            
            
        except Exception as inst:
            print(inst)
            print("Error: unable to fecth data")
            
    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return none                    #modify this             

    #Returns number of rows in table
    def rowCount(self, parent):
        return len(self.arraydata)
        
    #Returns number of columns in table
    def columnCount(self, parent):
        return len(self.arraydata[0])    

    #Returns the title of a particular column
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)
        
if __name__ == "__main__":
    main()