# cook_book = {
#     'яйчница': [
#         {'ingredient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#     'стейк': [
#         {'ingredient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#         {'ingredient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#         {'ingredient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#     'салат': [
#         {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#         {'ingredient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#         {'ingredient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#         {'ingredient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
# }


def get_shop_list_by_dishes(cook_book, quantity):
    shop_list = {}
    for name, count in quantity.items():
        for ingredient in cook_book[name]:
            new_shop_list_item = dict(ingredient)

            new_shop_list_item['quantity'] *= count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def get_cook_book_with_quantity(path):
    cook_book = {}
    quantity = {}
    with open(path, encoding='utf-8') as f:
        while True:
            name = f.readline().strip()
            if not name:
                break
            count = int(f.readline().strip())
            cook_book[name] = []
            quantity[name] = count
            line = f.readline().strip()
            while line:
                ingredients = line.split(" | ")
                ingredients_dict = {"ingredient_name": ingredients[0],
                                    "quantity": int(ingredients[1]),
                                    "measure": ingredients[2]}
                cook_book[name].append(ingredients_dict)
                line = f.readline().strip()

    return cook_book, quantity


def create_shop_list():
    cook_book, quantity = get_cook_book_with_quantity("cook_book.txt")
    shop_list = get_shop_list_by_dishes(cook_book, quantity)
    print_shop_list(shop_list)


create_shop_list()
