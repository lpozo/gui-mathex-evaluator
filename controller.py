from PyQt5.QtWidgets import QDialog

from model import MainModel
from view.window import Ui_EvaluatorMainWin


class MainCtrl(QDialog):
    def __init__(self):
        super().__init__()
        self._ui = Ui_EvaluatorMainWin()
        self._ui.setupUi(self)
        self._model = MainModel()
        self._ui.evalButton.clicked.connect(self.onEvaluateBtnClicked)
        self._ui.clearButton.clicked.connect(self.onClearBtnClicked)

    def showWindow(self):
        self.show()

    def evaluateExpression(self, exp):
        try:
            return str(self._model.eval_expression(exp))
        except SyntaxError:
            return f"Syntax error in expression: {exp}"
        except (NameError, ValueError) as err:
            return err

    def readExpression(self):
        exp = self._ui.expEdit.text()
        if not exp:
            return
        return exp

    def showResult(self, result):
        self._ui.expEdit.clear()
        self._ui.resultList.insertItem(0, result)

    def clearResults(self):
        self._ui.resultList.clear()

    def onEvaluateBtnClicked(self):
        self._ui.expEdit.setFocus()
        exp = self.readExpression()
        if exp is None:
            return
        result = str(self.evaluateExpression(exp))
        self.showResult(result)

    def onClearBtnClicked(self):
        self._ui.expEdit.setFocus()
        self.clearResults()
