#开发时间： 2022/7/12 10:35
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)


class  Student(Person):
    def __init__(self,name,age,num):
        super().__init__(name,age)
        self.num=num
    def info(self):
        super().info()
        print('学号',self.num)

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print('教龄',self.teachofyear)
stu=Student('王三',20,'147852')
tea=Teacher('李四',41,7)
stu.info()

print('____________')
tea.info()


#
# class A(object):
#     pass
#
# class B(object):
#     pass
#
# class C(A,B):
#     pass













































