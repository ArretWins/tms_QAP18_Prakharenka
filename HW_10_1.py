# Цветочница.
# Определить иерархию и создать несколько цветов. Собрать букет которых могут быть/не быть использовать аксессуары с определением его стоимости.
# Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (пример параметров: свежесть/цвет/длина стебля/стоимость...)
# Реализовать поиск цветов в букете по определенным параметрам.
# Узнать, есть ли цветок в букете.
class Flower:
    def __init__(self, name, color, freshness, stem_length, cost, lifespan):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.cost = cost
        self.lifespan = lifespan

    def info(self):
        return (f"{self.name}(Цвет: {self.color}, "
                f"Свежесть: {self.freshness}, Длина стебля: {self.stem_length} cm, "
                f"Стоимость: {self.cost} р.)")


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, cost):
        super().__init__('Роза', color, freshness, stem_length, cost, lifespan=4)


class Lilac(Flower):
    def __init__(self, color, freshness, stem_length, cost):
        super().__init__('Сирень', color, freshness, stem_length, cost, lifespan=10)


class Accessory:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def total_cost(self):
        total = sum(flower.cost for flower in self.flowers) + sum(accessory.cost for accessory in self.accessories)
        return total

    def average_lifespan(self):
        if not self.flowers:
            return "Нет цветов"
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        return total_lifespan / len(self.flowers)

    def sort_flowers(self, key):
        sorted_flowers = sorted(self.flowers, key=lambda flower: getattr(flower, key))
        return [flower.name for flower in sorted_flowers]

    def find_flowers(self, **kwargs):
        result = self.flowers
        for key, value in kwargs.items():
            result = [flower for flower in result if getattr(flower, key) == value]
        return result

    def has_flower(self, flower_name):
        return any(flower.name == flower_name for flower in self.flowers)


lilac = Lilac(color="blue", freshness=9, stem_length=30, cost=2)
otkrytka = Accessory(name="Открытка", cost=1)

print(lilac.info())

bouquet = Bouquet()
bouquet.add_flower(lilac)
bouquet.add_flower(lilac)
bouquet.add_flower(lilac)
bouquet.add_accessory(otkrytka)

print("Всего стоимость:", bouquet.total_cost(), "р.")
print("Средняя длительность жизни (ну или увядания хз как правильно):", bouquet.average_lifespan(), "дней")

sorted_flowers_by_stem_length = bouquet.sort_flowers('stem_length')
print("Отсортированы:", sorted_flowers_by_stem_length)


blue_flowers = bouquet.find_flowers(color='blue')
print("Есть ли синии цветы:", blue_flowers)
print("Есть ли ромашки в букете (мы их вообще не продаем)?", bouquet.has_flower('Ромашка'))
