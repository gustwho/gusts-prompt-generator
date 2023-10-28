import os
try:
    import PySide6
except:
    os.system("pip3 install pyside6")
import json
from data.loader import load
from data.loader import gen
from PySide6 import QtWidgets
from PySide6 import QtCore
from data.WindowUI import Ui_MainWindow
try:
    import updatechecker
except:
    print("Offline?")
def safe_int(n):
    try:
        return int(n)
    except:
        return 0
KnownEvents = []
updating = False
lastamt = 1
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.update_settings()
        self.update_boxes()

        genbtn: QtWidgets.QPushButton = self.GenerateBtn
        genbtn.clicked.connect(self.genbtn_click)

        CharsMenu: QtWidgets.QComboBox = self.CharsMenu
        CharsMenu.currentIndexChanged.connect(self.update_boxes)


    def update_settings(self):
        global updating,lastamt
        updating = True
        ListedChars: QtWidgets.QListWidget = self.ListedChars
        CharsMenu: QtWidgets.QComboBox = self.CharsMenu

        lastamt = CharsMenu.currentIndex()

        ListedChars.clear()
        CharsMenu.clear()
        valid = load("./prompts/")
        for i in valid:
            ListedChars.addItem(f"{i[0]} People - {i[1]} Prompts")
            CharsMenu.addItem(str(i[0]))
        updating = False
        CharsMenu.setCurrentIndex(lastamt)

    def update_boxes(self):
        Characters: QtWidgets.QHBoxLayout = self.Characters
        CharsMenu: QtWidgets.QComboBox = self.CharsMenu
        amt = safe_int(CharsMenu.currentText())
        if not updating and amt != Characters.count() and amt != 0:
            for i in reversed(range(Characters.count())):
                Characters.itemAt(i).widget().setParent(None)

            for i in range(amt):
                editBox = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
                editBox.setStyleSheet(u"background-color: white;")
                Characters.addWidget(editBox)

    def genbtn_click(self):
        Characters: QtWidgets.QHBoxLayout = self.Characters
        charnames = []
        for i in range(Characters.count()):
            editBox: QtWidgets.QPlainTextEdit = Characters.itemAt(i).widget()
            charnames.append(editBox.toPlainText())
        with open("./data/options.json","w") as f:
            f.write(json.dumps({
                "Characters": charnames,
                "BoldUsernames": False
            }))
        self.update_settings()
        text: QtWidgets.QPlainTextEdit = self.Generated
        suc,generated = gen()
        text.setPlainText(generated)

    def genbtn(self,event):
        genbtn: QtWidgets.QPushButton = self.GenerateBtn
        if genbtn.underMouse():
            if event.buttons() == QtCore.Qt.LeftButton:
                genbtn.setStyleSheet("border-radius: 5px; background-color: rgb(114, 174, 255);")
            else:
                genbtn.setStyleSheet("border-radius: 5px; background-color: rgb(123, 143, 243);")
        else:
            genbtn.setStyleSheet("border-radius: 5px; background-color: rgb(255, 255, 255);")

    def eventFilter(self, source, data):
        event = data.type()
        if not event in KnownEvents:
            KnownEvents.append(event)
            print(event)
        match event:
            case QtCore.QEvent.MouseMove:
                self.genbtn(data)
            case QtCore.QEvent.MouseButtonPress:
                self.genbtn(data)
            case QtCore.QEvent.MouseButtonRelease:
                self.genbtn(data)
        return super().eventFilter(source, data)

app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

app.installEventFilter(window)
app.exec()