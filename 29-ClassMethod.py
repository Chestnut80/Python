class MyClass:
    def sayHello(self):
        print('Hi!')

    def sayBye(self, name):
        print("See You Later! %s"%name)

obj = MyClass()

obj.sayHello()

obj.sayBye('John')
