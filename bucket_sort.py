import time
start_time = time.time()
data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
#準備桶子
max_score = 100
bucket = []
for i in range(max_score + 1):
   bucket.append(0)

#丟數據到桶子中
for score in data:
   bucket[score] = bucket[score] + 1

data_2 = []
for i in range(len(bucket)):
   if bucket[i] != 0:
      for j in range(bucket[i]):
        data_2.append(i)
        
end_time = time.time()



data = [['Abby', 58], ['Julia', 44], ['Jane', 31], ['Stephen', 76], ['Ryn', 82], ['Justin', 99], ['Caroline', 65], ['James', 87], ['Damon', 25], ['Elena', 76]]

def bucketsort_hash(data):
    max_score = 100
    bucket = []
    bucket_num = lambda x: int(x/33)
    
    for i in range(bucket_num(max_score)+1):
        bucket.append([])

    for x in data:
        index = bucket_num(x[1])
        print(index,flush=True)
        bucket[index].append(x)

    print("bucket",bucket,flush=True)

    for i, flag in enumerate(bucket):
        if flag != [] :
            bucket[i] = sorted(bucket[i], key=lambda x: x[1])
            
    print("bucket sorted after",bucket,flush=True)

    index = 0
    for i in bucket:
        if i != []:
            for j in i:
                data[index] = j
                index += 1

bucketsort_hash(data)
# print(data)

