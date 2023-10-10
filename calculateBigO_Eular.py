import time
import random

def compute_e_ver1(n):
    e = 0
    fact = 1
    for i in range(n):
        e += 1/fact
        fact *= (i+1)
    return e

def compute_e_ver2(n):
    e = 0
    fact = 1
    for i in range(n):
        e += 1/fact
        fact *= (i+1)
    return e

def measure_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

for n in [100, 1000, 10000, 100000, 500000]:
    if n > 30000:  # 시간 측정이 60초 이상이면 중지
        break
    random.seed(42)
    n_list = [random.randint(1, n) for _ in range(10)]
    print(f"n={n}")
    for i in range(10):
        t_ver1 = measure_time(compute_e_ver1, n_list[i])
        t_ver2 = measure_time(compute_e_ver2, n_list[i])
        print(f"Run {i+1}: ver1={t_ver1:.6f}, ver2={t_ver2:.6f}")


	
# n 입력받음
# compute_e_ver1 호출
# compute_e_ver2 호출
# 두 함수의 수행시간 출력
before_ver1 = time.process_time()
compute_e_ver1(n)
after_ver1 = time.process_time()
print(after_ver1 - before_ver1)

before_ver2 = time.process_time()
compute_e_ver2(n)
after_ver2 = time.process_time()
print(after_ver2 - before_ver2)