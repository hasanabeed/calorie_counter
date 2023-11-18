from load_data import load_data

def order_validator(order):
    items = [item.strip() for item in order.split(',')]
    meals_data = load_data("data/meals.json")
    combos_data = load_data("data/combos.json")

    meal_names = {meal['name'] for meal in meals_data['meals']}
    combo_names = {combo['name'] for combo in combos_data['combos']}

    invalid_items = [item for item in items if item not in meal_names and item not in combo_names]

    if invalid_items:
        return f"Invalid items in your order: {', '.join(invalid_items)}."
    
    return items