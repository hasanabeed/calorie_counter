from order_func import order_func
from order import Order

def process_order_result(result):
    if isinstance(result, list):
        order = Order(result)
        print('*' * 50)
        print(f"Order ID: {order.order_id}")
        print(f"Date: {order.date}")
        print(f"Menu Selected: {order.items}")
        print(f"Total Calories: {order.calories}")
        if order.order_accepted:
            print("Order accepted!")
            print(f"Total Price: {order.price} euros")
        else:
            print("Order refused!")
            print(f"Reason: {order.order_refused_reason}")
    else:
        print(result)

result = order_func()
process_order_result(result)