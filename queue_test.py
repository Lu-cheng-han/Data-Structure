from queue import Queue

q=Queue()
n=int(input("請輸入牌數: "))

for i in range(1,n+1):
    q.put(i)

while q.qsize() > 1:
    print(q.get(),flush=True)
    # q.put(q.get())
print(q.qsize())
print(q.get(),flush=True)

# len = [[0]*10 for _ in range(10)] 
# print(len)
