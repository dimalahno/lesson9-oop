from classes.products import Electronics, Clothing, Chemicals
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
chemicals1 = Chemicals("Стиральный порошок", 150, "Поверхностно-активные вещества")
chemicals2 = Chemicals("Шампунь", 200, "Гигиеническое косметическое средство")


# Создаем пользователей
customer = Customer(username="Dmitriy", email="dimalahno@rambler.ru", address="033 Russ Bur")
admin = Admin(username="root", email="dimalahno@rambler.ru", admin_level=5)

# Создаем корзину покупок и добавляем товары
cart = ShoppingCart(customer, admin)
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)
cart.add_item(chemicals1, 1)
cart.add_item(chemicals2, 2)

# Выводим детали корзины
print(cart.get_details())
