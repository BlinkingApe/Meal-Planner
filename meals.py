import ingredients as i


class Meal():
    ''' Base class for meals

    Parameters
    ----------
    name, str: name of the meal

    ingredients, list: [ingredients]

    '''

    def __init__(self, name, servings, ingredients):
        self.name = name
        self.servings = servings
        self.ingredients = ingredients

    def stats(self):
        args = []
        for ing in self.ingredients:
            args.append(ing.stats())
        meal_stats = list(map(sum, zip(*args)))
        return [round(x, 1) for x in meal_stats]

    def ing_dict(self):
        ing_dict = {}
        for ing in self.ingredients:
            key = ing.name
            value = ing.grams
            ing_dict[key] = value
        return ing_dict


class Brussel_Sprouts_Apples(Meal):
    def __init__(self):
        super().__init__(name='Brussel Sprouts w/ Apples',
                         servings=1,
                         ingredients=[i.BrusselSprouts(1),
                                      i.Apple(1)])


class Brussel_Sprouts_Apples_Hamburger(Meal):
    def __init__(self):
        super().__init__(name='Brussel Sprouts w/ Apples, Hamburger, and Potatoes',
                         servings=1,
                         ingredients=[i.BrusselSprouts(1),
                                      i.Apple(1),
                                      i.Hamburger(1),
                                      i.Potato(1)])


class Chickpea_Curry(Meal):
    def __init__(self):
        super().__init__(name='Chickpea Curry',
                         servings=1,
                         ingredients=[i.Chickpeas(1)])


class Chicken_Avacado_Salad(Meal):
    def __init__(self):
        super().__init__(name='Chicken & Avacado salad',
                         servings=1,
                         ingredients=[i.Chicken(1),
                                      i.Avacado(1),
                                      i.Romaine(1)])


class Chicken_Black_Bean_Chili(Meal):
    def __init__(self):
        super().__init__(name='Chicken & Black Bean Chili',
                         servings=1,
                         ingredients=[i.Chicken(1),
                                      i.BlackBeans(1)])


class Chicken_Broccoli_Pasta(Meal):
    def __init__(self):
        super().__init__(name='Chicken & Broccoli Pasta',
                         servings=1,
                         ingredients=[i.Chicken(1),
                                      i.Broccoli(1),
                                      i.Pasta(1)])


class Chicken_Pasta_Creamy(Meal):
    def __init__(self):
        super().__init__(name='Chicken Pasta w/ creamy sauce',
                         servings=1,
                         ingredients=[i.Chicken(1),
                                      i.Pasta(1)])


class Chicken_Soup(Meal):
    def __init__(self):
        super().__init__(name='Chicken Soup',
                         servings=1,
                         ingredients=[i.Chicken(1)])


class Chicory_Ham_Mashed_Potatoes(Meal):
    def __init__(self):
        super().__init__(name='Chicory & Ham w/ mashed potatoes',
                         servings=1,
                         ingredients=[i.Chicory(1),
                                      i.Ham(1),
                                      i.Potato(1)])


class Eggs_Spinach_Potato(Meal):
    def __init__(self):
        super().__init__(name='Eggs w/ Spinach & Potatoes',
                         servings=1,
                         ingredients=[i.Egg(1),
                                      i.Spinach(1),
                                      i.Potato(1)])


class Feta_Zucchini_Rice(Meal):
    def __init__(self):
        super().__init__(name='Feta Zucchini Rice w/ Bell Pepper',
                         servings=1,
                         ingredients=[i.Feta(1),
                                      i.Zucchini(1),
                                      i.Rice(1),
                                      i.BellPepper(1)])


class Frikos_Kohlrabi_Potato(Meal):
    def __init__(self):
        super().__init__(name='Frikos w/ Kohlrabi & Potatoes',
                         servings=1,
                         ingredients=[i.Hamburger(1),
                                      i.Kohlrabi(1),
                                      i.Potato(1)])


class Hamburger_Cabbage_Potatoes(Meal):
    def __init__(self):
        super().__init__(name='Hamburger w/ Cabbage and Potatoes',
                         servings=1,
                         ingredients=[i.Hamburger(400),
                                      i.Cabbage(500),
                                      i.Potato(200),
                                      i.SourCream(100)])


