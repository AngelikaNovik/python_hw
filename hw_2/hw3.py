# Вывести все целые степени двойки

n = int(input("введите число n "))
k = 0
res = 1
while res < n+1:
    print(res, end=" ")
    k += 1
    res = 2**k
