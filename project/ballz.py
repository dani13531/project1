from pyrogram import Client
from pyrogram.errors import RPCError
import asyncio
import os
from PyQt5 import QtCore, QtGui, QtWidgets

api_id = 25413486
api_hash = '35ec3fd3165e77412d6edc8223c78052'
class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(743, 476)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(sizePolicy)
        window.setMaximumSize(QtCore.QSize(743, 476))
        window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 751, 481))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabs.setFont(font)
        self.tabs.setAccessibleDescription("")
        self.tabs.setStyleSheet("")
        self.tabs.setObjectName("tabs")
        self.VKtab = QtWidgets.QWidget()
        self.VKtab.setObjectName("VKtab")
        self.VK_ID = QtWidgets.QLineEdit(self.VKtab)
        self.VK_ID.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.VK_ID.setText("")
        self.VK_ID.setObjectName("VK_ID")
        self.VKlabel = QtWidgets.QLabel(self.VKtab)
        self.VKlabel.setGeometry(QtCore.QRect(10, 0, 71, 16))
        self.VKlabel.setObjectName("VKlabel")
        self.VK_IDbtn = QtWidgets.QPushButton(self.VKtab)
        self.VK_IDbtn.setGeometry(QtCore.QRect(170, 20, 91, 21))
        self.VK_IDbtn.setObjectName("VK_IDbtn")
        self.VKoutput = QtWidgets.QPlainTextEdit(self.VKtab)
        self.VKoutput.setGeometry(QtCore.QRect(10, 50, 721, 391))
        self.VKoutput.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.VKoutput.setObjectName("VKoutput")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Users/danii/OneDrive/Рабочий стол/VKLogo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs.addTab(self.VKtab, icon1, "")
        self.TGtab = QtWidgets.QWidget()
        self.TGtab.setObjectName("TGtab")
        self.Tglb = QtWidgets.QLabel(self.TGtab)
        self.Tglb.setGeometry(QtCore.QRect(599, 0, 121, 20))
        self.Tglb.setObjectName("Tglb")
        self.codelabel = QtWidgets.QLabel(self.TGtab)
        self.codelabel.setGeometry(QtCore.QRect(590, 80, 141, 31))
        self.codelabel.setObjectName("codelabel")
        self.TGNumbinp = QtWidgets.QLineEdit(self.TGtab)
        self.TGNumbinp.setGeometry(QtCore.QRect(590, 20, 141, 22))
        self.TGNumbinp.setObjectName("TGNumbinp")
        self.TGcodeinp = QtWidgets.QLineEdit(self.TGtab)
        self.TGcodeinp.setGeometry(QtCore.QRect(590, 120, 141, 22))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(False)
        self.TGcodeinp.setFont(font)
        self.TGcodeinp.setObjectName("TGcodeinp")
        self.TGcodebtn = QtWidgets.QPushButton(self.TGtab)
        self.TGcodebtn.setGeometry(QtCore.QRect(590, 150, 141, 31))
        self.TGcodebtn.setObjectName("TGcodebtn")
        self.TGAccexitbtn = QtWidgets.QPushButton(self.TGtab)
        self.TGAccexitbtn.setGeometry(QtCore.QRect(590, 190, 141, 31))
        self.TGAccexitbtn.setObjectName("TGAccexitbtn")
        self.TGNumpbtn = QtWidgets.QPushButton(self.TGtab)
        self.TGNumpbtn.setGeometry(QtCore.QRect(590, 50, 141, 28))
        self.TGNumpbtn.setObjectName("TGNumpbtn")
        self.tabWidget = QtWidgets.QTabWidget(self.TGtab)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 581, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.showmsgtab = QtWidgets.QWidget()
        self.showmsgtab.setObjectName("showmsgtab")
        self.IDChannelinput = QtWidgets.QLineEdit(self.showmsgtab)
        self.IDChannelinput.setGeometry(QtCore.QRect(130, 10, 111, 21))
        self.IDChannelinput.setObjectName("IDChannelinput")
        self.IDChannellabel = QtWidgets.QLabel(self.showmsgtab)
        self.IDChannellabel.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.IDChannellabel.setObjectName("IDChannellabel")
        self.IDChannelbtn = QtWidgets.QPushButton(self.showmsgtab)
        self.IDChannelbtn.setGeometry(QtCore.QRect(250, 10, 111, 21))
        self.IDChannelbtn.setObjectName("IDChannelbtn")
        self.Tgoutput = QtWidgets.QPlainTextEdit(self.showmsgtab)
        self.Tgoutput.setGeometry(QtCore.QRect(10, 40, 561, 371))
        self.Tgoutput.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Tgoutput.setObjectName("Tgoutput")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Users/danii/OneDrive/Рабочий стол/685887 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.showmsgtab, icon2, "")
        self.searchmsgtab = QtWidgets.QWidget()
        self.searchmsgtab.setObjectName("searchmsgtab")
        self.TGIDChannelsearchinp = QtWidgets.QLineEdit(self.searchmsgtab)
        self.TGIDChannelsearchinp.setGeometry(QtCore.QRect(160, 10, 111, 21))
        self.TGIDChannelsearchinp.setObjectName("TGIDChannelsearchinp")
        self.Searchlabelid = QtWidgets.QLabel(self.searchmsgtab)
        self.Searchlabelid.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.Searchlabelid.setObjectName("Searchlabelid")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.searchmsgtab)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 40, 111, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Phraselabel = QtWidgets.QLabel(self.searchmsgtab)
        self.Phraselabel.setGeometry(QtCore.QRect(10, 40, 141, 20))
        self.Phraselabel.setObjectName("Phraselabel")
        self.SenderidLabel = QtWidgets.QLabel(self.searchmsgtab)
        self.SenderidLabel.setGeometry(QtCore.QRect(10, 70, 151, 20))
        self.SenderidLabel.setObjectName("SenderidLabel")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.searchmsgtab)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 70, 111, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.TGsearchinput = QtWidgets.QPushButton(self.searchmsgtab)
        self.TGsearchinput.setGeometry(QtCore.QRect(280, 70, 111, 21))
        self.TGsearchinput.setObjectName("TGsearchinput")
        self.TGoutputsearch = QtWidgets.QPlainTextEdit(self.searchmsgtab)
        self.TGoutputsearch.setGeometry(QtCore.QRect(10, 100, 561, 311))
        self.TGoutputsearch.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.TGoutputsearch.setObjectName("TGoutputsearch")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Users/danii/OneDrive/Рабочий стол/9349901.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.searchmsgtab, icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Users/danii/OneDrive/Рабочий стол/TGLogo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs.addTab(self.TGtab, icon4, "")
        self.PRtab = QtWidgets.QWidget()
        self.PRtab.setObjectName("PRtab")
        self.numbLab = QtWidgets.QLabel(self.PRtab)
        self.numbLab.setGeometry(QtCore.QRect(10, 0, 171, 16))
        self.numbLab.setObjectName("numbLab")
        self.PRlatinp = QtWidgets.QLineEdit(self.PRtab)
        self.PRlatinp.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.PRlatinp.setObjectName("PRlatinp")
        self.PRlatlongbtn = QtWidgets.QPushButton(self.PRtab)
        self.PRlatlongbtn.setGeometry(QtCore.QRect(330, 20, 91, 21))
        self.PRlatlongbtn.setObjectName("PRlatlongbtn")
        self.PRlonginp = QtWidgets.QLineEdit(self.PRtab)
        self.PRlonginp.setGeometry(QtCore.QRect(170, 20, 151, 21))
        self.PRlonginp.setObjectName("PRlonginp")
        self.PRoutput = QtWidgets.QPlainTextEdit(self.PRtab)
        self.PRoutput.setGeometry(QtCore.QRect(10, 50, 721, 391))
        self.PRoutput.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.PRoutput.setObjectName("PRoutput")
        self.label = QtWidgets.QLabel(self.PRtab)
        self.label.setGeometry(QtCore.QRect(430, 0, 131, 16))
        self.label.setObjectName("label")
        self.PRradiusinput = QtWidgets.QLineEdit(self.PRtab)
        self.PRradiusinput.setGeometry(QtCore.QRect(430, 20, 113, 22))
        self.PRradiusinput.setObjectName("PRradiusinput")
        self.PRradiusbtn = QtWidgets.QPushButton(self.PRtab)
        self.PRradiusbtn.setGeometry(QtCore.QRect(550, 20, 93, 21))
        self.PRradiusbtn.setObjectName("PRradiusbtn")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Users/danii/OneDrive/Рабочий стол/PRLogo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs.addTab(self.PRtab, icon5, "")
        window.setCentralWidget(self.centralwidget)
        self.tgfunctions()

        self.retranslateUi(window)
        self.tabs.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window)
        window.setTabOrder(self.VK_ID, self.TGNumbinp)
        window.setTabOrder(self.TGNumbinp, self.TGcodebtn)
        window.setTabOrder(self.TGcodebtn, self.PRlatinp)
        window.setTabOrder(self.PRlatinp, self.PRlatlongbtn)
        window.setTabOrder(self.PRlatlongbtn, self.VK_IDbtn)
        window.setTabOrder(self.VK_IDbtn, self.tabs)
        window.setTabOrder(self.tabs, self.TGcodeinp)
        window.setTabOrder(self.TGcodeinp, self.TGAccexitbtn)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Парсик"))
        self.VKlabel.setText(_translate("window", "Введите ID:"))
        self.VK_IDbtn.setText(_translate("window", "Ввод"))
        self.tabs.setTabText(self.tabs.indexOf(self.VKtab), _translate("window", "VK"))
        self.Tglb.setText(_translate("window", "Введите ваш номер:"))
        self.codelabel.setText(_translate("window", "Введите полученный \n"
"код:"))
        self.TGcodebtn.setText(_translate("window", "Ввод"))
        self.TGAccexitbtn.setText(_translate("window", "Выйти из аккаунта"))
        self.TGNumpbtn.setText(_translate("window", "Ввод"))
        self.IDChannellabel.setText(_translate("window", "Введите ID канала:"))
        self.IDChannelbtn.setText(_translate("window", "Ввод"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.showmsgtab), _translate("window", "Сообщения"))
        self.Searchlabelid.setText(_translate("window", "Введите ID канала:"))
        self.Phraselabel.setText(_translate("window", "Введите фразу поиска:"))
        self.SenderidLabel.setText(_translate("window", "Введите ID отправителя:"))
        self.TGsearchinput.setText(_translate("window", "Ввод"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchmsgtab), _translate("window", "Поиск"))
        self.tabs.setTabText(self.tabs.indexOf(self.TGtab), _translate("window", "Telegram"))
        self.numbLab.setText(_translate("window", "Введите координаты:"))
        self.PRlatlongbtn.setText(_translate("window", "Ввод"))
        self.label.setText(_translate("window", "Введите радиус (км):"))
        self.PRradiusbtn.setText(_translate("window", "Ввод"))
        self.tabs.setTabText(self.tabs.indexOf(self.PRtab), _translate("window", "Почта России"))
        return(self)
    def tgfunctions(self):
        self.TGNumpbtn.clicked.connect(self.f1)
        self.TGcodebtn.clicked.connect(self.TGauth)
        self.TGAccexitbtn.clicked.connect(self.accdel)
        self.IDChannelbtn.clicked.connect(self.TGmsg)
        self.TGsearchinput.clicked.connect(self.searchmsg)

    def f1(self):

        
        self.phone = self.TGNumbinp.text()

        if self.TGNumbinp.text() == "":

            self.Tgoutput.insertPlainText("Введите номер телефона!")

        else:
        
            file = str("acco" + self.phone + ".session")
            
            self.client = Client("acco" + self.phone, api_id, api_hash)
            
            if os.path.isfile(file) == True:

                self.Tgoutput.insertPlainText("Вы уже авторизованы!\n")

                self.client.start()

            else:

                self.client.connect()

                self.sent_code = self.client.send_code(self.phone)
                
                self.Tgoutput.insertPlainText("Вам был отправлен код авторизации. Введите его в соответствующее поле\n")

                return (self.client, self.sent_code, self.phone)
        

    def TGauth(self):
        try:

            print(self.phone, self.sent_code.phone_code_hash)

            code = self.TGcodeinp.text()
    
            self.client.sign_in(self.phone, self.sent_code.phone_code_hash, code)
            
            self.Tgoutput.insertPlainText("Вы успешно авторизованы!\n")
        
        except Exception:
            self.Tgoutput.insertPlainText("Произошла ошибка. Попробуйте ввести учетные данные заново.\n")
    
    def accdel(self):
        
        try: 
            self.client.stop()
        except Exception:
            None

        self.phone = self.TGNumbinp.text()

        print(self.TGNumbinp.text())

        if self.TGNumbinp.text() == "":

            self.Tgoutput.insertPlainText("Сначала введите свой номер телефона\n")

        else:

            file = str("acco" + self.phone +".session")

            print(file)

            try:
           
                os.remove(file)

                self.Tgoutput.insertPlainText("Ваша сессия завершена\n")
            
            except Exception:
                
                self.Tgoutput.insertPlainText("Ваша сессия уже завершена\n")

    def TGmsg(self):
        if self.TGNumbinp.text() == "":

            self.Tgoutput.insertPlainText("Введите номер телефона!")

        elif self.IDChannelinput.text == "":

            self.Tgoutput.setPlainText("Сначала введите ID канала")

        else:

            self.chatid = self.IDChannelinput.text()

            self.Tgoutput.setPlainText("")

            self.client.run(TGmsgas(self))
        

    def searchmsg(self):

        self.chatid = self.TGIDChannelsearchinp.text()

        self.que = self.lineEdit_3.text()

        self.user = self.lineEdit_4.text()

        self.client.run(searchmsg(self))

async def TGmsgas(self):
    async for message in self.client.get_chat_history(chat_id = self.chatid):
        if message.text == None:
            if message.photo == None:
                self.Tgoutput.insertPlainText(str(message) + "\n------------------------------------------------------------------\n")
            else: self.Tgoutput.insertPlainText(str(message.photo) + "\n------------------------------------------------------------------\n")
        else: self.Tgoutput.insertPlainText(str(message.text) + "\n------------------------------------------------------------------\n")

async def searchmsg(self):
    async for message in self.client.search_messages(chat_id= self.chatid, query= self.que, from_user= self.user):
        if message.text == None:
            if message.photo == None:
                self.TGoutputsearch.insertPlainText(str(message) + "\n------------------------------------------------------------------\n")
            else: self.TGoutputsearch.insertPlainText("Фотография" + "\n------------------------------------------------------------------\n")
        else: self.TGoutputsearch.insertPlainText(str(message.text) + "\n------------------------------------------------------------------\n")


if __name__ == "__main__":
    import sys
    appp = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(appp.exec_())