# Задание
# Создать классы цветов: общий класс для всех цветов и классы для нескольких
# видов. Создать экземпляры (объекты) цветов разных видов.
# Собрать букет (букет - еще один класс) с определением его стоимости.
# В букете цветы пусть хранятся в списке. Это будет список объектов.

# Для букета создать метод, который определяет время его увядания по среднему
# времени жизни всех цветов в букете.

# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)

# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).

class Color:
    def __init__(self, name, color, average_lifespan):
        self.name = name
        self.color = color
        self.average_lifespan = average_lifespan

    def __str__(self):
        return (
            f"{self.name} ({self.color}) - "
            f"Average Lifespan: {self.average_lifespan}"
        )


class Flower(Color):
    def __init__(self, name, color, average_lifespan, stem_length):
        super().__init__(name, color, average_lifespan)
        self.stem_length = stem_length

    def __str__(self):
        return f"{super().__str__()} - Stem Length: {self.stem_length}"


class Bouquet:
    def __init__(self):
        self.colors = []

    def add_color(self, color):
        self.colors.append(color)

    def get_average_lifespan(self):
        total_lifespan = sum([color.average_lifespan for color in self.colors])
        return total_lifespan / len(self.colors)

    def sort_by_average_lifespan(self):
        self.colors.sort(key=lambda color: color.average_lifespan)

    def sort_by_color(self):
        self.colors.sort(key=lambda color: color.color)

    def sort_by_stem_length(self):
        self.colors.sort(key=lambda color: color.stem_length)

    def sort_by_cost(self):
        self.colors.sort(key=lambda color: color.cost)

    def search_by_average_lifespan(self, average_lifespan):
        return [color for color in self.colors
                if color.average_lifespan == average_lifespan]


rose = Flower("Rose", "Red", 100, 10)
daisy = Flower("Daisy", "Yellow", 80, 8)
bouquet = Bouquet()
bouquet.add_color(rose)
bouquet.add_color(daisy)

print("Bouquet:")
for color in bouquet.colors:
    print(color)

print(f"Average Lifespan: {bouquet.get_average_lifespan()}")

bouquet.sort_by_average_lifespan()
print("Sorted by Average Lifespan:")
for color in bouquet.colors:
    print(color)

bouquet.sort_by_color()
print("Sorted by Color:")
for color in bouquet.colors:
    print(color)

bouquet.sort_by_stem_length()
print("Sorted by Stem Length:")
for color in bouquet.colors:
    print(color)

search_result = bouquet.search_by_average_lifespan(100)
print("Search Result:")
for color in search_result:
    print(color)
