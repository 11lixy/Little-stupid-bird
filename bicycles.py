bicycles = ['trek','cannondale','redline','specialized']#用方括号表示列表，用逗号分隔其中的元素
print(bicycles)
print(bicycles[0])#请求获取列表元素时，索引从0开始而不是从1，只返回该元素，不包括方括号和引号
print(bicycles[0].title())#使首字母大写
print(bicycles[-1])#将索引指定为-1，可以返回列表最后一个元素
message = "My first bicycle was a " + bicycles[0].title()+"!"#将句子储存在变量message中
print(message)


