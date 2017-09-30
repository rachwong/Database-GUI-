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
        #complete this
        
        
        
        topLayout = QHBoxLayout()
        topLayout.addWidget(enterLabel)
        topLayout.addWidget(self.titleEdit)
        topLayout.addWidget(self.enterButton)
        topLayout.addWidget(self.textbox)
        #complete this
        
        layout = QGridLayout()
        layout.addLayout(topLayout, 0, 0)
        
        #complete this
    
        self.setLayout(layout)
    def showdata(self):
        data = str(self.query())
        print(data)
        self.textbox.setText(data)
        
    def query(self):
        conn = mysql.connector.connect(user=my_user, password=my_password,
                                      host=my_host, database=my_database)
        cursor = conn.cursor()
        sql = "SELECT BOOK_ID, title, author, ISBN, publisher, status FROM BOOKS" 
        query = " WHERE title LIKE 'Java for Dummies'"
        fullquery = sql + query
        try:
                cursor.execute(fullquery)
                rows = cursor.fetchall()
                #print(rows)
                for row in rows:
                        ID = str(row[0])
                        title = str(row[1])
                        author = row[2]
                        isbn = row[3]
                        publisher = row[4]
                        status = row[5]
                        #print( "%s, %s, %s, %s, %s, %s" % (ID, title, author, isbn, publisher,status))
                        return ID, title, author, isbn, publisher, status
                        #stringdata = ID + title
                        
                        
        except:
                print("Error: unable to fecth data")

        cursor.close()
        conn.close()
if __name__ == "__main__":
    main()
