immutable_var = (['Fiat', 'Alfa Romeo', 'Lancia'],3,True) # итальянские марки неизменны
print('Итальянские марки автомобилей: ', immutable_var)
immutable_var[0][2]='Ferrari' # элементы кортежа изменить нельзя, но можно изменить список вложенный в кортеж
print('Итальянские марки автомобилей: ', immutable_var)
mutable_list =['MB', 'BMW', 'Audi', 'VW', 4, True]
print('Немецкие марки автомобилей: ', mutable_list)
mutable_list [4:6] = ['Opel', 5, True]# добавляем Opel
print('Немецкие марки автомобилей: ', mutable_list)
mutable_list.insert(5, ['Reno', 'Peugeot', 'Citroen']) # добавляем французкие марки
mutable_list[6]=mutable_list[6] + 3  # пересчитываем кол-во марок
print('Европейские марки автомобилей: ', mutable_list)
mutable_list[4] = 'Volvo' # меняем Opel на Volvo
print('Европейские марки автомобилей: ', mutable_list)

