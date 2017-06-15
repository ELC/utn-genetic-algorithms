"""Menu class"""

class Menu:
    """Define a Console Menu"""
    def __init__(self, name, parent=None):
        self.last_id = 1
        self.name = name
        self.items = []
        self.add_back_item()
        self.parent = parent
        self.open = True

    def __call__(self):
        """Execute the menu"""

        ui_util.clear_screen()

        while self.open:
            ui_util.clear_screen()
            while True:
                self._draw()

                selected_item = self._choose_item()

                ui_util.clear_screen()

                if selected_item is None:
                    self.show_error()
                else:
                    break

            selected_item()
        self.open = True

    def execute(self):
        self()

    def _draw(self):
        """Print the menu"""
        print(self.name)
        print()
        for item in self.items:
            item.draw()
        print()

    def _choose_item(self):
        while True:
            item_id = self._choose_item_id()
            return self._look_for_item_by_id(item_id)

    def _choose_item_id(self):
        option = int(input("Choose an option: "))
        return option

    def _look_for_item_by_id(self, item_id):
        for item in self.items:
            if item_id == item.id_:
                return item
        return None

    def show_error(self):
        print("Opcion incorrecta - Vuelva a ingresar\n")

    def update_item_id(self, item):
        if not item.id_ is None:
            return
        item.id_ = self.last_id
        self.last_id += 1

    def add_item(self, item):
        """Add an Item to the menu"""
        if isinstance(item, ItemClose):
            item.parent = self
        self.update_item_id(item)
        self.items.insert(len(self.items)-1, item)

    def add_back_item(self):
        back_item = ItemClose(
            id_=0,
            name="Salir/Volver",
            function=self.close_menu
            )
        self.update_item_id(back_item)
        self.items.append(back_item)

    def close_menu(self):
        self.open = False

if __name__ != "__main__":
    from exercise1.presentation.ui_console_item import Item, ItemClose
    import exercise1.presentation.ui_console_util as ui_util
