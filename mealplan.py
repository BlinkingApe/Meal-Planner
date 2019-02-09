'''
a mealplan object:
HAS
    number of meals, int
    all possible meals, list
    rejected meals, list
    mealplan, list
    shopping list, list

DOES
    prompts user for number of meals
    reduces all meals list by subtracting rejected meals
    selects number of meals randomly from reduced list
    prompts user for approval of list
    prompts user to reject meals from list
    prints meal plan
    prints ingredients list
'''

import meals
import random


class MealPlan():

    def __init__(self):

        self.number_meals = 0
        self.possible_meals = [cls for cls in meals.Meal.__subclasses__()]
        self.rejected_meals = []
        self.meal_plan = []
        self.shopping_list = {}

    def prompt_number_meals(self):
        while True:
            try:
                n = int(input("Enter number of meals [1 - 7]:"))
                if 0 < n < 8:
                    self.number_meals = n
                    break
                else:
                    print("Number must be between 1 and 7, try again...")
            except ValueError:
                print("Oops! Must be a single integer, try again...")

    def select_random_meals(self):
        number_to_select = self.number_meals - len(self.meal_plan)
        self.possible_meals = [meals for meals in self.possible_meals if meals not in self.rejected_meals]
        self.meal_plan.extend(random.sample(self.possible_meals, number_to_select))

    def print_meal_plan(self):
        print("Meals")
        print("-------")
        for i, meal in enumerate(self.meal_plan):
            print(str(i + 1) + '.' + meal().name)

    def prompt_approve_meals(self):
        while True:
            self.print_meal_plan()
            try:
                rejected_meal = int(input("Choose a meal to replace [1 - " + str(self.number_meals) + "]. Type '0' when you're satisfied with the meal plan:"))
                if 0 < rejected_meal < self.number_meals + 1:
                    self.rejected_meals.append(self.meal_plan[rejected_meal - 1])
                    del self.meal_plan[rejected_meal - 1]
                    self.select_random_meals()
                elif rejected_meal == 0:
                    break
                else:
                    print("Must be a number between 1 and " + str(self.number_meals) + ", or '0', try again...")
            except ValueError:
                print("Oops! Must be a single integer, try again...")

    def print_shopping_list(self):
        total_ingredients = {}
        for meal in self.meal_plan:
            for key, value in meal().ing_dict().items():
                if key in total_ingredients:
                    total_ingredients[key] += value
                else:
                    total_ingredients[key] = value
        self.shopping_list = dict(sorted(total_ingredients.items()))
        print("")
        print("Ingredients:")
        print("--------")
        for key, value in self.shopping_list.items():
            print(key + ': ' + str(value) + ' grams')
