from mealplan import MealPlan


def main():

    mp = MealPlan()
    mp.prompt_number_meals()
    mp.select_random_meals()
    mp.prompt_approve_meals()
    mp.print_meal_plan()
    mp.print_shopping_list()


if __name__ == '__main__':
    main()
