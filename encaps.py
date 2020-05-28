class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 500
print(obj._protectedVar)



class Private:
    def __init__(self):
        self.__privateVar = 15

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Private()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
