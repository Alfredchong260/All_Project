from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

bar = (
    Bar()
    .add_xaxis(['衬衫', '羊毛衫', '裤子', 'T恤'])
    .add_yaxis('商家A', [5, 20, 36, 75])
)
make_snapshot(snapshot, bar.render(), 'bar.png')
