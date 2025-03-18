# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.centralLayout_2 = QVBoxLayout(Dialog)
        self.centralLayout_2.setObjectName(u"centralLayout_2")
        self.centralWidget = QWidget(Dialog)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralLayout = QVBoxLayout(self.centralWidget)
        self.centralLayout.setObjectName(u"centralLayout")
        self.titleLabel = QLabel(self.centralWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Arial Hebrew"])
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferNoHinting)
        self.titleLabel.setFont(font)
        self.titleLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.titleLabel.setAutoFillBackground(False)
        self.titleLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.titleLabel.setScaledContents(False)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.centralLayout.addWidget(self.titleLabel)

        self.topWidget = QWidget(self.centralWidget)
        self.topWidget.setObjectName(u"topWidget")
        self.topLayout = QVBoxLayout(self.topWidget)
        self.topLayout.setObjectName(u"topLayout")
        self.loginLabel = QLabel(self.topWidget)
        self.loginLabel.setObjectName(u"loginLabel")
        font1 = QFont()
        font1.setBold(True)
        self.loginLabel.setFont(font1)
        self.loginLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loginLabel.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.topLayout.addWidget(self.loginLabel)

        self.usernameInput = QLineEdit(self.topWidget)
        self.usernameInput.setObjectName(u"usernameInput")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.usernameInput.sizePolicy().hasHeightForWidth())
        self.usernameInput.setSizePolicy(sizePolicy2)
        self.usernameInput.setMinimumSize(QSize(300, 30))
        self.usernameInput.setEchoMode(QLineEdit.EchoMode.Normal)
        self.usernameInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.usernameInput.setClearButtonEnabled(True)

        self.topLayout.addWidget(self.usernameInput)

        self.passwordLabel = QLabel(self.topWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font1)
        self.passwordLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.topLayout.addWidget(self.passwordLabel)

        self.passwordInput = QLineEdit(self.topWidget)
        self.passwordInput.setObjectName(u"passwordInput")
        sizePolicy2.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy2)
        self.passwordInput.setMinimumSize(QSize(300, 30))
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.passwordInput.setClearButtonEnabled(True)

        self.topLayout.addWidget(self.passwordInput)


        self.centralLayout.addWidget(self.topWidget)

        self.bottomWidget = QWidget(self.centralWidget)
        self.bottomWidget.setObjectName(u"bottomWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy3)
        self.bottomLayout = QHBoxLayout(self.bottomWidget)
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.leftButton = QPushButton(self.bottomWidget)
        self.leftButton.setObjectName(u"leftButton")
        self.leftButton.setFlat(True)

        self.bottomLayout.addWidget(self.leftButton)

        self.loginButton = QPushButton(self.bottomWidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setFlat(False)

        self.bottomLayout.addWidget(self.loginButton)

        self.rightButton = QPushButton(self.bottomWidget)
        self.rightButton.setObjectName(u"rightButton")
        self.rightButton.setFlat(True)

        self.bottomLayout.addWidget(self.rightButton)


        self.centralLayout.addWidget(self.bottomWidget)


        self.centralLayout_2.addWidget(self.centralWidget)


        self.retranslateUi(Dialog)

        self.loginButton.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"StoreHub", None))
#if QT_CONFIG(accessibility)
        Dialog.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"StoreHub", None))
        self.loginLabel.setText(QCoreApplication.translate("Dialog", u"Login:", None))
        self.usernameInput.setInputMask("")
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter login here...", None))
        self.passwordLabel.setText(QCoreApplication.translate("Dialog", u"Password:", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter password here...", None))
        self.leftButton.setText("")
        self.loginButton.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.rightButton.setText("")
    # retranslateUi

