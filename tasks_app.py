from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# define the database schema
def create_schema():
    conn = sqlite3.connect('tasks_management.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       description TEXT,
                       status TEXT NOT NULL,
                       priority TEXT NOT NULL,
                       due_date TEXT NOT NULL)''')
    conn.commit()
    conn.close()


create_schema()


@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('tasks_management.db')
    cursor = conn.cursor()
    status = request.args.get('status')
    priority = request.args.get('priority')
    if status:
        cursor.execute("SELECT * FROM tasks WHERE status=?", (status,))
    elif priority:
        cursor.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    else:
        cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    required_fields = ['title', 'status', 'priority', 'due_date']
    for field in required_fields:
        if field not in task:
            return jsonify({'error': f'{field} is required'}), 400
    conn = sqlite3.connect('tasks_management.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, status, priority, due_date) VALUES (?, ?, ?, ?, ?)",
                   (task['title'], task.get('description'), task['status'], task['priority'], task['due_date']))
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return jsonify({'id': task_id})


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    conn = sqlite3.connect('tasks_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    if task:
        return jsonify(task)
    else:
        return jsonify({'error': 'Task not found'}), 404


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = request.json
    conn = sqlite3.connect('tasks_management.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title=?, description=?, status=?, priority=?, due_date=? WHERE id=?", (
        task.get('title'), task.get('description'), task.get('status'), task.get('priority'), task.get('due_date'),
        task_id))
    conn.commit()
    conn.close()
    return '', 204


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return '', 204


# handle errors
@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': 'Bad request'}), 400


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
