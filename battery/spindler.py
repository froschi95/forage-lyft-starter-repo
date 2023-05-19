from .battery_interface import Battery
from datetime import date

class SpindlerBattery(Battery):
    
    def __init__(self, last_service_date, current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    
    def needs_service(self):
        date_by_which_battery_should_be_serviced = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if date_by_which_battery_should_be_serviced <= self.current_date:
            return True
        else:
            return False