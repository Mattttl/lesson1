class myClass:
    __privatevar = 27

    def __privateMeth(self):
        print("Im inside class, myClass")
    def hello(self):
        print(f"Private variable value: {myClass.__privatevar}")

foo = myClass()
foo.hello()
foo.__privateMeth