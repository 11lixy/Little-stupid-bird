#8-3
def make_shirt(size,word):
    """说明衣服的尺码和字样"""
    print("\n衣服是"+ size + "码的" ".")
    print("衣服上是" + word + "的字体" + ".")
#用位置实参调用函数
make_shirt('m','微软雅黑')
#用关键字实参调用函数
make_shirt(size='xl',word='仿宋体')

#8-4
#word形参设置默认值
def make_shirt(size,word='I love python '):
    """说明衣服的尺码和字样"""
    print("\n衣服是" + size + "码的" ".")
    print("衣服上是" + word + "的字体" + ".")
make_shirt('xl')
#给word形参提供了实参，就不再使用默认值
make_shirt(size='xl',word='默认字样')
make_shirt(size='M',word='默认字样')
make_shirt('xxl','其他字样')

#8-5
def describe_city(citys_name,citys_country='china'):
    """打印城市的名字，以及属于的国家"""
    print("\n" + citys_name.title() + " is in " + citys_country.title())
#位置实参调用函数
describe_city('beijing')
describe_city('shanghai')
#关键字实参调用函数，给形参提供了实参，不在使用默认值
describe_city(citys_country='Russia',citys_name='Moscow')
