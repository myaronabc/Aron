# Script Name       : stack.py

class Stack():
    ''' 定义 stack 类 '''
    def __init__(self):
        self.items = []         #初始化空栈，栈使用列表表示

    def push(self,items):
        self.items.append(items)        #将items压栈