from django.db import models



class Airplane(models.Model):
    AIRPLAN_FUEL_CONSUMPTION_PER_MINUTE = 0.80
    PASSENGER_CONSUMPTION_PER_MINUTE = 0.002

    liters = models.IntegerField()
    airplane_id = models.IntegerField()
    passengers = models.IntegerField()

    def __str__(self):
        return self.title

    @property
    def fuel_tank_capacity(self):
        return self.liters * self.airplane_id

    @property
    def fuel_consumption_per_minute(self):
        total_consumption = self.airplane_id * self.AIRPLAN_FUEL_CONSUMPTION_PER_MINUTE
        total_consumption += self.PASSENGER_CONSUMPTION_PER_MINUTE * self.passengers
        return total_consumption

    @property
    def maximum_minutes_to_fly(self):
        max_mins = self.fuel_tank_capacity / self.fuel_consumption_per_minute
        return round(max_mins, 2)
