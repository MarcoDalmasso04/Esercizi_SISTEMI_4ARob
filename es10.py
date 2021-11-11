x = [0, 1, 2, 3, 5, 6, 7, 8]

meta_1 = x[:len(x) // 2]
meta_2 = x[:len(x) // 2]

#meta_1 = x[:4]
#meta_2 = x[4:]

meta_1.append(5)

print(x)
print(meta_1)
print(meta_2)