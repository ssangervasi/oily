'''
https://projecteuler.net/problem=353

Put on hold because adding the sphere calculations is a bit too time consuming.
'''

import math
from decimal import Decimal
from typing import NamedTuple

pi = Decimal(pi)

def solve():
    return Solution(sum_of_risks=0)

class Solution:
    def __init__(self, sum_of_risks: Decimal):
        self.sum_of_risks = sum_of_risks

    def description(self) -> str:
        return f'The sum of risks is: {self.sum_of_risks}'


# class Journey:
#     def __init__(self):
#         self.legs = []

# class Leg:


class Cartesian(NamedTuple):
    x: Decimal
    y: Decimal
    z: Decimal

class Geographic(NamedTuple):
    lat: Decimal
    lon: Decimal

class Sphere:
    def __init__(self, radius: int = 1):
        self.radius = 1

    def geodesic_distance(self, start: Cartesian, end: Cartesian) -> Decimal:
        pass

    def cartesian_to_geographic(self, cartesian: Cartesian): -> Geographic:
        pass

    def geographic_to_cartesian(self, geographic: Geographic): -> Cartesian:
        pass
        
