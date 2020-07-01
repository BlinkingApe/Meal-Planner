import ingredients as i


class Meal():
  ''' Base class for meals

  Parameters
  ----------
  name, str: name of the meal

  ingredients, list: [ingredients]

  '''

  def __init__(self, name, ingredients, recipe):
    self.name = name
    self.ingredients = ingredients
    self.recipe = recipe

  def nutrition_dict(self):
    args = []
    for ing in self.ingredients:
      args.append(ing.stats())
    meal_stats = list(map(sum, zip(*args)))
    rounded_stats = [round(x, 1) for x in meal_stats]
    nutr_dict = {'Calories': rounded_stats[0],
                 'Fat': rounded_stats[1],
                 'Carbs': rounded_stats[2],
                 'Protein': rounded_stats[3]}
    return nutr_dict

  def ingredients_dict(self):
    ing_dict = {}
    for ing in self.ingredients:
      key = ing.name
      value = ing.grams
      ing_dict[key] = value
    return ing_dict


class Brussel_Sprouts_Apples(Meal):
  def __init__(self):
    super().__init__(name='Brussel Sprouts w/ Apples',
                     ingredients=[i.BrusselSprouts(1),
                                  i.Apple(1)],
                     recipe="none")


class Brussel_Sprouts_Apples_Hamburger(Meal):
  def __init__(self):
    super().__init__(name='Brussel Sprouts w/ Apples, Hamburger, and Potatoes',
                     ingredients=[i.BrusselSprouts(1),
                                  i.Apple(1),
                                  i.Hamburger(1),
                                  i.Potato(1)],
                     recipe="none")


class Chickpea_Curry(Meal):
  def __init__(self):
    super().__init__(name='Chickpea Curry',
                     ingredients=[i.Chickpeas(1)],
                     recipe="none")


class Chicken_Avacado_Salad(Meal):
  def __init__(self):
    super().__init__(name='Chicken & Avacado salad',
                     ingredients=[i.Chicken(1),
                                  i.Avacado(1),
                                  i.Romaine(1)],
                     recipe="none")


class Chicken_Black_Bean_Chili(Meal):
  def __init__(self):
    super().__init__(name='Chicken & Black Bean Chili',
                     ingredients=[i.Chicken(1),
                                  i.BlackBeans(1)],
                     recipe="none")


class Chicken_Broccoli_Pasta(Meal):
  def __init__(self):
    super().__init__(name='Chicken & Broccoli Pasta',
                     ingredients=[i.Chicken(1),
                                  i.Broccoli(1),
                                  i.Pasta(1)],
                     recipe="none")


class Chicken_Pasta_Creamy(Meal):
  def __init__(self):
    super().__init__(name='Chicken Pasta w/ creamy sauce',
                     ingredients=[i.Chicken(1),
                                  i.Pasta(1)],
                     recipe="none")


class Chicken_Soup(Meal):
  def __init__(self):
    super().__init__(name='Chicken Soup',
                     ingredients=[i.Chicken(1)],
                     recipe="none")


class Chicory_Ham_Mashed_Potatoes(Meal):
  def __init__(self):
    super().__init__(name='Chicory & Ham w/ mashed potatoes',
                     ingredients=[i.Chicory(500),
                                  i.Ham(150),
                                  i.Potato(1000),
                                  i.Butter(70),
                                  i.Milk(650),
                                  i.Flour(16),
                                  i.Gouda(150)],
                     recipe="Peel and boil potatoes. Blanch chicory for 5 minutes, then cut in half lengthwise and wrap in hame slices. Place these in casserole dish. Melt 40 grams butter, add flour and stir, add 500 grams milk and whisk until creamy. Cover chicory in sauce, top with cheese, and bake at 200 for 20 minutes. Drain potatoes, add 30 grams butter and 150 grams milk, then mash. Add salt and nutmeg to taste, add milk if too dry.")


