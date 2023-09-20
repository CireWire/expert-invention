# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: CireWire
Date: 09/19/2023
Description: This program scales a recipe based on user input.
License: MIT License
Version: 1.0
"""

# Define function to scale recipe
def scale_recipe(recipe, serving_size):
    scaled_recipe = {}
    for ingredient, data in recipe.items():
        quantity = data["quantity"]
        metric = data["metric"]
        try:
            scaled_quantity = quantity * serving_size
        except TypeError:
            print(f"Error: Invalid quantity for ingredient '{ingredient}'")
            continue
        scaled_recipe[ingredient] = {"quantity": scaled_quantity, "metric": metric}
    return scaled_recipe

# Define main function
def main():
    print("Welcome to the Recipe Scaler!")
    print("-----------------------------")

    # Input original recipe ingredients and quantities
    recipe = {}
    while True:
        ingredient = input("Enter ingredient name (or 'done' to finish): ")
        if ingredient.lower() == "done":
            break
        while True:
            try:
                quantity = float(input("Enter quantity: "))
                break
            except ValueError:
                print("Error: Invalid quantity. Please enter a number.")
        metric = input("Enter unit of measurement (e.g. cups, grams, ounces, whole count): ")
        recipe[ingredient] = {"quantity": quantity, "metric": metric}

    # Input desired serving size
    while True:
        try:
            serving_size = float(input("Enter desired serving size: "))
            break
        except ValueError:
            print("Error: Invalid serving size. Please enter a number.")

    # Scale recipe
    scaled_recipe = scale_recipe(recipe, serving_size)

    # Display scaled recipe
    print("\nScaled Recipe:")
    for ingredient, data in scaled_recipe.items():
        quantity = data["quantity"]
        metric = data["metric"]
        print(f"{ingredient}: {quantity:.2f} {metric}")

if __name__ == "__main__":
    main()
