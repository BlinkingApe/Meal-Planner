class Ingredient:
    ''' Base class for meal ingredients

    Parameters
    ----------
    name, str: name of the ingredient

    nutrition, list of floats: [kcal, fat, carbs, protein] per 100 gram

    store, str: name of preferred location of purchase

    section, int: numerical location in store, descending from proximity to door
    '''

    def __init__(self, name, nutrition, store, section):
        self.name = name
        self.nutrition = nutrition
        self.store = store
        self.section = section

    def stats(self):
        return [round(x * (self.grams / 100), 1) for x in self.nutrition]


class Apple(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Apple',
                         nutrition=[45, 0, 11, 0],
                         store='aldi',
                         section=5)
        self.grams = grams


class Avacado(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Avacado',
                         nutrition=[234, 21, 12, 3],
                         store='aldi',
                         section=5)
        self.grams = grams


class Beets(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Beets',
                         nutrition=[43, 0.2, 10, 1.6],
                         store='aldi',
                         section=5)
        self.grams = grams


class BellPepper(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Bell Pepper',
                         nutrition=[35, 0, 6, 1],
                         store='aldi',
                         section=5)
        self.grams = grams


class BlackBeans(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Black Beans',
                         nutrition=[339, 0.9, 63, 21],
                         store='aldi',
                         section=5)
        self.grams = grams


class Broccoli(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Broccoli',
                         nutrition=[34, 0.4, 7, 2.8],
                         store='aldi',
                         section=5)
        self.grams = grams


class BrusselSprouts(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Brussel Sprouts',
                         nutrition=[43, 0.3, 9, 3.4],
                         store='aldi',
                         section=5)
        self.grams = grams


class Butter(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Butter',
                         nutrition=[744, 82, 1, 1],
                         store='aldi',
                         section=5)
        self.grams = grams


class Cabbage(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Cabbage',
                         nutrition=[25, 0, 6, 1.3],
                         store='aldi',
                         section=5)
        self.grams = grams


class Carrot(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Carrot',
                         nutrition=[41, 0.2, 10, 0.9],
                         store='aldi',
                         section=5)
        self.grams = grams


class Chickpeas(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Chickpeas',
                         nutrition=[364, 6, 61, 19],
                         store='aldi',
                         section=5)
        self.grams = grams


class Chicken(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Chicken',
                         nutrition=[104, 2, 0, 23],
                         store='aldi',
                         section=5)
        self.grams = grams


class Chicory(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Chicory',
                         nutrition=[23, 0.3, 4.7, 1.7],
                         store='aldi',
                         section=5)
        self.grams = grams


class Chuck(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Chuck',
                         nutrition=[277, 20, 0, 25],
                         store='aldi',
                         section=5)
        self.grams = grams


class Corn(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Corn',
                         nutrition=[59, 1.1, 10.4, 2.1],
                         store='aldi',
                         section=5)
        self.grams = grams


class Egg(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Egg',
                         nutrition=[153, 11, 1, 13],
                         store='aldi',
                         section=5)
        self.grams = grams


class Fennel(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Fennel',
                         nutrition=[31, 0.2, 7, 1.2],
                         store='dm',
                         section=0)
        self.grams = grams


class Feta(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Feta',
                         nutrition=[264, 21, 4, 14],
                         store='aldi',
                         section=5)
        self.grams = grams


class GoatCreamCheese(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Goat Cream Cheese',
                         nutrition=[459, 46, 3.5, 3.5],
                         store='dm',
                         section=0)
        self.grams = grams


class Gouda(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Gouda',
                         nutrition=[356, 27, 2.2, 25],
                         store='aldi',
                         section=5)
        self.grams = grams


class Ham(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Ham',
                         nutrition=[145, 6, 1.5, 21],
                         store='aldi',
                         section=5)
        self.grams = grams


class Hamburger(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Hamburger',
                         nutrition=[332, 30, 0, 14],
                         store='aldi',
                         section=5)
        self.grams = grams


