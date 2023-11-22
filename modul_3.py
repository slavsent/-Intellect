t = (1, 2, [50, 60])
t[2] += [10, 20]

# TypeError: 'tuple' object does not support item assignment
# t это кортеж, а он относится к неизменяемым типам данным в python
# поэтому изменение элемента кортежа не возможно
