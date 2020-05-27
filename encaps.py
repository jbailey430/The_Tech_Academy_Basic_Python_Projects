class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 500
print(obj._protectedVar)



class Protected1:
    def __init__(self):
        self._privateVar = 15

    def getPrivate(self):
        print(self._privateVar)

    def setPrivate(self, private):
        self._privateVar = private

obj = Protected1()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
