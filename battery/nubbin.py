from .battery_interface import Battery
from datetime import date

class NubbinBattery(Battery):
    
    def __init__(self, last_service_date, current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    
    def needs_service(self):
        date_by_which_battery_should_be_serviced = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if date_by_which_battery_should_be_serviced.year <= self.current_date.year:
            return True
        else:
            return False