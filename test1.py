# 有四个数字：1、2、3、4，能组成多少个互丌相同且无重复数字的三位数？各
# 是多少？
sum = 0
for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
            if i != j and i !=m and j !=m:
                sum += 1
                print(i * 100 + j * 10 + m,sum)