from engine.interface_engine import IEngine


class CapuletEngine(IEngine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        service_mileage = 30000
        return self.current_mileage - self.last_service_mileage > service_mileage
