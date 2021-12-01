import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x300')

# 1. 创建表格的字段
columns = ('name', 'chinese', 'math', 'english')
columns_value = ('姓名', '语文', '数学', '英语')

# 2. 创建树形表格对象
tree_view = ttk.Treeview(root, show='headings', columns=columns)

# 3. 给表格添加字段的属性
tree_view.column('name', width=80, anchor=tk.CENTER)
tree_view.column('chinese', width=80, anchor=tk.CENTER)
tree_view.column('math', width=80, anchor=tk.CENTER)
tree_view.column('english', width=80, anchor=tk.CENTER)

# 4. 设置字段显示显示的中文名
tree_view.heading(columns[0], text=columns_value[0])
tree_view.heading(columns[1], text=columns_value[1])
tree_view.heading(columns[2], text=columns_value[2])
tree_view.heading(columns[3], text=columns_value[3])

# 5. 将表格显示到页面
tree_view.pack(fill=tk.BOTH, expand=True)

students = [
    {"name": "李四", "chinese": 50, "math": 40, "english": 30, "total": 120},
    {"name": "王五", "chinese": 100, "math": 100, "english": 100, "total": 300},
    {"name": "正心", "chinese": 100, "math": 100, "english": 100, "total": 300}
]
# 6. 往表格中添加数据
index = 1
for stu in students:
    tree_view.insert('', index, values=(stu['name'], stu['chinese'], stu['math'], stu['english']))
    index += 1


def tree_select(event):
    for item in tree_view.selection():  # 7.1 遍历选中的内容
        print('item', item)
        item_value = tree_view.item(item, 'values')
        print('item_value', item_value)


# 高级功能 7. 选中事件回调
tree_view.bind('<<TreeviewSelect>>', tree_select)
root.mainloop()
