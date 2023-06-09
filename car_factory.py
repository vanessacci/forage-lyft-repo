from datetime import date
from engine import *
from battery import *
from car import Car


class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine.CapuletEngine(current_date, last_service_date)
        battery = spindler_battery.SpindlerBattery(
            current_mileage, last_service_mileage)
        car = Car(engine, battery)
        if car.needs_service:
            return car

    def create_glissade(self, ccurrent_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine.WilloughbyEngine(
            current_date, last_service_date)
        battery = spindler_battery.SpindlerBattery(
            current_mileage, last_service_mileage)
        car = Car(engine, battery)
        if car.needs_service:
            return car

    def create_palindrome(self, ccurrent_date, last_service_date, current_mileage, last_service_mileage):
        engine = sternman_engine.SternmanEngine(
            current_date, last_service_date)
        battery = spindler_battery.SpindlerBattery(
            current_mileage, last_service_mileage)
        car = Car(engine, battery)
        if car.needs_service:
            return car

    def create_rorschach(self, ccurrent_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine.WilloughbyEngine(
            current_date, last_service_date)
        battery = nubbin_battery.NubbinBattery(
            current_mileage, last_service_mileage)
        car = Car(engine, battery)
        if car.needs_service:
            return car

    def create_thovex(self, ccurrent_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine.CapuletEngine(current_date, last_service_date)
        battery = nubbin_battery.NubbinBattery(
            current_mileage, last_service_mileage)
        car = Car(engine, battery)
        if car.needs_service:
            return car
