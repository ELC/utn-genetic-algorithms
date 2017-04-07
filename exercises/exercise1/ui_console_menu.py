"""Menu class"""

class Menu:
    """Define a Console Menu"""
    def __init__(self, name, items=None, parent=None):
        self.name = name
        self.items = items or []
        self.status = "ACTIVE"
        self.parent = parent
        self.close_item = Item("Salir/Volver", self.__close, id_="0")
        if parent:
            parent.add_item(self)

    def __close(self):
        self.status = None
        return 1

    def execute(self):
        """Execute item"""
        while self.status == "ACTIVE":
            selected_item = self.__choose_item()
            selected_item.execute()

    def __choose_item(self):
        selected_item = None
        while not selected_item:
            self.__draw()
            item_id = self.__choose_item_id()
            selected_item = self.__look_for_item_by_id(item_id)
        return selected_item

    def __look_for_item_by_id(self, item_id):
        for item in self.items:
            if item_id == item.id_:
                return item
        return None

    def __choose_item_id(self):
        print()
        option = input("Choose an option: ")
        print()
        return option

    def add_item(self, item):
        """Add an Item to the menu"""
        self.__validate_item_id(item)
        self.items.append(item)
        self.__validate_parent(item)
        self.__add_back_item()

    def __validate_item_id(self, item):
        if item.id_ is None:
            self.__generate_new_id(item)

    def __generate_new_id(self, item):
        if len(self.items) == 0:
            item.id_ = "1"
        else:
            last_item = self.items[-2]
            aux = int(last_item.id_) + 1
            item.id_ = str(aux)

    def __validate_parent(self, item):
        if item.parent != self:
            item.parent = self

    def __add_back_item(self):
        if self.close_item in self.items:
            self.items.remove(self.close_item)
        self.items.append(self.close_item)


    def remove_item(self, item):
        """Remove an Item from the menu"""
        self.items.remove(item)
        if item.parent == self:
            item.parent = None

    def __draw(self):
        """Print the menu"""
        print()
        print("############################################")
        print()
        print(self.name)
        print()
        for item in self.items:
            item.draw()
        print()

if __name__ != "__main__":
    from ui_console_item import Item
