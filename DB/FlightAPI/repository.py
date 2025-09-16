from flight import Flight
from database import DatabaseConnection


class FlightRepository:
    '''Класс-репозиторий для доступа к БД'''

    def __init__(self,connection: DatabaseConnection):
        self.connection=connection

    def create_flight(self, flight:Flight):
        """Добавление рейса"""

        conn = self.connection.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO flights
                        (plane,price)
                        VALUES (%s,%s)
            ''',(flight.plane,flight.price))
        result = cursor.fetchone()
        flight.id = result[0]
        conn.commit()

        cursor.close()
        conn.close()

        return flight
    
    def get_all(self):
        conn = self.connection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM flights ORDER BY id")
        rows = cursor.fetchall()

        flights = []
        for row in rows:
            flights.append(Flight(
                row[0],
                row[1],
                row[2]
            ))
              
        cursor.close()
        conn.close()
        return flights
        
    def get_by_id(self,flight_id:int):
        """Получить рейс по идентификатору"""
        conn = self.connection.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM flights WHERE id = %s",(flight_id,))
        row = cursor.fetchone()
        
        cursor.close()
        conn.close()

        if row:
            return Flight(
                row[0],
                row[1],
                row[2]
            )
        return None
    
    def update_flight(self, flight:Flight):
        """Изменить существующий рейс. 
            Если рейса не существует, ничего не делать."""
        conn = self.connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE flights
            SET price = %s, plane = %s
            WHERE id = %s
            ''',(flight.price, flight.plane, flight.id))
        
        result = cursor.fetchone()
        flight.id = result[0]
        conn.commit()

        cursor.close()
        conn.close()

        return flight
    
    def delete_flight(self,flight_id:int):
        """Удалить существующий рейс.
            Если рейса не существует, ничего не делать."""
        conn = self.connection.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM flights WHERE id = %s
            ''',(flight_id,))
        conn.commit()
        deleted = cursor.rowcount

        cursor.close()
        conn.close()

        return deleted >0

