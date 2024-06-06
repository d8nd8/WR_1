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
        print(cook_book)
linerunner("recipes.txt")
