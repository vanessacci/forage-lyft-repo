from battery.interface_battery import IBattery


class NubbinBattery(IBattery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        DAYS_IN_A_YEAR = 365
        service_year = 4
        return (self.current_date - self.last_service_date) >= (service_year * DAYS_IN_A_YEAR)
