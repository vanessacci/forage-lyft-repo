import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from tires import *
import unittest
from datetime import datetime


class TestCarriganTire(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear = [0, 0.9, 0, 0]

        tires = carrigan_tires.CarriganTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_engine_should_not_be_serviced(self):
        tire_wear = [0, 0.8, 0, 0]

        tires = carrigan_tires.CarriganTire(tire_wear)
        self.assertFalse(tires.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        tire_wear = [0, 1, 1, 1]

        tires = octoprime_tires.OctoprimeTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_engine_should_not_be_serviced(self):
        tire_wear = [0, 0.9, 0, 0]

        tires = octoprime_tires.OctoprimeTire(tire_wear)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
