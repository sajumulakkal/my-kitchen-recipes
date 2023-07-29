from . import recipes2_blueprint
from flask import render_template, abort


breakfast_recipes_names = ['pancakes', 'acai_bowl', 'honey_bran_muffins', 'breakfast_scramble',
                           'pumpkin_donuts', 'waffles', 'omelette', 'chocolate_donuts', 'oatmeal',
                           'morning_glory_muffins', 'blueberry_smoothie_bowl']
dinner_recipes_names = ['steak_fajitas', 'ground_beef_tacos', 'pizza', 'sweet_fire_chicken', 'tri_tip',
                        'shredded_chicken', 'taquitos', 'red_lentil_chili']
baked_goods_recipes_names = ['bagels', 'french_bread', 'pitas', 'irish_soda_bread', 'soft_rolls',
                             'pizza_dough', 'pitas2', 'banana_bread']
side_dishes_recipes_names = ['sweet_potatoes', 'spanish_rice', 'jasmine_rice', 'fruit_salad']
dessert_recipes_names = ['brownies', 'chocolate_chip_cookies', 'linzer_cookies', 'sugar_cookies',
                         'flourless_chocolate_cake']
drink_recipes_names = ['berry_smoothie', 'chocolate_milk_shake', 'apple_cider_vinegar_drink']


@recipes2_blueprint.route('/')
def recipes():
    return render_template('recipes2/recipes.html',
                           number_of_breakfast_recipes=len(breakfast_recipes_names),
                           number_of_dinner_recipes=len(dinner_recipes_names),
                           number_of_baked_goods_recipes=len(baked_goods_recipes_names),
                           number_of_side_dishes_recipes=len(side_dishes_recipes_names),
                           number_of_dessert_recipes=len(dessert_recipes_names),
                           number_of_drink_recipes=len(drink_recipes_names))


@recipes2_blueprint.route('/breakfast2/')
def breakfast_recipes():
    return render_template('recipes2/breakfast.html')


@recipes2_blueprint.route('/breakfast2/<recipe_name>/')
def breakfast_recipe(recipe_name):
    if recipe_name not in breakfast_recipes_names:
        abort(404)

    return render_template(f'recipes2/{recipe_name}.html')


@recipes2_blueprint.route('/dinner2/')
def dinner_recipes():
    return render_template('recipes2/dinner.html')


@recipes2_blueprint.route('/dinner2/<recipe_name>/')
def dinner_recipe(recipe_name):
    if recipe_name not in dinner_recipes_names:
        abort(404)

    return render_template(f'recipes2/{recipe_name}.html')


@recipes2_blueprint.route('/baked_goods2/')
def baked_goods_recipes():
    return render_template('recipes2/baked_goods.html')


@recipes2_blueprint.route('/baked_goods2/<recipe_name>/')
def baked_goods_recipe(recipe_name):
    if recipe_name not in baked_goods_recipes_names:
        abort(404)

    return render_template(f'recipes2/{recipe_name}.html')


@recipes2_blueprint.route('/side_dishes2/')
def side_dishes_recipes():
    return render_template('recipes2/side_dishes.html')


@recipes2_blueprint.route('/side_dishes2/<recipe_name>/')
def side_dishes_recipe(recipe_name):
    if recipe_name not in side_dishes_recipes_names:
        abort(404)

    return render_template(f'recipes2/{recipe_name}.html')


@recipes2_blueprint.route('/dessert2/')
def dessert_recipes():
    return render_template('recipes2/dessert.html')


@recipes2_blueprint.route('/dessert2/<recipe_name>/')
def dessert_recipe(recipe_name):
    if recipe_name not in dessert_recipes_names:
        abort(404)

    return render_template(f'recipes2/{recipe_name}.html')


@recipes2_blueprint.route('/drink2/')
def drink_recipes():
    return render_template('recipes2/drink.html')


@recipes2_blueprint.route('/drink2/<recipe_name>/')
def drink_recipe(recipe_name):
    if recipe_name not in drink_recipes_names:
        abort(404)

    return render_template(f'recipes2/{recipe_name}.html')
