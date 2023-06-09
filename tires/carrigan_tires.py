from tires.interface_tires import ITires

class CarriganTire(ITires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        worn_value = 0.9
        for value in self.tire_wear:
            if value >= worn_value:
                return True
        return False