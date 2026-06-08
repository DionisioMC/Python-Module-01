class Plant:
    def __init__(self, name: str,
                 height: float, growth: float, plant_age: int) -> None:
        self._name = name
        if height < 0:
            self._height = 0
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
            print(f"{self._name}: Error, growth rate can't be negative or zero")
        else:
            self._growth = growth

    def grow(self):
        self._height += self._growth
        self._plant_age += 1

    def age(self):
        total_growth = 0
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            self.grow()
            total_growth += self._growth
            self.show()
        print(f"Growth this week: {round(total_growth, 1)}cm")

    def show(self) -> None:
        print(f"{self._name.capitalize()}: ", end="")
        print(f"{round(self._height, 1)}cm, {self._plant_age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age

    def set_height(self, value: float):
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm")

    def set_age(self, value: float):
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._plant_age = value
            print(f"Age updated: {self._plant_age} days")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 growth: float, plant_age: int, color: str):
        super().__init__(name, height, growth, plant_age)
        self._color = color
        self._has_bloomed = False

    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if self._has_bloomed:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")

    def bloom(self):
        print(f"(asking the {self._name} to bloom)")
        self._has_bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 growth: float, plant_age: int, trunk_diameter: float):
        super().__init__(name, height, growth, plant_age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"(asking the {self._name} to produce shade)")
        print(f"Tree {self._name.capitalize()} now produces a shade of {self._trunk_diameter * 40}cm long and {self._trunk_diameter}cm wide")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}")


if __name__ == "__main__":
    rose = Flower("rose", 25, 1, 4, "red")
    rose.show()
    oak = Tree("oak", 200.0, 0.5, 365, 5.0)
    oak.show()
    oak.produce_shade()
