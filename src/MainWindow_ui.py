# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sun Feb 24 09:11:30 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frm_MainWindow(object):
    def setupUi(self, frm_MainWindow):
        frm_MainWindow.setObjectName(_fromUtf8("frm_MainWindow"))
        frm_MainWindow.resize(402, 652)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/IMG/img/WeCase.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(frm_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_weibo = QtGui.QWidget()
        self.tab_weibo.setObjectName(_fromUtf8("tab_weibo"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_weibo)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.listView = QtGui.QListView(self.tab_weibo)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout_3.addWidget(self.listView)
        self.tabWidget.addTab(self.tab_weibo, _fromUtf8(""))
        self.tab_atme = QtGui.QWidget()
        self.tab_atme.setObjectName(_fromUtf8("tab_atme"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_atme)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.listView_2 = QtGui.QListView(self.tab_atme)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.verticalLayout_2.addWidget(self.listView_2)
        self.tabWidget.addTab(self.tab_atme, _fromUtf8(""))
        self.tab_comment = QtGui.QWidget()
        self.tab_comment.setObjectName(_fromUtf8("tab_comment"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_comment)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.listView_3 = QtGui.QListView(self.tab_comment)
        self.listView_3.setObjectName(_fromUtf8("listView_3"))
        self.verticalLayout_4.addWidget(self.listView_3)
        self.tabWidget.addTab(self.tab_comment, _fromUtf8(""))
        self.tab_my = QtGui.QWidget()
        self.tab_my.setObjectName(_fromUtf8("tab_my"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_my)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.listView_4 = QtGui.QListView(self.tab_my)
        self.listView_4.setObjectName(_fromUtf8("listView_4"))
        self.verticalLayout_6.addWidget(self.listView_4)
        self.tabWidget.addTab(self.tab_my, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 30))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_me = QtGui.QPushButton(self.widget)
        self.pushButton_me.setObjectName(_fromUtf8("pushButton_me"))
        self.gridLayout.addWidget(self.pushButton_me, 0, 2, 1, 1)
        self.pushButton_refresh = QtGui.QPushButton(self.widget)
        self.pushButton_refresh.setObjectName(_fromUtf8("pushButton_refresh"))
        self.gridLayout.addWidget(self.pushButton_refresh, 0, 0, 1, 1)
        self.pushButton_new = QtGui.QPushButton(self.widget)
        self.pushButton_new.setObjectName(_fromUtf8("pushButton_new"))
        self.gridLayout.addWidget(self.pushButton_new, 0, 1, 1, 1)
        self.pushButton_settings = QtGui.QPushButton(self.widget)
        self.pushButton_settings.setObjectName(_fromUtf8("pushButton_settings"))
        self.gridLayout.addWidget(self.pushButton_settings, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        frm_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(frm_MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMinimumSize(QtCore.QSize(0, 0))
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_WeCase = QtGui.QMenu(self.menubar)
        self.menu_WeCase.setObjectName(_fromUtf8("menu_WeCase"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuO_ptions = QtGui.QMenu(self.menubar)
        self.menuO_ptions.setObjectName(_fromUtf8("menuO_ptions"))
        frm_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(frm_MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        frm_MainWindow.setStatusBar(self.statusbar)
        self.action_About = QtGui.QAction(frm_MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/IMG/img/where_s_my_weibo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_About.setIcon(icon1)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.action_Refresh = QtGui.QAction(frm_MainWindow)
        self.action_Refresh.setObjectName(_fromUtf8("action_Refresh"))
        self.action_Log_out = QtGui.QAction(frm_MainWindow)
        self.action_Log_out.setObjectName(_fromUtf8("action_Log_out"))
        self.action_Exit = QtGui.QAction(frm_MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/IMG/img/application-exit.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon2)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.action_Settings = QtGui.QAction(frm_MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/IMG/img/preferences-other.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Settings.setIcon(icon3)
        self.action_Settings.setObjectName(_fromUtf8("action_Settings"))
        self.actionUpdate = QtGui.QAction(frm_MainWindow)
        self.actionUpdate.setObjectName(_fromUtf8("actionUpdate"))
        self.menu_WeCase.addAction(self.action_Refresh)
        self.menu_WeCase.addSeparator()
        self.menu_WeCase.addAction(self.action_Log_out)
        self.menu_WeCase.addAction(self.action_Exit)
        self.menuHelp.addAction(self.action_About)
        self.menuO_ptions.addAction(self.action_Settings)
        self.menuO_ptions.addAction(self.actionUpdate)
        self.menubar.addAction(self.menu_WeCase.menuAction())
        self.menubar.addAction(self.menuO_ptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(frm_MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frm_MainWindow)

    def retranslateUi(self, frm_MainWindow):
        frm_MainWindow.setWindowTitle(QtGui.QApplication.translate("frm_MainWindow", "WeCase", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_weibo), QtGui.QApplication.translate("frm_MainWindow", "微博", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_atme), QtGui.QApplication.translate("frm_MainWindow", "@我", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_comment), QtGui.QApplication.translate("frm_MainWindow", "评论", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_my), QtGui.QApplication.translate("frm_MainWindow", "我的", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_me.setText(QtGui.QApplication.translate("frm_MainWindow", "Me", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_refresh.setText(QtGui.QApplication.translate("frm_MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new.setText(QtGui.QApplication.translate("frm_MainWindow", "New Weibo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_settings.setText(QtGui.QApplication.translate("frm_MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_WeCase.setTitle(QtGui.QApplication.translate("frm_MainWindow", "&WeCase", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("frm_MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuO_ptions.setTitle(QtGui.QApplication.translate("frm_MainWindow", "&Options", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("frm_MainWindow", "&About...", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Refresh.setText(QtGui.QApplication.translate("frm_MainWindow", "&Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Log_out.setText(QtGui.QApplication.translate("frm_MainWindow", "&Log out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("frm_MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Settings.setText(QtGui.QApplication.translate("frm_MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setText(QtGui.QApplication.translate("frm_MainWindow", "&Update", None, QtGui.QApplication.UnicodeUTF8))

import wecase_rc
