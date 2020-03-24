class NewClass(object):
    def __init__(self, attribute="default", name="Instace"):
        self.name = name
        self.__attribute = attribute

    def __str__(self):
        return "{} has attributes {}".format(self.name, self.__attribute)

    def setAttribute(self, attribute):
        self.__attribute = attribute

    def getAttribute(self):
        return self.__attribute

inst1 = NewClass(name="Monty", attribute="Python")
print(inst1)
print(inst1.name)
print(inst1.getAttribute())