class Eggs_Spinach_Potato(Meal):
  def __init__(self):
    super().__init__(name='Eggs w/ Spinach & Potatoes',
                     ingredients=[i.Egg(300),
                                  i.Spinach(250),
                                  i.Potato(800),
                                  i.OliveOil(35),
                                  i.Onion(40),
                                  i.Butter(40),
                                  i.Milk(200),
                                  i.Flour(5)],
                     recipe="none")


class Feta_Zucchini_Rice(Meal):
  def __init__(self):
    super().__init__(name='Feta Zucchini Rice w/ Bell Pepper',
                     ingredients=[i.Feta(1),
                                  i.Zucchini(1),
                                  i.Rice(1),
                                  i.BellPepper(1)],
                     recipe="none")


class Fennel_Ham_Mashed_Potatoes(Meal):
  def __init__(self):
    super().__init__(name='Chicory & Ham w/ mashed potatoes',
                     ingredients=[i.Fennel(500),
                                  i.Ham(150),
                                  i.Potato(1000),
                                  i.Butter(70),
                                  i.Milk(650),
                                  i.Flour(16),
                                  i.Gouda(150)],
                     recipe="Peel and boil potatoes. Blanch Fennel for 5 minutes, then cut in half lengthwise and wrap in hame slices. Place these in casserole dish. Melt 40 grams butter, add flour and stir, add 500 grams milk and whisk until creamy. Cover Fennel in sauce, top with cheese, and bake at 200 for 20 minutes. Drain potatoes, add 30 grams butter and 150 grams milk, then mash. Add salt and nutmeg to taste, add milk if too dry.")


class Frikos_Kohlrabi_Potato(Meal):
  def __init__(self):
    super().__init__(name='Frikos w/ Kohlrabi & Potatoes',
                     ingredients=[i.Hamburger(1),
                                  i.Kohlrabi(1),
                                  i.Potato(1)],
                     recipe="none")


class Hamburger_Cabbage_Potatoes(Meal):
  def __init__(self):
    super().__init__(name='Hamburger w/ Cabbage and Potatoes',
                     ingredients=[i.Hamburger(400),
                                  i.Cabbage(500),
                                  i.Potato(200),
                                  i.SourCream(100)],
                     recipe="none")


class Hamburger_Chili(Meal):
  def __init__(self):
    super().__init__(name='Hamburger Chili',
                     ingredients=[i.Hamburger(1),
                                  i.KidneyBeans(1),
                                  i.Corn(1),
                                  i.Carrot(1),
                                  i.BellPepper(1)],
                     recipe="none")


class Hamburger_Zucchini_Pasta(Meal):
  def __init__(self):
    super().__init__(name='Hamburger & Zucchini Pasta',
                     ingredients=[i.Hamburger(350),
                                  i.Zucchini(350),
                                  i.SourCream(100),
                                  i.Pasta(350),
                                  i.BellPepper(250)],
                     recipe="none")


class Hamburger_Zucchini_Rice(Meal):
  def __init__(self):
    super().__init__(name='Hamburger & Zucchini w/ Rice',
                     ingredients=[i.Hamburger(350),
                                  i.Zucchini(350),
                                  i.SourCream(100),
                                  i.Rice(250),
                                  i.BellPepper(250)],
                     recipe="none")


class Insalata_Caprese(Meal):
  def __init__(self):
    super().__init__(name='Insalata Caprese',
                     ingredients=[i.Tomato(1),
                                  i.Mozzarella(1)],
                     recipe="none")


class Hamburger_Feta_Rice(Meal):
  def __init__(self):
    super().__init__(name='Hamburger w/ Feta and Rice',
                     ingredients=[i.Hamburger(400),
                                  i.Feta(500),
                                  i.BellPepper(200),
                                  i.Rice(100)],
                     recipe="none")


class Lentil_Soup(Meal):
  def __init__(self):
    super().__init__(name='Lentil Soup',
                     ingredients=[i.Lentils(1)],
                     recipe="none")


