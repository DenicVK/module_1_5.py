immutable_var = (1, 'арбуз', 5.0, [1, 2, 3, 4, 5], True)
print (immutable_var)

#immutable_var[0] = 2
#TypeError: 'tuple' object does not support item assignment
#Главное свойство кортежа - это не возможность изменения содержимого кортежа после его написания

mutable_list = [5, 'дыня', 5.5, [1, 2, 3, 4, 5], False]
mutable_list[0] = 'ягода'
mutable_list[1] = 'малина'
print(mutable_list)
