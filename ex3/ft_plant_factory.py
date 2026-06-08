class Plant:
    def __init__(self, name: str,
                 height: float, growth: float, plant_age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.growth = growth
        self.plant_age = plant_age

    def grow(self):
        self.height += self.growth
        self.plant_age += 1

    def age(self):
        total_growth = 0
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            self.grow()
            total_growth += self.growth
            self.show()
        print(f"Growth this week: {round(total_growth, 1)}cm")

    def show(self) -> None:
        print(f"{self.name}: ", end="")
        print(f"{round(self.height, 1)}cm, {self.plant_age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("rose", 25.0, 0.8, 30)
    oak = Plant("oak", 200.0, 0.1, 365)
    cactus = Plant("cactus", 5.0, 0.2, 90)
    sunflower = Plant("sunflower", 80.0, 0.5, 45)
    fern = Plant("fern", 15.0, 0.2, 120)
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    fern.show()
