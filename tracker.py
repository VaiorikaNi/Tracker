import sys
from PyQt5 import QtWidgets
from controllers.task_controller import TaskController

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = TaskController()
    controller.ui_main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
