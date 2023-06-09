from battery.interface_battery import IBattery


class SpindlerBattery(IBattery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_year = 2
        service_date = self.last_service_date.replace(year=self.last_service_date.year + service_year)
        return self.current_date >= service_date
