from load_data import load_data

all_meals = load_data("data/meals.json")['meals']
all_combos = load_data("data/combos.json")['combos']

def calorie_counter(orders):
    total_calories = sum(
        combo_calorie_counter(order) if 'combo' in order else
        next((meal['calories'] for meal in all_meals if order in (meal['name'], meal['id'])), 0)
        for order in orders
    )
    return total_calories


def combo_calorie_counter(orders):
    combo_meal_dict = {combo['name']: combo['meals'] for combo in all_combos}
    total = calorie_counter(combo_meal_dict[orders]) if orders in combo_meal_dict else 0
    return total