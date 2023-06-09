from abc import ABC, abstractmethod
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.agg_engine = engine
        self.agg_battery = battery
        self.agg_tires = tires

    def needs_service(self):
        return (
            self.agg_battery.needs_service() or 
            self.agg_engine.needs_service() or
            self.agg_tires.needs_service()
            )
