from database import get_connection

def add_task(title):
    if not title.strip():
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title.strip(),)
    )

    conn.commit()
    conn.close()

def list_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, completed FROM tasks ORDER BY id DESC"
    )
    tasks = cursor.fetchall()

    conn.close()
    return tasks

def complete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()
