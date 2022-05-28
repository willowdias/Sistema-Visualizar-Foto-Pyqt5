from ast import Try
from email.mime import image
import imp
from tampledespy.formcarregafoto import*
from tampledespy.qrcode import*
from PIL import Image
import qrcode  
from PyQt5.QtWidgets import QDialog, QFileSystemModel, QLineEdit, QListWidget, QListWidgetItem, QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QWidget
from PyQt5.QtWidgets import QAction, QCheckBox,QDialog, QLabel, QLineEdit, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt 
import sys 
from iconesform_rc import  *
import time
import datetime
import json
class carregarfoto(QDialog):#essa tela puxa os quarto
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.FramelessWindowHint )
        self.ui.bt_close.clicked.connect(self.close)
        self.ui.bt_Visualisar.clicked.connect(self.carregarimagem)
        #label click dois click mostra arquivo sobre sistema
        self.ui.labe_icon_sobre.mouseDoubleClickEvent= self.sobre
        self.ui.frame_qmenu2.mouseDoubleClickEvent=self.maxminize
        self.ui.lineEdit.mouseDoubleClickEvent = self.escolhercaminho 
        self.ui.label.mouseDoubleClickEvent=self.escolhercaminho
        #tree viwer ver pasta aonde estao fotos
        self.model = QFileSystemModel()
        self.model.setRootPath('D:/')
        self.ui.pasta.setModel(self.model)
        self.ui.pasta.doubleClicked.connect(self.selecionarfoto)
        #botao ver frame pasta
        self.ui.actionMenu_Arquivo.triggered.connect(self.visualisarframepasta)
        #botao show
        self.ui.bt_maxmize.clicked.connect(self.maxminize)
        #salvar button
        self.ui.actionSalva.triggered.connect(self.salvar)
        self.ui.actionSave_Pdf.triggered.connect(self.salvar_como_pdf)
        self.ui.button_png.clicked.connect(self.formato_image)
        self.ui.button_jpg.clicked.connect(self.formato_image)
        self.ui.button_jpeg.clicked.connect(self.formato_image)
        self.ui.button_icon.clicked.connect(self.formato_image)
        self.ui.button_bmp.clicked.connect(self.formato_image)
        self.showMaximized()
        #BOTOES DE FORMATO IMAGEM
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
        menu.addAction(self.ui.actionSave_Pdf)
        menu.addSeparator()
        menu.addAction(self.ui.actionMenu_Arquivo)
        self.ui.botao_menu.setMenu(menu)
        #adicionar modo quadro label
        
        self.ui.label.setFrameStyle(QtWidgets.QFrame.Panel )
        self.ui.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ui.label.setLineWidth(14)
        self.ui.lineEdit_TxtDataAtual.setText(self.date_now())
        #abrir arquivo json
        data_file_dict = self.open_file_json('data.json','r')
        lista=[data_file_dict.get('user'),data_file_dict.get('profile_type'),data_file_dict.get('notification'),data_file_dict.get('receita_value')]
        count=0
        for line in lista:
            count += 1
            print("Line{}: {}".format(count, line.strip()))    
        self.ui.label_TxtTopDataUser.setText(str(lista[0]))
        self.ui.label_TxtTopDataUserType.setText(str(lista[1]))
        #essa opcao cria usario que logo 
        self.quantidade_leitura()
        
        #essa funçao chama Tempo pra atualizar quantos clientes connect
        self.timer = QTimer(self) 
        self.timer.timeout.connect(self.run)
        self.timer.start(1000)

    def open_file_json(self, file_name_str, mode):
        try:
            data_file = open(
                file_name_str,
                mode=mode,
                encoding='utf-8',
                errors='ignore')
            data_file = json.load(data_file)
        except IOError as e:
            return str(e)
        else:
            return data_file
    def quantidade_leitura(self):
        data_file_dict = self.open_file_json('data.json','r')
        lista=[data_file_dict.get('user'),data_file_dict.get('profile_type'),data_file_dict.get('notification'),data_file_dict.get('receita_value')]
            
        self.bufersize = 64 * 1024
        self.arquivo = open('db_banco/tabelasomar/quantidadevez.txt', 'a')
        self.arquivo.write(f'Usuario {str(lista[0]) }'+ f' profile_type { str(lista[1])}'+ f' Data acesso {str({self.date_now()})}')
        self.arquivo.write("\n")
        self.arquivo.close()
    def run(self):#reflesh
               
        self.ui.resulta_usuario.setText(str(self.valordeconneccao()))
    def valordeconneccao(self):
        arquivo = open('db_banco/tabelasomar/quantidadevez.txt', "r")
        conteudo = arquivo.readlines()
        arquivo.close()
        soma=0
        for linha in conteudo:
            soma += 1
                
        return soma
    def date_now(self):#colocar horas no line
        now = datetime.datetime.now()
        return str(now.strftime("%A %d/%m/%Y")).capitalize()
    def sobre(self,event):
        QMessageBox.about(self,"Sistema Open ",
        "Me chamo Willow Estou criando Sistema Pra ajuda\n"
        "Deseja Saber Mais Entre Contao\n"
        "(69)9-9927024-08")
    def maxminize(self,pressed):
        source = self.sender()
        if pressed:
           self.showNormal()
        else:
            self.showMaximized()
            

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
    def selecionarfoto(self,index):#carrega ao selecionar pela pasta ao lado esquerdo treeviw
        
        self.ui.lineEdit.setText(str(self.model.filePath(index)))
        self.carregarimagem()
    def carregarimagem(self):#carrega imagem na label
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
               self.carregarimagem()
        except:
            print("procura") 
    def formato_image(self):
        if self.ui.button_png.isChecked():
            self.checkbutton('PNG')
        if self.ui.button_jpg.isChecked():
            self.checkbutton('JPG')
        if self.ui.button_icon.isChecked():
            self.checkbutton('ICO')   
        if self.ui.button_jpeg.isChecked():
            self.checkbutton('JPEG')  
        if self.ui.button_bmp.isChecked():
            self.checkbutton('BMP')
        
    def checkbutton(self,text):
        print(text)
        self.formato=text
    def salvar(self):
        
        try:
            
            
            self.nova_imagem = self.pixmap.scaled(self.ui.label.width(), self.ui.label.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            imagem, _ = QFileDialog.getSaveFileName(
                    self.ui.label,
                    'Salvar imagem',f'logo.{str(self.formato)}',
                        r"Z:/pytho willow/Sistema Recibo/logo",
                        options=QFileDialog.DontUseNativeDialog
                    )
            self.nova_imagem.save(imagem, f'{str(self.formato)}')
            self.salva_como_qr_code(imagem)
            QMessageBox.about(self,"Save!","Imagem Salva")
        except:
            QMessageBox.about(self,"Alerta!","Nao A Foto Pra Salva\n"
            "Ou Formato nao selecionado")
    def salvar_como_pdf(self):
        try:
            self.photo=self.ui.lineEdit.text()
            image_1 = Image.open(f'{self.photo}')
            im_1 = image_1.convert('RGB')
            im_1.save(r'fotosclientes/imagens.pdf')
            QMessageBox.about(self,"Save!","Salvo Pasta C:\Photo Edit/fotosclientes/imagens.pdf")
        except:
            QMessageBox.about(self,"Alerta!","Nao A Foto Pra Salva Pdf")
    def salva_como_qr_code(self,text):
        Logo_link = f'{text}'
  
        logo = Image.open(Logo_link)
        
        # taking base width
        basewidth = 100
        
        # adjust image size
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
        QRcode = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )
        
        # taking url or text
        url = f'{text}'
        
        # addingg URL or text to QRcode
        QRcode.add_data(url)
        
        # generating QR code
        QRcode.make()
        
        # taking color name from user
        QRcolor = 'Red'
        
        # adding color to QR code
        QRimg = QRcode.make_image(
            fill_color=QRcolor, back_color="white").convert('RGB')
        
        # set size of QR code
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
            (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
        
        # save the QR code generated
        QRimg.save(f"fotosclientes/qrcode.png")
        
        QMessageBox.about(self,'Pix','QR code generated!')
        self.tela=qr_code()
        self.tela.exec_()
class qr_code(QDialog):#essa tela puxa os quarto
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_qr_code()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Drawer)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.abri_foto()
    def abri_foto(self):
        carregando=(f"fotosclientes/qrcode.png")
        pixmap = QtGui.QPixmap(carregando) # Setup pixmap with the provided image       
    
        self.ui.label.setPixmap(pixmap) # Set the pixmap onto the label
        self.ui.label.setScaledContents(True)
        self.ui.label.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    #app.setQuitOnLastWindowClosed(False)#nao deixa a tela fechar por completo
    ui = carregarfoto()
 
    ui.show()
    sys.exit(app.exec_())