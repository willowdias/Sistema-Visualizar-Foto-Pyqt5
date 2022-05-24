from ast import Try
from email.mime import image
import imp
from tampledespy.formcarregafoto import*
from PIL import Image

from PyQt5.QtWidgets import QDialog, QFileSystemModel, QLineEdit, QListWidget, QListWidgetItem, QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QWidget
from PyQt5.QtWidgets import QAction, QCheckBox,QDialog, QLabel, QLineEdit, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt 
import sys 
from iconesform_rc import  *
import time
class carregarfoto(QDialog):#essa tela puxa os quarto
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.FramelessWindowHint )
        self.ui.bt_Visualisar.clicked.connect(self.carregarimagem)
        #label click dois click mostra arquivo sobre sistema
        self.ui.labe_icon_sobre.mouseDoubleClickEvent= self.sobre
        self.ui.lineEdit.mouseDoubleClickEvent = self.escolhercaminho 
        #tree viwer ver pasta aonde estao fotos
        self.model = QFileSystemModel()
       
        self.model.setRootPath('D:/')
        self.ui.pasta.setModel(self.model)
        self.ui.pasta.doubleClicked.connect(self.selecionarfoto)
        #botao ver frame pasta
        self.ui.bt_visular_pasta.clicked.connect(self.visualisarframepasta)
        #botao show
        self.ui.bt_maxmize.clicked.connect(self.maxminize)
        #salvar button
        self.ui.bt_salvar_foto.clicked.connect(self.salvar)
        #create menu 
        menu = QMenu()
        menu.setStyleSheet("QMenu{background-color: rgb(97, 97, 97); text-align: center;font: 14pt MS Shell Dlg 2;}"
        "QMenu::item {padding: 2px 25px 2px 20px;border: 1px solid transparent; /* reserve space for selection border */}"
        "QMenu::item:selected {border-color: darkblue;background: rgba(100, 100, 100, 150)}")
       
        menu.setMinimumWidth(150)
        menu.setMinimumHeight(250)
        menu.addAction(self.ui.actionNovo)
        menu.addSeparator()
        menu.addAction(self.ui.actionSalva)
        menu.addSeparator()
        self.ui.botao_menu.setMenu(menu)
    def sobre(self,event):
        QMessageBox.about(self,"Sistema Open ",
        "Me chamo Willow Estou criando Sistema Pra ajuda\n"
        "Deseja Saber Mais Entre Contao\n"
        "(69)9-9927024-08")
    def maxminize(self,pressed):
        source = self.sender()
        if pressed:
            self.showMaximized()
        else:
            self.showNormal()

    def visualisarframepasta(self,pressed):
        source = self.sender()
        if pressed:
            self.animation = QtCore.QPropertyAnimation(self.ui.frame_pastas, b"minimumWidth")
            self.animation.setEndValue(500)
            self.animation.setDuration(600)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InBack)
            self.animation.start()
        else:
            self.animation = QtCore.QPropertyAnimation(self.ui.frame_pastas, b"minimumWidth")
            self.animation.setEndValue(0)
            self.animation.setDuration(600)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InBack)
            self.animation.start()
    def selecionarfoto(self,index):
        
        self.ui.lineEdit.setText(str(self.model.filePath(index)))
    def carregarimagem(self):
        try:
            self.carregar=self.ui.lineEdit.text()
            carregando=(f"{self.carregar}")
            tamanho=self.ui.line_with.text()
            largura=self.ui.line_heigt.text()
            while self.carregar==""  :
                if self.carregar=="":
                    self.ui.lineEdit.setStyleSheet("background-color: rgb(255, 255, 0);")
                    QMessageBox.about(self,"Alerta!","Imagem nao selecionada")
                    self.repaint()
                    time.sleep(1)
                    self.ui.lineEdit.setStyleSheet("background-color: white;")
                    break
            if tamanho=="" or largura=="":
                self.ui.line_heigt.setText("700") 
                self.ui.line_with.setText("1080")     
            else:
                pixmap = QtGui.QPixmap(carregando) # Setup pixmap with the provided image
                
                self.pixmap = pixmap.scaled(int(tamanho), int(largura), QtCore.Qt.KeepAspectRatio)
                self.ui.label.setPixmap( self.pixmap) # Set the pixmap onto the label
                self.ui.label.setScaledContents(True)
                self.ui.label.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center
                #self.ui.label.setStyleSheet(f"background-image: url({self.carregar});background-repeat: no-repeat;background-position: 50% 50%;background-position: center top; height: 120px;with:50px") # Set the pixmap onto the label
                
        except:
            QMessageBox.about(self,"Alerta!","Nao Foi Selecionado caminho")
            
            
           
    def escolhercaminho(self,event):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", ":/pytho willow/cardvenda/fotosclientes", "Image Files (*.png *.jpg *jpeg *.bmp);;All Files (*)") # Ask for file
            if fileName: # If the user gives a fileimagem, _ = QFileDialog.getOpenFileName(
               self.ui.lineEdit.setText(f"{fileName}")
        except:
            print("procura") 
    def salvar(self):#imagens
        largura=self.ui.line_heigt.text()
        self.nova_imagem = self.pixmap.scaledToWidth(int(largura))
        imagem, _ = QFileDialog.getSaveFileName(
                self.ui.label,
                'Salvar imagem','logo.png',
                    r"Z:/pytho willow/Sistema Recibo/logo",
                    options=QFileDialog.DontUseNativeDialog
                )
        self.nova_imagem.save(imagem, 'PNG')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    #app.setQuitOnLastWindowClosed(False)#nao deixa a tela fechar por completo
    ui = carregarfoto()
 
    ui.show()
    sys.exit(app.exec_())