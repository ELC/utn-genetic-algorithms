"""Item Class"""

class Item():
    """Define an Item for the Console Menu"""
    def __init__(self, name=None, function=None, parent=None, id_=None):
        self.id_ = id_
        self.name = name
        self.function = function
        self.parent = parent
        if parent:
            parent.add_item(self)

    def draw(self):
        """Print the Item in the desired way"""
        print(self.id_ + ". " + self.name)

    def execute(self):
        """Execute the associated function"""
        if self.id_ == "0":
            self.function()
            return
        print()
        self.function()
        print()
        input("Presione Enter para continuar")
