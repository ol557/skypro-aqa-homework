

# def sort_objects(objects, order):
#     color_objects = {'К': 3, 'С': 2, 'З': 1} # создаем словарь с порядком цветов
    
#     # сортируем объекты по цифрому порядку возрастания цветов
#     objects_sorted = sorted(objects, key=lambda x: color_objects[x])
    
#     # возврашаем отсортированный список объектов 
#     return objects_sorted

# # задем данные по объектам     
# objects = ['С', 'С', 'З', 'С', 'К', 'З', 'З', 'З', 'К', 'К', 'С', 'З', 'С', 'С', 'К', 'З']
# order = 'ЗСК'

# # запускаем функцию 
# sorted_objects = sort_objects(objects, order)
# # получаем ['З', 'З', 'З', 'З', 'З', 'З', 'С', 'С', 'С', 'С', 'С', 'С', 'К', 'К', 'К', 'К']
# print(sorted_objects) 


def sort_objects(objects):
    color_objects = {'К': 3, 'С': 2, 'З': 1} # создаем словарь с порядком цветов
    
    # сортируем объекты по лексикокрафическому порядку цветов 
    objects_sorted = sorted(objects)
    
    # возврашаем отсортированный список объектов 
    return objects_sorted

# задем данные по объектам     
objects = ['С', 'С', 'З', 'С', 'К', 'З', 'З', 'З', 'К', 'К', 'С', 'З', 'С', 'С', 'К', 'З']


# запускаем функцию 
sorted_objects = sort_objects(objects)
# получаем ['З', 'З', 'З', 'З', 'З', 'З', 'К', 'К', 'К', 'К', 'С', 'С', 'С', 'С', 'С', 'С']
print(sorted_objects) 