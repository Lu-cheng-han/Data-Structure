import timeit

setup_code = '''
import random
data = [random.randint(0, 100) for _ in range(100000000)]
max_score = 100
bucket = [0] * (max_score + 1)
'''

stmt_code = '''
for score in data:
    bucket[score] = bucket[score] + 1

data_2 = []
for i in range(len(bucket)):
    if bucket[i] != 0:
        for j in range(bucket[i]):
            data_2.append(i)
'''

setup_code_2 = '''
import random
data = [random.randint(0, 100) for _ in range(100000000)]
'''

stmt_code_2 = '''
data.sort()
'''
execution_time = timeit.timeit(stmt=stmt_code, setup=setup_code, number=1)
execution_time_2 = timeit.timeit(stmt=stmt_code_2, setup=setup_code_2, number=1)

print(f"{execution_time} 內建sec")
print(f"{execution_time_2} sec")
