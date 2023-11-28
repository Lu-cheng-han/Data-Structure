from queue import Queue

len = [[0]*10 for _ in range(10)] 
# len為2維陣列，記錄起點到每一點的長度，列表生成式。

maze = [[1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,0,1,0,1,1,1,1,1],
        [1,0,0,1,0,1,0,0,0,1],
        [1,0,1,1,0,1,1,0,0,1],
        [1,0,1,0,0,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]
# 陣列最外層包一圈牆。(1,1) 為起點，(8,8)為終點。

q = Queue()
q.put((1, 1))             # 先把起點放入佇列
len[1][1] = 1
maze[1][1] = 1           # 走過設為牆

while not q.empty():
    now=q.get()                     # 從佇列開頭取一個點
    x,y=now[0],now[1]               # 此點座標置於x,y
        
    if maze[x + 1][y + 0] == 0:     # 此點的右方有路 
        nx = x + 1                  # 下一點座標
        ny = y + 0                     
        q.put((nx,ny))              # 下一個點放入佇列
        len[nx][ny] = len[x][y] + 1 # 長度+1
        maze[nx][ny] = 1            # 走過設為牆

    if maze[x + 0][y + 1] == 0:     # 此點的下方有路
        nx = x + 0              
        ny = y + 1                     
        q.put((nx,ny))          
        len[nx][ny] = len[x][y] + 1; 
        maze[nx][ny] = 1            

    if maze[x - 1][y + 0] == 0:     # 此點的左方有路
        nx = x - 1
        ny = y + 0
        q.put((nx,ny)) 
        len[nx][ny] = len[x][y] + 1
        maze[nx][ny] = 1

    if  maze[x + 0][y - 1] == 0 :                  # 此點的上方有路
        nx = x + 0
        ny = y - 1
        q.put((nx,ny)) 
        len[nx][ny] = len[x][y] + 1
        maze[nx][ny] = 1
    
    '''
    x,y=q.get()
    for nx,ny in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
        if maze[nx][ny] == 0:
            q.put((nx,ny))                # 下一個點放入佇列
            len[nx][ny] = len[x][y] + 1   # 長度+1
            maze[nx][ny] = 1;       
    '''


if len[8][8] == 0:
    print('沒有路!')
else:
    for i in range(0,10):
        for j in range(0,10):
            print(len[i][j], end=' ')
        print()
       
    print('shortest path ', len[8][8])