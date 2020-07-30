class MyClass:
    var = 'Hi!' #클래스 멤버
    def sayHello(self):
        param1 = 'Hi'
        self.param2 ='Hello' #인스턴스 멤버
        print(param1)
        print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()
