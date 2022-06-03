from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/filter')
def func_filter():
    my_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    my_str = "hello world !"
    message = "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages. The following pages are a useful first step to get on your way writing programs with Python!"
    user_name = '<span style="color: red;">青等教育-正心</span>'
    return render_template('0301filter.html',
                           my_arr=my_arr,
                           my_str=my_str,
                           message=message,
                           user_name=user_name
                           )
