import ingredients as i


class Meal():
    ''' Base class for meals

    Parameters
    ----------
    name, str: name of the meal

    ingredients, list: [ingredients]

    '''

    def __init__(self, name, ingredients):
        self.name = name
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


class Hamburger_Cabbage_Potatoes(Meal):
    def __init__(self):
        super().__init__(name='Hamburger w/ Cabbage and Potatoes',
                         ingredients=[i.Hamburger(400),
                                      i.Cabbage(500),
                                      i.Potato(200),
                                      i.SourCream(100)])


class Hamburger_Feta_Rice(Meal):
    def __init__(self):
        super().__init__(name='Hamburger w/ Feta and Rice',
                         ingredients=[i.Hamburger(400),
                                      i.Feta(500),
                                      i.BellPepper(200),
                                      i.Rice(100)])


class Tuna_Casserole(Meal):
    def __init__(self):
        super().__init__(name='Tuna Casserole',
                         ingredients=[i.Tuna(500),
                                      i.Pasta(500),
                                      i.Peas(500),
                                      i.Gouda(100)])
