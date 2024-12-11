from models.database import get_connection

class Task:
    @staticmethod
    def add_task(title, subject, description, deadline):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, subject, description, deadline) VALUES (?, ?, ?, ?)",
            (title, subject, description, deadline)
        )
        connection.commit()
        connection.close()

    @staticmethod
    def delete_task(task_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        connection.commit()
        connection.close()

    @staticmethod
    def get_tasks():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        connection.close()
        return tasks

    @staticmethod
    def mark_as_completed(task_id, completed_date):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        task = cursor.fetchone()
        if task:
            cursor.execute(
                "INSERT INTO completions (task_id, title, subject, description, completed_date) VALUES (?, ?, ?, ?, ?)",
                (task[0], task[1], task[2], task[3], completed_date)
            )
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        connection.commit()
        connection.close()

    @staticmethod
    def get_completed_tasks():
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM completions")
        tasks = cursor.fetchall()
        connection.close()
        return tasks

    @staticmethod
    def revert_completion(completion_id):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM completions WHERE id = ?", (completion_id,))
        task = cursor.fetchone()
        if task:
            cursor.execute(
                "INSERT INTO tasks (title, subject, description, deadline) VALUES (?, ?, ?, ?)",
                (task[2], task[3], task[4], None)
            )
            cursor.execute("DELETE FROM completions WHERE id = ?", (completion_id,))
        connection.commit()
        connection.close()
