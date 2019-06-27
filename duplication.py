# _*_ coding=utf-8 _*_


# 去除列表重复元素

L = [1, 2, 3, 4, 'a', '5', 'a', 'v', 'g', 'g', 4]
L2 = [1, 2, 3, 4, 4]

# 集合去重
new = list(set(L))
print(new)

# 使用字典去重
l2 = {}.fromkeys(L).keys()
print(l2)

# 列表推导式
l3 = []
[l3.append(i) for i in L if i not in l3]
print(l3)

# sort 排序，该方法没有返回值
L2.sort()
print(L2)

# sorted排序，并使用列表推导式去重
single = []
[single.append(i) for i in sorted(L2) if i not in single]
print(single)

"""
sort与sorted区别：
sort是应用在list上的方法，sorted可以对所有可迭代对象进行操作
sort方法对所存在的列表对象进行操作，无返回值
sorted返回的是一个新的list，不是在原基础上操作
"""