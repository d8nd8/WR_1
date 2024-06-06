def linerunner(file_path):
    cook_book = {}
    with open("recipes.txt", "r") as f:
        while True:
            dish_name = f.readline().strip()

            if not dish_name:
                break

            ingredient_count = int(f.readline().strip())
            ingredients = []

            for _ in range(ingredient_count):
                ingredient_line = f.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(
                    ' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })

            cook_book[dish_name] = ingredients
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = linerunner("recipes.txt")
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                    ingredient_name = ingredient['ingredient_name']
                    quantity = ingredient['quantity'] * person_count
                    measure = ingredient['measure']

                    if ingredient_name not in shop_list:
                        shop_list[ingredient_name] = {"measure": measure, "quantity": quantity}

                    else:
                        shop_list[ingredient_name]['quantity'] += quantity

    print(shop_list)
linerunner("recipes.txt")
get_shop_list_by_dishes(['Запеченный картофель', 'Тост с авокадо'],3)
