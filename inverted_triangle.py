a = input()
a = int (a)
# for i in range(0,a):
#     for j in range(i,a):
#         print('@',end='')
#     print()

for i in range(a,0,-1):
    print(i*'@')