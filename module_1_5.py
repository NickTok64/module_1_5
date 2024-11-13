mutable_list =['MB', 'BMW', 'Audi', 'VW']
print('Немецкие марки автомобилей: ', mutable_list)
mutable_list.append('Opel') # добавляем Opel
print('Немецкие марки автомобилей: ', mutable_list)
mutable_list.extend(['Reno', 'Peugeot', 'Citroen']) # добавляем французкие марки
print('Европейские марки автомобилей: ', mutable_list)
mutable_list[4] = 'Volvo' # меняем Opel на Volvo
print('Европейские марки автомобилей: ', mutable_list)
immutable_tuple = ('Fiat', 'Alfa Romeo', 'Lancia') # итальянские марки неизменны
print('Итальянские марки автомобилей: ', immutable_tuple)