class Hamburger_Chili(Meal):
    def __init__(self):
        super().__init__(name='Hamburger Chili',
                         servings=1,
                         ingredients=[i.Hamburger(1),
                                      i.KidneyBeans(1),
                                      i.Corn(1),
                                      i.Carrot(1),
                                      i.BellPepper(1)])


class Insalata_Caprese(Meal):
    def __init__(self):
        super().__init__(name='Insalata Caprese',
                         servings=1,
                         ingredients=[i.Tomato(1),
                                      i.Mozzarella(1)])


class Hamburger_Feta_Rice(Meal):
    def __init__(self):
        super().__init__(name='Hamburger w/ Feta and Rice',
                         servings=1,
                         ingredients=[i.Hamburger(400),
                                      i.Feta(500),
                                      i.BellPepper(200),
                                      i.Rice(100)])


class Lentil_Soup(Meal):
    def __init__(self):
        super().__init__(name='Lentil Soup',
                         servings=1,
                         ingredients=[i.Lentils(1)])


class Potato_Salad(Meal):
    def __init__(self):
        super().__init__(name='Potato Salad',
                         servings=1,
                         ingredients=[i.Potato(1)])


class Potato_Soup(Meal):
    def __init__(self):
        super().__init__(name='Potato Soup',
                         servings=1,
                         ingredients=[i.Potato(1),
                                      i.Carrot(1),
                                      i.Bruewurst(1),
                                      i.VegetableBroth(1),
                                      i.SourCream(1),
                                      i.Chives(1)])


class Red_Beet_Risotto(Meal):
    def __init__(self):
        super().__init__(name='Red Beet Risotto',
                         servings=1,
                         ingredients=[i.Beets(1)])


class Salmon_Veggies(Meal):
    def __init__(self):
        super().__init__(name='Salmon w/ Roasted Veggies',
                         servings=1,
                         ingredients=[i.Salmon(1)])


class Steak_Veggies(Meal):
    def __init__(self):
        super().__init__(name='Steak w/ Roasted Veggies',
                         servings=1,
                         ingredients=[i.Steak(1)])


class Stew(Meal):
    def __init__(self):
        super().__init__(name='Stew',
                         servings=1,
                         ingredients=[i.Chuck(1),
                                      i.Carrot(1),
                                      i.Potato(1)])


class Stir_Fry(Meal):
    def __init__(self):
        super().__init__(name='Stir Fry',
                         servings=1,
                         ingredients=[i.Cabbage(1),
                                      i.Carrot(1)])


class Tuna_Casserole(Meal):
    def __init__(self):
        super().__init__(name='Tuna Casserole',
                         servings=1,
                         ingredients=[i.Tuna(500),
                                      i.Pasta(500),
                                      i.Peas(500),
                                      i.Gouda(100)])


class Tuna_Veggies(Meal):
    def __init__(self):
        super().__init__(name='Tuna Steak w/ Veggies',
                         servings=1,
                         ingredients=[i.TunaSteak(1),
                                      i.Carrot(1)])


class Veggie_Casserole(Meal):
    def __init__(self):
        super().__init__(name='Veggie Casserole',
                         servings=1,
                         ingredients=[i.Carrot(1),
                                      i.Fennel(1),
                                      i.Zucchini(1),
                                      i.BellPepper(1),
                                      i.GoatCreamCheese(1),
                                      i.PineNuts(1)])


class Veggie_Chili(Meal):
    def __init__(self):
        super().__init__(name='Veggie Chili',
                         servings=1,
                         ingredients=[i.OliveOil(1),
                                      i.Onion(1),
                                      i.BellPepper(1),
                                      i.Carrot(1),
                                      i.TomatoCanned(1),
                                      i.KidneyBeans(1),
                                      i.BlackBeans(1),
                                      i.VegetableBroth(1),
                                      i.SourCream(1),
                                      i.Cheddar(1)])


class Veggie_Curry(Meal):
    def __init__(self):
        super().__init__(name='Veggie Curry',
                         servings=1,
                         ingredients=[i.Zucchini(1),
                                      i.Carrot(1)])


class Veggie_Lasagna(Meal):
    def __init__(self):
        super().__init__(name='Veggie Lasagna',
                         servings=1,
                         ingredients=[i.Pumpkin(1),
                                      i.Carrot(1)])


class Veggie_Pasta(Meal):
    def __init__(self):
        super().__init__(name='Veggie Pasta w/ Red Sauce',
                         servings=1,
                         ingredients=[i.Pasta(1),
                                      i.Carrot(1)])
