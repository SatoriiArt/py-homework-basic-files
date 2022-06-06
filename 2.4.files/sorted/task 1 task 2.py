
def read_file(file):
    with open(file, 'rt', encoding='utf-8') as recipes:
        temp_list = []
        for line in recipes:
            temp_list.append(line.strip())
    return temp_list


def checkout(temp_list):
    count = 0
    cook_book = dict()
    while count < len(temp_list):
        food_name = temp_list[count]
        food_items = int(temp_list[count + 1])
        food_ingredients = []
        for i in range(food_items):
            item = dict()
            product = temp_list[count + 2 + i].split('|')
            item.update({'ingredient_name': product[0].strip(), 'quantity': int(
                product[1]), 'measure': product[2].strip()})
            food_ingredients.append(item)
        cook_book.update({food_name: food_ingredients})
        count = count + food_items + 3
    return cook_book


# print(checkout(read_file('recipes.txt')))
cook_book = checkout(read_file('recipes.txt'))


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()
    for i in dishes:
        for j in cook_book[i]:
            # print(j['ingredient_name'], j['quantity'], j['measure'])
            if j['ingredient_name'] not in shop_list:
                shop_list[j['ingredient_name']] = {
                    'measure': j['measure'], 'quantity': j['quantity'] * person_count}
            else:
                shop_list[j['ingredient_name']
                          ]['quantity'] += j['quantity'] * person_count
    return shop_list


shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

for i in shop_list:
    print(f'{i} : {shop_list[i]}')
