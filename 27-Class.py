class Myclass:
    var = "hi"

    def sayHello(self):
        print(self.var)

obj = Myclass() #클래스 객체 생성
print(obj.var) #멤버 호출
obj.sayHello() #메소드 호출
