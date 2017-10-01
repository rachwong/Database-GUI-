import sys
import mysql.connector
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

my_user = "rwon253"
my_password = "196ff4df"
my_host = "studdb-mysql.fos.auckland.ac.nz"
my_database = "stu_rwon253_COMPSCI_280_C_S2_2017"


def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.showMaximized()
    w.resize(400, 200)
    sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        enterLabel = QLabel("Enter title:")
        self.titleEdit = QLineEdit()
        self.enterButton = QPushButton("Enter")
        self.textbox = QTextEdit()
        self.enterButton.clicked.connect(self.showdata)

        title = "Harry Potter" 
        my_array = self.query(title)

        
        tablemodel = MyTableModel(my_array, self)
        tableview = QTableView()
        tableview.setModel(tablemodel)
        tableview.clicked.connect(self.viewClicked)
        tableview.setSelectionBehavior(QTableView.SelectRows)
        
        topLayout = QHBoxLayout()
        topLayout.addWidget(enterLabel)
        topLayout.addWidget(self.titleEdit)
        topLayout.addWidget(self.enterButton)
        topLayout.addWidget(self.textbox)
        topLayout.addWidget(tableview)
        #complete this
        
        layout = QGridLayout()
        layout.addLayout(topLayout, 0, 0)
        
        #complete this
    
        self.setLayout(layout)

    def viewClicked(self, clickedIndex):
        row=clickedIndex.row()
        model=clickedIndex.model()
        
    def showdata(self):
##        data = str(self.query(title))
##        print(data)
        self.textbox.setText("whatever")
    
    def query(self, name):
        conn = mysql.connector.connect(user=my_user, password=my_password,
                                      host=my_host, database=my_database)
        cursor = conn.cursor()
        sql = "SELECT BOOK_ID, title, author, ISBN, publisher, status FROM BOOKS WHERE title LIKE '%"
        #query = "Harry Potter"
        fullquery = sql + name + "%'"
        full_array = []
        try:
                cursor.execute(fullquery)
                rows = cursor.fetchall()
                #print(rows)
                for row in rows:
                        array = []
                        ID = row[0]
                        title = row[1]
                        author = row[2]
                        isbn = row[3]
                        publisher = row[4]
                        status = row[5]
                        #item = str(ID)+ ' ' + str(title) + ' ' + str(author)
                        #print( "%s, %s, %s, %s, %s, %s" % (ID, title, author, isbn, publisher,status))
                        array.append(str(ID))
                        array.append(str(title))
                        array.append(str(author))
                        full_array.append(array)
                        #return ID, title, author, isbn, publisher, status 
        except:
                print("Error: unable to fecth data")

        return full_array
        cursor.close()
        conn.close()

class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.header_labels = ['ID', 'Title', 'Author']

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)
    
    
if __name__ == "__main__":
    main()
