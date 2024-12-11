from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 800, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 800, 500))

        self.tab_active = QtWidgets.QWidget()
        self.activeTasksTable = QtWidgets.QTableWidget(self.tab_active)
        self.activeTasksTable.setGeometry(QtCore.QRect(50, 50, 700, 300))
        self.activeTasksTable.setColumnCount(4)
        self.activeTasksTable.setHorizontalHeaderLabels(["Название", "Предмет", "Описание", "Срок"])
        self.activeTasksTable.horizontalHeader().setStretchLastSection(True)

        self.addButton = QtWidgets.QPushButton(self.tab_active)
        self.addButton.setGeometry(QtCore.QRect(300, 400, 100, 30))
        self.addButton.setText("Добавить")

        self.completeButton = QtWidgets.QPushButton(self.tab_active)
        self.completeButton.setGeometry(QtCore.QRect(450, 400, 100, 30))
        self.completeButton.setText("Завершить")

        self.tabWidget.addTab(self.tab_active, "Активные задачи")

        self.tab_completed = QtWidgets.QWidget()
        self.completedTasksTable = QtWidgets.QTableWidget(self.tab_completed)
        self.completedTasksTable.setGeometry(QtCore.QRect(50, 50, 700, 300))
        self.completedTasksTable.setColumnCount(4)
        self.completedTasksTable.setHorizontalHeaderLabels(["Название", "Предмет", "Описание", "Срок"])
        self.completedTasksTable.horizontalHeader().setStretchLastSection(True)

        self.tabWidget.addTab(self.tab_completed, "Завершенные задачи")

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Трекер учебных задач")
        self.label.setText("Трекер учебных задач")
