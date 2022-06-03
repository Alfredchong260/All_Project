from flask import Flask, render_template, request, jsonify
from models import todo
import json

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/todo', methods=['GET', 'POST'])
def todo_view():
    if request.method == 'GET':
        # return jsonify(todo.todo_list)  # 默认是一个列表
        return json.dumps(todo.todo_list)  # 默认是一个列表
    if request.method == 'POST':
        item = {"id": todo.todo_list[-1]["id"] + 1,
                "title": request.json.get('title'),
                "done": False}
        todo.todo_list.append(item)
        return {'status': 'ok'}


@app.route('/todo/<int:_id>', methods=['PUT', 'DELETE'])
def todo_item(_id):
    if request.method == 'PUT':
        for item in todo.todo_list:
            if item['id'] == _id:
                item['done'] = not item['done']
                return {'status': 'ok'}
        return {'status': 'error'}
    if request.method == "DELETE":
        for item in todo.todo_list:
            if item['id'] == _id:
                todo.todo_list.remove(item)
                return {'status': 'ok'}
        return {'status': 'error'}
