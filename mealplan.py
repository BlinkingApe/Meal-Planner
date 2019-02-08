import meals
import random


def main():

    meal_plan = select_random_meals(n=3)
    print_meal_plan(meal_plan)
    print_shopping_list(meal_plan)


def select_random_meals(n=3):

    meals_list = [cls for cls in meals.Meal.__subclasses__()]

    return random.sample(meals_list, n)


def print_meal_plan(meal_plan):
    print("Meals")
    print("-------")
    for meal in meal_plan:
        print(meal().name)


def print_shopping_list(meal_plan):
    total_ingredients = {}
    for meal in meal_plan:
        for key, value in meal().ing_dict().items():
            if key in total_ingredients:
                total_ingredients[key] += value
            else:
                total_ingredients[key] = value
    sorted_total_ing = dict(sorted(total_ingredients.items()))
    print("")
    print("Ingredients:")
    print("--------")
    for key, value in sorted_total_ing.items():
        print(key + ': ' + str(value) + ' grams')


if __name__ == '__main__':
    main()
