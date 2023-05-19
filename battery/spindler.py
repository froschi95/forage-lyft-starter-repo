from battery_interface import Battery
from datetime import date

class SpindlerBattery(Battery):
    
    def __init__(self, last_service_date: date, current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    
    def needs_service(self):
        return self.last_service_date.year + 3 < self.current_date