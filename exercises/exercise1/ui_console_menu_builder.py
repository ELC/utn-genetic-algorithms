"""Builds and returns a Menu"""

class Menu_Builder():
    """Builds and returns a Menu"""

    @classmethod
    def build(cls):
        """Create Menu"""
        report_sub_menu = cls.__generate_report_menu()
        submenus = [
            report_sub_menu
        ]
        main_menu = cls.__generate_main_menu(submenus)

        return main_menu

    @classmethod
    def __generate_main_menu(cls, submenus):
        menu = Menu("Principal")

        items = [Item("Ejecutar", Console.execute),
                 Item("Configuración", Console.show_settings),
                ]

        for submenu in submenus:
            item = Item(submenu.name, submenu.execute)
            items.append(item)

        for item in items:
            menu.add_item(item)

        return menu


    @classmethod
    def __generate_report_menu(cls):
        report_sub_menu = Menu("Reporte")
        report_sub_menu_items = [Item("Reporte Completo", Console.full_report),
                                 Item("Reporte de Generaciones", Console.generations_report)
                                ]
        for items in report_sub_menu_items:
            report_sub_menu.add_item(items)
        return report_sub_menu


if __name__ != "__main__":
    from ui_console_menu import Menu
    from ui_console_item import Item
    from ui_console import Console
