"""
和文件相关的类定义
"""
import json

from data_define import Record
# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:

    def read_data(self) -> list[Record]:
        """
        读取文件的数据，读到的每一条数据都转换为Record对象，将他们都封装到list内返回即可
        """
        pass


# 定义一个子类：对Text类型的文件进行数据读取
class TextFileReader(FileReader):

    def __init__(self, path):  # 实例对象要传入一个path参数
        self.path = path    # 定义成员变量记录文件的路径

    # 复写父类的方法（实现抽象方法）
    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='UTF-8')

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()  # 消除读取到的每一行数据中的\n
            data_list = line.split(',')  # 用逗号把每一行的数据进行分割，得到一个列表
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3]) # 创建一个Record类对象
            record_list.append(record)

        f.close()
        return record_list

# 定义另一个子类：对JSON类型的文件进行数据读取
class JsonFileReader(FileReader):

    def __init__(self, path):  # 实例对象要传入一个path参数
        self.path = path  # 定义成员变量记录文件的路径

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='UTF-8')

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)   # 将json文件转换为字典
            record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)


        f.close()
        return record_list


# 测试
if __name__ == '__main__':
    # 创建实例对象，并传入文件路径
    text_file_reader = TextFileReader('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/11_OOP_面向对象/数据分析案例/2011年1月销售数据.txt')
    list1 = text_file_reader.read_data()
    json_file_reader = JsonFileReader('C:/Users/xiaozh52/pythonstudy/pycharm/itheima_python/11_OOP_面向对象/数据分析案例/2011年2月销售数据JSON.txt')
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)
