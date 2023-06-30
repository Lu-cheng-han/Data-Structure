
stk = []

n = int(input("輸入n: "))

while n != 0:
    stk.append(int(n % 2))
    n= n // 2

while len(stk) > 0:
    print(stk.pop())
