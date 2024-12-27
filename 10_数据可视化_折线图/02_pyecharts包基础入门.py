"""
演示pyecharts的基础入门
"""

# 导入package
from pyecharts.charts import Line # 折线类
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 标题类/图例类
# pyecharts：包； charts:模块; Line:类

# 创建一个折线图对象
line = Line() # line:实例

# 给折线图对象添加X轴的数据
line.add_xaxis(['中国', '美国', '英国'])

# 给折线图对象添加Y轴的数据
line.add_yaxis('GDP', [30, 20, 10])


# 设置全局配置项
# set_global_opts() 方法
line.set_global_opts(
    title_opts=TitleOpts(title='GDP展示', pos_left='center', pos_bottom='1%'),  # ctrl+P：查看需要传的所有参数
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)




# 通过render方法，将代码生成图表
line.render()