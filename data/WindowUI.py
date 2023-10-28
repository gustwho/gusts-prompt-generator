# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(760, 420)
        MainWindow.setMinimumSize(QSize(760, 420))
        MainWindow.setMaximumSize(QSize(760, 420))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(760, 420))
        self.centralwidget.setMaximumSize(QSize(760, 420))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(169, 201, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(247, 247, 247, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(160, 160, 160, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush8 = QBrush(QColor(240, 240, 240, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(120, 120, 120, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.centralwidget.setPalette(palette)
        self.centralwidget.setStyleSheet(u"background-color: rgb(169, 201, 240);")
        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(0, 0, 761, 71))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(16)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 70, 761, 51))
        self.Characters = QHBoxLayout(self.horizontalLayoutWidget)
        self.Characters.setObjectName(u"Characters")
        self.Characters.setContentsMargins(25, 0, 25, 0)
        self.GenerateBtn = QPushButton(self.centralwidget)
        self.GenerateBtn.setObjectName(u"GenerateBtn")
        self.GenerateBtn.setGeometry(QRect(270, 160, 221, 41))
        self.GenerateBtn.setFont(font)
        self.GenerateBtn.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 210, 761, 131))
        self.GenContainer = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.GenContainer.setObjectName(u"GenContainer")
        self.GenContainer.setContentsMargins(160, 0, 160, 0)
        self.Generated = QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.Generated.setObjectName(u"Generated")
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(11)
        self.Generated.setFont(font1)
        self.Generated.setStyleSheet(u"background-color: rgba(255,255,255,50);\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-style: solid;\n"
"border-radius: 5px;")
        self.Generated.setReadOnly(True)

        self.GenContainer.addWidget(self.Generated)

        self.ListedChars = QListWidget(self.centralwidget)
        self.ListedChars.setObjectName(u"ListedChars")
        self.ListedChars.setGeometry(QRect(120, 340, 521, 51))
        self.ListedChars.setStyleSheet(u"background-color: transparent; border:none;")
        self.ListedChars.setFlow(QListView.LeftToRight)
        self.ListedChars.setProperty("isWrapping", True)
        self.ListedChars.setSpacing(5)
        self.ListedChars.setUniformItemSizes(True)
        self.ListedChars.setSortingEnabled(False)
        self.CharsMenu = QComboBox(self.centralwidget)
        self.CharsMenu.setObjectName(u"CharsMenu")
        self.CharsMenu.setGeometry(QRect(240, 130, 281, 22))
        self.CharsMenu.setStyleSheet(u"background-color: rgba(255,255,255,50);\n"
"border-width: 1px;\n"
"border-color: white;\n"
"border-style: solid;\n"
"border-radius: 5px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 760, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Gust's Prompt/Quotes Generator", None))
        self.GenerateBtn.setText(QCoreApplication.translate("MainWindow", u"Generate!", None))
        self.Generated.setPlainText(QCoreApplication.translate("MainWindow", u"Click the generate button!", None))
    # retranslateUi

