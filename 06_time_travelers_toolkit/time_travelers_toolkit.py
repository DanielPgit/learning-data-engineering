import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

today_date = dt.date.today()
now_time = dt.datetime.now().time()

print(f"The current date is: {today_date}")
print(f"The current time is: {now_time}")

base_cost = Decimal("1000.00")

#To WHEN wants the customer to travel
target_year = randint(1, 10000)

dec = Decimal("0.01")

multiplier = Decimal("10.00")

year_diff = abs(target_year - today_date.year)

#Total cost based on the diffence between years and the multiplier (price I choose for travel)
final_cost = base_cost + (year_diff * multiplier)

final_cost = final_cost.quantize(dec) 
print(final_cost)


destinations_available = ["Rome", "Mars", "Halo", "A dinosaurs cavern", "My house", "A random park"]

random_destination = choice(destinations_available)

print(custom_module.generate_time_travel_message(target_year, random_destination, final_cost))