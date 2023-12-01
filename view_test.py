
number = [1,4,7,0,3,6,9,2,5,8]

rows = int(input())

number_quantity = 0
for row in range(1,rows + 1):
    for j in range(row):
        c = number_quantity % 10  
        print(number[c],flush=True,end= '')
        number_quantity += 1
    print('\r\n')


'''
1
4 7
0 3 6
9 2 5 8
1 4 7 0 3
6 9 2 5 8 1你講的不對ㄟ可以用python幫我把這題印出來嗎
'''