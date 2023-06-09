from datetime import date
from engine import *
from battery import *
from tires import *
from car import Car


class CarFactory():
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = capulet_engine.CapuletEngine(current_date, last_service_date)
        battery = spindler_battery.SpindlerBattery(
            current_mileage, last_service_mileage)
        tires = carrigan_tires.CarriganTire(tire_wear)
        car = Car(engine, battery, tires)
        if car.needs_service:
            return car

    @staticmethod
    def create_glissade(self, ccurrent_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = willoughby_engine.WilloughbyEngine(
            current_date, last_service_date)
        battery = spindler_battery.SpindlerBattery(
            current_mileage, last_service_mileage)
        tires = octoprime_tires.OctoprimeTire(tire_wear)
        car = Car(engine, battery, tires)
        if car.needs_service:
            return car

    @staticmethod
    def create_palindrome(self, ccurrent_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(
            current_mileage, last_service_mileage)
        tires = carrigan_tires.CarriganTire(tire_wear)
        car = Car(engine, battery, tires)
        if car.needs_service:
            return car

    @staticmethod
    def create_rorschach(self, ccurrent_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = willoughby_engine.WilloughbyEngine(
            current_date, last_service_date)
        battery = nubbin_battery.NubbinBattery(
            current_mileage, last_service_mileage)
        tires = octoprime_tires.OctoprimeTire(tire_wear)
        car = Car(engine, battery, tires)
        if car.needs_service:
            return car

    @staticmethod
    def create_thovex(self, ccurrent_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = capulet_engine.CapuletEngine(current_date, last_service_date)
        battery = nubbin_battery.NubbinBattery(
            current_mileage, last_service_mileage)
        tires = carrigan_tires.CarriganTire(tire_wear)
        car = Car(engine, battery, tires)
        if car.needs_service:
            return car
