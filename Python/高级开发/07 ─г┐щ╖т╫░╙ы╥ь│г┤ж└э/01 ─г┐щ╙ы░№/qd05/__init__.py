"""
   模块: 所有的 py 都是一个模块
   包:   包接口负责组织模块,然后暴露接口
   包 = 目录 + __init__.py


   . 是只有在包接口里面才能使用,表示当前模块的相对路径
"""
from .qd0501 import username, password
from .qd0502 import Triangle
from .qd0503 import check_login
