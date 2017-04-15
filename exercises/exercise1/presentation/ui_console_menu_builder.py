"""Builds and returns a Menu"""

def build():
    """Create Menu"""
    report_sub_menu = __generate_report_menu()
    settings_sub_menu = __generate_settings_menu()
    graphic_sub_menu = __generate_graphic_menu()
    submenus = [
        report_sub_menu,
        graphic_sub_menu,
        settings_sub_menu
    ]
    main_menu = __generate_main_menu(submenus)

    return main_menu

def __generate_main_menu(submenus):
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

def __generate_report_menu():
    report_sub_menu = Menu("Reporte")
    report_sub_menu_items = [
        Item("Reporte Completo", report.full_report),
        Item("Reporte de Generaciones", report.generations_report)
    ]
    report_sub_menu = _generate_sub_menu(
        report_sub_menu,
        report_sub_menu_items
        )
    return report_sub_menu

def __generate_settings_menu():
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
    settings_sub_menu = _generate_sub_menu(
        settings_sub_menu,
        settings_sub_menu_items
        )
    return settings_sub_menu

def __generate_graphic_menu():
    graphic_sub_menu = Menu("Graficos")
    graphic_sub_menu_items = [
        Item("Graficar Maximos, minimos y promedios", graphics.graphic_mma),
        Item("Graficar mínimos cuadrados", graphics.graphic_ls),
        Item("Graficar Rango", graphics.graphic_r),
    ]
    graphic_sub_menu = _generate_sub_menu(
        graphic_sub_menu,
        graphic_sub_menu_items
        )
    return graphic_sub_menu

def _generate_sub_menu(sub_menu, items):
    for item in items:
        sub_menu.add_item(item)
    return sub_menu

if __name__ != "__main__":
    from exercise1.presentation.ui_console_menu import Menu
    from exercise1.presentation.ui_console_item import Item
    from exercise1.presentation.ui_console import Console 
    import exercise1.presentation.graphics as graphics
    import exercise1.logic.report as report
