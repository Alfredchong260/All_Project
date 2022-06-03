from flask import Flask, render_template, request, redirect

from models import todo

app = Flask(__name__)


@app.route('/')
def hello_world():
    key = request.args.get('key', 'all')

    todo_list = []
    if key == 'undone':
        todo_list = todo.undone_list
    elif key == 'done':
        todo_list = todo.done_list
    elif key == 'all':
        # 获取所有的任务
        todo_list = todo.todo_list

    return render_template('todos.html',
                           todo_list=todo_list,
                           key=key,
                           undone_count=len(todo.undone_list))


@app.route('/clear_done')
def clear_done():
    for item in todo.done_list:
        todo.todo_list.remove(item)

    return redirect('/')


@app.route('/add_todo', methods=["POST"])
def add_todo():
    # 1. 获取任务数据
    info = request.form.get('info', None)
    if info:
        # 2. 构建任务信息
        todo.count += 1
        item = {
            'id': todo.count,
            'info': info,
            'done': False
        }
        # 3. 将任务添加到任务列表
        todo.todo_list.append(item)

    # 4. 调转到首页
    return redirect('/')   # 前端默认表单提交 --> jinja2 模板渲染 --> 后端重定向进行调转
    # ajax 动态加载: {'status':'ok', 'message': '添加任务成功'}  --> 发送给前端 --> 前端进行调转


@app.route('/clear_todo')
def clear_todo():
    # 1. 获取id
    todo_id = request.args.get('id', None)
    print(todo_id)
    # 2. 判断 id 是否是数字
    if todo_id and todo_id.isdigit():
        todo_id = int(todo_id)
        current_todo = list(filter(lambda item: item['id'] == todo_id, todo.todo_list))
        # 3. 如果存在就进行删除
        if current_todo[0] in todo.todo_list:
            todo.todo_list.remove(current_todo[0])
    # 4. 重定向到首页
    return redirect('/')


@app.route('/change_todo', methods=['PUT'])
def change_todo():
    todo_id = request.json.get('id', None)
    done = request.json.get('done', None)

    new_todo = {
        'id': int(todo_id),
        'done': done
    }
    for item in todo.todo_list:
        if item['id'] == new_todo['id']:
            item.update(new_todo)

    return {'status': 'ok', 'message': '修改成功'}


if __name__ == '__main__':
    app.run(debug=True)