class Joghurt(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Joghurt',
                         nutrition=[72, 4, 3, 4],
                         store='aldi',
                         section=5)
        self.grams = grams


class KidneyBeans(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Kidney Beans',
                         nutrition=[333, 0.8, 60, 24],
                         store='aldi',
                         section=5)
        self.grams = grams


class Kohlrabi(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Kohlrabi',
                         nutrition=[27, 0.1, 6, 1.7],
                         store='aldi',
                         section=5)
        self.grams = grams


class Lentils(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Lentils',
                         nutrition=[116, 0.4, 20, 9],
                         store='aldi',
                         section=5)
        self.grams = grams


class Mayo(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Mayonnaise',
                         nutrition=[712, 77, 3, 1],
                         store='aldi',
                         section=5)
        self.grams = grams


class Milk(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Milk',
                         nutrition=[62, 3.4, 4.7, 3.2],
                         store='aldi',
                         section=5)
        self.grams = grams


class Mozzarella(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Mozarella',
                         nutrition=[280, 17, 3.1, 28],
                         store='aldi',
                         section=5)
        self.grams = grams


class Mushroom(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Mushroom',
                         nutrition=[85, 0, 3, 2],
                         store='aldi',
                         section=5)
        self.grams = grams


class Oats(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Oats',
                         nutrition=[372, 7, 59, 14],
                         store='dm',
                         section=0)
        self.grams = grams


class Pasta(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Pasta',
                         nutrition=[354, 2, 72, 12],
                         store='dm',
                         section=0)
        self.grams = grams


class Peas(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Peas',
                         nutrition=[88, 0.4, 14, 5],
                         store='dm',
                         section=0)
        self.grams = grams


class PineNuts(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Pine Nuts',
                         nutrition=[673, 68, 13, 14],
                         store='dm',
                         section=0)
        self.grams = grams


class Potato(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Potato',
                         nutrition=[77, 0, 17, 2],
                         store='dm',
                         section=0)
        self.grams = grams


class Pumpkin(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Pumpkin',
                         nutrition=[26, 0.1, 7, 1],
                         store='dm',
                         section=0)
        self.grams = grams


class Rice(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Rice',
                         nutrition=[353, 1, 77, 7],
                         store='dm',
                         section=0)
        self.grams = grams


class Romaine(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Romaine',
                         nutrition=[17, 0.3, 3.3, 1.2],
                         store='dm',
                         section=0)
        self.grams = grams


class Salmon(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Salmon',
                         nutrition=[208, 13, 0, 20],
                         store='aldi',
                         section=5)
        self.grams = grams


class SourCream(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Sour Cream',
                         nutrition=[116, 10, 3, 0],
                         store='dm',
                         section=0)
        self.grams = grams


class Spinach(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Spinach',
                         nutrition=[25, 1, 1, 3],
                         store='dm',
                         section=0)
        self.grams = grams


class Steak(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Steak',
                         nutrition=[271, 19, 0, 25],
                         store='aldi',
                         section=5)
        self.grams = grams


class Sugar(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Sugar',
                         nutrition=[400, 0, 100, 0],
                         store='dm',
                         section=0)
        self.grams = grams


class SweetPotato(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Sweet Potato',
                         nutrition=[86, 0, 20, 2],
                         store='dm',
                         section=0)
        self.grams = grams


class Tomato(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Tomato',
                         nutrition=[18, 0.2, 3.9, 0.9],
                         store='aldi',
                         section=5)
        self.grams = grams


class Tuna(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Tuna',
                         nutrition=[113, 1.2, 0.4, 26],
                         store='dm',
                         section=0)
        self.grams = grams


class TunaSteak(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Tuna Steak',
                         nutrition=[130, 0.6, 0, 28.7],
                         store='dm',
                         section=0)
        self.grams = grams


class Zucchini(Ingredient):
    def __init__(self, grams):
        super().__init__(name='Zucchini',
                         nutrition=[17, 0.3, 3.1, 1.2],
                         store='aldi',
                         section=5)
        self.grams = grams
