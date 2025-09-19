"""工具函数"""

class BussinessException(Exception):
    """bussiness exception"""
    pass
#####################################################################################
import json
def dump_json(data, filename:str)->bool:
    """将数据以JSON格式写入文件
    
    :param data: 要写入的JSON数据，可以是字典、列表等可序列化对象
    :type data: 可JSON序列化的对象

    :param filename: 目标文件路径及名称
    :type filename: str

    :return: 操作是否成功，成功返回True，失败返回False
    :rtype: bool

    :raises Exception: 当写入过程中发生任何错误时捕获异常并打印
    """
    try:
        # dir_name = os.path.dirname(filename)
        # os.makedirs(dir_name,exist_ok=True)
        with open(filename,'w', encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(e)
        return False
def load_small_json(json_name:str):
    """从JSON文件加载数据
    
    Args:
        json_name: JSON文件的路径及名称
        
    Returns:
        从JSON文件中加载的数据，通常为字典或列表
        
    Raises:
        FileNotFoundError: 当指定的JSON文件不存在时
        json.JSONDecodeError: 当文件内容不是有效的JSON格式时
        Exception: 其他可能发生的异常（如权限问题等）
    """
    with open(json_name,'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
#####################################################################################
