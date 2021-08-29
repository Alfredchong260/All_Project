from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(['衬衫', '羊毛衫', '裤子', 'T恤'])
    .add_yaxis('商家A', [5, 20, 36, 75])
    .add_yaxis('商家B', [15, 6, 45, 35])
    .set_global_opts(title_opts=opts.TitleOpts(title='商家价格对比'),
    toolbox_opts=opts.ToolboxOpts(),
    datazoom_opts=opts.DataZoomOpts(),
    tooltip_opts=opts.TooltipOpts(trigger='axis'),
    axispointer_opts=opts.AxisPointerOpts(type_='shadow')
))

bar.render()
