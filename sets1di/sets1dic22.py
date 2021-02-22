# z = set()
# i = 0
# while i < 10:
#     i += 1
#     x = input('введите 10 чисел: ',)
#     z.add(x)
# print(z)

z = set()
for x in range (1,11):
    x = int(input('введите 10 чисел: '))
    z.add(x)
print(tuple(z))

z.add(123)
print(z)