# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/julio/Desktop/SIMNAV/simnav/gui/base/ui/pantalla_inicio.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaBienvenida(object):
    def setupUi(self, VentanaBienvenida):
        VentanaBienvenida.setObjectName("VentanaBienvenida")
        VentanaBienvenida.setWindowModality(QtCore.Qt.NonModal)
        VentanaBienvenida.resize(976, 771)
        VentanaBienvenida.setMinimumSize(QtCore.QSize(976, 771))
        VentanaBienvenida.setMaximumSize(QtCore.QSize(16777215, 155555))
        VentanaBienvenida.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(VentanaBienvenida)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(200, 200, 200, 200)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setItalic(True)
        self.titulo.setFont(font)
        self.titulo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout_3.addWidget(self.titulo)
        self.descripcion = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.descripcion.setFont(font)
        self.descripcion.setAlignment(QtCore.Qt.AlignCenter)
        self.descripcion.setObjectName("descripcion")
        self.verticalLayout_3.addWidget(self.descripcion)
        self.nueva_simulacion = QtWidgets.QPushButton(self.centralwidget)
        self.nueva_simulacion.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nueva_simulacion.sizePolicy().hasHeightForWidth())
        self.nueva_simulacion.setSizePolicy(sizePolicy)
        self.nueva_simulacion.setMaximumSize(QtCore.QSize(50000, 80))
        self.nueva_simulacion.setAutoDefault(False)
        self.nueva_simulacion.setObjectName("nueva_simulacion")
        self.verticalLayout_3.addWidget(self.nueva_simulacion)
        self.abrir_simulacion = QtWidgets.QPushButton(self.centralwidget)
        self.abrir_simulacion.setMaximumSize(QtCore.QSize(50000, 80))
        self.abrir_simulacion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.abrir_simulacion.setAutoDefault(False)
        self.abrir_simulacion.setDefault(False)
        self.abrir_simulacion.setFlat(False)
        self.abrir_simulacion.setObjectName("abrir_simulacion")
        self.verticalLayout_3.addWidget(self.abrir_simulacion)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        VentanaBienvenida.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VentanaBienvenida)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        VentanaBienvenida.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaBienvenida)
        self.statusbar.setObjectName("statusbar")
        VentanaBienvenida.setStatusBar(self.statusbar)
        self.actionAbrir = QtWidgets.QAction(VentanaBienvenida)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalir = QtWidgets.QAction(VentanaBienvenida)
        self.actionSalir.setObjectName("actionSalir")
        self.actionNuevo = QtWidgets.QAction(VentanaBienvenida)
        self.actionNuevo.setObjectName("actionNuevo")
        self.menuFile.addAction(self.actionNuevo)
        self.menuFile.addAction(self.actionAbrir)
        self.menuFile.addAction(self.actionSalir)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(VentanaBienvenida)
        QtCore.QMetaObject.connectSlotsByName(VentanaBienvenida)

    def retranslateUi(self, VentanaBienvenida):
        _translate = QtCore.QCoreApplication.translate
        VentanaBienvenida.setWindowTitle(_translate("VentanaBienvenida", "Simnav"))
        self.titulo.setText(_translate("VentanaBienvenida", "SIMNAV"))
        self.descripcion.setText(_translate("VentanaBienvenida", "Desarrollado bajo la licencia LGPL por Julio Navarro como requisito\n"
" parcial para obtener el titulo de ingeniero quimico"))
        self.nueva_simulacion.setText(_translate("VentanaBienvenida", "Nueva simulación"))
        self.abrir_simulacion.setText(_translate("VentanaBienvenida", "Abrir simulación"))
        self.menuFile.setTitle(_translate("VentanaBienvenida", "File"))
        self.actionAbrir.setText(_translate("VentanaBienvenida", "Abrir"))
        self.actionSalir.setText(_translate("VentanaBienvenida", "Salir"))
        self.actionNuevo.setText(_translate("VentanaBienvenida", "Nuevo"))

