#!/usr/bin/env python3
def ft_garden_data():
    class Plant:
        def __init__(plant, name, height, age):
            plant.name = name
            plant.height = height
            plant.age = age

        def info_print(plant):
            return f"{plant.name}: {plant.height}cm, {plant.age} days old"

    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(p1.info_print())
    print(p2.info_print())
    print(p3.info_print())


if __name__ == "__main__":
    ft_garden_data()
