from PyQt4 import QtCore, QtGui
import sys
import os
import codecs
import subprocess

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_editor_adv.ui'
#
# Created: Sun Mar 13 20:20:04 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!
import webbrowser

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(801, 600)
        self.tabList = []

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(-1, -1, 811, 571))
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.horizontalWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_2.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuText = QtGui.QMenu(self.menubar)
        self.menuText.setObjectName(_fromUtf8("menuText"))
        self.menuDocument = QtGui.QMenu(self.menubar)
        self.menuDocument.setObjectName(_fromUtf8("menuDocument"))
        self.menuNavigation = QtGui.QMenu(self.menubar)
        self.menuNavigation.setObjectName(_fromUtf8("menuNavigation"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionNew_Windows = QtGui.QAction(MainWindow)
        self.actionNew_Windows.setObjectName(_fromUtf8("actionNew_Windows"))

        # open new window
        self.actionNew_Window = QtGui.QAction(MainWindow)
        self.actionNew_Window.setObjectName(_fromUtf8("actionNew_Window"))
        self.actionNew_Window.setShortcut("Shift+Ctrl+N")
        self.actionNew_Window.setToolTip("Create a new document in a new window")
        self.actionNew_Window.triggered.connect(self.new_window)

        # open existing file menu option
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.setToolTip("Open a File")
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.triggered.connect(self.open_file)

        self.actionOpen_Recent = QtGui.QAction(MainWindow)
        self.actionOpen_Recent.setObjectName(_fromUtf8("actionOpen_Recent"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))

        # save as menu item
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionSave_As.setShortcut("Shift+Ctrl+S")
        self.actionSave_As.setToolTip("Save current document as another file")
        self.actionSave_As.triggered.connect(self.save_as)

        self.actionSave_All = QtGui.QAction(MainWindow)
        self.actionSave_All.setObjectName(_fromUtf8("actionSave_All"))
        self.actionRevert = QtGui.QAction(MainWindow)
        self.actionRevert.setObjectName(_fromUtf8("actionRevert"))
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionDetach_Tab = QtGui.QAction(MainWindow)
        self.actionDetach_Tab.setObjectName(_fromUtf8("actionDetach_Tab"))
        self.actionClose_Tab = QtGui.QAction(MainWindow)
        self.actionClose_Tab.setObjectName(_fromUtf8("actionClose_Tab"))

        # close window menu item
        self.actionClose_Window = QtGui.QAction(MainWindow)
        self.actionClose_Window.setObjectName(_fromUtf8("actionClose_Window"))
        self.actionClose_Window.setToolTip("Close this Windows")
        self.actionClose_Window.setShortcut("Ctrl+Q")
        self.actionClose_Window.triggered.connect(sys.exit, 0)

        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionPaste_Special = QtGui.QAction(MainWindow)
        self.actionPaste_Special.setObjectName(_fromUtf8("actionPaste_Special"))
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionSelect_All = QtGui.QAction(MainWindow)
        self.actionSelect_All.setObjectName(_fromUtf8("actionSelect_All"))
        self.actionChange_the_selection = QtGui.QAction(MainWindow)
        self.actionChange_the_selection.setObjectName(_fromUtf8("actionChange_the_selection"))
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionFind_Next = QtGui.QAction(MainWindow)
        self.actionFind_Next.setObjectName(_fromUtf8("actionFind_Next"))
        self.actionFind_Previous = QtGui.QAction(MainWindow)
        self.actionFind_Previous.setObjectName(_fromUtf8("actionFind_Previous"))
        self.actionFind_and_Replace = QtGui.QAction(MainWindow)
        self.actionFind_and_Replace.setObjectName(_fromUtf8("actionFind_and_Replace"))
        self.actionSelect_Font = QtGui.QAction(MainWindow)
        self.actionSelect_Font.setObjectName(_fromUtf8("actionSelect_Font"))
        self.actionColor_Scheme = QtGui.QAction(MainWindow)
        self.actionColor_Scheme.setObjectName(_fromUtf8("actionColor_Scheme"))
        self.actionLine_numbers = QtGui.QAction(MainWindow)
        self.actionLine_numbers.setObjectName(_fromUtf8("actionLine_numbers"))
        self.actionStatusbar = QtGui.QAction(MainWindow)
        self.actionStatusbar.setObjectName(_fromUtf8("actionStatusbar"))
        self.actionConvert = QtGui.QAction(MainWindow)
        self.actionConvert.setObjectName(_fromUtf8("actionConvert"))
        self.actionMove_Selection = QtGui.QAction(MainWindow)
        self.actionMove_Selection.setObjectName(_fromUtf8("actionMove_Selection"))
        self.actionDuplicate_Line_Selection = QtGui.QAction(MainWindow)
        self.actionDuplicate_Line_Selection.setObjectName(_fromUtf8("actionDuplicate_Line_Selection"))
        self.actionIncrease_Indent = QtGui.QAction(MainWindow)
        self.actionIncrease_Indent.setObjectName(_fromUtf8("actionIncrease_Indent"))
        self.actionDecrease_Indent = QtGui.QAction(MainWindow)
        self.actionDecrease_Indent.setObjectName(_fromUtf8("actionDecrease_Indent"))
        self.actionAuto_Indent = QtGui.QAction(MainWindow)
        self.actionAuto_Indent.setObjectName(_fromUtf8("actionAuto_Indent"))
        self.actionLine_Ending = QtGui.QAction(MainWindow)
        self.actionLine_Ending.setObjectName(_fromUtf8("actionLine_Ending"))
        self.actionTab_Size = QtGui.QAction(MainWindow)
        self.actionTab_Size.setObjectName(_fromUtf8("actionTab_Size"))
        self.actionWord_Wrap = QtGui.QAction(MainWindow)
        self.actionWord_Wrap.setObjectName(_fromUtf8("actionWord_Wrap"))
        self.actionWrite_Unicode_BOM = QtGui.QAction(MainWindow)
        self.actionWrite_Unicode_BOM.setObjectName(_fromUtf8("actionWrite_Unicode_BOM"))
        self.actionFiletype = QtGui.QAction(MainWindow)
        self.actionFiletype.setObjectName(_fromUtf8("actionFiletype"))
        self.actionPrevious_Tab = QtGui.QAction(MainWindow)
        self.actionPrevious_Tab.setObjectName(_fromUtf8("actionPrevious_Tab"))
        self.actionNext_Tab = QtGui.QAction(MainWindow)
        self.actionNext_Tab.setObjectName(_fromUtf8("actionNext_Tab"))
        self.actionGo_To = QtGui.QAction(MainWindow)
        self.actionGo_To.setObjectName(_fromUtf8("actionGo_To"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))

        # contents menu item
        self.actionContents = QtGui.QAction(MainWindow)
        self.actionContents.setShortcut("F1")
        self.actionContents.setToolTip("Display the Mousepad user manual")
        self.actionContents.triggered.connect(self.open_content_in_browser)
        self.actionContents.setObjectName(_fromUtf8("actionContents"))

        self.actionAbout_2 = QtGui.QAction(MainWindow)
        self.actionAbout_2.setObjectName(_fromUtf8("actionAbout_2"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionNew_Window)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Recent)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSave_All)
        self.menuFile.addAction(self.actionRevert)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDetach_Tab)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Tab)
        self.menuFile.addAction(self.actionClose_Window)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionPaste_Special)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addAction(self.actionChange_the_selection)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFind_Next)
        self.menuEdit.addAction(self.actionFind_Previous)
        self.menuEdit.addAction(self.actionFind_and_Replace)
        self.menuView.addAction(self.actionSelect_Font)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionColor_Scheme)
        self.menuView.addAction(self.actionLine_numbers)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionStatusbar)
        self.menuText.addAction(self.actionConvert)
        self.menuText.addAction(self.actionMove_Selection)
        self.menuText.addSeparator()
        self.menuText.addAction(self.actionDuplicate_Line_Selection)
        self.menuText.addSeparator()
        self.menuText.addAction(self.actionIncrease_Indent)
        self.menuText.addAction(self.actionDecrease_Indent)
        self.menuDocument.addAction(self.actionAuto_Indent)
        self.menuDocument.addAction(self.actionLine_Ending)
        self.menuDocument.addAction(self.actionTab_Size)
        self.menuDocument.addAction(self.actionWord_Wrap)
        self.menuDocument.addSeparator()
        self.menuDocument.addAction(self.actionWrite_Unicode_BOM)
        self.menuDocument.addSeparator()
        self.menuDocument.addAction(self.actionFiletype)
        self.menuNavigation.addAction(self.actionPrevious_Tab)
        self.menuNavigation.addAction(self.actionNext_Tab)
        self.menuNavigation.addSeparator()
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.actionGo_To)
        self.menuHelp.addAction(self.actionContents)
        self.menuHelp.addAction(self.actionAbout_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuText.menuAction())
        self.menubar.addAction(self.menuDocument.menuAction())
        self.menubar.addAction(self.menuNavigation.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuText.setTitle(_translate("MainWindow", "Text", None))
        self.menuDocument.setTitle(_translate("MainWindow", "Document", None))
        self.menuNavigation.setTitle(_translate("MainWindow", "Navigation", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionNew_Windows.setText(_translate("MainWindow", "New Windows", None))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen_Recent.setText(_translate("MainWindow", "Open Recent", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As", None))
        self.actionSave_All.setText(_translate("MainWindow", "Save All", None))
        self.actionRevert.setText(_translate("MainWindow", "Revert", None))
        self.actionPrint.setText(_translate("MainWindow", "Print", None))
        self.actionDetach_Tab.setText(_translate("MainWindow", "Detach Tab", None))
        self.actionClose_Tab.setText(_translate("MainWindow", "Close Tab", None))
        self.actionClose_Window.setText(_translate("MainWindow", "Close Window", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionCut.setText(_translate("MainWindow", "Cut", None))
        self.actionCopy.setText(_translate("MainWindow", "Copy", None))
        self.actionPaste.setText(_translate("MainWindow", "Paste", None))
        self.actionPaste_Special.setText(_translate("MainWindow", "Paste Special", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All", None))
        self.actionChange_the_selection.setText(_translate("MainWindow", "Change the selection", None))
        self.actionFind.setText(_translate("MainWindow", "Find", None))
        self.actionFind_Next.setText(_translate("MainWindow", "Find Next", None))
        self.actionFind_Previous.setText(_translate("MainWindow", "Find Previous", None))
        self.actionFind_and_Replace.setText(_translate("MainWindow", "Find and Replace", None))
        self.actionSelect_Font.setText(_translate("MainWindow", "Select Font", None))
        self.actionColor_Scheme.setText(_translate("MainWindow", "Color Scheme", None))
        self.actionLine_numbers.setText(_translate("MainWindow", "Line Numbers", None))
        self.actionStatusbar.setText(_translate("MainWindow", "Statusbar", None))
        self.actionConvert.setText(_translate("MainWindow", "Convert", None))
        self.actionMove_Selection.setText(_translate("MainWindow", "Move Selection", None))
        self.actionDuplicate_Line_Selection.setText(_translate("MainWindow", "Duplicate Line / Selection", None))
        self.actionIncrease_Indent.setText(_translate("MainWindow", "Increase Indent", None))
        self.actionDecrease_Indent.setText(_translate("MainWindow", "Decrease Indent", None))
        self.actionAuto_Indent.setText(_translate("MainWindow", "Auto Indent", None))
        self.actionLine_Ending.setText(_translate("MainWindow", "Line Ending", None))
        self.actionTab_Size.setText(_translate("MainWindow", "Tab Size", None))
        self.actionWord_Wrap.setText(_translate("MainWindow", "Word Wrap", None))
        self.actionWrite_Unicode_BOM.setText(_translate("MainWindow", "Write Unicode BOM", None))
        self.actionFiletype.setText(_translate("MainWindow", "Filetype", None))
        self.actionPrevious_Tab.setText(_translate("MainWindow", "Previous Tab", None))
        self.actionNext_Tab.setText(_translate("MainWindow", "Next Tab", None))
        self.actionGo_To.setText(_translate("MainWindow", "Go to", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionContents.setText(_translate("MainWindow", "Contents", None))
        self.actionAbout_2.setText(_translate("MainWindow", "About", None))

    # creates new file and opens it in the new tab
    def new_file(self):
        self.textEdit.setText("")

        # todo
        # create new tab with untitled file

    # open new window
    def new_window(self):
        try:
            process_id = os.fork()

            if process_id == 0:
                proc = QtCore.QProcess()

                # todo
                # fix this problem:
                #
                # [xcb] Unknown sequence number while processing queue
                # [xcb] Most likely this is a multi-threaded client and XInitThreads has not been called
                # [xcb] Aborting, sorry about that.
                # #python: ../../src/xcb_io.c:274: poll_for_event: Assertion `!xcb_xlib_threads_sequence_lost' failed.
                # main.py: Fatal IO error: client killed

                proc.execute("python", (os.path.dirname(os.path.realpath(__file__)) + "/main.py",))
            else:
                pass
        except OSError:
            print("New process cannot be opened.")
        except IOError:
            print("New process cannot be opened.")
        except Exception:
            print("unknown exception")

    # open existing file
    def open_file(self):
        # get the filename
        filename = QtGui.QFileDialog.getOpenFileName()

        # ensure that your file is correct file
        if os.path.isfile(filename):
            try:
                # open the file
                file_handler = codecs.open(filename, "r", "utf-8")

                file_content = ""

                # reads the file
                for line in file_handler.readlines():
                    file_content += line

                # set editorEdit text to new read text
                self.textEdit.setText(file_content)

                # add new opened file to tab list
                self.tabList.append([filename, file_content])

                file_handler.close()
            except IOError:
                QtGui.QErrorMessage.showMessage("An error occured while reading file. Ensure"
                                                " that you have rights to open the file.\n")
        else: # this file is not correct
            QtGui.QErrorMessage.showMessage("Your file is not a regular file.\n")

    def open_content_in_browser(self):
        url = "http://docs.xfce.org/"

        # webbrowser.BaseBrowser.open_new_tab(url)
        webbrowser.open_new_tab(url)

    def save_as(self):
        filename = QtGui.QFileDialog.getSaveFileName()

        try:
            file_handler = codecs.open(filename, "w", "utf-8")

            file_handler.write(self.textEdit.toPlainText())
        except IOError:
            print("Error while saving file.\n")