class Potato_Salad(Meal):
  def __init__(self):
    super().__init__(name='Potato Salad',
                     ingredients=[i.Potato(1)],
                     recipe="none")


class Potato_Soup(Meal):
  def __init__(self):
    super().__init__(name='Potato Soup',
                     ingredients=[i.Potato(1000),
                                  i.Carrot(400),
                                  i.Bruewurst(360),
                                  i.VegetableBroth(25),
                                  i.SourCream(100),
                                  i.Chives(20)],
                     recipe="none")


class Red_Beet_Risotto(Meal):
  def __init__(self):
    super().__init__(name='Red Beet Risotto',
                     ingredients=[i.Beets(1)],
                     recipe="none")


class Salmon_Veggies(Meal):
  def __init__(self):
    super().__init__(name='Salmon w/ Roasted Veggies',
                     ingredients=[i.Salmon(1)],
                     recipe="none")


class Steak_Veggies(Meal):
  def __init__(self):
    super().__init__(name='Steak w/ Roasted Veggies',
                     ingredients=[i.Steak(1)],
                     recipe="none")


class Stew(Meal):
  def __init__(self):
    super().__init__(name='Stew',
                     ingredients=[i.Chuck(1),
                                  i.Carrot(1),
                                  i.Potato(1)],
                     recipe="none")


class Stir_Fry(Meal):
  def __init__(self):
    super().__init__(name='Stir Fry',
                     ingredients=[i.Cabbage(500),
                                  i.Carrot(400),
                                  i.Zucchini(250),
                                  i.Egg(200),
                                  i.OliveOil(50),
                                  i.Onion(125)],
                     recipe="Finely chop onion, cabbage and zucchini, grate carrot. Fry all vegetables in olive oil high heat. Add eggs and stir till fried.")


class Tuna_Casserole(Meal):
  def __init__(self):
    super().__init__(name='Tuna Casserole',
                     ingredients=[i.Tuna(500),
                                  i.Pasta(500),
                                  i.Peas(500),
                                  i.Gouda(100)],
                     recipe="none")


class Tuna_Veggies(Meal):
  def __init__(self):
    super().__init__(name='Tuna Steak w/ Veggies',
                     ingredients=[i.TunaSteak(1),
                                  i.Carrot(1)],
                     recipe="none")


class Veggie_Casserole(Meal):
  def __init__(self):
    super().__init__(name='Veggie Casserole',
                     ingredients=[i.Carrot(1),
                                  i.Fennel(1),
                                  i.Zucchini(1),
                                  i.BellPepper(1),
                                  i.GoatCreamCheese(1),
                                  i.PineNuts(1)],
                     recipe="none")


class Veggie_Chili(Meal):
  def __init__(self):
    super().__init__(name='Veggie Chili',
                     ingredients=[i.OliveOil(30),
                                  i.Onion(125),
                                  i.BellPepper(350),
                                  i.Carrot(300),
                                  i.TomatoCanned(800),
                                  i.KidneyBeans(500),
                                  i.BlackBeans(500),
                                  i.VegetableBroth(10),
                                  i.SourCream(20),
                                  i.Cheddar(30)],
                     recipe="none")


class Veggie_Curry(Meal):
  def __init__(self):
    super().__init__(name='Veggie Curry',
                     ingredients=[i.Zucchini(1),
                                  i.Carrot(1)],
                     recipe="none")


class Veggie_Lasagna(Meal):
  def __init__(self):
    super().__init__(name='Veggie Lasagna',
                     ingredients=[i.Pumpkin(1),
                                  i.Carrot(1)],
                     recipe="none")


class Veggie_Pasta(Meal):
  def __init__(self):
    super().__init__(name='Veggie Pasta w/ Red Sauce',
                     ingredients=[i.Pasta(1),
                                  i.Carrot(1)],
                     recipe="none")
