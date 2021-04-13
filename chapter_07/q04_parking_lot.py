from typing import Dict
from datetime import datetime
import math


class Car:
    def __init__(self, plate) -> None:
        self.plate = plate


class ParkingTicket:
    def __init__(self, slot, plate) -> None:
        self.slot = slot
        self.plate = plate
        self.parking_time = datetime.now()


class ParkingSlot:
    def __init__(self, car) -> None:
        self.car = car
        self.parking_time = datetime.now()

    def get_parking_time(self):
        return datetime.now() - self.parking_time


class ParkingLot:
    PRICE = 4.0  # Per hour

    def __init__(self) -> None:
        self.slots_free = set(range(4))  # Slot numbers
        self.slots_busy: Dict[int, ParkingSlot] = {}

    def park(self, car):
        try:
            slot = self.slots_free.pop()
        except KeyError:
            raise RuntimeError("Parking lot is full")

        self.slots_busy[slot] = ParkingSlot(car)

        return ParkingTicket(slot, car.plate)

    def take_car(self, ticket: ParkingTicket) -> Car:
        # Find car by slot and plate on ticket
        try:
            slot = self.slots_busy.pop(ticket.slot)
        except KeyError:
            raise RuntimeError("Car not found!")

        if slot.car.plate != ticket.plate:
            raise RuntimeError(f"Plate mismatch!")

        # Calculate price using the parking time
        parking_time = slot.get_parking_time()
        price = self._calculate_price(parking_time)
        print(f"Time parked was: {parking_time}. Price is: {price}")

        # Free parking slot and return the car
        self.slots_free.add(ticket.slot)

        return slot.car

    def _calculate_price(self, parking_time):
        hours = math.ceil(parking_time.total_seconds() / 3600.0)
        return hours * self.PRICE


pl = ParkingLot()
car = Car("MMM1234")

ticket = pl.park(car)
car_taken = pl.take_car(ticket)

assert car is car_taken

car1 = Car("MMG1074")
car2 = Car("ABC1297")
car3 = Car("FGC9873")
car4 = Car("HJR7492")

t1 = pl.park(car1)
t2 = pl.park(car2)
t3 = pl.park(car3)
assert pl.take_car(t1) is car1
pl.park(car1)
pl.park(car4)

pl.park(Car("JKQ1857"))
