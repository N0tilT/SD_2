from service import FlightService
from flight import Flight

service = FlightService("flights.db")

print("ADD 3")
print(service.create_flight(Flight(0,111,"111")))
print(service.create_flight(Flight(0,222,"222")))
print(service.create_flight(Flight(0,333,"333")))
print("GET ALL")
print(service.get_all())

print("UPDATE 2")
print(service.update_flight(Flight(2,222,"hello")))
print(service.get_by_id(2))

print("DELETE 3")
print(service.delete_flight(3))
print(service.get_all())

print("DELETE ALL")
print(service.delete_flight(1))
print(service.delete_flight(2))

print(service.get_all())