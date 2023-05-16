from battery_interface import Battery
from datetime import date

class SpindlerBattery(Battery):
    
    def __init__(self, last_service_date: date, current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = date.today()

    
    def needs_service(self):
        return self.current_date - self.last_service_date >= 4