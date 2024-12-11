from PyQt5.QtWidgets import QInputDialog, QMessageBox
from models.database import get_connection, create_tables
from ui.main_window import Ui_MainWindow
from PyQt5 import QtWidgets

class TaskController:
    def __init__(self):
        self.connection = get_connection()
        create_tables(self.connection)
        self.cursor = self.connection.cursor()

        self.ui_main = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.ui_main)

        self.ui.addButton.clicked.connect(self.add_task)
        self.ui.completeButton.clicked.connect(self.complete_task)

        self.load_tasks()

    def load_tasks(self):
        self.ui.activeTasksTable.setRowCount(0)
        self.ui.activeTasksTable.setColumnCount(5)  # Увеличиваем число колонок
        self.ui.activeTasksTable.setHorizontalHeaderLabels(["ID", "Название", "Предмет", "Описание", "Срок"])
        self.ui.activeTasksTable.setColumnHidden(0, True)  # Скрываем колонку с ID

        tasks = self.cursor.execute(
            "SELECT id, name, subject, description, due_date FROM tasks WHERE completed = 0").fetchall()
        for row, task in enumerate(tasks):
            self.ui.activeTasksTable.insertRow(row)
            for col, value in enumerate(task):
                self.ui.activeTasksTable.setItem(row, col, QtWidgets.QTableWidgetItem(str(value)))

        self.ui.completedTasksTable.setRowCount(0)
        completed_tasks = self.cursor.execute(
            "SELECT name, subject, description, due_date FROM tasks WHERE completed = 1").fetchall()
        for row, task in enumerate(completed_tasks):
            self.ui.completedTasksTable.insertRow(row)
            for col, value in enumerate(task):
                self.ui.completedTasksTable.setItem(row, col, QtWidgets.QTableWidgetItem(str(value)))

    def add_task(self):
        try:
            name, ok = QInputDialog.getText(self.ui_main, "Добавить задачу", "Введите название:")
            if not ok or not name.strip():
                return
            subject, ok = QInputDialog.getText(self.ui_main, "Добавить задачу", "Введите предмет:")
            if not ok or not subject.strip():
                return
            description, ok = QInputDialog.getText(self.ui_main, "Добавить задачу", "Введите описание (необязательно):")
            due_date, ok = QInputDialog.getText(self.ui_main, "Добавить задачу", "Введите срок (ГГГГ-ММ-ДД):")
            if not ok or not due_date.strip():
                return

            self.cursor.execute("INSERT INTO tasks (name, subject, description, due_date) VALUES (?, ?, ?, ?)", (name, subject, description, due_date))
            self.connection.commit()
            self.load_tasks()
        except Exception as e:
            QMessageBox.critical(self.ui_main, "Ошибка", f"Не удалось добавить задачу: {e}")

    def complete_task(self):
        selected = self.ui.activeTasksTable.currentRow()
        if selected == -1:
            QMessageBox.warning(self.ui_main, "Предупреждение", "Выберите задачу для завершения.")
            return

        task_id_item = self.ui.activeTasksTable.item(selected, 0)  # Получаем ID задачи из скрытой колонки
        if not task_id_item:
            QMessageBox.warning(self.ui_main, "Ошибка", "Не удалось получить ID задачи.")
            return

        task_id = int(task_id_item.text())  # Преобразуем ID в целое число
        try:
            self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
            self.connection.commit()
            self.load_tasks()
        except Exception as e:
            QMessageBox.critical(self.ui_main, "Ошибка", f"Не удалось завершить задачу: {e}")

