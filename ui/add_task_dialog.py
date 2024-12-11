from PyQt5 import QtCore, QtGui, QtWidgets

class AddTaskDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить задачу")
        self.setFixedSize(400, 300)

        # Основной layout
        layout = QtWidgets.QVBoxLayout()

        # Поле для названия задачи
        self.title_label = QtWidgets.QLabel("Название задачи:")
        self.title_input = QtWidgets.QLineEdit()
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)

        # Поле для описания
        self.description_label = QtWidgets.QLabel("Описание задачи:")
        self.description_input = QtWidgets.QPlainTextEdit()
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)

        # Поле для названия предмета
        self.subject_label = QtWidgets.QLabel("Название предмета:")
        self.subject_input = QtWidgets.QLineEdit()
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_input)

        # Поле для срока завершения
        self.due_date_label = QtWidgets.QLabel("Срок завершения (ГГГГ-ММ-ДД):")
        self.due_date_input = QtWidgets.QLineEdit()
        layout.addWidget(self.due_date_label)
        layout.addWidget(self.due_date_input)

        # Кнопки
        self.button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        )
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)

        self.setLayout(layout)

    def get_data(self):
        """Возвращает данные из формы."""
        return {
            "title": self.title_input.text(),
            "description": self.description_input.toPlainText(),
            "subject": self.subject_input.text(),
            "due_date": self.due_date_input.text(),
        }
