from load_data import load_data

all_meals = {meal['name']: meal['price'] for meal in load_data("data/meals.json")['meals']}
all_combos = {combo['name']: combo['price'] for combo in load_data("data/combos.json")['combos']}

def price_counter(orders):
    total = sum(all_combos[order] if 'combo' in order and order in all_combos else
                all_meals[order] if order in all_meals else 0 for order in orders)

    return total

def combo_price_counter(orders):
    # all_combos_data = load_data("data/combos.json")
    # all_meals_data = load_data("data/meals.json")

    combo_meal_dict = {
        combo['name']: {
            'meals': combo['meals'],
            'price': sum(meal['price'] for meal in all_meals['meals'] if meal['name'] in combo['meals'])
        }
        for combo in all_combos['combos']
    }

    total = sum(
        combo_meal_dict[order]['price'] if order in combo_meal_dict else
        next((meal['price'] for meal in all_meals['meals'] if order == meal['name']), 0)
        for order in orders
    )

    return total