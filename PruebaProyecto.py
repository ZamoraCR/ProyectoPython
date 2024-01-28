import os
import json
from datetime import datetime

class ERP:
    def __init__(self):
        self.menu_options = {
            1: "Mostrar información de Maracusa S.A.",
            2: "Productos",
            3: "Ventas",
            4: "Salir del programa"
        }
        self.products = []
        self.sales = []

    def show_menu(self):
        print("Menú:")
        for option, description in self.menu_options.items():
            print(f"{option}. {description}")

    def show_maracusa_info(self):
        print("¡Bienvenido a Maracusa S.A.!")
        # Información creativa sobre Maracusa S.A.

    def product_module(self):
        # Implementar lógica para el módulo de productos
        pass

    def sales_module(self):
        # Implementar lógica para el módulo de ventas
        pass

    def save_data_to_file(self):
        # Guardar datos en archivos planos
        with open("products.json", "w") as products_file:
            json.dump(self.products, products_file)

        with open("sales.json", "w") as sales_file:
            json.dump(self.sales, sales_file)

    def load_data_from_file(self):
        # Cargar datos desde archivos planos
        if os.path.exists("products.json"):
            with open("products.json", "r") as products_file:
                self.products = json.load(products_file)

        if os.path.exists("sales.json"):
            with open("sales.json", "r") as sales_file:
                self.sales = json.load(sales_file)

if __name__ == "__main__":
    erp_system = ERP()
    erp_system.load_data_from_file()

    while True:
        erp_system.show_menu()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            erp_system.show_maracusa_info()
        elif choice == "2":
            erp_system.product_module()
        elif choice == "3":
            erp_system.sales_module()
        elif choice == "4":
            erp_system.save_data_to_file()
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
