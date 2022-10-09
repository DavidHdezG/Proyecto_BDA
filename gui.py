import cx_Oracle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QDialog, QLineEdit, QDialogButtonBox, QFormLayout, \
    QMessageBox
import Connection


class Ui_Proyecto(object):

    def setupUi(self, Proyecto):
        self.cursor = Connection.cursor
        Proyecto.setObjectName("Proyecto")
        Proyecto.resize(640, 480)
        Proyecto.setFixedSize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Proyecto)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 10, 461, 461))
        self.table.setObjectName("table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.addDepto = QtWidgets.QPushButton(self.centralwidget)
        self.addDepto.setGeometry(QtCore.QRect(490, 120, 131, 21))
        self.addDepto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addDepto.setObjectName("addDepto")
        self.updateDepto = QtWidgets.QPushButton(self.centralwidget)
        self.updateDepto.setGeometry(QtCore.QRect(482, 150, 147, 21))
        self.updateDepto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.updateDepto.setObjectName("updateDepto")
        self.delDepto = QtWidgets.QPushButton(self.centralwidget)
        self.delDepto.setGeometry(QtCore.QRect(490, 180, 131, 21))
        self.delDepto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delDepto.setObjectName("delDepto")
        self.addEmp = QtWidgets.QPushButton(self.centralwidget)
        self.addEmp.setGeometry(QtCore.QRect(490, 210, 131, 21))
        self.addEmp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addEmp.setObjectName("addEmp")
        self.delEmp = QtWidgets.QPushButton(self.centralwidget)
        self.delEmp.setGeometry(QtCore.QRect(490, 240, 131, 21))
        self.delEmp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delEmp.setObjectName("delEmp")
        self.updateEmp = QtWidgets.QPushButton(self.centralwidget)
        self.updateEmp.setGeometry(QtCore.QRect(490, 270, 131, 21))
        self.updateEmp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.updateEmp.setObjectName("updateEmp")
        self.noEmpDepto = QtWidgets.QPushButton(self.centralwidget)
        self.noEmpDepto.setGeometry(QtCore.QRect(490, 300, 131, 41))
        self.noEmpDepto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.noEmpDepto.setObjectName("noEmpDepto")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(490, 30, 131, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(True)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStatusTip("")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        Proyecto.setCentralWidget(self.centralwidget)
        self.comboBox.currentIndexChanged.connect(lambda: self.reloadTable())
        self.addEmp.clicked.connect(lambda: self.addEmpButton())
        self.updateEmp.clicked.connect(lambda: self.updateEmpButton())
        self.delEmp.clicked.connect(lambda: self.deleteEmpButton())
        self.updateDepto.clicked.connect(lambda: self.updateDeptoButton())
        self.delDepto.clicked.connect(lambda: self.removeDeptButton())
        self.addDepto.clicked.connect(lambda: self.addDeptButton())
        self.noEmpDepto.clicked.connect((lambda: self.noEmpDeptoButton()))
        self.retranslateUi(Proyecto)
        QtCore.QMetaObject.connectSlotsByName(Proyecto)
        self.reloadTable()

    def retranslateUi(self, Proyecto):
        _translate = QtCore.QCoreApplication.translate
        Proyecto.setWindowTitle(_translate("Proyecto", "Proyecto"))
        self.addDepto.setText(_translate("Proyecto", "Añadir departamento"))
        self.updateDepto.setText(_translate("Proyecto", "Actualizar departamento"))
        self.delDepto.setText(_translate("Proyecto", "Borrar departamento"))
        self.addEmp.setText(_translate("Proyecto", "Añadir empleado"))
        self.delEmp.setText(_translate("Proyecto", "Borrar empleado"))
        self.updateEmp.setText(_translate("Proyecto", "Actualizar empleado"))
        self.noEmpDepto.setText(_translate("Proyecto", "No. de empleados \n"" en departamento"))
        self.comboBox.setItemText(0, _translate("Proyecto", "Departamentos"))
        self.comboBox.setItemText(1, _translate("Proyecto", "Empleados"))

    def reloadTable(self):
        self.table.clear()
        self.table.setRowCount(0)
        if self.comboBox.currentText() == "Departamentos":

            self.cursor.execute('SELECT * FROM DEPT')
            rows = self.cursor.fetchall()
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels(["DEPTNO", "DNAME", "LOC"])
            n = 0
            for row in rows:
                self.table.insertRow(n)
                self.table.setItem(n, 0, QTableWidgetItem(str(row[0])))
                self.table.setItem(n, 1, QTableWidgetItem(row[1]))
                self.table.setItem(n, 2, QTableWidgetItem(row[2]))
                n = +1
        else:
            self.cursor.execute('SELECT * FROM emp')
            rows = self.cursor.fetchall()
            self.table.setColumnCount(8)
            self.table.setHorizontalHeaderLabels(["EMPNO", "ENAME", "JOB", "MGR", "HIREDATE", "SAL", "COMM", "DEPTNO"])
            n = 0
            for row in rows:
                self.table.insertRow(n)
                self.table.setItem(n, 0, QTableWidgetItem(str(row[0])))
                self.table.setItem(n, 1, QTableWidgetItem(str(row[1])))
                self.table.setItem(n, 2, QTableWidgetItem(str(row[2])))
                self.table.setItem(n, 3, QTableWidgetItem(str(row[3])))
                self.table.setItem(n, 4, QTableWidgetItem(str(row[4])))
                self.table.setItem(n, 5, QTableWidgetItem(str(row[5])))
                self.table.setItem(n, 6, QTableWidgetItem(str(row[6])))
                self.table.setItem(n, 7, QTableWidgetItem(str(row[7])))
                n = +1
        self.table.resizeColumnsToContents()

    def noEmpDeptoButton(self):
        try:
            dialog = DelInputDialog(None, 'departamento', "Número de empleados")

            if dialog.exec_():
                inputs = dialog.getInputs()
                res = self.cursor.callfunc('no_emp_deptno', int, [inputs])
                if res == -1:
                    QMessageBox.information(None, "Departamento " + inputs, "El departamento no tiene empleados asignados")
                else:
                    QMessageBox.information(None, "Departamento " + inputs, "Número de Empleados: " + str(res))

        except cx_Oracle.DatabaseError as e:
            QMessageBox.critical(None, "Error", str(e))

    def addDeptButton(self):
        try:
            dialog = DeptInputDialog(None, "Añadir Departamento")

            if dialog.exec_():
                inputs = dialog.getInputs()
                self.cursor.callproc('Add_depto', [inputs[0], inputs[1], inputs[2]])
                self.reloadTable()
        except cx_Oracle.DatabaseError as e:
            QMessageBox.critical(None, "Error", str(e))

    def updateDeptoButton(self):
        try:
            dialog = DeptInputDialog(None, "Actualizar Departamento")

            if dialog.exec_():
                inputs = dialog.getInputs()
                self.cursor.callproc('update_depto', [inputs[0], inputs[1], inputs[2]])
                self.reloadTable()
        except cx_Oracle.DatabaseError as e:
            QMessageBox.critical(None, "Error", str(e))

    def removeDeptButton(self):
        try:
            dialog = DelInputDialog(None, 'departamento', "Borrar departamento")
            if dialog.exec_():
                inputs = dialog.getInputs()
                self.cursor.callproc('delete_depto', [inputs])
                self.reloadTable()
        except cx_Oracle.DatabaseError as e:
            QMessageBox.critical(None, "Error", str(e))

    def addEmpButton(self):
        try:
            dialog = EmpInputDialog(None, "Añadir Empleado")

            if dialog.exec_():
                inputs = dialog.getInputs()
                self.cursor.callproc('Add_emp',
                                     [inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6],
                                      inputs[7]])
                self.reloadTable()
        except cx_Oracle.DatabaseError as e:
            print(e)
            QMessageBox.critical(None, "Error", str(e))

    def deleteEmpButton(self):
        try:
            dialog = DelInputDialog(None, 'empleado', "Borrar Empleado")
            if dialog.exec_():
                inputs = dialog.getInputs()
                self.cursor.callproc('delete_emp', [inputs])
                self.reloadTable()
        except cx_Oracle.DatabaseError as e:
            print(e)
            QMessageBox.critical(None, "Error", str(e))

    def updateEmpButton(self):
        try:
            dialog = EmpInputDialog(None, "Actualizar Empleado")

            if dialog.exec_():
                inputs = dialog.getInputs()
                self.cursor.callproc('update_emp',
                                     [inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6],
                                      inputs[7]])
                self.reloadTable()
        except cx_Oracle.DatabaseError as e:
            print(e)
            QMessageBox.critical(None, "Error", str(e))


