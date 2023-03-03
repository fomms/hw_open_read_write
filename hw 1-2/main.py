from pprint import pprint

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredient_count = int(file.readline())
        ingredient = []
        for _ in range(ingredient_count):
            ing = file.readline().strip()
            name, quantity, measure = ing.split(' | ')
            ingredient.append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})
        cook_book[dish] = ingredient
        file.readline()

pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        for ing_list in cook_book[dish]:
            if ing_list['ingredient_name'] in list(res.keys()):
                res[ing_list['ingredient_name']]['quantity'] += ing_list['quantity'] * person_count
            else:
                res2 = {ing_list['ingredient_name']: {'measure': ing_list['measure'], 'quantity': ing_list['quantity'] * person_count}}
                res.update(res2)
    return res


print()
dishes1 = ['Омлет', 'Фахитос']
person_count1 = 3
pprint(get_shop_list_by_dishes(dishes1, person_count1), sort_dicts=False)
print()
dishes2 = ['Омлет', 'Фахитос', 'Запеченный картофель', 'Утка по-пекински']
person_count2 = 2
pprint(get_shop_list_by_dishes(dishes2, person_count2), sort_dicts=False)





