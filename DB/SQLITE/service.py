import sqlite3
from flight import Flight

class FlightService:
    def __init__(self,db_name: str = ""):
        self.db_name = db_name
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_name)
    
    def init_db(self):
        """Иницилизация таблиц"""
        with self.get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS flights(
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         plane TEXT NOT NULL,
                         price REAL NOT NULL
                         )
                ''')
            conn.commit()
            
    def create_flight(self, flight:Flight):
        """Добавление рейса"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO flights
                         (plane,price)
                         VALUES (?,?)
                ''',(flight.plane,flight.price))
            conn.commit()
            return cursor.rowcount > 0
    
    def get_all(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flights")
            rows = cursor.fetchall()

            flights = []
            for row in rows:
                flights.append(Flight(
                    row[0],
                    row[1],
                    row[2]
                ))
            return flights
        
    def get_by_id(self,flight_id:int):
        """Получить рейс по идентификатору"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM flights WHERE id = ?",(flight_id,))
            row = cursor.fetchone()

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
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE flights
                SET price = ?, plane = ?
                WHERE id = ?
                ''',(flight.price, flight.plane, flight.id))
            conn.commit()
            return cursor.rowcount > 0
    
    def delete_flight(self,flight_id:int):
        """Удалить существующий рейс.
            Если рейса не существует, ничего не делать."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM flights WHERE id = ?
                ''',(flight_id,))
            conn.commit()
            return cursor.rowcount > 0