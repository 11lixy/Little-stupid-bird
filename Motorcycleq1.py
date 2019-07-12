motorcycle = ['honda','suzuki','kawasaki','aprolia']
motorcycle.sort()#方法sort()永久按字母排列顺序
print(motorcycle)
motorcycle.sort(reverse=True)#添加revers=True，使得按字母相反的顺序排列
print(motorcycle)
print("Here is the original list:")
print(motorcycle)
print("Here is the sorted list:")
print(sorted(motorcycle))#对列表进行临时排序，按照字母顺序
print("Here is the original list again")
print(motorcycle)
