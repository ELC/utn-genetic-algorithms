"""Builds and returns a Menu"""

class Menu_Builder():
    """Builds and returns a Menu"""

    @classmethod
    def build(cls):
        """Create Menu"""
        report_sub_menu = cls.__generate_report_menu()
        settings_sub_menu = cls.__generate_settings_menu()
        graphic_sub_menu = cls.__generate_graphic_menu()
        submenus = [
            report_sub_menu,
            graphic_sub_menu,
            settings_sub_menu
        ]
        main_menu = cls.__generate_main_menu(submenus)

        return main_menu

    @staticmethod
    def __generate_main_menu( submenus):
        """Generate the main manu"""
        menu = Menu("Principal")

        items = [Item("Ejecutar", Console.execute),
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
        report_sub_menu_items = [
            Item("Reporte Completo", Console.full_report),
            Item("Reporte de Generaciones", Console.generations_report)
        ]
        report_sub_menu = cls.__generate_sub_menu(
            report_sub_menu,
            report_sub_menu_items
            )
        return report_sub_menu

    @classmethod
    def __generate_settings_menu(cls):
        settings_sub_menu = Menu("Configuracion")
        settings_sub_menu_items = [
            Item("Mostrar configuracion actual", Console.show_settings),
            Item("Cambiar probabilidad de Cross Over", Console.set_cross_over_prob),
            Item("Cambiar cantidad de bits de los individuos", Console.set_individual_bits),
            Item("Cambiar cantidad maxima de generaciones", Console.set_generations),
            Item("Cambiar probabilidad de mutación", Console.set_mutation_prob),
            Item("Cambiar Tamaño inicial de la población", Console.set_population_size),
            Item("Cambiar mostrar reporte (en desuso)", Console.set_report)
        ]
        settings_sub_menu = cls.__generate_sub_menu(
            settings_sub_menu,
            settings_sub_menu_items
            )
        return settings_sub_menu

    @classmethod
    def __generate_graphic_menu(cls):
        graphic_sub_menu = Menu("Graficos")
        graphic_sub_menu_items = [
            Item("Graficar Maximos, minimos y promedios", Console.graphic_mma),
            Item("Graficar mínimos cuadrados", Console.graphic_ls),
            Item("Graficar Rango", Console.graphic_r),
        ]
        graphic_sub_menu = cls.__generate_sub_menu(
            graphic_sub_menu,
            graphic_sub_menu_items
            )
        return graphic_sub_menu

    @staticmethod
    def __generate_sub_menu(sub_menu, items):
        for item in items:
            sub_menu.add_item(item)
        return sub_menu


if __name__ != "__main__":
    from ui_console_menu import Menu
    from ui_console_item import Item
    from ui_console import Console
