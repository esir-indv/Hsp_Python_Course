# @Version  : 1.0
# @Author   : 韩顺平

# 要求：可以从控制台接收用户信息,【姓名，年龄，薪水】, 如下图

name = input("请输入姓名: ")
age = input("请输入年龄: ")
score = input("请输入成绩: ")

print("\n输入的信息如下: ")
print("name:", name)
print("age:", age)
print("score:", score)

# 注意， 接收到的数据类型是str
print(type(age))
print(type(score))

# 如果我们希望对接收到的数据进行算术运算，则需要进行类型转换
print(10 + float(score))
print(20 + int(age))

# 当然，我们也可以在接收数据的时候，直接转成需要的类型
age = int(input("请输入年龄: "))

print("age的类型是:", type(age))



