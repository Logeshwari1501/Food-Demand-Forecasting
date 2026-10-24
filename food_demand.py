# Food Demand Forecasting and Inventory Analytics

food_items = {
    "Biryani": [50, 55, 60, 65],
    "Meals": [40, 45, 42, 48],
    "Fried Rice": [30, 35, 38, 40],
    "Noodles": [25, 28, 30, 32]
}

inventory = {
    "Biryani": 45,
    "Meals": 50,
    "Fried Rice": 25,
    "Noodles": 40
}

print("FOOD DEMAND FORECASTING & INVENTORY ANALYTICS")
print("-" * 50)

for item, sales in food_items.items():

    predicted_demand = round(sum(sales) / len(sales))
    current_stock = inventory[item]
    reorder = max(0, predicted_demand - current_stock)

    print("\nFood Item:", item)
    print("Predicted Demand:", predicted_demand)
    print("Current Inventory:", current_stock)

    if reorder > 0:
        print("Recommendation: Order", reorder, "units")
    else:
        print("Recommendation: Stock is sufficient")