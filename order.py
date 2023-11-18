import uuid
from datetime import datetime
from func_cal_counter import calorie_counter
from func_price_counter import price_counter

class Order:
    def __init__(self, items, date=None):
        self.order_id = str(uuid.uuid4().hex)[:6]
        self.order_accepted = False
        self.order_refused_reason = ""
        self.date = date if date else datetime.now()
        self.items = items

    @property
    def calories(self):
        total_calories = calorie_counter(self.items)
        if total_calories <= 2000:
            self.order_accepted = True
        else:
            self.order_refused_reason = "Your order exceeds the maximum amount of calories allowed"
        return total_calories

    @property
    def price(self):
        return price_counter(self.items)
