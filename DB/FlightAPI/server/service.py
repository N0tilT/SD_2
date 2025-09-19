from repository import FlightRepository
from flight import Flight

class FlightService:
    def __init__(self,repository:FlightRepository):
        self.repository = repository

    def create_flight(self, flight:Flight):
        """Добавление рейса"""
        return self.repository.create_flight(flight)
    
    def get_all(self):
        '''Получить все полёты'''
        return self.repository.get_all()
        
    def get_by_id(self,flight_id:int):
        '''Получить полёт по id'''
        return self.repository.get_by_id(flight_id)
    
    def update_flight(self, flight:Flight):
        """Изменить существующий рейс. 
            Если рейса не существует, ничего не делать."""
        return self.repository.update_flight(flight)
    
    def delete_flight(self,flight_id:int):
        """Удалить существующий рейс.
            Если рейса не существует, ничего не делать."""
        return self.repository.delete_flight(flight_id)