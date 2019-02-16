from mealplan import MealPlan


def main():

    mp = MealPlan()
    mp.prompt_number_meals()
    mp.select_random_meals()
    mp.prompt_approve_meals()
    mp.write_to_file()


if __name__ == '__main__':
    main()
