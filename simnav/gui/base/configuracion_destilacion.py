# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simnav/gui/vistas/diseños/designer/configuracion_destilacion.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Destilacion(object):
    def setupUi(self, Destilacion):
        Destilacion.setObjectName("Destilacion")
        Destilacion.resize(350, 420)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Destilacion)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Destilacion)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(Destilacion)
        self.tabWidget.setObjectName("tabWidget")
        self.torre = QtWidgets.QWidget()
        self.torre.setObjectName("torre")
        self.gridLayout = QtWidgets.QGridLayout(self.torre)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.numeroDePlatosLabel = QtWidgets.QLabel(self.torre)
        self.numeroDePlatosLabel.setObjectName("numeroDePlatosLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.numeroDePlatosLabel)
        self.numeroDePlatosLineEdit = QtWidgets.QLineEdit(self.torre)
        self.numeroDePlatosLineEdit.setObjectName("numeroDePlatosLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numeroDePlatosLineEdit)
        self.presionLabel = QtWidgets.QLabel(self.torre)
        self.presionLabel.setObjectName("presionLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.presionLabel)
        self.presionLineEdit = QtWidgets.QLineEdit(self.torre)
        self.presionLineEdit.setObjectName("presionLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.presionLineEdit)
        self.flujoDestiladoLabel = QtWidgets.QLabel(self.torre)
        self.flujoDestiladoLabel.setObjectName("flujoDestiladoLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.flujoDestiladoLabel)
        self.flujoDestiladoLineEdit = QtWidgets.QLineEdit(self.torre)
        self.flujoDestiladoLineEdit.setObjectName("flujoDestiladoLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.flujoDestiladoLineEdit)
        self.tipoDeCondensadorLabel = QtWidgets.QLabel(self.torre)
        self.tipoDeCondensadorLabel.setObjectName("tipoDeCondensadorLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tipoDeCondensadorLabel)
        self.tipoDeCondensadorComboBox = QtWidgets.QComboBox(self.torre)
        self.tipoDeCondensadorComboBox.setObjectName("tipoDeCondensadorComboBox")
        self.tipoDeCondensadorComboBox.addItem("")
        self.tipoDeCondensadorComboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tipoDeCondensadorComboBox)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.torre, "")
        self.alimentacion = QtWidgets.QWidget()
        self.alimentacion.setObjectName("alimentacion")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.alimentacion)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tablaAlimentacion = QtWidgets.QTableWidget(self.alimentacion)
        self.tablaAlimentacion.setObjectName("tablaAlimentacion")
        self.tablaAlimentacion.setColumnCount(2)
        self.tablaAlimentacion.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaAlimentacion.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaAlimentacion.setHorizontalHeaderItem(1, item)
        self.tablaAlimentacion.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tablaAlimentacion)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.eliminarAlimentacion = QtWidgets.QPushButton(self.alimentacion)
        self.eliminarAlimentacion.setObjectName("eliminarAlimentacion")
        self.horizontalLayout.addWidget(self.eliminarAlimentacion)
        self.agregarAlimentacion = QtWidgets.QPushButton(self.alimentacion)
        self.agregarAlimentacion.setObjectName("agregarAlimentacion")
        self.horizontalLayout.addWidget(self.agregarAlimentacion)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.alimentacion, "")
        self.salidas_laterales = QtWidgets.QWidget()
        self.salidas_laterales.setObjectName("salidas_laterales")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.salidas_laterales)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tablaProductos = QtWidgets.QTableWidget(self.salidas_laterales)
        self.tablaProductos.setObjectName("tablaProductos")
        self.tablaProductos.setColumnCount(2)
        self.tablaProductos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(1, item)
        self.tablaProductos.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.tablaProductos)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.eliminarProducto = QtWidgets.QPushButton(self.salidas_laterales)
        self.eliminarProducto.setObjectName("eliminarProducto")
        self.horizontalLayout_2.addWidget(self.eliminarProducto)
        self.agregarProducto = QtWidgets.QPushButton(self.salidas_laterales)
        self.agregarProducto.setObjectName("agregarProducto")
        self.horizontalLayout_2.addWidget(self.agregarProducto)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.salidas_laterales, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton = QtWidgets.QPushButton(Destilacion)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight)

        self.retranslateUi(Destilacion)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Destilacion)

    def retranslateUi(self, Destilacion):
        _translate = QtCore.QCoreApplication.translate
        Destilacion.setWindowTitle(_translate("Destilacion", "Form"))
        self.label.setText(_translate("Destilacion", "Configuración columna de destilación"))
        self.numeroDePlatosLabel.setText(_translate("Destilacion", "Numero de platos"))
        self.presionLabel.setText(_translate("Destilacion", "Presión"))
        self.flujoDestiladoLabel.setText(_translate("Destilacion", "Flujo Destilado"))
        self.tipoDeCondensadorLabel.setText(_translate("Destilacion", "Tipo de condensador"))
        self.tipoDeCondensadorComboBox.setItemText(0, _translate("Destilacion", "Parcial"))
        self.tipoDeCondensadorComboBox.setItemText(1, _translate("Destilacion", "Total"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.torre), _translate("Destilacion", "Datos torre"))
        item = self.tablaAlimentacion.horizontalHeaderItem(0)
        item.setText(_translate("Destilacion", "Corriente"))
        item = self.tablaAlimentacion.horizontalHeaderItem(1)
        item.setText(_translate("Destilacion", "Plato"))
        self.eliminarAlimentacion.setText(_translate("Destilacion", "Eliminar"))
        self.agregarAlimentacion.setText(_translate("Destilacion", "Agregar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alimentacion), _translate("Destilacion", "Alimentación"))
        item = self.tablaProductos.horizontalHeaderItem(0)
        item.setText(_translate("Destilacion", "Flujo (kmol/h)"))
        item = self.tablaProductos.horizontalHeaderItem(1)
        item.setText(_translate("Destilacion", "Plato"))
        self.eliminarProducto.setText(_translate("Destilacion", "Eliminar"))
        self.agregarProducto.setText(_translate("Destilacion", "Agregar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.salidas_laterales), _translate("Destilacion", "Salidas Laterales"))
        self.pushButton.setText(_translate("Destilacion", "Aceptar"))

