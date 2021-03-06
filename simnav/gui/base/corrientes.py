from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Corrientes(object):
    def setupUi(self, VentanaCorrientes):
        VentanaCorrientes.setObjectName("VentanaCorrientes")
        VentanaCorrientes.resize(650, 350)
        VentanaCorrientes.setMinimumSize(QtCore.QSize(650, 350))
        VentanaCorrientes.setMaximumSize(QtCore.QSize(650, 350))
        VentanaCorrientes.setBaseSize(QtCore.QSize(650, 350))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        VentanaCorrientes.setFont(font)
        self.centralwidget = QtWidgets.QWidget(VentanaCorrientes)
        self.centralwidget.setObjectName("Corrientes")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.listaCorrientes = QtWidgets.QListWidget(self.centralwidget)
        self.listaCorrientes.setObjectName("listaCorrientes")
        self.verticalLayout_5.addWidget(self.listaCorrientes)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.eliminarCorriente = QtWidgets.QPushButton(self.centralwidget)
        self.eliminarCorriente.setObjectName("eliminarCorriente")
        self.horizontalLayout_7.addWidget(self.eliminarCorriente)
        self.agregarCorriente = QtWidgets.QPushButton(self.centralwidget)
        self.agregarCorriente.setObjectName("agregarCorriente")
        self.horizontalLayout_7.addWidget(self.agregarCorriente)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(9, 9, 9, 9)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.flujoLabel = QtWidgets.QLabel(self.centralwidget)
        self.flujoLabel.setObjectName("flujoLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.flujoLabel)
        self.flujoLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.flujoLineEdit.setObjectName("flujoLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.flujoLineEdit)
        self.temperaturaLabel = QtWidgets.QLabel(self.centralwidget)
        self.temperaturaLabel.setObjectName("temperaturaLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.temperaturaLabel)
        self.temperaturaLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.temperaturaLineEdit.setObjectName("temperaturaLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.temperaturaLineEdit)
        self.presionLabel = QtWidgets.QLabel(self.centralwidget)
        self.presionLabel.setObjectName("presionLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.presionLabel)
        self.presionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.presionLineEdit.setObjectName("presionLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.presionLineEdit)
        self.composicionLabel = QtWidgets.QLabel(self.centralwidget)
        self.composicionLabel.setObjectName("composicionLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.composicionLabel)
        self.modificarComposicion = QtWidgets.QPushButton(self.centralwidget)
        self.modificarComposicion.setObjectName("modificarComposicion")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.modificarComposicion)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.actualizarCorriente = QtWidgets.QPushButton(self.centralwidget)
        self.actualizarCorriente.setObjectName("actualizarCorriente")
        self.verticalLayout_6.addWidget(self.actualizarCorriente, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.retranslateUi(VentanaCorrientes)
        QtCore.QMetaObject.connectSlotsByName(VentanaCorrientes)

    def retranslateUi(self, VentanaCorrientes):
        _translate = QtCore.QCoreApplication.translate
        VentanaCorrientes.setWindowTitle(_translate("VentanaCorrientes", "Corrientes"))
        self.label_4.setText(_translate("VentanaCorrientes", "Corrientes"))
        self.eliminarCorriente.setText(_translate("VentanaCorrientes", "Eliminar"))
        self.agregarCorriente.setText(_translate("VentanaCorrientes", "Agregar"))
        self.label_6.setText(_translate("VentanaCorrientes", "Datos Corriente"))
        self.flujoLabel.setText(_translate("VentanaCorrientes", "Flujo"))
        self.temperaturaLabel.setText(_translate("VentanaCorrientes", "Temperatura (K)"))
        self.presionLabel.setText(_translate("VentanaCorrientes", "presion (kPA)"))
        self.composicionLabel.setText(_translate("VentanaCorrientes", "Composicion"))
        self.modificarComposicion.setText(_translate("VentanaCorrientes", "Modificar"))
        self.actualizarCorriente.setText(_translate("VentanaCorrientes", "Guardar Cambios"))