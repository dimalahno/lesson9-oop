# 3. Класс для управления корзиной покупок
from classes.users import Customer, Admin


class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self, customer: Customer, admin: Admin):
        self.items = []
        self.customer = customer
        self.admin = admin

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины, общей стоимости,
        клиенте и администраторе, зарегистрировавшем покупку.
        """
        details = f"Покупатель: {self.customer.get_details()} приобрел:\n"
        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общая сумма: {self.get_total()} руб\n"
        details += f"Покупки зарегистрировал: {self.admin.get_details()}"
        return details