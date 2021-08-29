from pyecharts.charts import Bar
# from pyecharts import options as opts

# bar = Bar()
# bar.add_xaxis(['衬衫', '羊毛衫', '裤子', 'T恤'])
# bar.add_yaxis('商家A', [5, 20, 36, 75])
# bar.set_global_opts(title_opts=opts.TitleOpts(title='Main Title', subtitle='Sub Title'))

# bar.render()

bar = (
    Bar()
    .add_xaxis(['衬衫', '羊毛衫', '裤子', 'T恤'])
    .add_yaxis('商家A', [5, 20, 36, 75])
    # .set_global_opts(title_opts=opts.TitleOpts(title='Main Title', subtitle='Sub Title'))
)
bar.render()
