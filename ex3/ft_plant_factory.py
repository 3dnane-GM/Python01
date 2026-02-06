#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: aezzirar <aezzirar@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/06 10:34:58 by aezzirar        #+#    #+#               #
#  Updated: 2026/02/06 12:55:17 by aezzirar        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plant_factory():
    class Plant:

        total = 0

        def __init__(self, name, height, age):
            self.name = name.capitalize()
            self.height = height
            self.age = age
            Plant.total += 1

        def get_info(self):
            return f"Created: {self.name} ({self.height}cm, {self.age} days)"

        @staticmethod
        def get_total():
            return f"\nTotal plants created: {Plant.total}"

    print("=== Plant Factory Output ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("Cactus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)

    print(p1.get_info())
    print(p2.get_info())
    print(p3.get_info())
    print(p4.get_info())
    print(p5.get_info())
    print(Plant.get_total())


if __name__ == "__main__":
    ft_plant_factory()
