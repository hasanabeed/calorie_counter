from load_data import load_data
from order_validator import order_validator

def display_menu(meals, combos):
    meal_names = ', '.join(meal['name'] for meal in meals)
    combo_names = ', '.join(combo['name'] for combo in combos)
    print(f"The menu is here: {meal_names}, and {combo_names}.")

def get_user_orders():
    print("Please enter the names of your orders here, separating them with a ',': ")
    return input()

def order_func():
    all_meals = load_data("data/meals.json")['meals']
    all_combos = load_data("data/combos.json")['combos']

    display_menu(all_meals, all_combos)

    user_orders = get_user_orders()
    result = order_validator(user_orders)

    return result