class Plant:
    class Stats:
        def __init__(self):
            self.grow = 0
            self.age = 0
            self.show = 0

    def __init__(self, name: str,
                 height: float, growth: float, plant_age: int) -> None:
        self._name = name
        self._stats = self.Stats()
        if height < 0:
            self._height = 0.0
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height
        if plant_age < 0:
            self._plant_age = 0
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._plant_age = plant_age
        if growth <= 0:
            self._growth = 0.1
            print(f"{self._name}: ", end="")
            print("Error, growth rate can't be negative or zero")
        else:
            self._growth = growth

    def grow(self, times: int) -> None:
        self._height += self._growth * times
        self._stats.grow += 1

    def age(self, days: int) -> None:
        total_growth = 0.0
        for i in range(1, days + 1):
            print(f"=== Day {i} ===")
            self.grow(1)
            self._plant_age += 1
            total_growth += self._growth
            self.show()
        self._stats.age += 1
        print(f"Growth this week: {round(total_growth, 1)}cm")

    @staticmethod
    def has_an_year(plant_age: int) -> bool:
        if plant_age > 365:
            return True
        else:
            return False

    @classmethod
    def create_anon(cls):
        anon = cls("Unknown plant", 0.0, 0.1, 0)
        return anon

    def show(self) -> None:
        self._stats.show += 1
        print(f"{self._name.capitalize()}: ", end="")
        print(f"{round(self._height, 1)}cm, {self._plant_age} days old")

    def display_stats(self) -> None:
        stats = self._stats
        print(f"Stats: {stats.grow} grow, {stats.age} age, {stats.show} show")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._plant_age = value
            print(f"Age updated: {self._plant_age} days")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 growth: float, plant_age: int, color: str) -> None:
        super().__init__(name, height, growth, plant_age)
        self._color = color
        self._has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._has_bloomed:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")

    def grow_and_bloom(self):
        print(f"[asking the {self._name} to grow and bloom]")
        self.grow(1)
        self._has_bloomed = True

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._has_bloomed = True


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 growth: float, plant_age: int, color: str) -> None:
        super().__init__(name, height, growth, plant_age, color)
        self._seed_num = 0

    def show(self):
        super().show()
        print(f" Seeds: {self._seed_num}")

    def grow(self, times: int) -> None:
        self._stats.grow += 1
        self._height += self._growth * times

    def age(self, days: int) -> None:
        self._stats.age += 1
        self._plant_age += days
        self.grow(days)

    def bloom(self) -> None:
        self._has_bloomed = True

    def produce_seeds(self, days: int, seeds: int) -> None:
        print(f"[make {self._name} grow, age and bloom]")
        self.age(days)
        self.bloom()
        self._seed_num += seeds


class Tree(Plant):
    _stats: "Tree.TreeStats"

    class TreeStats(Plant.Stats):
        def __init__(self):
            self.grow = 0
            self.age = 0
            self.show = 0
            self.shade = 0

    def __init__(self, name: str, height: float,
                 growth: float, plant_age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, growth, plant_age)
        self._trunk_diameter = trunk_diameter
        self._stats = self.TreeStats()

    def produce_shade(self) -> None:
        self._stats.shade += 1
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name.capitalize()} now produces ", end="")
        print(f"a shade of {self._trunk_diameter * 40}cm long and ", end="")
        print(f"{self._trunk_diameter}cm wide")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}")

    def display_stats(self):
        stats = self._stats
        super().display_stats()
        print(f" {stats.shade} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, growth: float,
                 plant_age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, growth, plant_age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season.capitalize()}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self, times: int) -> None:
        super().grow(times)
        self._nutritional_value += times

    def age(self, days: int) -> None:
        self._stats.age += 1
        print(f"[make {self._name} grow and age for 20 days]")
        self.grow(days)
        self._plant_age += days
        self.show()


def display_stats(plant: Plant | Tree) -> None:
    print(f"[statistics for {plant._name.capitalize()}]")
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.has_an_year(30)}")
    print(f"Is 30 days more than a year? -> {Plant.has_an_year(400)}")
    print("\n=== Flower")
    rose = Flower("rose", 15.0, 8.0, 10, "red")
    rose.show()
    display_stats(rose)
    rose.grow_and_bloom()
    rose.show()
    display_stats(rose)
    print("\n=== Tree")
    oak = Tree("oak", 200.0, 0.5, 365, 5.0)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)
    print("\n=== Seed")
    sunflower = Seed("sunflower", 80.0, 1.5, 45, "yellow")
    sunflower.show()
    sunflower.produce_seeds(20, 42)
    sunflower.show()
    display_stats(sunflower)
    print("\n=== Anonymous")
    anonymous = Plant.create_anon()
    anonymous.show()
    display_stats(anonymous)
