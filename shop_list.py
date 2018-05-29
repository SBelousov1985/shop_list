# cook_book = {
#     'яйчница': [
#         {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#         {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#     'стейк': [
#         {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#         {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#         {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#     'салат': [
#         {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#         {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#         {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#         {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
# }


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
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
                ingridients = line.split(" | ")
                ingridients_dict = {"ingridient_name": ingridients[0],
                                    "quantity": int(ingridients[1]),
                                    "measure": ingridients[2]}
                cook_book[name].append(ingridients_dict)
                line = f.readline().strip()

    return cook_book, quantity


def create_shop_list():
    cook_book, quantity = get_cook_book_with_quantity("cook_book.txt")
    #person_count = int(input('Введите количество человек: '))
    #dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    #    .lower().split(', ')
    #shop_list = get_shop_list_by_dishes(dishes, person_count)
    #print_shop_list(shop_list)


create_shop_list()
