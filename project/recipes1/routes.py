# recipes1/routes.py

from . import recipes1_blueprint
from flask import render_template, abort

# Duplicate the recipe names from the original recipes module
breakfast_recipes1_names = ['pancakes', 'acai_bowl', 'honey_bran_muffins', 'breakfast_scramble',
                           'pumpkin_donuts', 'waffles', 'omelette', 'chocolate_donuts', 'oatmeal',
                           'morning_glory_muffins', 'blueberry_smoothie_bowl']
dinner_recipes1_names = ['steak_fajitas', 'ground_beef_tacos', 'pizza', 'sweet_fire_chicken', 'tri_tip',
                        'shredded_chicken', 'taquitos', 'red_lentil_chili']
baked_goods_recipes1_names = ['bagels', 'french_bread', 'pitas', 'irish_soda_bread', 'soft_rolls',
                             'pizza_dough', 'pitas2', 'banana_bread']
side_dishes_recipes1_names = ['sweet_potatoes', 'spanish_rice', 'jasmine_rice', 'fruit_salad']
dessert_recipes1_names = ['brownies', 'chocolate_chip_cookies', 'linzer_cookies', 'sugar_cookies',
                         'flourless_chocolate_cake']
drink_recipes1_names = ['berry_smoothie', 'chocolate_milk_shake', 'apple_cider_vinegar_drink']


@recipes1_blueprint.route('/recipes1/', endpoint='recipes1_index')
def recipes1_index():
    return render_template('recipes1/recipes1.html',
                           number_of_breakfast_recipes1=len(breakfast_recipes1_names),
                           number_of_dinner_recipes1=len(dinner_recipes1_names),
                           number_of_baked_goods_recipes1=len(baked_goods_recipes1_names),
                           number_of_side_dishes_recipes1=len(side_dishes_recipes1_names),
                           number_of_dessert_recipes1=len(dessert_recipes1_names),
                           number_of_drink_recipes1=len(drink_recipes1_names))


@recipes1_blueprint.route('/recipes1/breakfast1/', endpoint='breakfast_recipes1_index')
def breakfast_recipes1_index():
    return render_template('recipes1/breakfast.html')


@recipes1_blueprint.route('/recipes1/breakfast1/<recipes1_name>/', endpoint='breakfast_recipes1_detail')
def breakfast_recipes1_detail(recipes1_name):
    if recipes1_name not in breakfast_recipes1_names:
        abort(404)

    return render_template(f'recipes1/{recipes1_name}.html')


@recipes1_blueprint.route('/recipes1/dinner1/', endpoint='dinner_recipes1_index')
def dinner_recipes1_index():
    return render_template('recipes1/dinner.html')


@recipes1_blueprint.route('/recipes1/dinner1/<recipes1_name>/', endpoint='dinner_recipes1_detail')
def dinner_recipes1_detail(recipes1_name):
    if recipes1_name not in dinner_recipes1_names:
        abort(404)

    return render_template(f'recipes1/{recipes1_name}.html')


@recipes1_blueprint.route('/recipes1/baked_goods1/', endpoint='baked_goods_recipes1_index')
def baked_goods_recipes1_index():
    return render_template('recipes1/baked_goods.html')


@recipes1_blueprint.route('/recipes1/baked_goods1/<recipes1_name>/', endpoint='baked_goods_recipes1_detail')
def baked_goods_recipes1_detail(recipes1_name):
    if recipes1_name not in baked_goods_recipes1_names:
        abort(404)

    return render_template(f'recipes1/{recipes1_name}.html')


@recipes1_blueprint.route('/recipes1/side_dishes1/', endpoint='side_dishes_recipes1_index')
def side_dishes_recipes1_index():
    return render_template('recipes1/side_dishes.html')


@recipes1_blueprint.route('/recipes1/side_dishes1/<recipes1_name>/', endpoint='side_dishes_recipes1_detail')
def side_dishes_recipes1_detail(recipes1_name):
    if recipes1_name not in side_dishes_recipes1_names:
        abort(404)

    return render_template(f'recipes1/{recipes1_name}.html')


@recipes1_blueprint.route('/recipes1/dessert1/', endpoint='dessert_recipes1_index')
def dessert_recipes1_index():
    return render_template('recipes1/dessert.html')


@recipes1_blueprint.route('/recipes1/dessert1/<recipes1_name>/', endpoint='dessert_recipes1_detail')
def dessert_recipes1_detail(recipes1_name):
    if recipes1_name not in dessert_recipes1_names:
        abort(404)

    return render_template(f'recipes1/{recipes1_name}.html')


@recipes1_blueprint.route('/recipes1/drink1/', endpoint='drink_recipes1_index')
def drink_recipes1_index():
    return render_template('recipes1/drink.html')


@recipes1_blueprint.route('/recipes1/drink1/<recipes1_name>/', endpoint='drink_recipes1_detail')
def drink_recipes1_detail(recipes1_name):
    if recipes1_name not in drink_recipes1_names:
        abort(404)

    return render_template(f'recipes1/{recipes1_name}.html')
