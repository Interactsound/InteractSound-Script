"""
___________________________________

INTERACT SOUND 1.0

Credits : 
Maxime FAURE : www.maximefaure.net 
Jérémy REVENIAUD : www.jeremy-reveniaud.com

Release 1.0, April 2016
___________________________________

"""

from PySide import QtCore, QtGui
import shiboken
import sys
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.cmds as cmds
import maya.OpenMayaUI as omui
import maya.mel as mel
import random

#GLOBALS
listFace = []
AudioNodeWave = []
groupe = cmds.group(em=True, n='group')
global Locator


"""
___________________________________
UI QT
___________________________________

"""

class Ui_MainForm(object):
    def setupUi(self, MainForm):

        #MAIN WINDOW
        MainForm.setObjectName("MainForm")
        MainForm.resize(400, 350)
        MainForm.setMinimumSize(QtCore.QSize(400, 350))
        MainForm.setMaximumSize(QtCore.QSize(400, 350))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setWeight(50)
        font.setBold(False)
        MainForm.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainForm.setWindowIcon(icon)

        #TAB
        self.Tab = QtGui.QTabWidget(MainForm)
        self.Tab.setGeometry(QtCore.QRect(0, 0, 411, 351))
        self.Tab.setObjectName("Tab")

        #SETUP
        self.setup = QtGui.QWidget()
        self.setup.setObjectName("setup")
        self.verticalLayoutWidget = QtGui.QWidget(self.setup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 7, 381, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setOpenExternalLinks(False)
        self.label_12.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.createAudioSetup = QtGui.QPushButton(self.verticalLayoutWidget)
        self.createAudioSetup.setObjectName("createAudioSetup")
        self.verticalLayout.addWidget(self.createAudioSetup)
        self.connectAudio = QtGui.QPushButton(self.verticalLayoutWidget)
        self.connectAudio.setObjectName("connectAudio")
        self.verticalLayout.addWidget(self.connectAudio)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Tab.addTab(self.setup, "")

        #EXTRUDE
        self.extrude = QtGui.QWidget()
        self.extrude.setObjectName("extrude")
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.extrude)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setMidLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.memorizeSelection = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.memorizeSelection.setObjectName("memorizeSelection")
        self.verticalLayout_3.addWidget(self.memorizeSelection)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.keepFacesTogether = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.keepFacesTogether.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.keepFacesTogether.setAutoFillBackground(False)
        self.keepFacesTogether.setObjectName("keepFacesTogether")
        self.horizontalLayout_4.addWidget(self.keepFacesTogether)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.extrudeOnSound = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.extrudeOnSound.setObjectName("extrudeOnSound")
        self.verticalLayout_3.addWidget(self.extrudeOnSound)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.Tab.addTab(self.extrude, "")

        #LOCATOR
        self.locator = QtGui.QWidget()
        self.locator.setObjectName("locator")
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.locator)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(9, 9, 381, 189))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.aimConstraint = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.aimConstraint.setObjectName("aimConstraint")
        self.verticalLayout_4.addWidget(self.aimConstraint)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.xConstraint = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.xConstraint.setObjectName("xConstraint")
        self.horizontalLayout_2.addWidget(self.xConstraint)
        self.yConstraint = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.yConstraint.setObjectName("yConstraint")
        self.horizontalLayout_2.addWidget(self.yConstraint)
        self.zConstraint = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.zConstraint.setObjectName("zConstraint")
        self.horizontalLayout_2.addWidget(self.zConstraint)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rotateConstraint = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.rotateConstraint.setObjectName("rotateConstraint")
        self.horizontalLayout_3.addWidget(self.rotateConstraint)
        self.translateConstraint = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.translateConstraint.setObjectName("translateConstraint")
        self.horizontalLayout_3.addWidget(self.translateConstraint)
        self.scaleConstraint = QtGui.QCheckBox(self.verticalLayoutWidget_4)
        self.scaleConstraint.setObjectName("scaleConstraint")
        self.horizontalLayout_3.addWidget(self.scaleConstraint)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.updateLocator = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.updateLocator.setObjectName("updateLocator")
        self.verticalLayout_5.addWidget(self.updateLocator)
        self.createLocator = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.createLocator.setObjectName("createLocator")
        self.verticalLayout_5.addWidget(self.createLocator)
        self.createLocatorSetup = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.createLocatorSetup.setObjectName("createLocatorSetup")
        self.verticalLayout_5.addWidget(self.createLocatorSetup)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.Tab.addTab(self.locator, "")

        #DUPLICATOR
        self.duplicator = QtGui.QWidget()
        self.duplicator.setObjectName("duplicator")
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.duplicator)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 381, 307))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.instanceDuplicatorRandom = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.instanceDuplicatorRandom.setObjectName("instanceDuplicatorRandom")
        self.verticalLayout_6.addWidget(self.instanceDuplicatorRandom)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.numberDuplicationRandom = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.numberDuplicationRandom.setMaximum(200)
        self.numberDuplicationRandom.setObjectName("numberDuplicationRandom")
        self.gridLayout_2.addWidget(self.numberDuplicationRandom, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self.verticalLayoutWidget_3)
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 2, 1, 1)
        self.maximalDistance = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.maximalDistance.setMaximum(100)
        self.maximalDistance.setMinimum(-100)
        self.maximalDistance.setObjectName("maximalDistance")
        self.gridLayout_2.addWidget(self.maximalDistance, 2, 1, 1, 1)
        self.minimalDistance = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.minimalDistance.setMaximum(100)
        self.minimalDistance.setMinimum(-100)
        self.minimalDistance.setObjectName("minimalDistance")
        self.gridLayout_2.addWidget(self.minimalDistance, 1, 1, 1, 1)
        self.horizontalSlider_2 = QtGui.QSlider(self.verticalLayoutWidget_3)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setMinimum(-100)
        self.horizontalSlider_2.setProperty("value", 0)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_2.addWidget(self.horizontalSlider_2, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.horizontalSlider_3 = QtGui.QSlider(self.verticalLayoutWidget_3)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setMinimum(-100)
        self.horizontalSlider_3.setProperty("value", 0)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout_2.addWidget(self.horizontalSlider_3, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.duplicateRandomly = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.duplicateRandomly.setObjectName("duplicateRandomly")
        self.gridLayout_2.addWidget(self.duplicateRandomly, 3, 0, 1, 3)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.instanceDuplicatorRegular = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.instanceDuplicatorRegular.setObjectName("instanceDuplicatorRegular")
        self.verticalLayout_6.addWidget(self.instanceDuplicatorRegular)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalSlider_4 = QtGui.QSlider(self.verticalLayoutWidget_3)
        self.horizontalSlider_4.setMaximum(200)
        self.horizontalSlider_4.setProperty("value", 0)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout_3.addWidget(self.horizontalSlider_4, 0, 2, 1, 1)
        self.numberDuplicationWidth_2 = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.numberDuplicationWidth_2.setMaximum(200)
        self.numberDuplicationWidth_2.setObjectName("numberDuplicationWidth_2")
        self.gridLayout_3.addWidget(self.numberDuplicationWidth_2, 1, 1, 1, 1)
        self.horizontalSlider_5 = QtGui.QSlider(self.verticalLayoutWidget_3)
        self.horizontalSlider_5.setMaximum(200)
        self.horizontalSlider_5.setProperty("value", 0)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.gridLayout_3.addWidget(self.horizontalSlider_5, 1, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.duplicateRegularly = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.duplicateRegularly.setObjectName("duplicateRegularly")
        self.gridLayout_3.addWidget(self.duplicateRegularly, 2, 0, 1, 3)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.numberDuplicationWidth = QtGui.QSpinBox(self.verticalLayoutWidget_3)
        self.numberDuplicationWidth.setMaximum(200)
        self.numberDuplicationWidth.setObjectName("numberDuplicationWidth")
        self.gridLayout_3.addWidget(self.numberDuplicationWidth, 0, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 3, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.Tab.addTab(self.duplicator, "")

        #PARENTIT
        self.parentIt = QtGui.QWidget()
        self.parentIt.setObjectName("parentIt")
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.parentIt)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(9, 9, 381, 311))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.exponential = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        self.exponential.setObjectName("exponential")
        self.gridLayout_4.addWidget(self.exponential, 0, 0, 1, 3)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 3, 0, 1, 1)
        self.numberCubes = QtGui.QSpinBox(self.verticalLayoutWidget_5)
        self.numberCubes.setMaximum(200)
        self.numberCubes.setObjectName("numberCubes")
        self.gridLayout_4.addWidget(self.numberCubes, 1, 1, 1, 1)
        self.horizontalSlider_6 = QtGui.QSlider(self.verticalLayoutWidget_5)
        self.horizontalSlider_6.setMaximum(200)
        self.horizontalSlider_6.setProperty("value", 0)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.gridLayout_4.addWidget(self.horizontalSlider_6, 1, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.duplicateAndParent = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.duplicateAndParent.setObjectName("duplicateAndParent")
        self.gridLayout_4.addWidget(self.duplicateAndParent, 2, 0, 1, 3)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        self.Tab.addTab(self.parentIt, "")

        #COLOR
        self.color = QtGui.QWidget()
        self.color.setObjectName("color")
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.color)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(9, 9, 381, 111))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.objectsAreInstances = QtGui.QCheckBox(self.verticalLayoutWidget_6)
        self.objectsAreInstances.setObjectName("objectsAreInstances")
        self.verticalLayout_8.addWidget(self.objectsAreInstances)
        self.colorize = QtGui.QPushButton(self.verticalLayoutWidget_6)
        self.colorize.setObjectName("colorize")
        self.verticalLayout_8.addWidget(self.colorize)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.Tab.addTab(self.color, "")

        #TRANSLATE UI
        self.retranslateUi(MainForm)
        self.Tab.setCurrentIndex(4)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL("valueChanged(int)"), self.numberDuplicationRandom.setValue)
        QtCore.QObject.connect(self.numberDuplicationRandom, QtCore.SIGNAL("valueChanged(int)"), self.horizontalSlider.setValue)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL("valueChanged(int)"), self.minimalDistance.setValue)
        QtCore.QObject.connect(self.minimalDistance, QtCore.SIGNAL("valueChanged(int)"), self.horizontalSlider_2.setValue)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL("valueChanged(int)"), self.maximalDistance.setValue)
        QtCore.QObject.connect(self.maximalDistance, QtCore.SIGNAL("valueChanged(int)"), self.horizontalSlider_3.setValue)
        QtCore.QObject.connect(self.horizontalSlider_4, QtCore.SIGNAL("valueChanged(int)"), self.numberDuplicationWidth.setValue)
        QtCore.QObject.connect(self.numberDuplicationWidth, QtCore.SIGNAL("valueChanged(int)"), self.horizontalSlider_4.setValue)
        QtCore.QObject.connect(self.horizontalSlider_5, QtCore.SIGNAL("valueChanged(int)"), self.numberDuplicationWidth_2.setValue)
        QtCore.QObject.connect(self.numberDuplicationWidth_2, QtCore.SIGNAL("valueChanged(int)"), self.horizontalSlider_5.setValue)
        QtCore.QObject.connect(self.horizontalSlider_6, QtCore.SIGNAL("valueChanged(int)"), self.numberCubes.setValue)
        QtCore.QObject.connect(self.numberCubes, QtCore.SIGNAL("valueChanged(int)"), self.horizontalSlider_6.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "Interact Sound", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainForm", "This plugin require the Maya Bonus Tools package. ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainForm", "You can download it here : http://area.autodesk.com/bonustools", None, QtGui.QApplication.UnicodeUTF8))
        self.createAudioSetup.setText(QtGui.QApplication.translate("MainForm", "Create audio wave", None, QtGui.QApplication.UnicodeUTF8))
        self.connectAudio.setText(QtGui.QApplication.translate("MainForm", "Cache Audio Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.setup), QtGui.QApplication.translate("MainForm", "Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainForm", "1. Select faces to extrude", None, QtGui.QApplication.UnicodeUTF8))
        self.memorizeSelection.setText(QtGui.QApplication.translate("MainForm", "2. Memorize selection", None, QtGui.QApplication.UnicodeUTF8))
        self.keepFacesTogether.setText(QtGui.QApplication.translate("MainForm", "Keep faces together", None, QtGui.QApplication.UnicodeUTF8))
        self.extrudeOnSound.setText(QtGui.QApplication.translate("MainForm", "3. Extrude on sound", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.extrude), QtGui.QApplication.translate("MainForm", "Extrude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainForm", "CONSTRAINT ON :", None, QtGui.QApplication.UnicodeUTF8))
        self.aimConstraint.setText(QtGui.QApplication.translate("MainForm", "Aim ", None, QtGui.QApplication.UnicodeUTF8))
        self.xConstraint.setText(QtGui.QApplication.translate("MainForm", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.yConstraint.setText(QtGui.QApplication.translate("MainForm", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.zConstraint.setText(QtGui.QApplication.translate("MainForm", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.rotateConstraint.setText(QtGui.QApplication.translate("MainForm", "Rotate", None, QtGui.QApplication.UnicodeUTF8))
        self.translateConstraint.setText(QtGui.QApplication.translate("MainForm", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleConstraint.setText(QtGui.QApplication.translate("MainForm", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.updateLocator.setText(QtGui.QApplication.translate("MainForm", "Update locator", None, QtGui.QApplication.UnicodeUTF8))
        self.createLocator.setText(QtGui.QApplication.translate("MainForm", "Create locator", None, QtGui.QApplication.UnicodeUTF8))
        self.createLocatorSetup.setText(QtGui.QApplication.translate("MainForm", "Create locator setup", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.locator), QtGui.QApplication.translate("MainForm", "Locator", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainForm", "Random duplicator ", None, QtGui.QApplication.UnicodeUTF8))
        self.instanceDuplicatorRandom.setText(QtGui.QApplication.translate("MainForm", "Instance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainForm", "Number of duplication :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainForm", "Maximal distance :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainForm", "Minimal distance :", None, QtGui.QApplication.UnicodeUTF8))
        self.duplicateRandomly.setText(QtGui.QApplication.translate("MainForm", "Duplicate Randomly", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainForm", "Regular duplicator", None, QtGui.QApplication.UnicodeUTF8))
        self.instanceDuplicatorRegular.setText(QtGui.QApplication.translate("MainForm", "Instance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainForm", "Number of duplication in length  :", None, QtGui.QApplication.UnicodeUTF8))
        self.duplicateRegularly.setText(QtGui.QApplication.translate("MainForm", "Duplicate Regularly", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainForm", "Number of duplication in width  :", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.duplicator), QtGui.QApplication.translate("MainForm", "Duplicator", None, QtGui.QApplication.UnicodeUTF8))
        self.exponential.setText(QtGui.QApplication.translate("MainForm", "Exponential", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainForm", "Number of cubes", None, QtGui.QApplication.UnicodeUTF8))
        self.duplicateAndParent.setText(QtGui.QApplication.translate("MainForm", "Duplicate and parent", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.parentIt), QtGui.QApplication.translate("MainForm", "ParantIt", None, QtGui.QApplication.UnicodeUTF8))
        self.objectsAreInstances.setText(QtGui.QApplication.translate("MainForm", "Check if objects are instances", None, QtGui.QApplication.UnicodeUTF8))
        self.colorize.setText(QtGui.QApplication.translate("MainForm", "Colorize", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.color), QtGui.QApplication.translate("MainForm", "Color", None, QtGui.QApplication.UnicodeUTF8))



#MayaQWidgetDockableMixin under-class
class MyMainWindow(MayaQWidgetDockableMixin, QtGui.QWidget, Ui_MainForm):
    def __init__(self, parent=None):
        #Parent initialize
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Tab.setCurrentIndex(0)

        """SIGNALS CONNEXIONS"""

        #AUDIO SETUP
        self.createAudioSetup.clicked.connect(self.createAudioNode)
        self.connectAudio.clicked.connect(self.cacheAudioNode)

        #EXTRUDE
        self.memorizeSelection.clicked.connect(self.listFaces)
        self.extrudeOnSound.clicked.connect(self.lancerExtrude)

        #LOCATOR
        self.updateLocator.clicked.connect(self.updateLocator_)
        self.createLocator.clicked.connect(self.createLocator_)
        self.createLocatorSetup.clicked.connect(self.lancerSetupLocator)

        #DUPLICATOR
        self.duplicateRandomly.clicked.connect(self.lancerDuplicateArround)
        self.duplicateRegularly.clicked.connect(self.lancerRegularDuplicator)
        
        #PARENT IT
        self.duplicateAndParent.clicked.connect(self.lancerArrayModifier)

        #COLOR
        self.colorize.clicked.connect(self.LancerColorize)
       

    """
    _____________________________________
    PROGRAM
    _____________________________________

    """
    
    #listFace = cmds.ls(selection=True)
    def extrudeListFace(self,keepFacesTogether):
        if len(AudioNodeWave)==0:
            cmds.error( "Please enter an audioWave in memory first" ) 
        else : 
            if len(listFace) == 0 :
                cmds.error( "Please enter faces in memory first" ) 

            else :
                if keepFacesTogether==True :
                    extrusion = cmds.polyExtrudeFacet()
                else :
                    extrusion = cmds.polyExtrudeFacet(kft=False)
                Controller = cmds.circle(n='controllerExtrude')
                cmds.setAttr (Controller[0]+".tx", cb=False)
                cmds.setAttr (Controller[0]+".ty", cb=False)
                cmds.setAttr (Controller[0]+".tz", cb=False)
                cmds.setAttr (Controller[0]+".rx", cb=False)
                cmds.setAttr (Controller[0]+".ry", cb=False)
                cmds.setAttr (Controller[0]+".rz", cb=False)
                cmds.addAttr(Controller[0], ln = "MinExtrude", at="float", dv=-0.5)
                cmds.setAttr(Controller[0]+".MinExtrude", k=True, e=True)
                cmds.addAttr(Controller[0], ln = "MaxExtrude", at="float", dv=10.0)
                cmds.setAttr(Controller[0]+".MaxExtrude", k=True, e=True)

                cmds.connectAttr( Controller[0]+".translateX" , extrusion[0]+".thickness")
                SetRange = cmds.createNode( 'setRange', n='setRange' )
                cmds.setAttr( SetRange+".oldMinX", 0)
                cmds.setAttr( SetRange+".oldMaxX", 1)

                cmds.connectAttr( Controller[0]+".MinExtrude",  SetRange+".minX")
                cmds.connectAttr( Controller[0]+".MaxExtrude",  SetRange+".maxX")
                cmds.connectAttr( SetRange+".outValue.outValueX",  Controller[0]+".translateX" )

                cmds.connectAttr( AudioNodeWave+".output", SetRange+".valueX" )
    
    def cacheAudioNode(self):
        global AudioNodeWave
        tmp = cmds.ls(selection=True, showType=True)
        if tmp[1] == "audioWave":
            AudioNodeWave = tmp[0]
            return AudioNodeWave
        else :
            cmds.error("Please select audioWave Node")
    
    def createAudioNode(self):
        global AudioNodeWave
        AudioNodeWave=cmds.createNode("audioWave", n='audioNodeWave')
        AudioNode = cmds.createNode("audio", n="audioNode")
        cmds.connectAttr(AudioNode+".filename", AudioNodeWave+".audio")
        cmds.connectAttr( "time1.outTime", AudioNodeWave+".input") 
        return AudioNodeWave
    
    def listFaces(self):
        global listFace
        tmp= cmds.ls(selection=True, showType=True)
        if tmp[1]=='float3':
            listFace = cmds.ls(selection=True)
            return listFace
        else : 
            cmds.error("Please select only faces")
    
    def lancerExtrude(self):
        #keepFacesTogether = cmds.checkBox("kft", query = True, value= True)
        #extrudeListFace(keepFacesTogether)
        self.extrudeListFace(self.keepFacesTogether.isChecked())
    
    def updateLocator_(self):
        global Locator 
        Locator = cmds.ls(selection=True)
    
    def createLocator_(self):
        global Locator 
        Locator = cmds.spaceLocator( p=(0, 0, 0) )

        cmds.addAttr(Locator, ln = "min", at="float", dv=1.0)
        cmds.setAttr(Locator[0]+".min", k=True, e=True)
        cmds.addAttr(Locator, ln = "max", at="float", dv=10.0)
        cmds.setAttr(Locator[0]+".max", k=True, e=True)
        cmds.addAttr(Locator, ln = "distance_max", at="float", dv=40.0)
        cmds.setAttr(Locator[0]+".distance_max", k=True, e=True)
    
    def setupLocator(self,AimConstraint, xC, yC, zC, r, s, t):
        Objects = cmds.ls( selection=True)   

        gMainProgressBar = mel.eval('$tmp = $gMainProgressBar');

        cmds.progressBar( gMainProgressBar,
                                    edit=True,
                                    beginProgress=True,
                                    isInterruptable=True,
                                    status='"Example Calculation ...',
                                    maxValue=len(Objects) )

        for i in range ( len(Objects) ):
            
            Distance = cmds.createNode( 'distanceBetween', n='Distance' )
            
            cmds.connectAttr( Locator[0]+".translate" , Distance+'.point1')
            cmds.connectAttr( Objects[i]+".translate" , Distance+'.point2')
            
            SetRange = cmds.createNode( 'setRange', n='setRange' )
            cmds.connectAttr( Locator[0]+".distance_max",  SetRange+".oldMaxX")
            cmds.connectAttr( Locator[0]+".min",  SetRange+".maxX")
            cmds.connectAttr( Locator[0]+".max",  SetRange+".minX")
            cmds.connectAttr(Distance+".distance" , SetRange+".valueX" )
            
            if(r):
                if (yC) :
                    cmds.connectAttr( SetRange+".outValue.outValueX" , Objects[i]+".rotate.rotateY")
                if (xC) :
                    cmds.connectAttr( SetRange+".outValue.outValueX" , Objects[i]+".rotate.rotateX")
                if (zC) :
                    cmds.connectAttr( SetRange+".outValue.outValueX" , Objects[i]+".rotate.rotateZ")
            if(s):
                if (yC) :
                    cmds.connectAttr( SetRange+".outValue.outValueX" , Objects[i]+".scale.scaleY")
                if (xC) :
                    cmds.connectAttr( SetRange+".outValue.outValueX" , Objects[i]+".scale.scaleX")
                if (zC) :
                    cmds.connectAttr( SetRange+".outValue.outValueX" , Objects[i]+".scale.scaleZ")
            if(t):
                if (yC) :
                    cmds.connectAttr( SetRange+".outValue.outValueX" , Objects[i]+".translate.translateY")
                if (xC) :
                    cmds.connectAttr( SetRange+".outValue.outValueX" , Objects[i]+".translate.translateX")
                if (zC) :
                    cmds.connectAttr( SetRange+".outValue.outValueX" , Objects[i]+".translate.translateZ")
            
            #cmds.connectAttr( Distance+".distance" , Objects[i]+".translate.translateY")
            if (AimConstraint==True):
                cmds.select(Locator, Objects[i])
                cmds.aimConstraint()
            cmds.parent(Objects[i], groupe)
            if cmds.progressBar(gMainProgressBar, query=True, isCancelled=True ) :
                break
            cmds.progressBar(gMainProgressBar, edit=True, step=1)
        cmds.progressBar(gMainProgressBar, edit=True, endProgress=True)
    
    def ArrayModifier(self,exponentiel, nbCube):
        cubes = []
        cubesShape = []
        selection = cmds.ls(selection=True)
        print len(selection)
        gMainProgressBar = mel.eval('$tmp = $gMainProgressBar');
        cmds.progressBar( gMainProgressBar,
                                    edit=True,
                                    beginProgress=True,
                                    isInterruptable=True,
                                    status='"Example Calculation ...',
                                    maxValue=nbCube)
        for i in range (nbCube):
            cube = cmds.instance(selection)
            cubes.append( cube[0])
            cubesShape.append( cmds.listRelatives(cube, children=True))
            cmds.progressBar(gMainProgressBar, edit=True, step=1)
        cmds.progressBar(gMainProgressBar, edit=True, endProgress=True) 

        Controller = cmds.circle(n='controllerExtrude')
        cmds.setAttr (Controller[0]+".tx", cb=False)
        cmds.setAttr (Controller[0]+".ty", cb=False)
        cmds.setAttr (Controller[0]+".tz", cb=False)
        cmds.setAttr (Controller[0]+".rx", cb=False)
        cmds.setAttr (Controller[0]+".ry", cb=False)
        cmds.setAttr (Controller[0]+".rz", cb=False)
        cmds.addAttr(Controller[0], ln = "RotationX", at="float", dv=0.0)
        cmds.setAttr(Controller[0]+".RotationX", k=True, e=True)
        cmds.addAttr(Controller[0], ln = "RotationY", at="float", dv=0.0)
        cmds.setAttr(Controller[0]+".RotationY", k=True, e=True)
        cmds.addAttr(Controller[0], ln = "RotationZ", at="float", dv=0.0)
        cmds.setAttr(Controller[0]+".RotationZ", k=True, e=True)
        cmds.addAttr(Controller[0], ln = "TranslationX", at="float", dv=0.0)
        cmds.setAttr(Controller[0]+".TranslationX", k=True, e=True)
        cmds.addAttr(Controller[0], ln = "TranslationY", at="float", dv=0.0)
        cmds.setAttr(Controller[0]+".TranslationY", k=True, e=True)
        cmds.addAttr(Controller[0], ln = "TranslationZ", at="float", dv=0.0)
        cmds.setAttr(Controller[0]+".TranslationZ", k=True, e=True)
        cmds.addAttr(Controller[0], ln = "echelleX", at="float", dv=1.0)
        cmds.setAttr(Controller[0]+".echelleX", k=True, e=True)
        cmds.addAttr(Controller[0], ln = "echelleY", at="float", dv=1.0)
        cmds.setAttr(Controller[0]+".echelleY", k=True, e=True)
        cmds.addAttr(Controller[0], ln = "echelleZ", at="float", dv=1.0)
        cmds.setAttr(Controller[0]+".echelleZ", k=True, e=True)
        
        cmds.progressBar( gMainProgressBar,
                                    edit=True,
                                    beginProgress=True,
                                    isInterruptable=True,
                                    status='"Example Calculation ...',
                                    maxValue=len(cubes) )
        for i in range (len(cubes)):
            if i==0:
                #rotate
                cmds.addAttr(cubes[i], ln = "RotationXcontroller", at="float", dv=0.0)
                cmds.setAttr(cubes[i]+".RotationXcontroller", k=True, e=True)
                cmds.addAttr(cubes[i], ln = "RotationYcontroller", at="float", dv=0.0)
                cmds.setAttr(cubes[i]+".RotationYcontroller", k=True, e=True)
                cmds.addAttr(cubes[i], ln = "RotationZcontroller", at="float", dv=0.0)
                cmds.setAttr(cubes[i]+".RotationZcontroller", k=True, e=True)
                cmds.connectAttr( Controller[0]+".RotationX",  cubes[i]+".RotationXcontroller")
                cmds.connectAttr( Controller[0]+".RotationY",  cubes[i]+".RotationYcontroller")
                cmds.connectAttr( Controller[0]+".RotationZ",  cubes[i]+".RotationZcontroller")
                cmds.expression(o=cubes[i], s=""" 
                rotateX = RotationXcontroller;
                rotateY = RotationYcontroller;
                rotateZ = RotationZcontroller;
                """)
        
                #translate
                cmds.addAttr(cubes[i], ln = "TranslationXcontroller", at="float", dv=0.0)
                cmds.setAttr(cubes[i]+".TranslationXcontroller", k=True, e=True)
                cmds.addAttr(cubes[i], ln = "TranslationYcontroller", at="float", dv=0.0)
                cmds.setAttr(cubes[i]+".TranslationYcontroller", k=True, e=True)
                cmds.addAttr(cubes[i], ln = "TranslationZcontroller", at="float", dv=0.0)
                cmds.setAttr(cubes[i]+".TranslationZcontroller", k=True, e=True)
                cmds.connectAttr( Controller[0]+".TranslationX",  cubes[i]+".TranslationXcontroller")
                cmds.connectAttr( Controller[0]+".TranslationY",  cubes[i]+".TranslationYcontroller")
                cmds.connectAttr( Controller[0]+".TranslationZ",  cubes[i]+".TranslationZcontroller")
                cmds.expression(o=cubes[i], s=""" 
                translateX = TranslationXcontroller;
                translateY = TranslationYcontroller;
                translateZ = TranslationZcontroller;
                """)
        
                cmds.addAttr(cubes[i], ln = "echelleXcontroller", at="float", dv=0.0)
                cmds.setAttr(cubes[i]+".echelleXcontroller", k=True, e=True)
                cmds.addAttr(cubes[i], ln = "echelleYcontroller", at="float", dv=0.0)
                cmds.setAttr(cubes[i]+".echelleYcontroller", k=True, e=True)
                cmds.addAttr(cubes[i], ln = "echelleZcontroller", at="float", dv=0.0)
                cmds.setAttr(cubes[i]+".echelleZcontroller", k=True, e=True)
                cmds.connectAttr( Controller[0]+".echelleX",  cubes[i]+".echelleXcontroller")
                cmds.connectAttr( Controller[0]+".echelleY",  cubes[i]+".echelleYcontroller")
                cmds.connectAttr( Controller[0]+".echelleZ",  cubes[i]+".echelleZcontroller")
                cmds.expression(o=cubes[i], s=""" 
                scaleX =echelleXcontroller;
                scaleY = echelleYcontroller;
                scaleZ = echelleZcontroller;
                """)
            elif i>0 :

                cmds.parent(cubes[i], cubes[i-1])
                if (exponentiel==True):
                    """plusMinusAverage = cmds.createNode( 'plusMinusAverage', n='plusMinusAverage' )
                    
                    cmds.connectAttr( cubes[i-1]+".translate",  plusMinusAverage+".input3D[0]")
                    cmds.connectAttr( cubes[i]+".translate",  plusMinusAverage+".input3D[1]")
                    cmds.setAttr(plusMinusAverage+".operation", 2)
                    cmds.connectAttr( plusMinusAverage+".output3D",  cubes[i]+".rotatePivot")
                    cmds.connectAttr( plusMinusAverage+".output3D",  cubes[i]+".scalePivot")
                    """
                    cmds.addAttr(cubes[i], ln = "RotationXparent", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".RotationXparent", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "RotationYparent", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".RotationYparent", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "RotationZparent", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".RotationZparent", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "RotationXcontroller", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".RotationXcontroller", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "RotationYcontroller", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".RotationYcontroller", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "RotationZcontroller", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".RotationZcontroller", k=True, e=True)
                    cmds.connectAttr( cubes[i-1]+".rotateX",  cubes[i]+".RotationXparent")
                    cmds.connectAttr( cubes[i-1]+".rotateY",  cubes[i]+".RotationYparent")
                    cmds.connectAttr( cubes[i-1]+".rotateZ",  cubes[i]+".RotationZparent")
                    cmds.connectAttr( Controller[0]+".RotationX",  cubes[i]+".RotationXcontroller")
                    cmds.connectAttr( Controller[0]+".RotationY",  cubes[i]+".RotationYcontroller")
                    cmds.connectAttr( Controller[0]+".RotationZ",  cubes[i]+".RotationZcontroller")
                    cmds.expression(o=cubes[i], s=""" 
                    rotateX = RotationXparent + RotationXcontroller;
                    rotateY = RotationYparent + RotationYcontroller;
                    rotateZ = RotationZparent + RotationZcontroller;
                    """)
            
                    #control translat
                    cmds.addAttr(cubes[i], ln = "TranslationXparent", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".TranslationXparent", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "TranslationYparent", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".TranslationYparent", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "TranslationZparent", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".TranslationZparent", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "TranslationXcontroller", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".TranslationXcontroller", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "TranslationYcontroller", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".TranslationYcontroller", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "TranslationZcontroller", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".TranslationZcontroller", k=True, e=True)
                    cmds.connectAttr( cubes[i-1]+".translateX",  cubes[i]+".TranslationXparent")
                    cmds.connectAttr( cubes[i-1]+".translateY",  cubes[i]+".TranslationYparent")
                    cmds.connectAttr( cubes[i-1]+".translateZ",  cubes[i]+".TranslationZparent")
                    cmds.connectAttr( Controller[0]+".TranslationX",  cubes[i]+".TranslationXcontroller")
                    cmds.connectAttr( Controller[0]+".TranslationY",  cubes[i]+".TranslationYcontroller")
                    cmds.connectAttr( Controller[0]+".TranslationZ",  cubes[i]+".TranslationZcontroller")
                    cmds.expression(o=cubes[i], s=""" 
                    translateX = TranslationXparent + TranslationXcontroller;
                    translateY = TranslationYparent + TranslationYcontroller;
                    translateZ = TranslationZparent + TranslationZcontroller;
                    """)
            
                    #control scale
                    cmds.addAttr(cubes[i], ln = "echelleXparent", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".echelleXparent", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "echelleYparent", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".echelleYparent", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "echelleZparent", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".echelleZparent", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "echelleXcontroller", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".echelleXcontroller", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "echelleYcontroller", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".echelleYcontroller", k=True, e=True)
                    cmds.addAttr(cubes[i], ln = "echelleZcontroller", at="float", dv=0.0)
                    cmds.setAttr(cubes[i]+".echelleZcontroller", k=True, e=True)
                    cmds.connectAttr( cubes[i-1]+".scaleX",  cubes[i]+".echelleXparent")
                    cmds.connectAttr( cubes[i-1]+".scaleY",  cubes[i]+".echelleYparent")
                    cmds.connectAttr( cubes[i-1]+".scaleZ",  cubes[i]+".echelleZparent")
                    cmds.connectAttr( Controller[0]+".echelleX",  cubes[i]+".echelleXcontroller")
                    cmds.connectAttr( Controller[0]+".echelleY",  cubes[i]+".echelleYcontroller")
                    cmds.connectAttr( Controller[0]+".echelleZ",  cubes[i]+".echelleZcontroller")
                    cmds.expression(o=cubes[i], s=""" 
                    scaleX = echelleXparent * echelleXcontroller;
                    scaleY = echelleYparent * echelleYcontroller;
                    scaleZ = echelleZparent * echelleZcontroller;
                    """)
                else :
                    cmds.connectAttr( Controller[0]+".TranslationX",  cubes[i]+".translateX")
                    cmds.connectAttr( Controller[0]+".TranslationY",  cubes[i]+".translateY")
                    cmds.connectAttr( Controller[0]+".TranslationZ",  cubes[i]+".translateZ")
                    cmds.connectAttr( Controller[0]+".RotationX",  cubes[i]+".rotateX")
                    cmds.connectAttr( Controller[0]+".RotationY",  cubes[i]+".rotateY")
                    cmds.connectAttr( Controller[0]+".RotationZ",  cubes[i]+".rotateZ")
                    cmds.connectAttr( Controller[0]+".echelleX",  cubes[i]+".scaleX")
                    cmds.connectAttr( Controller[0]+".echelleY",  cubes[i]+".scaleY")
                    cmds.connectAttr( Controller[0]+".echelleZ",  cubes[i]+".scaleZ")
                """
        
            cmds.connectAttr( Controller[0]+".TranslationX",  cubes[i]+".translateX")
            cmds.connectAttr( Controller[0]+".TranslationY",  cubes[i]+".translateY")
            cmds.connectAttr( Controller[0]+".TranslationZ",  cubes[i]+".translateZ")
            cmds.connectAttr( Controller[0]+".echelleX",  cubes[i]+".scaleX")
            cmds.connectAttr( Controller[0]+".echelleY",  cubes[i]+".scaleY")
            cmds.connectAttr( Controller[0]+".echelleZ",  cubes[i]+".scaleZ")
            """
            cmds.progressBar(gMainProgressBar, edit=True, step=1)
        cmds.progressBar(gMainProgressBar, edit=True, endProgress=True) 

    def lancerArrayModifier(self):
        self.ArrayModifier(self.exponential.isChecked(),self.numberCubes.value())

    def CreerCouleurAleatoireObjetSelect(self,instanceOrNot):
        cubes = cmds.ls(selection=True, fl=True)
        gMainProgressBar = mel.eval('$tmp = $gMainProgressBar');
        cmds.progressBar( gMainProgressBar,
                                    edit=True,
                                    beginProgress=True,
                                    isInterruptable=True,
                                    status='"Example Calculation ...',
                                    maxValue=len(cubes) )
        Controller = cmds.circle(n='colorControl')
        cmds.addAttr(Controller[0], ln = "R", at="float", dv=random.uniform(0,1), minValue=0, maxValue=1)
        cmds.setAttr(Controller[0]+".R", k=True, e=True)
        cmds.addAttr(Controller[0], ln = "V", at="float", dv=random.uniform(0,1), minValue=0, maxValue=1)
        cmds.setAttr(Controller[0]+".V", k=True, e=True)
        cmds.addAttr(Controller[0], ln = "B", at="float", dv=random.uniform(0,1), minValue=0, maxValue=1)
        cmds.setAttr(Controller[0]+".B", k=True, e=True)

        cmds.addAttr(Controller[0], ln = "randomColor", at="float", dv=random.uniform(0,1), minValue=0, maxValue=1)
        cmds.setAttr(Controller[0]+".randomColor", k=True, e=True)
        shader = cmds.shadingNode("lambert",asShader=True, n="lamber_randomColor")
        tripleShading = cmds.createNode( 'tripleShadingSwitch', n='tripleShading' )
        cmds.connectAttr(tripleShading+".output", shader+".color")
        for i in range(len(cubes)):
            
            cmds.addAttr(cubes[i], ln = "multR", at="float", dv=random.uniform(0,1))
            cmds.setAttr(cubes[i]+".multR", k=True, e=True)
            cmds.addAttr(cubes[i], ln = "multV", at="float", dv=random.uniform(0,1))
            cmds.setAttr(cubes[i]+".multV", k=True, e=True)
            cmds.addAttr(cubes[i], ln = "multB", at="float", dv=random.uniform(0,1))
            cmds.setAttr(cubes[i]+".multB", k=True, e=True)
            shape = cmds.listRelatives(cubes[i], children=True)    
            if (instanceOrNot):
                cmds.connectAttr(  shape[0]+".instObjGroups["+str(i)+"]", tripleShading+".input["+str(i)+"].inShape")
            else :
                cmds.connectAttr(  shape[0]+".instObjGroups[0]", tripleShading+".input["+str(i)+"].inShape")
            
            cmds.addAttr(cubes[i], ln = "R", at="float", dv=random.uniform(0,1), minValue=0, maxValue=1)
            cmds.setAttr(cubes[i]+".R", k=True, e=True)
            cmds.addAttr(cubes[i], ln = "V", at="float", dv=random.uniform(0,1), minValue=0, maxValue=1)
            cmds.setAttr(cubes[i]+".V", k=True, e=True)
            cmds.addAttr(cubes[i], ln = "B", at="float", dv=random.uniform(0,1), minValue=0, maxValue=1)
            cmds.setAttr(cubes[i]+".B", k=True, e=True)
            
            stringExpression="""
            R = ("""+Controller[0]+""".randomColor * multR + """+Controller[0]+""".R )*0.5;
            V = ("""+Controller[0]+""".randomColor * multV + """+Controller[0]+""".V )*0.5;
            B = ("""+Controller[0]+""".randomColor * multB + """+Controller[0]+""".B )*0.5;
            """ 
            cmds.expression(o=cubes[i], s=stringExpression)  

            cmds.connectAttr( cubes[i]+".R", tripleShading+".input["+str(i)+"].inComp1")
            cmds.connectAttr(cubes[i]+".V",  tripleShading+".input["+str(i)+"].inComp2")
            cmds.connectAttr( cubes[i]+".B", tripleShading+".input["+str(i)+"].inComp3")
            
            cmds.select(cubes[i])
            cmds.hyperShade( assign=shader )
            
            if cmds.progressBar(gMainProgressBar, query=True, isCancelled=True ) :
                break
            cmds.progressBar(gMainProgressBar, edit=True, step=1)
        cmds.progressBar(gMainProgressBar, edit=True, endProgress=True) 

    def LancerColorize(self):
        self.CreerCouleurAleatoireObjetSelect(self.objectsAreInstances.isChecked())

    def regularDuplicator(self,nbCubeLarge, nbCubeLongueur, instanceOrNot):
        cubes = []
        selection = cmds.ls(selection=True)
        groupe = cmds.group(em=True, n="groupRegularDupli")

        gMainProgressBar = mel.eval('$tmp = $gMainProgressBar');
        cmds.progressBar( gMainProgressBar,
                                    edit=True,
                                    beginProgress=True,
                                    isInterruptable=True,
                                    status='"Example Calculation ...',
                                    maxValue=nbCubeLongueur )
        for i in range (nbCubeLarge):
            try : 
                if (instanceOrNot) : 
                    cube = cmds.instance(selection)
                else : 
                    cube = cmds.duplicate(selection)
                cmds.move(i+i*0.1,0,0,cube[0])
                cubes.append( cube[0])
                cmds.parent(cube[0], groupe)
                for j in range(nbCubeLongueur):
                    if (instanceOrNot) : 
                        cube = cmds.instance(selection)
                    else : 
                        cube = cmds.duplicate(selection)
                    cmds.move(i+i*0.1, 0, j+j*0.1, cube[0])
                    cubes.append( cube[0])
                    cmds.parent(cube[0], groupe)
                    cmds.progressBar(gMainProgressBar, edit=True, step=1)
            except:
                cmds.progressBar(gMainProgressBar, edit=True, endProgress=True)
        cmds.progressBar(gMainProgressBar, edit=True, endProgress=True)
    #regularDuplicator(10,10, False)

    def duplicateArround(self,number, randomSeed, min, max ,instanceOrNot):
        random.seed(randomSeed)
        object = cmds.ls(selection=True)
        try : 
            transformName="groupe"
            instanceGroup=cmds.group(empty=True,name=transformName+'_instance_grp#')
            
            gMainProgressBar = mel.eval('$tmp = $gMainProgressBar');

            cmds.progressBar( gMainProgressBar,
                                        edit=True,
                                        beginProgress=True,
                                        isInterruptable=True,
                                        status='"Example Calculation ...',
                                        maxValue=number )
            for i in range(0,number):
                if (instanceOrNot):
                    objectInstance= cmds.instance(object)
                else:
                    objectInstance= cmds.duplicate(object)
                cmds.parent(objectInstance,instanceGroup)   
                
                mx=random.uniform(min,max)
                my=random.uniform(min,max)
                mz=random.uniform(min,max)
                
                rx=random.uniform(0,360)
                ry=random.uniform(0,360)
                rz=random.uniform(0,360)
                
                sx=random.uniform(0.2,1)
                sy=random.uniform(0.2,1)
                sz=random.uniform(0.2,1)
                
                cmds.move(mx,my,mz,objectInstance)
                cmds.rotate(rx,ry,rz,objectInstance)
                cmds.scale(sx,sy,sz,objectInstance)
                cmds.progressBar(gMainProgressBar, edit=True, step=1)
            cmds.progressBar(gMainProgressBar, edit=True, endProgress=True)
        except : 
            cmds.progressBar(gMainProgressBar, edit=True, endProgress=True)          
   
    def lancerSetupLocator(self):
        """
        AimContraint = cmds.checkBox("aimContraint", query = True, value=True)
        xC = cmds.checkBox("xC", query = True, value=True)
        yC = cmds.checkBox("yC", query = True, value=True)
        zC = cmds.checkBox("zC", query = True, value=True)
        r = cmds.checkBox("r", query = True, value=True)
        s = cmds.checkBox("s", query = True, value=True)
        t = cmds.checkBox("t", query = True, value=True)
        """
        self.setupLocator(self.aimConstraint.isChecked(),self.xConstraint.isChecked(), self.yConstraint.isChecked(), self.zConstraint.isChecked(), self.rotateConstraint.isChecked(), self.scaleConstraint.isChecked(), self.translateConstraint.isChecked())

    def lancerDuplicateArround(self):
        """
        NombreDuplicate = cmds.intSliderGrp("NombreDuplicate", query = True, value= True)
        MinDuplicate = cmds.intSliderGrp("MinDuplicate", query = True, value= True)    
        MaxDuplicate = cmds.intSliderGrp("MaxDuplicate", query = True, value= True)
        """
        self.duplicateArround(self.numberDuplicationRandom.value(), 1500, self.minimalDistance.value(), self.maximalDistance.value(), self.instanceDuplicatorRandom.isChecked())

    def lancerRegularDuplicator(self):
        self.regularDuplicator(self.numberDuplicationWidth.value(),self.numberDuplicationWidth_2.value(),self.instanceDuplicatorRegular.isChecked() )
    

    """ ______________________________________________
        
        #MAYA INTERFACE
        ______________________________________________

        def creerWindow():
        #creation de la fenetre en tab layout 
        cmds.window(title="NokeyBeat", width=560, backgroundColor=[0.133,0.168,0.211] )
        cmds.columnLayout()

        cmds.text( label='nokeybeat', align='center', height=60, width=560)

        cmds.setParent('..')
        form = cmds.formLayout()
        tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)), backgroundColor=[0.133,0.168,0.211] )

        child1 = cmds.rowColumnLayout(numberOfColumns=1)
        cmds.text( label='selectionnez des faces', align='center', height=60 )
        cmds.button(label="rentrer la selection de faces en mémoire", command="listFace = listFaces()",backgroundColor=[0.137, 0.67, 0.86])
        cmds.checkBox("kft", label="keep faces together", value = True)
        cmds.button( label="creer des extrusions sur le son", command="lancerExtrude()",backgroundColor=[0.137, 0.67, 0.86])

        cmds.setParent( '..' )

        child2 = cmds.rowColumnLayout(numberOfColumns=3)

        cmds.checkBox("r", label="rotate ?", value = True)
        cmds.checkBox("s", label="Scale ?", value = True)
        cmds.checkBox("t", label="Translate ?", value = True)
        cmds.checkBox("xC", label="x ? ", value = True)
        cmds.checkBox("yC", label="y ?", value = True)
        cmds.checkBox("zC", label="z ?", value = True)


        cmds.checkBox("aimContraint", label="Aim contraint ?", value = True)
        cmds.button( label="update locator", command="updateLocator()",backgroundColor=[0.137, 0.67, 0.86])
        cmds.button( label="creer  locator", command="createLocator()",backgroundColor=[0.137, 0.67, 0.86])
        cmds.button( label="Creer le setup locator", command="lancerSetupLocator()",backgroundColor=[0.137, 0.67, 0.86])
        cmds.setParent( '..' )

        child3 = cmds.rowColumnLayout(numberOfColumns=1)
        cmds.intSliderGrp("NombreDuplicate", label="Nombre d'instances : ", value = 0.0, field = True, min=0, max=1000)
        cmds.intSliderGrp("MinDuplicate", label="Min : ", value = 0.0, field = True, min=-100, max=100)
        cmds.intSliderGrp("MaxDuplicate", label="Max : ", value = 0.0, field = True, min=-100, max=100)
        cmds.button( label="Dupliquer autour", command="lancerDuplicateArround()",backgroundColor=[0.137, 0.67, 0.86])
        cmds.button( label="regularDupli10x10", command="regularDuplicator(10,10, False)", backgroundColor=[0.137, 0.67, 0.86])
        cmds.setParent( '..' )


        child4 = cmds.rowColumnLayout(numberOfColumns=1)
        cmds.button( label="créer le setup d'audio", command="AudioNodeWave =createAudioNode()",backgroundColor=[0.137, 0.67, 0.86])
        cmds.button( label="rentrer le node audioWave en mémoire", command="AudioNodeWave=cacheAudioNode()", backgroundColor=[0.137, 0.67, 0.86])
        cmds.setParent( '..' )

        child5 = cmds.rowColumnLayout(numberOfColumns=1)
        cmds.button( label="color instance", command="CreerCouleurAleatoireObjetSelect(True)",backgroundColor=[0.137, 0.67, 0.86])
        cmds.button( label="color no instance", command="CreerCouleurAleatoireObjetSelect(False)", backgroundColor=[0.137, 0.67, 0.86])
        cmds.button( label="arraymodifier", command="ArrayModifier(False, 10)", backgroundColor=[0.137, 0.67, 0.86])
        cmds.button( label="arraymodifier exp", command="ArrayModifier(True, 10)", backgroundColor=[0.137, 0.67, 0.86])
        cmds.setParent( '..' )

        cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'Extrusion sur le son'), (child2, 'setup locator'), (child3, "duplicator"), (child4, "Setup sonore"), (child5, "Setup color")  ) ) 
        cmds.setParent( '..')

        cmds.showWindow()
    #ArrayModifier(False, 20)
    creerWindow()
    """

if __name__ == "__main__":
    #Parent widget to maya interface
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow= shiboken.wrapInstance(long(mayaMainWindowPtr), QtGui.QWidget)
    #Widget instance
    myapp = MyMainWindow(parent=mayaMainWindow)
    myapp.show(dockable=True)