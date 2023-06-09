import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from battery import *
import unittest
from datetime import datetime

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = spindler_battery.SpindlerBattery(
            today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = spindler_battery.SpindlerBattery(
            today, last_service_date)
        self.assertFalse(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = nubbin_battery.NubbinBattery(
            today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery = nubbin_battery.NubbinBattery(
            today, last_service_date)
        self.assertFalse(battery.needs_service())




if __name__ == '__main__':
    unittest.main()