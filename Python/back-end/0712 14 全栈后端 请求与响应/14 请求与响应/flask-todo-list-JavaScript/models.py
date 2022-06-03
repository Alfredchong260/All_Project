todo_list = [
    {"id": 0, "title": "吃饭", "done": True},
    {"id": 1, "title": "睡觉", "done": True},
    {"id": 2, "title": "打豆豆", "done": True},
]


class TodoList:
    def __init__(self, task_list):
        self.todo_list = task_list
        self.count = len(task_list)

    @property
    def undone_list(self):
        return list(filter(lambda item: not item['done'], self.todo_list))

    @property
    def done_list(self):
        return list(filter(lambda item: item['done'], self.todo_list))


todo = TodoList(todo_list)
