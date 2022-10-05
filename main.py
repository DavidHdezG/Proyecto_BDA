from PyQt5 import QtWidgets

import gui

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Proyecto = QtWidgets.QMainWindow()
    ui = gui.Ui_Proyecto()
    ui.setupUi(Proyecto)
    Proyecto.show()
    sys.exit(app.exec_())