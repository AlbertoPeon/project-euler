
size = 1001

acc = [1]
for i in range(size * 2 - 2):
    step = (i + 4)//4 * 2
    acc.append(acc[-1] + step)

print(sum(acc))
