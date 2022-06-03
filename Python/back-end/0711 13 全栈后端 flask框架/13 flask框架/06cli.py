from flask import Flask, render_template
import click

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command()
def hello():
    """say hello"""
    print(app.config)  # app.config 只有在程序运行之后才会有的配置文件对象
    # click.echo('hello flask cli !')
