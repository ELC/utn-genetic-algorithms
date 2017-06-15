"""Builds and returns a Menu"""

def build():
    """Create Menu"""
    submenus = [
        _report_menu(),
        _settings_menu(),
        _graphic_menu()
    ]
    main_menu = _main_menu(submenus)

    return main_menu

def _main_menu(submenus):
    """Generate the main manu"""
    title = "Principal"

    items = [Item("Ejecutar", Console.execute),
            ]
    for submenu in submenus:
        items.append(
            ItemClose(submenu.name, function=submenu.execute)
        )

    return _generate_menu(title, items)

def _report_menu():
    title = "Reporte"
    items = [
        Item("Reporte Completo", Console.full_report),
        Item("Reporte de Generaciones", Console.generations_report)
    ]
    return _generate_menu(title, items)

def _settings_menu():
    title = "Configuracion"
    items = [
        Item("Mostrar configuracion actual", Console.show_settings),
        Item("Cambiar probabilidad de Cross Over", Console.set_cross_over_prob),
        Item("Cambiar cantidad de bits de los cromosomas", Console.set_chromosome_bits),
        Item("Cambiar cantidad maxima de generaciones", Console.set_generations),
        Item("Cambiar probabilidad de mutación", Console.set_mutation_prob),
        Item("Cambiar Tamaño inicial de la población", Console.set_population_size),
        Item("Cambiar Modo Elitista", Console.set_elitism),
        Item("Reiniciar configuracion por defecto", Settings.reset_configuration)
    ]

    return _generate_menu(title, items)

def _graphic_menu():
    title = "Graficos2"
    items = [
        Item("Graficar Maximos, minimos y promedios", graphics.graphic_mma),
        Item("Graficar Rango", graphics.graphic_r),
    ]

    return _generate_menu(title, items)

def _generate_menu(title, items):
    sub_menu = Menu(name=title)
    for item in items:
        sub_menu.add_item(item)
    return sub_menu

if __name__ != "__main__":
    from exercise1.presentation.ui_console_menu import Menu
    from exercise1.presentation.ui_console_item import Item, ItemClose
    import exercise1.presentation.ui_console as Console
    import exercise1.presentation.graphics as graphics
    from exercise1.logic.settings_manager import Settings
