"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1. 设计一个类，可以完成数据的封装
2. 设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
"""

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar  # 导入柱状图模块
from pyecharts.options import *   # 将所有图表选项导入进来
from pyecharts.globals import ThemeType # 导入主题类型

text_file_reader = TextFileReader('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/11_OOP_面向对象/数据分析案例/2011年1月销售数据.txt')
json_file_reader = JsonFileReader('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/11_OOP_面向对象/数据分析案例/2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并为1个list来存储
all_data: list[Record] = jan_data + feb_data

# 数据准备结束
# 开始进行数据计算
data_dict = {}  # 创建一个空字典
for record in all_data:  # 该条数据是在总的数据里面的，或者说，将总的数据一条一条拿过来
    if record.date in data_dict.keys():
        # 当前日期已经有记录了，所以和之前的记录做累加即可
        data_dict[record.date] += record.money #之前记录的当前日期key对应的销售额，加上该条数据的销售额

    else:
        data_dict[record.date] = record.money # 如果这个日期key第一次记录，那么以当前数据的销售额初始化该日期key对应的销售额

# print(data_dict)  # 得到一个dict['日期': 每一天的销售额']


# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))    # 添加X轴数据
bar.add_yaxis('销售额', list(data_dict.values()), label_opts=LabelOpts(is_show=False))  # 添加Y轴的名称和Y轴数据
bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额') # 设置图表标题
)

bar.render('每日销售额柱状图.html')  # 生成图表，并命名图表文件