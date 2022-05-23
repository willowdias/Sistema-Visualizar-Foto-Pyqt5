from ast import Try
from email.mime import image
import imp
from tampledespy.formcarregafoto import*
from PIL import Image

from PyQt5.QtWidgets import QDialog, QFileSystemModel, QLineEdit, QListWidget, QListWidgetItem, QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QWidget
from PyQt5.QtWidgets import QAction, QCheckBox,QDialog, QLabel, QLineEdit, QMainWindow, QMessageBox, QTableWidgetItem
from iconesform_rc import  *

class carregarfoto(QDialog):#essa tela puxa os quarto
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.bt_Confirma.clicked.connect(self.carregarimagem)

        self.ui.lineEdit.mouseDoubleClickEvent = self.escolhercaminho 
    def carregarimagem(self):
        try:
            self.carregar=self.ui.lineEdit.text()
            carregando=(f"{self.carregar}")
            img=Image.open(carregando)
            print(img)
            pixmap = QtGui.QPixmap(carregando) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.ui.label.width(), self.ui.label.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.ui.label.setPixmap(pixmap) # Set the pixmap onto the label
            self.ui.label.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center
        except:
            QMessageBox.information(self,"Alerta!","nao Foi Selecionado caminho")
    def escolhercaminho(self,event):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", ":/pytho willow/cardvenda/fotosclientes", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)") # Ask for file
            if fileName: # If the user gives a fileimagem, _ = QFileDialog.getOpenFileName(
               self.ui.lineEdit.setText(f"{fileName}")
        except:
            print("procura")      
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    #app.setQuitOnLastWindowClosed(False)#nao deixa a tela fechar por completo
    ui = carregarfoto()
 
    ui.show()
    sys.exit(app.exec_())