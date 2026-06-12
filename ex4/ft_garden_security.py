class Plant:
    def __init__(self, name: str,
                 height: float, growth: float, plant_age: int) -> None:
        self._name = name.capitalize()
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
        print(f"{self._name}: ", end="")
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

    def set_age(self, value: int):
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._plant_age = value
            print(f"Age updated: {self._plant_age} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 0.8, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-3)
    print()
    print("Current state: ", end="")
    rose.show()
