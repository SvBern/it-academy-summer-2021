# 1
list1 = ['a', 'b', 'c']
cort1 = tuple(list1)
print(type(list1), list1)
print(type(cort1), cort1)

# 2
cort1 = ('a', 'b', 'c')
list1 = [cort1]
print(type(cort1), cort1)
print(type(list1), list1)

# 3
a, b, c = 'a', 2, 'python'
print('a=', a, 'b=', b, 'c=', c)

# 4
cort1 = 1,
print(len(cort1))
n = 1
for i in cort1 * 3:
    print(n)
    n += 1
