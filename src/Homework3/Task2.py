# 1
list1 = [x + y for x in 'ab' for y in 'bcd']
print(list1)

# 2
list2 = list1[::2]
print(list2)

# 3
list3 = [str(x) + 'a' for x in range(5) if x != 0]
print(list3)

# 4
print(list3.pop(1))

# 5
list4 = list3.copy()
list4[1:1] = ['2a']
print('list3:', list3)
print('list4:', list4)
