# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'queue_editor_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.editor_button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.editor_button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.editor_button_box.setOrientation(QtCore.Qt.Horizontal)
        self.editor_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.editor_button_box.setObjectName("editor_button_box")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.select_mode_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.select_mode_label.setAlignment(QtCore.Qt.AlignCenter)
        self.select_mode_label.setObjectName("select_mode_label")
        self.horizontalLayout.addWidget(self.select_mode_label)
        self.mode_combo_box = QtWidgets.QComboBox(Dialog)
        self.mode_combo_box.setGeometry(QtCore.QRect(210, 10, 181, 41))
        self.mode_combo_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mode_combo_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.mode_combo_box.setObjectName("mode_combo_box")
        self.mode_combo_box.addItem("")
        self.stages_spin_box = QtWidgets.QSpinBox(Dialog)
        self.stages_spin_box.setGeometry(QtCore.QRect(340, 90, 51, 41))
        self.stages_spin_box.setAlignment(QtCore.Qt.AlignCenter)
        self.stages_spin_box.setMinimum(1)
        self.stages_spin_box.setObjectName("stages_spin_box")
        self.difficulty_spin_box = QtWidgets.QSpinBox(Dialog)
        self.difficulty_spin_box.setGeometry(QtCore.QRect(340, 140, 51, 41))
        self.difficulty_spin_box.setAlignment(QtCore.Qt.AlignCenter)
        self.difficulty_spin_box.setMinimum(1)
        self.difficulty_spin_box.setObjectName("difficulty_spin_box")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 151, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.all_stages_check_box = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.all_stages_check_box.setChecked(True)
        self.all_stages_check_box.setObjectName("all_stages_check_box")
        self.verticalLayout.addWidget(self.all_stages_check_box)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 151, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.farm_bios_check_box = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.farm_bios_check_box.setObjectName("farm_bios_check_box")
        self.verticalLayout_2.addWidget(self.farm_bios_check_box)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 190, 151, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.zero_boosts_check_box = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.zero_boosts_check_box.setObjectName("zero_boosts_check_box")
        self.verticalLayout_3.addWidget(self.zero_boosts_check_box)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(220, 90, 111, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stages_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.stages_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stages_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stages_label.setObjectName("stages_label")
        self.verticalLayout_4.addWidget(self.stages_label)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(220, 140, 111, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.difficulty_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.difficulty_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.difficulty_label.setObjectName("difficulty_label")
        self.verticalLayout_5.addWidget(self.difficulty_label)
        self.mission_mode_combo_box = QtWidgets.QComboBox(Dialog)
        self.mission_mode_combo_box.setGeometry(QtCore.QRect(120, 140, 101, 41))
        self.mission_mode_combo_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mission_mode_combo_box.setObjectName("mission_mode_combo_box")
        self.mission_mode_combo_box.addItem("")
        self.mission_mode_label = QtWidgets.QLabel(Dialog)
        self.mission_mode_label.setGeometry(QtCore.QRect(10, 140, 121, 41))
        self.mission_mode_label.setObjectName("mission_mode_label")

        self.retranslateUi(Dialog)
        self.mission_mode_combo_box.setCurrentIndex(-1)
        self.editor_button_box.accepted.connect(Dialog.accept)
        self.editor_button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.select_mode_label.setText(_translate("Dialog", "Select mode:"))
        self.mode_combo_box.setItemText(0, _translate("Dialog", "Test"))
        self.all_stages_check_box.setText(_translate("Dialog", "All stages"))
        self.farm_bios_check_box.setText(_translate("Dialog", "Farm bios"))
        self.zero_boosts_check_box.setText(_translate("Dialog", "Stop when 0 boost points"))
        self.stages_label.setText(_translate("Dialog", "Stages:"))
        self.difficulty_label.setText(_translate("Dialog", "Difficulty:"))
        self.mission_mode_combo_box.setItemText(0, _translate("Dialog", "ULTIMATE TEST"))
        self.mission_mode_label.setText(_translate("Dialog", "Select mission mode:"))
