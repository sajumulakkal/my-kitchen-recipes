# recipes1/routes.py
from . import recipes1_blueprint
from flask import render_template, abort

# Duplicate the recipe names from the original recipes module
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


# Use endpoint names to avoid naming conflicts
@recipes1_blueprint.route('/', endpoint='recipes1')
def recipes():
    return render_template('recipes1/recipes.html',
                           number_of_breakfast_recipes=len(breakfast_recipes_names),
                           number_of_dinner_recipes=len(dinner_recipes_names),
                           number_of_baked_goods_recipes=len(baked_goods_recipes_names),
                           number_of_side_dishes_recipes=len(side_dishes_recipes_names),
                           number_of_dessert_recipes=len(dessert_recipes_names),
                           number_of_drink_recipes=len(drink_recipes_names))


@recipes1_blueprint.route('/breakfast/', endpoint='breakfast1')
def breakfast_recipes():
    return render_template('recipes1/breakfast.html')


@recipes1_blueprint.route('/breakfast/<recipe_name>/', endpoint='breakfast_recipe1')
def breakfast_recipe(recipe_name):
    if recipe_name not in breakfast_recipes_names:
        abort(404)

    return render_template(f'recipes1/{recipe_name}.html')


@recipes1_blueprint.route('/dinner/', endpoint='dinner1')
def dinner_recipes():
    return render_template('recipes1/dinner.html')


@recipes1_blueprint.route('/dinner/<recipe_name>/', endpoint='dinner_recipe1')
def dinner_recipe(recipe_name):
    if recipe_name not in dinner_recipes_names:
        abort(404)

    return render_template(f'recipes1/{recipe_name}.html')


@recipes1_blueprint.route('/baked_goods/', endpoint='baked_goods1')
def baked_goods_recipes():
    return render_template('recipes1/baked_goods.html')


@recipes1_blueprint.route('/baked_goods/<recipe_name>/', endpoint='baked_goods_recipe1')
def baked_goods_recipe(recipe_name):
    if recipe_name not in baked_goods_recipes_names:
        abort(404)

    return render_template(f'recipes1/{recipe_name}.html')


@recipes1_blueprint.route('/side_dishes/', endpoint='side_dishes1')
def side_dishes_recipes():
    return render_template('recipes1/side_dishes.html')


@recipes1_blueprint.route('/side_dishes/<recipe_name>/', endpoint='side_dishes_recipe1')
def side_dishes_recipe(recipe_name):
    if recipe_name not in side_dishes_recipes_names:
        abort(404)

    return render_template(f'recipes1/{recipe_name}.html')


@recipes1_blueprint.route('/dessert/', endpoint='dessert1')
def dessert_recipes():
    return render_template('recipes1/dessert.html')


@recipes1_blueprint.route('/dessert/<recipe_name>/', endpoint='dessert_recipe1')
def dessert_recipe(recipe_name):
    if recipe_name not in dessert_recipes_names:
        abort(404)

    return render_template(f'recipes1/{recipe_name}.html')


@recipes1_blueprint.route('/drink/', endpoint='drink1')
def drink_recipes():
    return render_template('recipes1/drink.html')


@recipes1_blueprint.route('/drink/<recipe_name>/', endpoint='drink_recipe1')
def drink_recipe(recipe_name):
    if recipe_name not in drink_recipes_names:
        abort(404)

    return render_template(f'recipes1/{recipe_name}.html')
