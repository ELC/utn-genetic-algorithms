"""Menu class"""

class Menu:
    """Define a Console Menu"""
    def __init__(self, name, items=None, parent=None):
        self.name = name
        self.items = items or []
        self.status = "ACTIVE"
        self.close_item = Item(
            name="Salir/Volver",
            function=self._close,
            id_="0")
        self.parent = parent
        if parent:
            parent.add_item(self)

    def _close(self):
        self.status = None
        return 1

    def execute(self):
        """Execute the menu"""
        while self.status == "ACTIVE":
            selected_item = self._choose_item()
            selected_item.execute()

    def _choose_item(self):
        selected_item = None
        while not selected_item:
            self._draw()
            item_id = self._choose_item_id()
            selected_item = self._look_for_item_by_id(item_id)
        return selected_item

    def _look_for_item_by_id(self, item_id):
        for item in self.items:
            if item_id == item.id_:
                return item
        return None

    def _choose_item_id(self):
        option = input("Choose an option: ")
        ui_util.clear_screen()
        return option

    def add_item(self, item):
        """Add an Item to the menu"""
        self._validate_item_id(item)
        self.items.append(item)
        self._validate_parent(item)
        self._add_back_item()

    def _validate_item_id(self, item):
        if item.id_ is None:
            self._generate_new_id(item)

    def _generate_new_id(self, item):
        if len(self.items) == 0:
            item.id_ = "1"
        else:
            last_item = self.items[-2]
            aux = int(last_item.id_) + 1
            item.id_ = str(aux)

    def _validate_parent(self, item):
        if item.parent != self:
            item.parent = self

    def _add_back_item(self):
        if self.close_item in self.items:
            self.items.remove(self.close_item)
        self.items.append(self.close_item)


    def _draw(self):
        """Print the menu"""
        ui_util.clear_screen()
        print(self.name)
        print()
        for item in self.items:
            item.draw()
        print()

if __name__ != "__main__":
    from exercise1.presentation.ui_console_item import Item
    import exercise1.presentation.ui_console as Console
    import exercise1.presentation.ui_console_util as ui_util