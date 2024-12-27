"""
演示python递归
需求:通过递归，找出一个指定文件夹内的全部文件

思路：
写一个函数，列出文件夹内的全部内容，如果是文件就收集到list
如果是文件夹，就递归调用自己，再次判断
"""
import os


def test_os():
    """演示os模块的3个基础方法"""
    print(os.listdir('C:/pythonTest'))  # 列出C:/pythonTest下面的所有文件（包括文件和文件夹）  # 列出路径下的内容
    print(os.path.isdir('C:/pythonTest/a')) # 判断C:/pythonTest/a是否是文件夹  # 判断指定路径是不是文件夹
    print(os.path.exists('C:/pythonTest')) # 判断C:/pythonTest 文件或文件夹是否存在  # 判断指定路径是否存在


def get_files_recursion_from_dir(path):
    """
    从指定的路径（文件夹）中使用递归的方式，获取全部的文件列表
    :param path: 指定的文件夹
    :return: list,包含全部的文件，如果路径不存在或者无文件就返回一个空list
    """
    print(f'当前判断的文件夹是：{path}')
    file_list = []  # 定义一个空list，用于接收返回的文件元素

    if os.path.exists(path):  # 如果指定的路径存在
        for f in os.listdir(path):  # 首先输出该路径下的所有文件和文件夹，然后循环遍历所有文件和文件夹
            new_path = path + '/' +f # 这是将之前的指定路径，换成循环遍历到的文件或文件夹的新路径
            if os.path.isdir(new_path): # 如果遍历到文件夹，再次调用自己，逻辑再走一遍
                # 递归要有一个明确的递归条件
                file_list += get_files_recursion_from_dir(new_path) # 自己调用自己，递归
            else: # 如果遍历到文件，就添加到最终的list里
                file_list.append(new_path)

    else: # 如果指定的路径不存在
        print(f'指定的目录{path}，不存在') # 输出目录不存在
        return [] # 返回空list

    return file_list  # 最终将list返回出去


# 测试
if __name__ == '__main__':
    print(get_files_recursion_from_dir('C:/pythonTest'))