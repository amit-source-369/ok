# Unpacking List :

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [8, 9, 10, 11, 12, 13, 14]

a, b, *rest, c = list1
x, *_, z = list2
print(a)
print(b)
print(rest)
print(c)
print(x)
print(z)