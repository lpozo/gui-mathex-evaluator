# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EvaluatorMainWin(object):
    def setupUi(self, EvaluatorMainWin):
        EvaluatorMainWin.setObjectName("EvaluatorMainWin")
        EvaluatorMainWin.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(EvaluatorMainWin)
        self.verticalLayout.setObjectName("verticalLayout")
        self.expGroupBox = QtWidgets.QGroupBox(EvaluatorMainWin)
        self.expGroupBox.setObjectName("expGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.expGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.expEdit = QtWidgets.QLineEdit(self.expGroupBox)
        self.expEdit.setObjectName("expEdit")
        self.horizontalLayout.addWidget(self.expEdit)
        self.evalButton = QtWidgets.QPushButton(self.expGroupBox)
        self.evalButton.setObjectName("evalButton")
        self.horizontalLayout.addWidget(self.evalButton)
        self.verticalLayout.addWidget(self.expGroupBox)
        self.resultList = QtWidgets.QListWidget(EvaluatorMainWin)
        self.resultList.setObjectName("resultList")
        self.verticalLayout.addWidget(self.resultList)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.clearButton = QtWidgets.QPushButton(EvaluatorMainWin)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_2.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(EvaluatorMainWin)
        QtCore.QMetaObject.connectSlotsByName(EvaluatorMainWin)
        EvaluatorMainWin.setTabOrder(self.expEdit, self.evalButton)
        EvaluatorMainWin.setTabOrder(self.evalButton, self.resultList)
        EvaluatorMainWin.setTabOrder(self.resultList, self.clearButton)

    def retranslateUi(self, EvaluatorMainWin):
        _translate = QtCore.QCoreApplication.translate
        EvaluatorMainWin.setWindowTitle(_translate("EvaluatorMainWin", "Math Expressions Evaluator"))
        EvaluatorMainWin.setToolTip(_translate("EvaluatorMainWin", "Evaluate the Expression"))
        self.expGroupBox.setTitle(_translate("EvaluatorMainWin", "Enter a Math Expression:"))
        self.expEdit.setToolTip(_translate("EvaluatorMainWin", "Enter a Math Expression"))
        self.evalButton.setText(_translate("EvaluatorMainWin", "&Evaluate"))
        self.resultList.setToolTip(_translate("EvaluatorMainWin", "Evaluation Results"))
        self.clearButton.setToolTip(_translate("EvaluatorMainWin", "Clear Results"))
        self.clearButton.setText(_translate("EvaluatorMainWin", "&Clear Results"))