class DelInputDialog(QDialog):
    def __init__(self, parent=None, table='', title=""):
        super().__init__(parent)
        close = False
        self.idAux = QLineEdit(self)
        self.setWindowTitle(title)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Número de " + table, self.idAux)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return self.idAux.text()

    def AuxReject(self):
        super().reject()


class DeptInputDialog(QDialog):
    def __init__(self, parent=None, title=""):
        super().__init__(parent)

        self.deptno = QLineEdit(self)
        self.dname = QLineEdit(self)
        self.loc = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);
        self.setWindowTitle(title)
        layout = QFormLayout(self)
        layout.addRow("Número de departamento", self.deptno)
        layout.addRow("Nombre ", self.dname)
        layout.addRow("Localización", self.loc)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return self.deptno.text(), self.dname.text(), self.loc.text()


class EmpInputDialog(QDialog):
    def __init__(self, parent=None, title=""):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.empno = QLineEdit(self)
        self.ename = QLineEdit(self)
        self.job = QLineEdit(self)
        self.mgr = QLineEdit(self)
        self.mgr.setPlaceholderText("Opcional")
        self.hireDate = QLineEdit(self)
        self.sal = QLineEdit(self)
        self.comm = QLineEdit(self)
        self.comm.setPlaceholderText("Opcional")
        self.deptno = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Número de empleado", self.empno)
        layout.addRow("Nombre ", self.ename)
        layout.addRow("Puesto", self.job)

        layout.addRow("MGR", self.mgr)
        layout.addRow("Fecha de contratación", self.hireDate)
        layout.addRow("Salario", self.sal)
        layout.addRow("Comisión", self.comm)
        layout.addRow("Número de departamento", self.deptno)
        layout.addWidget(buttonBox)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return self.empno.text(), self.ename.text(), self.job.text(), self.mgr.text(), self.hireDate.text(), self.sal.text(), self.comm.text(), self.deptno.text()
