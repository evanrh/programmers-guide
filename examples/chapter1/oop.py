class HelloObject:
    def __init__(self, a):
        self.num = a
    def hello(self):
        print("Hello!")

a = HelloObject(2)
a.hello() 
