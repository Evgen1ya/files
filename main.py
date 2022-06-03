from pprint import pprint

cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as recipes:
    for line in recipes:
        name = line.strip()
        number = int (recipes.readline().strip())
        recipe = []
        for item in range(number):
            ingredients = {}
            ingredient_name = recipes.readline().split('|')
            ingredients['ingredient'] = ingredient_name[0].strip()
            ingredients['quantity'] = int(ingredient_name[1].strip())
            ingredients['measure'] = ingredient_name[2].strip()
            recipe.append(ingredients)
        recipes.readline()
        cook_book[name] = recipe

pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ing = {}
    for i in dishes:
        count = dishes.count(i)
        for dish in cook_book.get(i):
            ing[dish['ingredient']] = {'measure': dish['measure'], 'quantity': dish.get('quantity') * int(person_count) * count}
    return pprint(ing)

person_count = 2
dishes = ['Омлет', 'Фахитос', 'Фахитос']
get_shop_list_by_dishes(dishes, person_count)

files = ['1.txt', '2.txt', '3.txt']
analyzed_files = {}
for file in files:
    with open(file, 'r', encoding='utf-8') as file_:
        lines_ = file_.readlines()
        lines_len = len(lines_)
        # print(lines_len)
    analyzed_files.update({lines_len: {'file': file, 'text': lines_, 'len': lines_len}})
# pprint(analyzed_files)

with open('sum.txt', 'w', encoding='utf-8') as file_sum:
    for key, value in sorted(analyzed_files.items()):
        file_sum.write(f"{value.get('file')}\n{value.get('len')}\n{''.join(value.get('text'))}\n")
