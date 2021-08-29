from pyecharts import options as opts
from pyecharts.charts import Graph

nodes = [
    {"name": "翰政", "symbolSize": 10},
    {"name": "宥唯", "symbolSize": 20},
    {"name": "宇胜", "symbolSize": 30},
    {"name": "伟杰", "symbolSize": 40},
    {"name": "曹哥", "symbolSize": 50},
    {"name": "苓峰", "symbolSize": 40},
    {"name": "满祥", "symbolSize": 30},
]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get("name"), "target": j.get("name")})
c = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph-基本示例"))
    .render("graph_base.html")
)
