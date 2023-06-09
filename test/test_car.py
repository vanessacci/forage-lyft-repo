import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from battery import *
from engine import *
import unittest
from datetime import datetime
from car import Car



class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(
            today, last_service_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(
            today, last_service_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(
            last_service_date, last_service_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(
            last_service_date, last_service_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        engine = willoughby_engine.WilloughbyEngine(
            current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(
            today, last_service_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        engine = willoughby_engine.WilloughbyEngine(
            current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(
            today, last_service_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        engine = willoughby_engine.WilloughbyEngine(
            current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(
            last_service_date, last_service_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        engine = willoughby_engine.WilloughbyEngine(
            current_mileage, last_service_mileage)
        battery = spindler_battery.SpindlerBattery(
            last_service_date, last_service_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(
            today, last_service_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(
            today, last_service_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(
            last_service_date, last_service_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(
            last_service_date, last_service_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        engine = willoughby_engine.WilloughbyEngine(
            current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(
            today, last_service_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        engine = willoughby_engine.WilloughbyEngine(
            current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(
            today, last_service_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        engine = willoughby_engine.WilloughbyEngine(
            current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(
            last_service_date, last_service_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        engine = willoughby_engine.WilloughbyEngine(
            current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(
            last_service_date, last_service_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(
            today, last_service_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(
            today, last_service_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(
            last_service_date, last_service_date)
        car = Car(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(
            last_service_date, last_service_date)
        car = Car(engine, battery)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
