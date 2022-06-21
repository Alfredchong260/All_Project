from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


class Config:
    # 数据库链接配置参数
    SQLALCHEMY_DATABASE_URI = 'sqlite:///article.db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/school'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
    SECRET_KEY = 'secret key'


app.config.from_object(Config)

# 创建数据库链接对象
db = SQLAlchemy()
migrate = Migrate()

db.init_app(app)


migrate.init_app(app, db)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    phone = db.Column(db.String(20))

    # 定义关系 关系不是字段 关联作者的所有文章
    articles = db.relationship('Article')

    def __repr__(self):
        return f'<Author {self.id}:{self.name}>'


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    body = db.Column(db.Text)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    # 关系 将文章关联到作者
    author = db.relationship('Author', back_populates='articles')

    def __repr__(self):
        return f'<Article {self.id}:{self.title}>'


@app.cli.command()
def create():
    author1 = Author(name='烽火戏诸侯', phone='110110')
    author2 = Author(name='我吃西红柿', phone='110111')
    author3 = Author(name='辰东', phone='110112')

    db.session.add(author1)
    db.session.add(author2)
    db.session.add(author3)
    db.session.commit()

    article1 = Article(title='剑来',
                       body='大千世界，无奇不有。天道崩塌，我陈平安，唯有一剑，可搬山，断江，倒海，降妖，镇魔，敕神，摘星，摧城，开天！')
    article2 = Article(title='雪中悍刀行',
                       body="该小说讲述一个关于庙堂权争与刀剑交错的时代，一个暗潮涌动粉墨登场的江湖。荣获首届网络文学双年奖之银奖作品。")
    db.session.add(article1)
    db.session.add(article2)

    article3 = Article(title='星辰变',
                       body="当鱼跃龙门化身为龙的时候，他便不是鱼，而是龙！他是龙，龙则是不会呆在鱼群中，他需要的而是无限的天空，上穷碧落下黄泉，翱翔九天。")
    article4 = Article(title='沧元图',
                       body="我叫孟川，今年十五岁，是东宁府“镜湖道院”的当代大师兄。")
    article5 = Article(title='飞剑问道',
                       body="在这个世界，有狐仙、河神、水怪、大妖，也有求长生的修行者。")

    db.session.add(article3)
    db.session.add(article4)
    db.session.add(article5)

    article6 = Article(title='圣墟',
                       body="在破败中崛起，在寂灭中复苏。沧海成尘，雷电枯竭，那一缕幽雾又一次临近大地，世间的枷锁被打开了，一个全新的世界就此揭开神秘的一角……")

    article7 = Article(title='遮天',
                       body="冰冷与黑暗并存的宇宙深处，九具庞大的龙尸拉着一口青铜古棺，亘古长存。")
    article8 = Article(title='完美世界',
                       body="一粒尘可填海，一根草斩尽日月星辰，弹指间天翻地覆。群雄并起，万族林立，诸圣争霸，乱天动地。问苍茫大地，谁主沉浮？")

    db.session.add(article6)
    db.session.add(article7)
    db.session.add(article8)

    db.session.commit()


@app.cli.command()
def search():
    # author = Author.query.get(3)
    # print(author)
    # # articles = Article.query.filter(Article.author_id == author.id).all()
    # # print(articles)
    # print(author.articles)
    # # author.articles.remove(author.articles[-1])
    # atr8 = Article.query.get(8)
    # author.articles.append(atr8)
    # db.session.commit()
    # print(author.articles)

    atr8: Article = Article.query.get(8)
    # author = Author.query.get(atr8.author_id)
    # author = Author.query.filter(Author.id == atr8.author_id).first()
    # print(author)
    print(atr8.author)
    print(atr8.author.articles)
    print(atr8.author.articles[-1].author)


"""
    外键约束
    关系

    Author
    
        articles 作者的所有文章(关系) --> 默认使用外键进行关联
    
    Article
        
        外键
        
        author 文章的作者(关系)  --> 指定 articles 作为反向关联

"""
