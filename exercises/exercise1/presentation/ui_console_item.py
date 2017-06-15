"""Item Class"""

class Item():
    """Define an Item for the Console Menu"""
    def __init__(self, name=None, function=None, id_=None):
        self.id_ = id_
        self.name = name
        self.function = function

    def __call__(self):
        """Execute the associated function"""
        print()
        self.function()
        print()
        self.stop()

    def draw(self):
        """Print the Item in the desired way"""
        print(str(self.id_) + ". " + self.name)

    def execute(self):
        self()

    def stop(self):
        input("Presione Enter para continuar")

class ItemClose(Item):
    def stop(self):
        pass
