from tires.interface_tires import ITires

class OctoprimeTire(ITires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        worn_sum = 3
        return sum(self.tire_wear) >= worn_sum
