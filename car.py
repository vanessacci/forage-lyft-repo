from abc import ABC, abstractmethod
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.agg_engine = engine
        self.agg_battery = battery

    def needs_service(self):
        return (self.agg_battery.needs_service() or 
        self.agg_engine.needs_service())
